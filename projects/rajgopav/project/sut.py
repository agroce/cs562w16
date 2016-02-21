import copy
import traceback
import re
import sys
from itertools import chain, combinations
# BEGIN STANDALONE CODE
from bintrees import BinaryTree
def displayTree(tree):
        list = []
        printHelper(tree.root, list)
        return list

def printHelper(node, list):
        if node == None:
                return
        list.append(node.key)
        printHelper(node.left,list)
        printHelper(node.right,list)
# END STANDALONE CODE
class sut(object):
    def act0(self):
        self.__test.append(('''self.p_key[0] = 1 ''',self.guard0,self.act0))
        self.log('''self.p_key[0] = 1''')
        try:
            self.p_key[0] = 1

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 1''')
        self.p_key_used[0]=False
    def guard0(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        self.__test.append(('''self.p_key[0] = 2 ''',self.guard1,self.act1))
        self.log('''self.p_key[0] = 2''')
        try:
            self.p_key[0] = 2

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 2''')
        self.p_key_used[0]=False
    def guard1(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        self.__test.append(('''self.p_key[0] = 3 ''',self.guard2,self.act2))
        self.log('''self.p_key[0] = 3''')
        try:
            self.p_key[0] = 3

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 3''')
        self.p_key_used[0]=False
    def guard2(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        self.__test.append(('''self.p_key[0] = 4 ''',self.guard3,self.act3))
        self.log('''self.p_key[0] = 4''')
        try:
            self.p_key[0] = 4

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 4''')
        self.p_key_used[0]=False
    def guard3(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act4(self):
        self.__test.append(('''self.p_key[0] = 5 ''',self.guard4,self.act4))
        self.log('''self.p_key[0] = 5''')
        try:
            self.p_key[0] = 5

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 5''')
        self.p_key_used[0]=False
    def guard4(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act5(self):
        self.__test.append(('''self.p_key[0] = 6 ''',self.guard5,self.act5))
        self.log('''self.p_key[0] = 6''')
        try:
            self.p_key[0] = 6

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 6''')
        self.p_key_used[0]=False
    def guard5(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act6(self):
        self.__test.append(('''self.p_key[0] = 7 ''',self.guard6,self.act6))
        self.log('''self.p_key[0] = 7''')
        try:
            self.p_key[0] = 7

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 7''')
        self.p_key_used[0]=False
    def guard6(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act7(self):
        self.__test.append(('''self.p_key[0] = 8 ''',self.guard7,self.act7))
        self.log('''self.p_key[0] = 8''')
        try:
            self.p_key[0] = 8

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 8''')
        self.p_key_used[0]=False
    def guard7(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act8(self):
        self.__test.append(('''self.p_key[0] = 9 ''',self.guard8,self.act8))
        self.log('''self.p_key[0] = 9''')
        try:
            self.p_key[0] = 9

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 9''')
        self.p_key_used[0]=False
    def guard8(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act9(self):
        self.__test.append(('''self.p_key[0] = 10 ''',self.guard9,self.act9))
        self.log('''self.p_key[0] = 10''')
        try:
            self.p_key[0] = 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_key[0] = 10''')
        self.p_key_used[0]=False
    def guard9(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act10(self):
        self.__test.append(('''self.p_val[0] = 1 ''',self.guard10,self.act10))
        self.log('''self.p_val[0] = 1''')
        try:
            self.p_val[0] = 1

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 1''')
        self.p_val_used[0]=False
    def guard10(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act11(self):
        self.__test.append(('''self.p_val[0] = 2 ''',self.guard11,self.act11))
        self.log('''self.p_val[0] = 2''')
        try:
            self.p_val[0] = 2

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 2''')
        self.p_val_used[0]=False
    def guard11(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act12(self):
        self.__test.append(('''self.p_val[0] = 3 ''',self.guard12,self.act12))
        self.log('''self.p_val[0] = 3''')
        try:
            self.p_val[0] = 3

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 3''')
        self.p_val_used[0]=False
    def guard12(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act13(self):
        self.__test.append(('''self.p_val[0] = 4 ''',self.guard13,self.act13))
        self.log('''self.p_val[0] = 4''')
        try:
            self.p_val[0] = 4

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 4''')
        self.p_val_used[0]=False
    def guard13(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act14(self):
        self.__test.append(('''self.p_val[0] = 5 ''',self.guard14,self.act14))
        self.log('''self.p_val[0] = 5''')
        try:
            self.p_val[0] = 5

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 5''')
        self.p_val_used[0]=False
    def guard14(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act15(self):
        self.__test.append(('''self.p_val[0] = 6 ''',self.guard15,self.act15))
        self.log('''self.p_val[0] = 6''')
        try:
            self.p_val[0] = 6

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 6''')
        self.p_val_used[0]=False
    def guard15(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act16(self):
        self.__test.append(('''self.p_val[0] = 7 ''',self.guard16,self.act16))
        self.log('''self.p_val[0] = 7''')
        try:
            self.p_val[0] = 7

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 7''')
        self.p_val_used[0]=False
    def guard16(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act17(self):
        self.__test.append(('''self.p_val[0] = 8 ''',self.guard17,self.act17))
        self.log('''self.p_val[0] = 8''')
        try:
            self.p_val[0] = 8

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 8''')
        self.p_val_used[0]=False
    def guard17(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act18(self):
        self.__test.append(('''self.p_val[0] = 9 ''',self.guard18,self.act18))
        self.log('''self.p_val[0] = 9''')
        try:
            self.p_val[0] = 9

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 9''')
        self.p_val_used[0]=False
    def guard18(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act19(self):
        self.__test.append(('''self.p_val[0] = 10 ''',self.guard19,self.act19))
        self.log('''self.p_val[0] = 10''')
        try:
            self.p_val[0] = 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_val[0] = 10''')
        self.p_val_used[0]=False
    def guard19(self):
        return (((self.p_val_used[0]) or (self.p_val[0] == None) or (self.__relaxUsedRestriction)))
    
    def act20(self):
        self.__test.append(('''self.p_list[0] = [] ''',self.guard20,self.act20))
        self.log('''self.p_list[0] = []''')
        try:
            self.p_list[0] = []

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_list[0] = []''')
        self.p_list_used[0]=False
    def guard20(self):
        return (((self.p_list_used[0]) or (self.p_list[0] == None) or (self.__relaxUsedRestriction)))
    
    def act21(self):
        self.__test.append(('''self.p_bt[0]  = BinaryTree() ''',self.guard21,self.act21))
        self.log('''self.p_bt[0]  = BinaryTree()''')
        try:
            self.p_bt[0]  = BinaryTree()

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_bt[0]  = BinaryTree()''')
        self.p_bt_used[0]=False
    def guard21(self):
        return (((self.p_bt_used[0]) or (self.p_bt[0] == None) or (self.__relaxUsedRestriction)))
    
    def act22(self):
        self.__test.append(('''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0] ''',self.guard22,self.act22))
        self.log('''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0]''')
        try:
            self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0]''')
        self.p_bt_used[0]=True
        self.p_val_used[0]=True
        self.p_val_used[0]=True
        self.p_key_used[0]=True
    def guard22(self):
        return (self.p_bt[0] != None) and (self.p_bt[0] != None) and (self.p_list[0] != None) and (self.p_val[0] != None) and (self.p_val[0] != None) and (self.p_key[0] != None)
    
    def act23(self):
        self.__test.append(('''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0] ''',self.guard23,self.act23))
        self.log('''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0]''')
        try:
            self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0])
        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.logPost('''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0]''')
        self.p_key_used[0]=True
        self.p_key_used[0]=True
        self.p_key_used[0]=True
        self.p_key_used[0]=True
    def guard23(self):
        return (self.p_bt[0] != None) and (self.p_bt[0] != None) and (self.p_bt[0] != None) and (self.p_bt[0] != None) and (self.p_bt[0] != None) and (self.p_list[0] != None) and (self.p_list[0] != None) and (self.p_key[0] != None) and (self.p_key[0] != None) and (self.p_key[0] != None) and (self.p_key[0] != None) and (len(self.p_bt[0]) > 5)
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__modules.append(r"bintree.py")
        self.__features = []
        self.__replayBacktrack = False
        self.__noReassigns = False
        self.__test = []
        self.__pools = []
        self.__psize = {}
        self.__consts = []
        self.p_bt = {}
        self.p_bt_used = {}
        self.__psize["bt"] = 1
        self.__pools.append("self.p_bt")
        self.p_bt[0] = None
        self.p_bt_used[0] = True
        self.p_bt[1] = None
        self.p_bt_used[1] = True
        self.p_list = {}
        self.p_list_used = {}
        self.__psize["list"] = 1
        self.__pools.append("self.p_list")
        self.p_list[0] = None
        self.p_list_used[0] = True
        self.p_list[1] = None
        self.p_list_used[1] = True
        self.p_val = {}
        self.p_val_used = {}
        self.__psize["val"] = 1
        self.__pools.append("self.p_val")
        self.p_val[0] = None
        self.p_val_used[0] = True
        self.p_val[1] = None
        self.p_val_used[1] = True
        self.p_key = {}
        self.p_key_used = {}
        self.__psize["key"] = 1
        self.__pools.append("self.p_key")
        self.p_key[0] = None
        self.p_key_used[0] = True
        self.p_key[1] = None
        self.p_key_used[1] = True
    # BEGIN INITIALIZATION CODE
    # END INITIALIZATION CODE
        self.__actions = []
        self.__names = {}
        self.__poolPrefix = "self.p_"
        self.__names["<<RESTART>>"] = ("<<RESTART>>", lambda x: True, lambda x: self.restart())
        self.__orderings = {}
        self.__okExcepts = {}
        self.__preCode = {}
        self.__refCode = {}
        self.__propCode = {}
        self.__orderings["<<RESTART>>"] = -1
        self.__failure = None
        self.__log = None
        self.__logAction = self.logPrint
        self.__relaxUsedRestriction = False
        self.__simplifyCache = {}
        self.__actions.append(('''self.p_key[0] = 1 ''',self.guard0,self.act0))

        self.__names['''self.p_key[0] = 1 '''] = ('''self.p_key[0] = 1 ''',self.guard0,self.act0)

        self.__orderings['''self.p_key[0] = 1 '''] = 1

        self.__okExcepts['''self.p_key[0] = 1 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 2 ''',self.guard1,self.act1))

        self.__names['''self.p_key[0] = 2 '''] = ('''self.p_key[0] = 2 ''',self.guard1,self.act1)

        self.__orderings['''self.p_key[0] = 2 '''] = 2

        self.__okExcepts['''self.p_key[0] = 2 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 3 ''',self.guard2,self.act2))

        self.__names['''self.p_key[0] = 3 '''] = ('''self.p_key[0] = 3 ''',self.guard2,self.act2)

        self.__orderings['''self.p_key[0] = 3 '''] = 3

        self.__okExcepts['''self.p_key[0] = 3 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 4 ''',self.guard3,self.act3))

        self.__names['''self.p_key[0] = 4 '''] = ('''self.p_key[0] = 4 ''',self.guard3,self.act3)

        self.__orderings['''self.p_key[0] = 4 '''] = 4

        self.__okExcepts['''self.p_key[0] = 4 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 5 ''',self.guard4,self.act4))

        self.__names['''self.p_key[0] = 5 '''] = ('''self.p_key[0] = 5 ''',self.guard4,self.act4)

        self.__orderings['''self.p_key[0] = 5 '''] = 5

        self.__okExcepts['''self.p_key[0] = 5 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 6 ''',self.guard5,self.act5))

        self.__names['''self.p_key[0] = 6 '''] = ('''self.p_key[0] = 6 ''',self.guard5,self.act5)

        self.__orderings['''self.p_key[0] = 6 '''] = 6

        self.__okExcepts['''self.p_key[0] = 6 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 7 ''',self.guard6,self.act6))

        self.__names['''self.p_key[0] = 7 '''] = ('''self.p_key[0] = 7 ''',self.guard6,self.act6)

        self.__orderings['''self.p_key[0] = 7 '''] = 7

        self.__okExcepts['''self.p_key[0] = 7 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 8 ''',self.guard7,self.act7))

        self.__names['''self.p_key[0] = 8 '''] = ('''self.p_key[0] = 8 ''',self.guard7,self.act7)

        self.__orderings['''self.p_key[0] = 8 '''] = 8

        self.__okExcepts['''self.p_key[0] = 8 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 9 ''',self.guard8,self.act8))

        self.__names['''self.p_key[0] = 9 '''] = ('''self.p_key[0] = 9 ''',self.guard8,self.act8)

        self.__orderings['''self.p_key[0] = 9 '''] = 9

        self.__okExcepts['''self.p_key[0] = 9 '''] = ''''''

        self.__actions.append(('''self.p_key[0] = 10 ''',self.guard9,self.act9))

        self.__names['''self.p_key[0] = 10 '''] = ('''self.p_key[0] = 10 ''',self.guard9,self.act9)

        self.__orderings['''self.p_key[0] = 10 '''] = 10

        self.__okExcepts['''self.p_key[0] = 10 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 1 ''',self.guard10,self.act10))

        self.__names['''self.p_val[0] = 1 '''] = ('''self.p_val[0] = 1 ''',self.guard10,self.act10)

        self.__orderings['''self.p_val[0] = 1 '''] = 11

        self.__okExcepts['''self.p_val[0] = 1 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 2 ''',self.guard11,self.act11))

        self.__names['''self.p_val[0] = 2 '''] = ('''self.p_val[0] = 2 ''',self.guard11,self.act11)

        self.__orderings['''self.p_val[0] = 2 '''] = 12

        self.__okExcepts['''self.p_val[0] = 2 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 3 ''',self.guard12,self.act12))

        self.__names['''self.p_val[0] = 3 '''] = ('''self.p_val[0] = 3 ''',self.guard12,self.act12)

        self.__orderings['''self.p_val[0] = 3 '''] = 13

        self.__okExcepts['''self.p_val[0] = 3 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 4 ''',self.guard13,self.act13))

        self.__names['''self.p_val[0] = 4 '''] = ('''self.p_val[0] = 4 ''',self.guard13,self.act13)

        self.__orderings['''self.p_val[0] = 4 '''] = 14

        self.__okExcepts['''self.p_val[0] = 4 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 5 ''',self.guard14,self.act14))

        self.__names['''self.p_val[0] = 5 '''] = ('''self.p_val[0] = 5 ''',self.guard14,self.act14)

        self.__orderings['''self.p_val[0] = 5 '''] = 15

        self.__okExcepts['''self.p_val[0] = 5 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 6 ''',self.guard15,self.act15))

        self.__names['''self.p_val[0] = 6 '''] = ('''self.p_val[0] = 6 ''',self.guard15,self.act15)

        self.__orderings['''self.p_val[0] = 6 '''] = 16

        self.__okExcepts['''self.p_val[0] = 6 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 7 ''',self.guard16,self.act16))

        self.__names['''self.p_val[0] = 7 '''] = ('''self.p_val[0] = 7 ''',self.guard16,self.act16)

        self.__orderings['''self.p_val[0] = 7 '''] = 17

        self.__okExcepts['''self.p_val[0] = 7 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 8 ''',self.guard17,self.act17))

        self.__names['''self.p_val[0] = 8 '''] = ('''self.p_val[0] = 8 ''',self.guard17,self.act17)

        self.__orderings['''self.p_val[0] = 8 '''] = 18

        self.__okExcepts['''self.p_val[0] = 8 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 9 ''',self.guard18,self.act18))

        self.__names['''self.p_val[0] = 9 '''] = ('''self.p_val[0] = 9 ''',self.guard18,self.act18)

        self.__orderings['''self.p_val[0] = 9 '''] = 19

        self.__okExcepts['''self.p_val[0] = 9 '''] = ''''''

        self.__actions.append(('''self.p_val[0] = 10 ''',self.guard19,self.act19))

        self.__names['''self.p_val[0] = 10 '''] = ('''self.p_val[0] = 10 ''',self.guard19,self.act19)

        self.__orderings['''self.p_val[0] = 10 '''] = 20

        self.__okExcepts['''self.p_val[0] = 10 '''] = ''''''

        self.__actions.append(('''self.p_list[0] = [] ''',self.guard20,self.act20))

        self.__names['''self.p_list[0] = [] '''] = ('''self.p_list[0] = [] ''',self.guard20,self.act20)

        self.__orderings['''self.p_list[0] = [] '''] = 21

        self.__okExcepts['''self.p_list[0] = [] '''] = ''''''

        self.__actions.append(('''self.p_bt[0]  = BinaryTree() ''',self.guard21,self.act21))

        self.__names['''self.p_bt[0]  = BinaryTree() '''] = ('''self.p_bt[0]  = BinaryTree() ''',self.guard21,self.act21)

        self.__orderings['''self.p_bt[0]  = BinaryTree() '''] = 22

        self.__okExcepts['''self.p_bt[0]  = BinaryTree() '''] = ''''''

        self.__actions.append(('''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0] ''',self.guard22,self.act22))

        self.__names['''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0] '''] = ('''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0] ''',self.guard22,self.act22)

        self.__orderings['''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0] '''] = 23

        self.__okExcepts['''self.p_bt[0].insert(self.p_key[0],self.p_val[0]); self.p_list[0].append(self.p_val[0]);print self.p_bt[0] '''] = ''''''

        self.__actions.append(('''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0] ''',self.guard23,self.act23))

        self.__names['''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0] '''] = ('''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0] ''',self.guard23,self.act23)

        self.__orderings['''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0] '''] = 24

        self.__okExcepts['''self.p_bt[0].__contains__(self.p_key[0]) and (self.p_bt[0].__getitem__(self.p_key[0]) in self.p_list[0] '''] = ''''''

        self.__actions_backup = list(self.__actions)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
    # BEGIN RELOAD CODE
    # END RELOAD CODE
        self.__noReassigns = False
        self.__test = []
        self.__pools = []
        self.__psize = {}
        self.__consts = []
        self.p_bt = {}
        self.p_bt_used = {}
        self.__psize["bt"] = 1
        self.__pools.append("self.p_bt")
        self.p_bt[0] = None
        self.p_bt_used[0] = True
        self.p_bt[1] = None
        self.p_bt_used[1] = True
        self.p_list = {}
        self.p_list_used = {}
        self.__psize["list"] = 1
        self.__pools.append("self.p_list")
        self.p_list[0] = None
        self.p_list_used[0] = True
        self.p_list[1] = None
        self.p_list_used[1] = True
        self.p_val = {}
        self.p_val_used = {}
        self.__psize["val"] = 1
        self.__pools.append("self.p_val")
        self.p_val[0] = None
        self.p_val_used[0] = True
        self.p_val[1] = None
        self.p_val_used[1] = True
        self.p_key = {}
        self.p_key_used = {}
        self.__psize["key"] = 1
        self.__pools.append("self.p_key")
        self.p_key[0] = None
        self.p_key_used[0] = True
        self.p_key[1] = None
        self.p_key_used[1] = True
        try:
            test_after_restart(self)
        except:
            pass
    def log(self, name):
        if self.__log == None:
            return
        if (self.__log == 'All') or (self.__log >= 1):
            try:
                self.__logAction(name,"""displayTree(self.p_bt[0])""",displayTree(self.p_bt[0]),False)
            except:
                pass
    def logPost(self, name):
        if self.__log == None:
            return
        if (self.__log == 'All') or (self.__log >= 1):
            try:
                self.__logAction(name,"""displayTree(self.p_bt[0])""",displayTree(self.p_bt[0]),True)
            except:
                pass
    def state(self):
        if self.__replayBacktrack:
            return self.captureReplay(self.__test)
        return [ copy.deepcopy(self.p_bt),copy.deepcopy(self.p_bt_used),copy.deepcopy(self.p_list),copy.deepcopy(self.p_list_used),copy.deepcopy(self.p_val),copy.deepcopy(self.p_val_used),copy.deepcopy(self.p_key),copy.deepcopy(self.p_key_used)]
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_bt = copy.deepcopy(old[0])
        self.p_bt_used = copy.deepcopy(old[1])
        self.p_list = copy.deepcopy(old[2])
        self.p_list_used = copy.deepcopy(old[3])
        self.p_val = copy.deepcopy(old[4])
        self.p_val_used = copy.deepcopy(old[5])
        self.p_key = copy.deepcopy(old[6])
        self.p_key_used = copy.deepcopy(old[7])
    def check(self):
        return True
    """
    BOILERPLATE METHODS OF SUT
    ==========================
    These are the set of methods available on each SUT by default
    
    Examples
    --------
    
    t.enabled()
    t.actions()
    """
    
    def setReplayBacktrack(self, val):
        self.__replayBacktrack = val
    
    def test(self):
        """
        Returns the current test as a sequence of (name, guard, actions)
        """
        return self.__test
    
    def getOkExceptions(self,name):
        return self.__okExcepts[name]
    
    def getPreCode(self,name):
        try:
            return self.__preCode[name]
        except:
            return None
    
    def getRefCode(self,name):
        try:
            return self.__refCode[name]
        except:
            return None
    
    def getPropCode(self,name):
        try:
            return self.__propCode[name]
        except:
            return None        
    
    
    def prettyName(self, name):
        newName = name
        for p in self.__pools:
            pfind = newName.find(p+"[")
            while pfind != -1:
                closePos = newName.find("]",pfind)
                findRef = newName.find("_REF",pfind)
                index = newName[newName.find("[",pfind)+1:closePos]
                access = newName[pfind:newName.find("]",pfind)+1]
                if (findRef != -1) and (findRef < closePos):
                    newAccess = p.replace(self.__poolPrefix,"") + "_REF" + index                
                else:
                    newAccess = p.replace(self.__poolPrefix,"") + index
                newName = newName.replace(access, newAccess)
                pfind = newName.find(p+"[")
        return newName
    
    def prettyPrintTest(self, test, columns=80):
        i = 0
        for (s,_,_) in test:
            steps = "# STEP " + str(i)
            print self.prettyName(s).ljust(columns - len(steps),' '),steps
            i += 1
    
    def captureReplay(self, test):
        captured = ""
        for step in test:
            captured += self.serializable(step)
            captured += "#!#!"
        return captured[:-4]
    
    def replayable(self,stest):
        steps = stest.split("#!#!")
        if steps == ['']:
            return []
        return map(self.playable, steps)
    
    def enabled(self):
        """
        Returns all enabled action objects.
        """
        return filter(lambda (s, g, a): g(), self.__actions)
    
    def features(self):
        return self.__features
    
    def actions(self):
        """
        Returns all the action objects whether enabled or disabled.
        """
        return self.__actions
    
    def disable(self,f):
        """
        Disable an action by name.
        """
        newActions = []
        for (name, act, guard) in self.__actions:
            if not re.match(f, name):
                newActions.append((name, act, guard))
        self.__actions = newActions
    
    def enableAll(self):
        """
        Enable all actions.
        """
        self.__actions = self.__actions_backup
    
    def serializable(self, step):
        return step[0]
    
    def playable(self, name):
        return self.__names[name]
    
    def safely(self, act):
        try:
            act[2]()
        except:
            self.__failure = sys.exc_info()
            return False
        return True
    
    def failure(self):
        return self.__failure
    
    def replay(self, test, catchUncaught = False):
        self.restart()
        for (name, guard, act) in test:
            if guard():
                if catchUncaught:
                    try:
                        act()
                    except:
                        pass
                else:
                    act()
                    
            if not self.check():
                return False
        return True
    
    def replayUntil(self, test, pred, catchUncaught = False):
        self.restart()
        newt = []
        if pred():
            return newt
    
        for (name, guard, act) in test:
    
            newt.append((name, guard, act))
            if guard():
                if catchUncaught:
                    try:
                        act()
                    except:
                        pass
                else:
                    act()
            if pred():
                return newt
            if not self.check():
                return False
        return None
    
    def failsCheck(self, test):
        try:
            return not self.replay(test, catchUncaught = True)
        except:
            return True
        return False
    
    def fails(self, test):
        try:
            return not self.replay(test)
        except:
            return True
        return False
    
    def logOff(self):
        self.__log = None
    
    def logAll(self):
        self.__log = 'All'
    
    def setLog(self, level):
        self.__log = level
    
    def setLogAction(self, f):
        self.__logAction = f
    
    def logPrint(self, name, code, text, after):
        print "[",
        if after:
            print "POST",
        print "LOG " + name + "  :  " + str(code) + "] " + str(text)
    
    def __candidates(self, t, n):
        candidates = []
        s = len(t) / n
        for i in xrange(0,n):
            tc = t[0:i*s]
            tc.extend(t[(i+1)*s:])
            candidates.append(tc)
        return candidates
    
    def reduce(self, test, pred, pruneGuards = False, keepLast = True):
        """
        This function takes a test that has failed, and attempts to reduce it using a simplified version of Zeller's Delta-Debugging algorithm.
        pruneGuards determines if disabled guards are automatically removed from reduced tests, keepLast determines if the last action must remain unchanged
        (this is useful for keeping the fault detected from changing).
        """
        try:
            test_before_reduce(self)
        except:
            pass
    
        if len(test) < 2:
            return test
        
        if keepLast:
            tb = test[:-1]
            addLast = [test[-1]]
        else:
            tb = test
            addLast = []
        n = 2
        count = 0
        stests = {}
        while True:
            stest = self.captureReplay(tb)
            assert ((stest,n) not in stests)
            stests[(stest,n)] = True
            count += 1
            c = self.__candidates(tb, n)
            reduced = False
            for tc in c:
                if pred(tc + addLast):
                    tb = tc
                    n = 2
                    if pruneGuards:
                        self.restart()
                        newtb = []
                        for a in tb:
                            if a[1]():
                                newtb.append(a)
                                try:
                                    a[2]()
                                except:
                                    pass
                        tb = newtb
                    reduced = True
                    break
            if not reduced:
                if n == len(tb):
                    try:
                        test_after_reduce(self)
                    except:
                        pass
                    return tb + addLast
                n = min(n*2, len(tb))
            elif len(tb) == 1:
                try:
                    test_after_reduce(self)
                except:
                    pass
                if pred([] + addLast):
                    return ([] + addLast)
                else:
                    return (tb + addLast)
    
    def poolUses(self,str):
        uses = []
        for p in self.__pools:
            pos = str.find(p,0)
            while pos != -1:
                access  = str[pos:str.find("]",pos)+1]
                if access not in uses:
                    uses.append((access,access[access.find("[")+1:access.find("]")]))
                pos = str.find(p,pos+1)
        return uses
    
    def powerset(self,iterable):
        xs = list(iterable)
        return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1) )
    
    def reduceEssentials(self, test, original, pred, pruneGuards = False, keepLast = True):
        possibleRemove = test
        if keepLast:
            possibleRemove = test[:-1]
        removals = list(self.powerset(possibleRemove))
        removals = sorted(removals, key=lambda x: len(x), reverse=True)
        workingRemovals = []
        failedRemovals = []
        for rset in removals:
            if rset == []:
                continue
            foundSuperset = False
            for (w, _) in workingRemovals:
                allPresent = True
                for r in rset:
                    if r not in w:
                        allPresent = False
                        break
                if allPresent:
                    foundSuperset = True
                    break
            if foundSuperset:
                continue
            newOrig = filter(lambda x: x not in rset, original)
            if pred(newOrig):
                reduced = self.reduce(newOrig, pred, pruneGuards, keepLast)
                workingRemovals.append((rset,reduced))
            else:
                failedRemovals.append(rset)
        return (workingRemovals, failedRemovals)
                
    def actionModify(self,action,old,new):
        name = action[0]
        newName = name.replace(old,new)
        return self.__names[newName]
    
    def levDist(self,s1,s2):
        if len(s1) > len(s2):
            s1,s2 = s2,s1
        distances = range(len(s1) + 1)
        for index2,char2 in enumerate(s2):
            newDistances = [index2+1]
            for index1,char1 in enumerate(s1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1+1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]
    
    def getEnabled(self, test, checkEnabled):
        self.restart()
        enableChange = {}
        for i in xrange(0,len(test)):
            if checkEnabled:
                enableChange[i] = map(lambda x:x[0], self.enabled())
                self.safely(test[i])
            else:
                enableChange[i] = map(lambda x:x[0], self.actions())
        return enableChange
    
    def numReassigns(self, test):
    
        if not self.__noReassigns:
            return 0
        
        lhsPools = []
        reuses = []
    
        i = 0
        for s in test:
            if " = " in s[0]:
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if len(lhsp) == 1:
                    for p in self.poolUses(lhs):
                        if p in lhsPools:
                            reuses.append((i,p))
                        else:
                            lhsPools.append(p)
            i += 1
        return len(reuses)
    
    def reduceLengthStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING REDUCE LENGTH STEP"
        # Replace any action with another action, if that allows test to be further reduced
        enableChange = self.getEnabled(test,checkEnabled)
    
        reassignCount = self.numReassigns(test)
        
        for i in xrange(0,len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue        
            for name2 in enableChange[i]:
                if name1 != name2:
                    if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        rtestC = self.reduce(testC, pred, pruneGuards, keepLast)
                        if len(rtestC) < len(test):
                            if verbose:
                                print "NORMALIZER: RULE ReduceAction: STEP",i,name1,"-->",name2,"REDUCING LENGTH FROM",len(test),"TO",len(rtestC)
                            return (True, rtestC)
        return (False, test)
    
    def replaceAllStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING REPLACE ALL STEP"    
        # Replace all occurrences of an action with a simpler action
        enableChange = self.getEnabled(test,checkEnabled)    
    
        reassignCount = self.numReassigns(test)
        
        donePairs = []
        for i in xrange(0,len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue        
            for name2 in enableChange[i]:
                if (self.__orderings[name1] > self.__orderings[name2]) and ((name1,name2) not in donePairs):
                    if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                        continue
                    donePairs.append((name1,name2))
                    testC = map(lambda x: self.actionModify(x,name1,name2), test)
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print "NORMALIZER: RULE SimplifyAll:",name1,"-->",name2
                        return (True, testC)
        return (False, test)
    
    def replacePoolStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING REPLACE POOL STEP"        
        # Replace pools with lower-numbered pools
    
        pools = []
        for s in test:
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p)
    
        reassignCount = self.numReassigns(test)                
    
        # First try the simple version:
    
        if self.__noReassigns:
        
            for (p,i) in pools:
                for n in xrange(0,int(i)):
                    new = p.replace("["+i+"]","[" + str(n) + "]")    
                    testC = map(lambda x: self.actionModify(x,p,new), test)
                    if (testC != test) and (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print "NORMALIZER: RULE ReplacePool:",p,"WITH",new
                        return (True, testC)    
    
            # Remained of this code is now not needed, probably, due to noReassignRule
            return (False, test)
        
        # Reduce number of pools but may need to move assignment to a later position, or only change after the position
        for pos in xrange(0,len(test)):
            for (p,i) in pools:
                for n in xrange(0,int(i)):
                    new = p.replace("["+i+"]","[" + str(n) + "]")    
                    prefix = []
                    moved = []
                    for j in xrange(0,pos):
                        if new in test[j][0]:
                            moved.append(test[j])
                        else:
                            prefix.append(test[j])
                    suffix = map(lambda x: self.actionModify(x,p,new), moved + test[pos:])
                    testC = prefix + map(lambda x: self.actionModify(x,p,new), suffix)
                    if (testC != test) and (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            if pos == 0:
                                print "NORMALIZER: RULE ReplacePool:",p,"WITH",new
                            else:
                                print "NORMALIZER: RULE ReplaceMovePool:",p,"WITH",new," -- MOVED TO",pos
                        return (True, testC)
                    # Not possible, try with only replacing between pos and pos2
                    for pos2 in xrange(len(test),pos,-1):
                        prefix = test[:pos]
                        suffix = map(lambda x: self.actionModify(x,p,new), test[pos:pos2])
                        testC = prefix + suffix + test[pos2:]
                        if (testC != test) and (self.numReassigns(testC) <= reassignCount) and pred(testC):
                            if verbose:
                                print "NORMALIZER: RULE ReplacePool:",p,"WITH",new,"FROM",pos,"TO",pos2
                            return (True, testC)
        return (False, test)
    
    
    def replaceSingleStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING REPLACE SINGLE STEP"        
        # Replace any single action with a lower-numbered action
        enableChange = self.getEnabled(test,checkEnabled)    
    
        reassignCount = self.numReassigns(test)
        
        for i in xrange(0,len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue        
            for name2 in enableChange[i]:
                if self.__orderings[name1] > self.__orderings[name2]:
                    if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print "NORMALIZER: RULE SimplifySingle: STEP",i,name1,"-->",name2
                        return (True, testC)
        return (False, test)
    
    def swapPoolStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING SWAP POOL STEP"        
        # Swap two pool uses in between two positions, if this lowers the minimal action ordering between them
        pools = []
        for s in test:
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p)
    
        reassignCount = self.numReassigns(test)
                    
        swaps = []
        for (p1,i1) in pools:
            for (p2,i2) in pools:
                for pos1 in xrange(0,len(test)):
                    for pos2 in xrange(len(test),pos1,-1):
                        if (p1 != p2) and (p1.split("[")[0] == p2.split("[")[0]):
                            p1new = p1.replace("[" + i1 + "]", "[" + i2 + "]")
                            p2new = p2.replace("[" + i2 + "]", "[" + i1 + "]")
                            p2newTemp = p2.replace("[" + i2 + "]", "[**]")
                            tempTest = map(lambda x:(x[0].replace(p2,p2newTemp),x[1],x[2]), test[pos1:pos2])
                            tempTest2 = map(lambda x:(x[0].replace(p1,p1new),x[1],x[2]), tempTest)
                            testC = test[:pos1] + map(lambda x: self.actionModify(x,p2newTemp,p2new), tempTest2) + test[pos2:]
                            leastTestC = -1
                            leastTest = -1
                            for s in xrange(0,len(test)):
                                if test[s] != testC[s]:
                                    ordTest = self.__orderings[test[s][0]]
                                    if (leastTest == -1) or (ordTest < leastTest):
                                        leastTest = ordTest
                                    ordTestC = self.__orderings[testC[s][0]]
                                    if (leastTestC == -1) or (ordTestC < leastTestC):
                                        leastTestC = ordTestC
                            if leastTestC < leastTest:
                                if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                                    if verbose:
                                        print "NORMALIZER: RULE SwapPool:",p1,"AND",p2,"BETWEEN STEP",pos1,"AND",pos2
                                    return (True, testC)
        return (False, test)
    
    def noReassignStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if not self.__noReassigns:
            return (False, test)
        
        if verbose == "VERY":
            print "STARTING NOREASSIGNS STEP"
        # Replace reassignments with fresh variables
        pools = []
        lhsPools = []
        reuses = []
    
        i = 0
        for s in test:
            if " = " in s[0]:
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if len(lhsp) == 1:
                    for p in self.poolUses(lhs):
                        if p in lhsPools:
                            reuses.append((i,p))
                        else:
                            lhsPools.append(p)
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p[0])
            i += 1
    
        for (i,pu) in reuses:
            prefix = test[0:i]
            (p,pnum) = pu
            newp = None
            for ni in xrange(0,self.__psize[p.split("[")[0].replace(self.__poolPrefix,"")]):
                if int(ni) == int(pnum):
                    continue
                tnewp = p.replace("[" + str(pnum) + "]","[" + str(ni) + "]")
                print "REPLACING",tnewp,ni,p,pnum
                if tnewp not in pools:
                    newp = tnewp
                    break
            if newp == None:
                continue
            if verbose:
                print "NORMALIZER: RULE NoReassigns:",i,test[i][0],p,"TO",newp
            suffix = []
            for s in test[i:]:
                suffix.append(self.actionModify(s,p,newp))
            return (True, prefix+suffix)
                
        return (False, test)
    
    def swapActionOrderStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING SWAP ACTION ORDER STEP"        
        # Try to swap any out-of-order actions
        lastMover = len(test)
        if keepLast:
            lastMover -= 1
            
        for i in xrange(0,lastMover):
            for j in xrange(i+1,lastMover):
                step1 = test[i][0]
                step2 = test[j][0]
                if self.__orderings[step2] < self.__orderings[step1]:
                        frag1 = test[:i]
                        frag2 = [test[j]]
                        frag3 = test[i+1:j]
                        frag4 = [test[i]]
                        frag5 = test[j+1:]
                        testC = frag1 + frag2 + frag3 + frag4 + frag5
                        if pred(testC):
                            if verbose:
                                print "NORMALIZER: RULE SwapAction:",i,test[i][0],"WITH STEP",j,test[j][0]
                            return (True, testC)
        return (False, test)
    
    def normalize(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, speed = "FAST", checkEnabled = False, distLimit = None, reorder=True,
                  noReassigns = False):
        """
        Attempts to produce a normalized test case
        """
        try:
            test_before_normalize(self)
        except:
            pass
    
        if noReassigns:
            self.__noReassigns = True
        else:
            self.__noReassigns = False
        
        # Check the cache
        stest = self.captureReplay(test)
        if stest in self.__simplifyCache:
            if verbose:
                print "NORMALIZER: FOUND TEST IN CACHED RESULTS"
            return self.__simplifyCache[stest]
        history = [stest]
            
        # Turns off requirement that you can't initialize an unused variable, allowing reducer to take care of redundant assignments
        self.relax()
                 
        # Default speed is fast, if speed not recognized
        simplifiers = [self.noReassignStep, self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep, self.reduceLengthStep]
        #simplifiers = [self.noReassignStep, self.replaceAllStep, self.replaceSingleStep, self.swapActionOrderStep, self.reduceLengthStep]
        # Default approach tries a reduce after any change
        reduceOnChange = True
        if speed == "SLOW":
            simplifiers = [self.reduceLengthStep, self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep]
        elif speed == "ONEREDUCE":
            # Runs one attempt at length reduction before normal simplification, without reduction step
            (changed, test) = self.reduceLengthStep(test, pred, pruneGuards, keepLast, verbose, checkEnabled, distLimit)
            if changed:
                stest = self.captureReplay(test)
                history.append(stest)
            simplifiers = [self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep]
        elif speed == "MEDIUM":
            # Runs one attempt at length reduction before normal simplification
            (changed, test) = self.reduceLengthStep(test, pred, pruneGuards, keepLast, verbose)
            if changed:
                stest = self.captureReplay(test)
                history.append(stest)
        elif speed == "VERYFAST":
            reduceOnChange = False
            if distLimit == None:
                distLimit = 3 # maximum of 3 char change when replacing actions!  allows numeric switches, simple pool modifications, but very few method changes
        elif speed == "VERYFASTREDUCE":
            reduceOnChange = True
            if distLimit == None:
                distLimit = 3 # maximum of 3 char change when replacing actions!  allows numeric switches, simple pool modifications, but very few method changes            
    
        numChanges = 0
        changed = True
        stests = {}
        while changed:
            stest = self.captureReplay(test)
            assert (stest not in stests)
            stests[stest] = True
            changed = False
            if reorder:
                newSimplifiers = list(simplifiers)
            for s in simplifiers:
                oldTest = test
                (changed, test) = s(test, pred, pruneGuards, keepLast, verbose, checkEnabled, distLimit)
                if changed:
                    if reduceOnChange:
                        test = self.reduce(test, pred, pruneGuards, keepLast)
                    stest = self.captureReplay(test)
                    if stest in self.__simplifyCache:
                        if verbose:
                            print "NORMALIZER: FOUND TEST IN CACHED RESULTS"
                        result = self.__simplifyCache[stest]
                        for t in history:
                            self.__simplifyCache[t] = result
                        self.stopRelax()
                        return result                
                    history.append(stest)
                    if reorder:
                        simplifiers = newSimplifiers
                    break
                elif reorder:
                    newSimplifiers.remove(s)
                    newSimplifiers.append(s)
    
        # No changes, this is 1-simple (fix-point)
        try:
            test_after_normalize(self)
        except:
            pass
    
        self.stopRelax()
        # restore normal TSTL semantics!
    
        # Update the simplification cache and return
        for t in history:
            self.__simplifyCache[t] = test    
        return test
    
    def freshSimpleVariants(self, name, previous, replacements):
    #    print "FINDING FRESH SIMPLES FOR",name
        prevNames = map(lambda x:x[0], previous)
        prevNames.reverse()
        lastAppear = []
        eqFind = name.find("=")
        if eqFind != -1:
            poolAssign = name[0:eqFind-1]
        else:
            poolAssign = None
        pools = self.poolUses(name)
        lastAppearMap = {}
        for (p,i) in pools:
            for n in prevNames:
                if p[0:p.find("[")] in self.__consts:
                    if n.find(p + " = ") == -1:
                        continue
                lastAppearMap[p] = [n]
                break
            skeys = replacements.keys()
            skeys = filter(lambda x: x < len(previous), skeys)
            skeys = sorted(skeys, reverse = True)
            for i in skeys:
    #            print "i = ",i
                foundAny = False
                for r in replacements[i]:
                    if p[0:p.find("[")] in self.__consts:
                        if r.find(p + " = ") == -1:
                            continue
                    foundAny = True
                    if p in lastAppearMap:
                        lastAppearMap[p].append(r)
                    else:
                        lastAppearMap[p] = [r]
                if foundAny:
                    break
        for n in lastAppearMap:
            lastAppear.extend(lastAppearMap[n])
    #    print "LAST APPEAR = ",lastAppear
        freshSimples = []
        for (p,i) in pools:
            if p == poolAssign:
                continue
            for n in self.__names:
                if n in lastAppear:
                    continue
                if (p + " = ") in n:
                    uses = self.poolUses(n[n.find("=")+1:])
                    if uses == []:
                        freshSimples.append([self.__names[n],self.__names[name]])
        freshSimples = sorted(freshSimples,key = lambda x:self.__orderings[x[0][0]])
        return freshSimples
    
    def generalize(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None,
                   returnCollect = False, collected = None, depth = 0, silent=False, targets = None):
        
        if collected is None:
            collected = {}
    
        newCollected = {}
            
        # Change so double assignments are allowed
        self.relax()
    
        enableChange = self.getEnabled(test,checkEnabled)
        
        canReplace = {}
        canSwap = {}
        canMakeSimple = {}
        for i in xrange(0,len(test)):
            canSwap[i] = []
        for i in xrange(0,len(test)):
            canReplace[i] = []
            canMakeSimple[i] = []
            if i not in enableChange:
                continue
            for a in enableChange[i]:
                if (distLimit != None) and (self.levDist(a, test[i][0]) > distLimit):
                    continue
                if a != test[i][0]:
                    testC = test[:i] + [self.__names[a]] + test[i+1:]
                    if pred(testC):
                        if returnCollect:
                            stestC = self.captureReplay(testC)
                            if stestC not in collected:
                                collected[stestC] = True
                                newCollected[stestC] = True                            
                            if stestC in targets:
                                self.stopRelax()
                                return (True, stestC, dict(collected))                                                    
                        canReplace[i].append(a)
            for j in xrange(i+1,len(test)):
                if i == j or test[i][0] == test[j][0]:
                    continue
                testC = test[:i]+[test[j]]+test[i+1:j]+[test[i]]+test[j+1:]
                if pred(testC):
                    if returnCollect:
                        stestC = self.captureReplay(testC)
                        if stestC not in collected:
                            collected[stestC] = True
                            newCollected[stestC] = True                        
                            if stestC in targets:
                                self.stopRelax()
                                return (True, stestC, dict(collected))                        
                    canSwap[i].append(j)
                    canSwap[j].append(i)
            for v in self.freshSimpleVariants(test[i][0],test[:i],canReplace):
                testC = test[:i] + v + test[i+1:]
                if pred(testC):
                    canMakeSimple[i].append(v)
        if not silent:
            noOrder = []
            endSwappable = -1
            for i in xrange(0,len(test)):
                if endSwappable >= i:
                    continue
                foundSwap = False
                for j in xrange(len(test)-1,i,-1):
                    allSwappable = True
                    for k1 in xrange(i,j+1):
                        for k2 in xrange(k1+1,j+1):
                                if k2 not in canSwap[k1]:
                                        allSwappable = False
                                        break
                        if not allSwappable:
                            break
                    if allSwappable:
                        noOrder.append((i,j))
                        for k1 in xrange(i,j+1):
                            for k2 in xrange(i,j+1):
                                if k2 in canSwap[k1]:
                                    canSwap[k1].remove(k2)
                        endSwappable = j
                        break
            for i in xrange(0,len(test)):
                for (begin,end) in noOrder:
                    if i == begin:
                        print "#["
                pn = self.prettyName(test[i][0])
                spaces = " " * (90-len(pn)-len(" # STEP"))
                print self.prettyName(test[i][0]),spaces,"# STEP",i
                if canReplace[i] != []:
                    firstRep = None
                    lastRep = None
                    for rep in canReplace[i]:
                        if firstRep == None:
                            firstRep = rep
                            lastRep = rep
                        elif self.__orderings[rep] != (self.__orderings[lastRep] + 1):
                            if firstRep == lastRep:
                                print "#  or",self.prettyName(firstRep)
                            else:
                                print "#  or",self.prettyName(firstRep)
                                print "#   -",self.prettyName(lastRep)
                            firstRep = rep
                            lastRep = rep
                        else:
                            lastRep = rep
                    if firstRep == lastRep:
                        print "#  or",self.prettyName(firstRep)
                    else:
                        print "#  or",self.prettyName(firstRep)
                        print "#   -",self.prettyName(lastRep)
                if canMakeSimple[i] != []:
                    for v in canMakeSimple[i]:
                        print "#  or ("
                        for s in v[:-1]:
                            print "#     ",self.prettyName(s[0]),";"
                        print "#     ",self.prettyName(v[-1][0])
                        print "#     )"
                if canSwap[i] != []:
                    if len(canSwap[i]) == 1:
                        print "#  swaps with step",
                    else:
                        print "#  swaps with steps",
                    for j in canSwap[i]:
                        print j,
                    print
                for (begin,end) in noOrder:
                    if i == end:
                        print "#] (steps in [] can be in any order)"
        # Restore semantics
        self.stopRelax()
        if returnCollect:
            if depth == 0:
                return (False, None, dict(collected))
            else:
                allCollected = dict(collected)
                for c in newCollected:
                    (found, stest, cGen) = self.generalize(self.replayable(c), pred, pruneGuards, keepLast, verbose, checkEnabled,
                                                    distLimit, returnCollect=True, collected = allCollected,
                                                    depth = depth-1, silent=True, targets = targets)
                    for c2 in cGen:
                        if c2 not in allCollected:
                            allCollected[c2] = True
                    if found == True:
                        return (True, stest, dict(allCollected))
                return (False, None, dict(allCollected))
    
    def relax(self):
        self.__relaxUsedRestriction = True
    
    def stopRelax(self):
        self.__relaxUsedRestriction = False
