#!/usr/bin/python


from treap import Treap
from treap import TreapNode


class MutableTreap(Treap):

   def __init__(self):
      Treap.__init__(self)
      self.root = None

   def insert(self, value, priority=None):
      if not self.contains(value):
         self.root = MutableTreap.__insert(self.root, value, priority)

   def delete(self, value):
      if self.contains(value):
         self.root = MutableTreap.__delete(self.root, value)

   def merge(self, other):
      self.root = MutableTreap.__merge(self.root, other.root)

   def split(self, value):
      self.root = MutableTreap.__insert(self.root, value, TreapNode.INFINITY)

      right = MutableTreap()
      right.root = self.root.right
      self.root = self.root.left

      return right
      

   @staticmethod
   def __insert(node, value, priority=None):
      if node is None:
         return TreapNode(value, priority)

      if node.value < value:
         node.right = MutableTreap.__insert(node.right, value, priority)
         if node.right.priority > node.priority:
            node = Treap.__rotateLeft(node)
      else:
         node.left  = MutableTreap.__insert(node.left,  value, priority)
         if node.left.priority > node.priority:
            node = Treap.__rotateRight(node)

      return node


   @staticmethod
   def __delete(node, value):
      if node.left is None and node.right is None:
         node = None
      elif node.value > value:
         node.left = MutableTreap.__delete(node.left, value)
      elif node.value < value:
         node.right = MutableTreap.__delete(node.right, value)
      elif Treap.cmp(node.left, node.right) > 0: 
         node = Treap.__rotateLeft(node)
         node.left = MutableTreap.__delete(node.left, value)
      else:
         node = Treap.__rotateRight(node)
         node.right = MutableTreap.__delete(node.right, value)

      return node


   @staticmethod
   def __merge(A, B):
      if A is None: return B
      if B is None: return A

      if A.priority < B.priority:
         B.left = MutableTreap.__merge(A, B.left)
         return B
      else:
         A.right = MutableTreap.__merge(A.right, B)
         return A

