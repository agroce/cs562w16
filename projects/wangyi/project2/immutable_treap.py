#!/usr/bin/python


from treap import TreapNode
from treap import Treap


class ImmutableTreap(Treap):

   def __init__(self):
      Treap.__init__(self)
      self.root = None

   def insert(self, value, priority=None):
      ret = ImmutableTreap()

      if not self.contains(value):
         ret.root = ImmutableTreap.__insert(self.root, value, priority)
      else:
         ret.root = self.root

      return ret

   def delete(self, value):
      if not self.contains(value):
         return self

      t = ImmutableTreap()
      t.root = ImmutableTreap.__delete(self.root, value)
      return t

   def merge(self, other):
      t = ImmutableTreap()
      t.root = ImmutableTreap.__merge(self.root, other.root)
      return t

   def split(self, value):
      root = ImmutableTreap.__insert(self.root, value, TreapNode.INFINITY)

      left = ImmutableTreap()
      right = ImmutableTreap()
      left.root, right.root = root.left, root.right

      return left, right


   @staticmethod
   def __insert(node, value, priority=None):
      if node is None:
         return TreapNode(value, priority)

      new = TreapNode(node=node)

      if new.value < value:
         new.right = ImmutableTreap.__insert(new.right, value, priority)
         if new.right.priority > new.priority:
            new = ImmutableTreap.__rotateLeft(new)
      else:
         new.left  = ImmutableTreap.__insert(new.left,  value, priority)
         if new.left.priority > new.priority:
            new = ImmutableTreap.__rotateRight(new)

      return new

   @staticmethod
   def __delete(node, value):
      if node.left is None and node.right is None:
         return None

      new = TreapNode(node=node)

      if node.value > value:
         new.left = ImmutableTreap.__delete(new.left, value)
      elif node.value < value:
         new.right = ImmutableTreap.__delete(new.right, value)
      elif Treap.cmp(node.left, node.right) > 0:
         new.right = TreapNode(node=new.right)
         new = Treap.__rotateLeft(new)
         new.left = ImmutableTreap.__delete(new.left, value)
      else:
         new.left = TreapNode(node=new.left)
         new = Treap.__rotateRight(new)
         new.right = ImmutableTreap.__delete(new.right, value)

      return new


   @staticmethod
   def __merge(A, B):
      if A is None: return B
      if B is None: return A

      if A.priority < B.priority:
         R = TreapNode(node=B)
         R.left = ImmutableTreap.__merge(A, B.left)
      else:
         R = TreapNode(node=A)
         R.right = ImmutableTreap.__merge(A.right, B)

      return R


def main():

   return 0


if __name__ == '__main__':
   import sys
   sys.exit(main())

