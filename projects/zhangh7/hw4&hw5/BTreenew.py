import bisect 
import itertools
import operator
import random
import unittest
import copy

class Stack(object):

    def __init__(self, *arg):
        super(Stack, self).__init__()
        self.__stack = list(copy.copy(arg))
        self.__size = len(self.__stack)

    def push(self, value):
        self.__stack.append(value)
        self.__size += 1

    def pop(self):
        if self.__size <= 0:
            return None
        else:
            value = self.__stack[-1]
            self.__size -= 1
            del self.__stack[-1]
            return value

    def __len__(self):
        return self.__size

    def empty(self):
        return self.__size <= 0

    def __str__(self):
        return "".join(["Stack(list=", str(map(lambda s: str(s), self.__stack)), ",size=", str(self.__size), ')'])


class Node(object):
          
    def __init__(self, is_leaf, keys, childs=None, parent=None):
        self.keys = list(sorted(keys))
        self.is_leaf = is_leaf
        self.__size = self.length(self.keys)
        if not self.is_leaf and childs is None:
            self.childs = [None for x in xrange(0, self.__size + 1)]
        else:
            self.childs = childs
        self.parent = parent
		
    def length(self, keys):
        if keys is None:
            return 0
        return len(keys)

    def __str__(self):
        return "".join(['Node(keys=', ",".join(map(lambda key: str(key), self.keys)),
                        ',Leaf' if self.is_leaf else ',Not Leaf',
                        ',childs num=', '0' if self.is_leaf else str(self.length(self.childs)), ')\n'])

    def __len__(self):
        return self.__size

    def append(self, key):
        result = self.__size
        self.__size += 1

        for x in xrange(0, result):
            if self.keys[x] > key:
                self.keys.insert(x, key)
                if not self.is_leaf:
                    self.childs.insert(x, None)
                return x
        self.keys.append(key)
        if not self.is_leaf:
            self.childs.append(None)
        return result

    def search_child(self, instance):
        if self.childs is None:
            return None
        for x in xrange(0, self.__size):
            if self.keys[x] > instance:
                return self.childs[x]
        return self.childs[self.__size]

    def leaf_remove(self, index):
        if self.is_leaf:
            del self.keys[index]
            self.__size -= 1

class _BPlusLeaf(Node):
    __slots__ = ["tree", "contents", "data", "next"]

    def __init__(self, tree, contents=None, data=None, next=None):
        self.tree = tree
        self.contents = contents or []
        self.data = data or []
        self.next = next
        self.__size = 0
        assert self.length(self.contents) == self.length(self.data), "one data per key"

    def insert(self, index, key, data, ancestors):
        self.contents.insert(index, key)
        self.data.insert(index, data)

        if self.length(self.contents) > self.tree.order:
            self.shrink(ancestors)
        

    def lateral(self, parent, parent_index, dest, dest_index):
        if parent_index > dest_index:
            dest.contents.append(self.contents.pop(0))
            dest.data.append(self.data.pop(0))
            parent.contents[dest_index] = self.contents[0]
        else:
            dest.contents.insert(0, self.contents.pop())
            dest.data.insert(0, self.data.pop())
            parent.contents[parent_index] = dest.contents[0]

    def split(self):
        center = self.length(self.contents) // 2
        median = self.contents[center - 1]
        sibling = type(self)(
                self.tree,
                self.contents[center:],
                self.data[center:],
                self.next)
        self.contents = self.contents[:center]
        self.data = self.data[:center]
        self.next = sibling
        return sibling, sibling.contents[0]

    def remove(self, index, ancestors):
        minimum = self.tree.order // 2
        if index >= self.length(self.contents):
            self, index = self.next, 0

        key = self.contents[index]

        # if any leaf that could accept the key can do so
        # without any rebalancing necessary, then go that route
        current = self
        while current is not None and current.contents[0] == key:
            if self.length(current.contents) > minimum:
                if current.contents[0] == key:
                    index = 0
                else:
                    index = bisect.bisect_left(current.contents, key)
                current.contents.pop(index)
                current.data.pop(index)
                return
            current = current.next

        self.grow(ancestors)

    def grow(self, ancestors):
        minimum = self.tree.order // 2
        parent, parent_index = ancestors.pop()
        left_sib = right_sib = None

        # try borrowing from a neighbor - try right first
        if parent_index + 1 < self.length(parent.children):
            right_sib = parent.children[parent_index + 1]
            if self.length(right_sib.contents) > minimum:
                right_sib.lateral(parent, parent_index + 1, self, parent_index)
                return

        # fallback to left
        if parent_index:
            left_sib = parent.children[parent_index - 1]
            if self.length(left_sib.contents) > minimum:
                left_sib.lateral(parent, parent_index - 1, self, parent_index)
                return

        # join with a neighbor - try left first
        if left_sib:
            left_sib.contents.extend(self.contents)
            left_sib.data.extend(self.data)
            parent.remove(parent_index - 1, ancestors)
            return

        # fallback to right
        self.contents.extend(right_sib.contents)
        self.data.extend(right_sib.data)
        parent.remove(parent_index, ancestors)

class BTree(object):
    def __init__(self, load_factor=4, *vargs):
        """Constructor for BTree"""
        self.__root = None
        self.__load_factor = load_factor
        self.__size = 0
        map(self.insert, vargs)
    
    def length(self, node):
        if node is None:
            return 0
        return len(node)

    def insert(self, key):
        if self.__root is None:
            self.__root = Node(True, [key])
            self.__size += 1
            return

        cur_node = self.__root
        while not cur_node.is_leaf:
            self.__split(cur_node)
            cur_node = cur_node.search_child(key)

        left_node, right_node = self.__split(cur_node)
        if left_node is None or right_node is None:
            cur_node.append(key)
        else:
            parent_key = None
            parent = left_node.parent
            for i in xrange(self.length(parent)):
                if parent.childs[i] is left_node:
                    parent_key = parent.keys[i]

            if parent_key <= key:
                right_node.append(key)
            else:
                left_node.append(key)

        self.__size += 1

    def treesize(self):
        return self.__size

    def __split(self, node):
        if self.full(node):
            parent_node = node.parent
            middle_key = node.keys[self.__load_factor - 1]
            if parent_node is None:
                parent_node = self.__root = Node(False, [])

            parent_middle_index = parent_node.append(middle_key)
            left_node = Node(node.is_leaf, node.keys[:self.__load_factor - 1],
                             None if node.is_leaf else node.childs[:self.__load_factor],
                             parent_node)

            right_node = Node(node.is_leaf, node.keys[self.__load_factor:],
                              None if node.is_leaf else node.childs[self.__load_factor:],
                              parent_node)

            if not node.is_leaf:
                for child in left_node.childs:
                    if child is not None:
                        child.parent = left_node
                for child in right_node.childs:
                    if child is not None:
                        child.parent = right_node

            parent_node.childs[parent_middle_index] = left_node
            parent_node.childs[parent_middle_index + 1] = right_node
            self.__root.is_leaf = False
            return left_node, right_node
        return None, None

    def search(self, instance):
        return self.__search(self.__root, instance)

    def full(self, node):
        return self.length(node) >= (self.__load_factor * 2 - 1)

    def __search(self, root, instance):
        cur_node = root
        #if (self.__size == 0):
        #    return None, None
        while True:
            cur_len = self.length(cur_node)
            x = 0
            while x < cur_len and cur_node.keys[x] < instance:
                x += 1
            if x < cur_len and cur_node.keys[x] == instance:
                return cur_node, x
            elif cur_node is None:
                return None, None
            elif cur_node.is_leaf:
                return None, None
            else:
                cur_node = cur_node.childs[x]

    def min(self):
        if self.__size is 0:
            return None
        cur_node = self.__root
        while not cur_node.is_leaf:
            cur_node = cur_node.childs[0]
        return cur_node.keys[0]

    def max(self):
        if self.__root is None:
            return None
        cur_node = self.__root
        while not cur_node.is_leaf:
            cur_node = cur_node.childs[-1]
        return cur_node.keys[-1]

    def mid_order(self):
        result = []
        stack = Stack()
        cur_node = self.__root
        if (cur_node is None):
            return result
        if cur_node.is_leaf:
            return cur_node.keys
        while True:
            if cur_node.is_leaf:
                result.extend(cur_node.keys)
                if stack.empty():
                    return result
                cur_node, i = stack.pop()
                result.append(cur_node.keys[i])
                if i < self.length(cur_node) - 1:
                    stack.push((cur_node, i + 1))
                cur_node = cur_node.childs[i + 1]
            else:
                stack.push((cur_node, 0))
                cur_node = cur_node.childs[0]
        return result

    def delete(self, key):
        #if (self.__size == 0):
        #    return False
        node, index = self.search(key)
        if node is None:
            return None
        return self.__delete(node, index)

    def __delete(self, node, index):
        #if node is None:
        #    return False
        if node.is_leaf:
            self.__size -= 1

            if self.will_starve(node):
                change_index, bro_node, bro_index = self.__check_brother_borrow(node)
                if bro_node is None:
                    del node.keys[index]

                    self.__merge_brother(node)
                else:
                    parent = node.parent
                    node.keys[index] = parent.keys[change_index]
                    parent.keys[change_index] = bro_node.keys[bro_index]
                    bro_node.leaf_remove(bro_index)
            else:
                node.leaf_remove(index)
        else:
            succ, succ_index = self.__successor(node, index)
            node.keys[index] = succ.keys[succ_index]
            return self.__delete(succ, succ_index)
        return None, None

    def __successor(self, node, i):
        if not node.is_leaf:
            child_node = node.childs[i + 1]
            while not child_node.is_leaf:
                child_node = child_node.childs[0]
            return self.__successor(child_node, -1)
        else:
            if i < self.length(node) - 1:
                return node, i + 1
            else:
                return None, None

    def will_starve(self, node):
        return self.length(node) < self.__load_factor

    def successor(self, key):
        node, index = self.search(key)
        if node is None:
            return None, None
        return self.__successor(node, index)

    def __str__(self):
        return "\n".join(self.mid_order(lambda s: str(s)))

    def test(self):
        node = self.successor('0')
        print(node)

    def __check_brother_borrow(self, node):
        parent = node.parent
        node_index = -1
        for i in xrange(self.length(parent.childs)):
            if parent.childs[i] is node:
                node_index = i

        if node_index >= 1 and not self.will_starve(parent.childs[node_index - 1]):
            return node_index - 1, parent.childs[node_index - 1], -1

        if node_index >= 0 and not self.will_starve(parent.childs[node_index + 1]):
            return node_index, parent.childs[node_index + 1], 0

        return None, None, None

    def __merge_brother(self, node):
        parent = node.parent
        if parent is self.__root and self.length(parent.keys) > 0:
            return

        node_index = -1
        for i in xrange(self.length(parent.childs)):
            if parent.childs[i] is node:
                node_index = i

        smaller_node = None
        is_left = True
        if node_index >= 1:
            smaller_node = parent.childs[node_index - 1]

        if node_index >= 0 and (smaller_node is None or self.length(smaller_node) > parent.childs[node_index + 1]):
            smaller_node = parent.childs[node_index + 1]
            is_left = False

        if self.length(smaller_node) < self.__load_factor - 1 or self.length(node) < self.__load_factor - 1:
            if is_left:
                new_keys = smaller_node.keys
                new_keys.append(parent.keys[node_index - 1])
                new_keys.extend(node.keys)
            else:
                new_keys = node.keys
                new_keys.append(parent.keys[node_index - 1])
                new_keys.extend(smaller_node.keys)

            new_childs = None
            if not node.is_leaf:
                if is_left:
                    new_childs = smaller_node.childs
                    new_childs.extend(node.childs)
                else:
                    new_childs = node.childs
                    new_childs.extend(smaller_node.childs)

            new_node = Node(node.is_leaf, new_keys, new_childs, parent)

            if is_left:
                del parent.childs[node_index - 1]
                del parent.keys[node_index - 1]
                parent.childs[node_index - 1] = new_node
            else:
                del parent.childs[node_index + 1]
                del parent.keys[node_index + 1]
                parent.childs[node_index] = new_node

            if parent is self.__root and self.length(parent.keys):
                new_node.parent = None
                self.__root = new_node
            else:
                self.__merge_brother(parent)		

class BPlusTree(BTree):
    LEAF = _BPlusLeaf

    def __init__(self, order):
        self.order = order
        self._root = self._bottom = self.LEAF(self)
        self.length = 0


    def _get(self, key):
        node, index = self._path_to(key)[-1]

        if index == self.length(node.contents):
            if node.next:
                node, index = node.next, 0
            else:
                return

        while node.contents[index] == key:
            yield node.data[index]
            index += 1
            if index == self.length(node.contents):
                if node.next:
                    node, index = node.next, 0
                else:
                    return

    def _path_to(self, item):
        path = super(BPlusTree, self)._path_to(item)
        node, index = path[-1]
        while hasattr(node, "children"):
            node = node.children[index]
            index = bisect.bisect_left(node.contents, item)
            path.append((node, index))
        return path

    def get(self, key, default=None):
        try:
            return self._get(key).next()
        except StopIteration:
            return default

    def getlist(self, key):
        return list(self._get(key))

    def insert(self, key):
        path = self._path_to(key)
        node, index = path.pop()
        node._insert(index, key, path)
        self.length += 1

    def remove(self, key):
        path = self._path_to(key)
        node, index = path.pop()
        node.remove(index, path)
        self.length -= 1

    def treenum(self):
        return self.length

    __getitem__ = get
    __setitem__ = insert
    __delitem__ = remove

    def __contains__(self, key):
        for item in self._get(key):
            return True
        return False

    def iteritems(self):
        node = self._root
        while hasattr(node, "children"):
            node = node.children[0]

        while node:
            for pair in itertools.izip(node.contents, node.data):
                yield pair
            node = node.next

    def iterkeys(self):
        return itertools.imap(operator.itemgetter(0), self.iteritems())

    def itervalues(self):
        return itertools.imap(operator.itemgetter(1), self.iteritems())

    __iter__ = iterkeys

    def items(self):
        return list(self.iteritems())

    def keys(self):
        return list(self.iterkeys())

    def values(self):
        return list(self.itervalues())

    def _build_bulkloaded_leaves(self, items):
        minimum = self.order // 2
        leaves, seps = [[]], []

        for item in items:
            if self.length(leaves[-1]) >= self.order:
                seps.append(item)
                leaves.append([])
            leaves[-1].append(item)

        if self.length(leaves[-1]) < minimum and seps:
            last_two = leaves[-2] + leaves[-1]
            leaves[-2] = last_two[:minimum]
            leaves[-1] = last_two[minimum:]
            seps.append(last_two[minimum])

        leaves = [self.LEAF(
                self,
                contents=[p[0] for p in pairs],
                data=[p[1] for p in pairs])
            for pairs in leaves]

        for i in xrange(self.length(leaves) - 1):
            leaves[i].next = leaves[i + 1]

        return leaves, [s[0] for s in seps]



