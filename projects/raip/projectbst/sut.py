import copy
import traceback
import re
import sys
from itertools import chain, combinations
import coverage
# BEGIN STANDALONE CODE
import binary_search_tree


def checktreeBST(tree):
	p = tree.inorder()
	s = sorted(set(p))
	if s == p:
	
		return True
	else:

		return False

def _inorder(self,node):
        if node == None:
                return

        if node != None:
                        self._inorder(node.left)

                        if node:
                                self.__nodes.append(node.key)

                        self._inorder(node.right)

        return self.__nodes

def inorder(self):
	self.__nodes = []
     	return self._inorder(self.root)



def checkroot(self):
	if self.root == None:
		return 0
	else:
		return 1
	

# END STANDALONE CODE
class sut(object):
    def act0(self):
        self.__test.append(('''self.p_key[0]= 0 ''',self.guard0,self.act0))
        self.log('''self.p_key[0]= 0''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 0

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 0''')
        self.p_key_used[0]=False
    def guard0(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        self.__test.append(('''self.p_key[0]= 1 ''',self.guard1,self.act1))
        self.log('''self.p_key[0]= 1''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 1''')
        self.p_key_used[0]=False
    def guard1(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        self.__test.append(('''self.p_key[0]= 2 ''',self.guard2,self.act2))
        self.log('''self.p_key[0]= 2''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 2

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 2''')
        self.p_key_used[0]=False
    def guard2(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        self.__test.append(('''self.p_key[0]= 3 ''',self.guard3,self.act3))
        self.log('''self.p_key[0]= 3''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 3

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 3''')
        self.p_key_used[0]=False
    def guard3(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act4(self):
        self.__test.append(('''self.p_key[0]= 4 ''',self.guard4,self.act4))
        self.log('''self.p_key[0]= 4''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 4

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 4''')
        self.p_key_used[0]=False
    def guard4(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act5(self):
        self.__test.append(('''self.p_key[0]= 5 ''',self.guard5,self.act5))
        self.log('''self.p_key[0]= 5''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 5

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 5''')
        self.p_key_used[0]=False
    def guard5(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act6(self):
        self.__test.append(('''self.p_key[0]= 6 ''',self.guard6,self.act6))
        self.log('''self.p_key[0]= 6''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 6

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 6''')
        self.p_key_used[0]=False
    def guard6(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act7(self):
        self.__test.append(('''self.p_key[0]= 7 ''',self.guard7,self.act7))
        self.log('''self.p_key[0]= 7''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 7

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 7''')
        self.p_key_used[0]=False
    def guard7(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act8(self):
        self.__test.append(('''self.p_key[0]= 8 ''',self.guard8,self.act8))
        self.log('''self.p_key[0]= 8''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 8

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 8''')
        self.p_key_used[0]=False
    def guard8(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act9(self):
        self.__test.append(('''self.p_key[0]= 9 ''',self.guard9,self.act9))
        self.log('''self.p_key[0]= 9''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 9

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 9''')
        self.p_key_used[0]=False
    def guard9(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act10(self):
        self.__test.append(('''self.p_key[0]= 10 ''',self.guard10,self.act10))
        self.log('''self.p_key[0]= 10''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[0]= 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[0]= 10''')
        self.p_key_used[0]=False
    def guard10(self):
        return (((self.p_key_used[0]) or (self.p_key[0] == None) or (self.__relaxUsedRestriction)))
    
    def act11(self):
        self.__test.append(('''self.p_key[1]= 0 ''',self.guard11,self.act11))
        self.log('''self.p_key[1]= 0''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 0

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 0''')
        self.p_key_used[1]=False
    def guard11(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act12(self):
        self.__test.append(('''self.p_key[1]= 1 ''',self.guard12,self.act12))
        self.log('''self.p_key[1]= 1''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 1''')
        self.p_key_used[1]=False
    def guard12(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act13(self):
        self.__test.append(('''self.p_key[1]= 2 ''',self.guard13,self.act13))
        self.log('''self.p_key[1]= 2''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 2

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 2''')
        self.p_key_used[1]=False
    def guard13(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act14(self):
        self.__test.append(('''self.p_key[1]= 3 ''',self.guard14,self.act14))
        self.log('''self.p_key[1]= 3''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 3

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 3''')
        self.p_key_used[1]=False
    def guard14(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act15(self):
        self.__test.append(('''self.p_key[1]= 4 ''',self.guard15,self.act15))
        self.log('''self.p_key[1]= 4''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 4

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 4''')
        self.p_key_used[1]=False
    def guard15(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act16(self):
        self.__test.append(('''self.p_key[1]= 5 ''',self.guard16,self.act16))
        self.log('''self.p_key[1]= 5''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 5

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 5''')
        self.p_key_used[1]=False
    def guard16(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act17(self):
        self.__test.append(('''self.p_key[1]= 6 ''',self.guard17,self.act17))
        self.log('''self.p_key[1]= 6''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 6

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 6''')
        self.p_key_used[1]=False
    def guard17(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act18(self):
        self.__test.append(('''self.p_key[1]= 7 ''',self.guard18,self.act18))
        self.log('''self.p_key[1]= 7''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 7

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 7''')
        self.p_key_used[1]=False
    def guard18(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act19(self):
        self.__test.append(('''self.p_key[1]= 8 ''',self.guard19,self.act19))
        self.log('''self.p_key[1]= 8''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 8

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 8''')
        self.p_key_used[1]=False
    def guard19(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act20(self):
        self.__test.append(('''self.p_key[1]= 9 ''',self.guard20,self.act20))
        self.log('''self.p_key[1]= 9''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 9

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 9''')
        self.p_key_used[1]=False
    def guard20(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act21(self):
        self.__test.append(('''self.p_key[1]= 10 ''',self.guard21,self.act21))
        self.log('''self.p_key[1]= 10''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_key[1]= 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_key[1]= 10''')
        self.p_key_used[1]=False
    def guard21(self):
        return (((self.p_key_used[1]) or (self.p_key[1] == None) or (self.__relaxUsedRestriction)))
    
    def act22(self):
        self.__test.append(('''self.p_int[0]= 0 ''',self.guard22,self.act22))
        self.log('''self.p_int[0]= 0''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 0

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 0''')
        self.p_int_used[0]=False
    def guard22(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act23(self):
        self.__test.append(('''self.p_int[0]= 1 ''',self.guard23,self.act23))
        self.log('''self.p_int[0]= 1''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 1''')
        self.p_int_used[0]=False
    def guard23(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act24(self):
        self.__test.append(('''self.p_int[0]= 2 ''',self.guard24,self.act24))
        self.log('''self.p_int[0]= 2''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 2

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 2''')
        self.p_int_used[0]=False
    def guard24(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act25(self):
        self.__test.append(('''self.p_int[0]= 3 ''',self.guard25,self.act25))
        self.log('''self.p_int[0]= 3''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 3

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 3''')
        self.p_int_used[0]=False
    def guard25(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act26(self):
        self.__test.append(('''self.p_int[0]= 4 ''',self.guard26,self.act26))
        self.log('''self.p_int[0]= 4''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 4

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 4''')
        self.p_int_used[0]=False
    def guard26(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act27(self):
        self.__test.append(('''self.p_int[0]= 5 ''',self.guard27,self.act27))
        self.log('''self.p_int[0]= 5''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 5

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 5''')
        self.p_int_used[0]=False
    def guard27(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act28(self):
        self.__test.append(('''self.p_int[0]= 6 ''',self.guard28,self.act28))
        self.log('''self.p_int[0]= 6''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 6

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 6''')
        self.p_int_used[0]=False
    def guard28(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act29(self):
        self.__test.append(('''self.p_int[0]= 7 ''',self.guard29,self.act29))
        self.log('''self.p_int[0]= 7''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 7

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 7''')
        self.p_int_used[0]=False
    def guard29(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act30(self):
        self.__test.append(('''self.p_int[0]= 8 ''',self.guard30,self.act30))
        self.log('''self.p_int[0]= 8''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 8

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 8''')
        self.p_int_used[0]=False
    def guard30(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act31(self):
        self.__test.append(('''self.p_int[0]= 9 ''',self.guard31,self.act31))
        self.log('''self.p_int[0]= 9''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 9

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 9''')
        self.p_int_used[0]=False
    def guard31(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act32(self):
        self.__test.append(('''self.p_int[0]= 10 ''',self.guard32,self.act32))
        self.log('''self.p_int[0]= 10''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[0]= 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[0]= 10''')
        self.p_int_used[0]=False
    def guard32(self):
        return (((self.p_int_used[0]) or (self.p_int[0] == None) or (self.__relaxUsedRestriction)))
    
    def act33(self):
        self.__test.append(('''self.p_int[1]= 0 ''',self.guard33,self.act33))
        self.log('''self.p_int[1]= 0''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 0

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 0''')
        self.p_int_used[1]=False
    def guard33(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act34(self):
        self.__test.append(('''self.p_int[1]= 1 ''',self.guard34,self.act34))
        self.log('''self.p_int[1]= 1''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 1''')
        self.p_int_used[1]=False
    def guard34(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act35(self):
        self.__test.append(('''self.p_int[1]= 2 ''',self.guard35,self.act35))
        self.log('''self.p_int[1]= 2''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 2

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 2''')
        self.p_int_used[1]=False
    def guard35(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act36(self):
        self.__test.append(('''self.p_int[1]= 3 ''',self.guard36,self.act36))
        self.log('''self.p_int[1]= 3''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 3

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 3''')
        self.p_int_used[1]=False
    def guard36(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act37(self):
        self.__test.append(('''self.p_int[1]= 4 ''',self.guard37,self.act37))
        self.log('''self.p_int[1]= 4''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 4

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 4''')
        self.p_int_used[1]=False
    def guard37(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act38(self):
        self.__test.append(('''self.p_int[1]= 5 ''',self.guard38,self.act38))
        self.log('''self.p_int[1]= 5''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 5

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 5''')
        self.p_int_used[1]=False
    def guard38(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act39(self):
        self.__test.append(('''self.p_int[1]= 6 ''',self.guard39,self.act39))
        self.log('''self.p_int[1]= 6''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 6

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 6''')
        self.p_int_used[1]=False
    def guard39(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act40(self):
        self.__test.append(('''self.p_int[1]= 7 ''',self.guard40,self.act40))
        self.log('''self.p_int[1]= 7''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 7

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 7''')
        self.p_int_used[1]=False
    def guard40(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act41(self):
        self.__test.append(('''self.p_int[1]= 8 ''',self.guard41,self.act41))
        self.log('''self.p_int[1]= 8''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 8

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 8''')
        self.p_int_used[1]=False
    def guard41(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act42(self):
        self.__test.append(('''self.p_int[1]= 9 ''',self.guard42,self.act42))
        self.log('''self.p_int[1]= 9''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 9

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 9''')
        self.p_int_used[1]=False
    def guard42(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act43(self):
        self.__test.append(('''self.p_int[1]= 10 ''',self.guard43,self.act43))
        self.log('''self.p_int[1]= 10''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_int[1]= 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_int[1]= 10''')
        self.p_int_used[1]=False
    def guard43(self):
        return (((self.p_int_used[1]) or (self.p_int[1] == None) or (self.__relaxUsedRestriction)))
    
    def act44(self):
        self.__test.append(('''self.p_bst[0]= binary_search_tree.BinarySearchTree()  ''',self.guard44,self.act44))
        self.log('''self.p_bst[0]= binary_search_tree.BinarySearchTree() ''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0]= binary_search_tree.BinarySearchTree() 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_bst[0]= binary_search_tree.BinarySearchTree() ''')
        self.p_bst_used[0]=False
    def guard44(self):
        return (((self.p_bst_used[0]) or (self.p_bst[0] == None) or (self.__relaxUsedRestriction)))
    
    def act45(self):
        self.__test.append(('''self.p_bst[1]= binary_search_tree.BinarySearchTree()  ''',self.guard45,self.act45))
        self.log('''self.p_bst[1]= binary_search_tree.BinarySearchTree() ''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1]= binary_search_tree.BinarySearchTree() 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.logPost('''self.p_bst[1]= binary_search_tree.BinarySearchTree() ''')
        self.p_bst_used[1]=False
    def guard45(self):
        return (((self.p_bst_used[1]) or (self.p_bst[1] == None) or (self.__relaxUsedRestriction)))
    
    def act46(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard46,self.act46))
        self.log('''self.p_bst[0].put(self.p_key[0],self.p_int[0])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[0],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[0].contains(self.p_key[0]) and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[0],self.p_int[0])''')
        self.p_int_used[0]=True
    def guard46(self):
        return (self.p_int[0] != None) and (self.p_bst[0] != None) and (self.p_key[0] != None)
    
    def act47(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard47,self.act47))
        self.log('''self.p_bst[0].put(self.p_key[0],self.p_int[1])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[0],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[0].contains(self.p_key[0]) and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[0],self.p_int[1])''')
        self.p_int_used[1]=True
    def guard47(self):
        return (self.p_int[1] != None) and (self.p_bst[0] != None) and (self.p_key[0] != None)
    
    def act48(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard48,self.act48))
        self.log('''self.p_bst[0].put(self.p_key[1],self.p_int[0])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[1],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[0].contains(self.p_key[1]) and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[1],self.p_int[0])''')
        self.p_int_used[0]=True
    def guard48(self):
        return (self.p_int[0] != None) and (self.p_bst[0] != None) and (self.p_key[1] != None)
    
    def act49(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard49,self.act49))
        self.log('''self.p_bst[0].put(self.p_key[1],self.p_int[1])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[1],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[0].contains(self.p_key[1]) and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[1],self.p_int[1])''')
        self.p_int_used[1]=True
    def guard49(self):
        return (self.p_int[1] != None) and (self.p_bst[0] != None) and (self.p_key[1] != None)
    
    def act50(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard50,self.act50))
        self.log('''self.p_bst[1].put(self.p_key[0],self.p_int[0])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[0],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[1].contains(self.p_key[0]) and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[0],self.p_int[0])''')
        self.p_int_used[0]=True
    def guard50(self):
        return (self.p_int[0] != None) and (self.p_bst[1] != None) and (self.p_key[0] != None)
    
    def act51(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard51,self.act51))
        self.log('''self.p_bst[1].put(self.p_key[0],self.p_int[1])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[0],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[1].contains(self.p_key[0]) and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[0],self.p_int[1])''')
        self.p_int_used[1]=True
    def guard51(self):
        return (self.p_int[1] != None) and (self.p_bst[1] != None) and (self.p_key[0] != None)
    
    def act52(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard52,self.act52))
        self.log('''self.p_bst[1].put(self.p_key[1],self.p_int[0])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[1],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[1].contains(self.p_key[1]) and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[1],self.p_int[0])''')
        self.p_int_used[0]=True
    def guard52(self):
        return (self.p_int[0] != None) and (self.p_bst[1] != None) and (self.p_key[1] != None)
    
    def act53(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard53,self.act53))
        self.log('''self.p_bst[1].put(self.p_key[1],self.p_int[1])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[1],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[1].contains(self.p_key[1]) and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[1],self.p_int[1])''')
        self.p_int_used[1]=True
    def guard53(self):
        return (self.p_int[1] != None) and (self.p_bst[1] != None) and (self.p_key[1] != None)
    
    def act54(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard54,self.act54))
        self.log('''self.p_bst[0].put(self.p_key[0],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[0],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     
        self.logPost('''self.p_bst[0].put(self.p_key[0],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[0]=True
        self.p_key_used[0]=True
    def guard54(self):
        return (self.p_int[0] != None) and (self.p_bst[0] != None) and (self.p_key[0] != None) and ((self.p_bst[0].contains(self.p_key[0]) == False))
    
    def act55(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard55,self.act55))
        self.log('''self.p_bst[0].put(self.p_key[0],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[0],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     
        self.logPost('''self.p_bst[0].put(self.p_key[0],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[0]=True
        self.p_key_used[0]=True
    def guard55(self):
        return (self.p_int[1] != None) and (self.p_bst[0] != None) and (self.p_key[0] != None) and ((self.p_bst[0].contains(self.p_key[0]) == False))
    
    def act56(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard56,self.act56))
        self.log('''self.p_bst[0].put(self.p_key[1],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[1],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     
        self.logPost('''self.p_bst[0].put(self.p_key[1],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[0]=True
        self.p_key_used[1]=True
    def guard56(self):
        return (self.p_int[0] != None) and (self.p_bst[0] != None) and (self.p_key[1] != None) and ((self.p_bst[0].contains(self.p_key[1]) == False))
    
    def act57(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard57,self.act57))
        self.log('''self.p_bst[0].put(self.p_key[1],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[1],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     
        self.logPost('''self.p_bst[0].put(self.p_key[1],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[0]=True
        self.p_key_used[1]=True
    def guard57(self):
        return (self.p_int[1] != None) and (self.p_bst[0] != None) and (self.p_key[1] != None) and ((self.p_bst[0].contains(self.p_key[1]) == False))
    
    def act58(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard58,self.act58))
        self.log('''self.p_bst[1].put(self.p_key[0],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[0],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     
        self.logPost('''self.p_bst[1].put(self.p_key[0],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[1]=True
        self.p_key_used[0]=True
    def guard58(self):
        return (self.p_int[0] != None) and (self.p_bst[1] != None) and (self.p_key[0] != None) and ((self.p_bst[1].contains(self.p_key[0]) == False))
    
    def act59(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard59,self.act59))
        self.log('''self.p_bst[1].put(self.p_key[0],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[0],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     
        self.logPost('''self.p_bst[1].put(self.p_key[0],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[1]=True
        self.p_key_used[0]=True
    def guard59(self):
        return (self.p_int[1] != None) and (self.p_bst[1] != None) and (self.p_key[0] != None) and ((self.p_bst[1].contains(self.p_key[0]) == False))
    
    def act60(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard60,self.act60))
        self.log('''self.p_bst[1].put(self.p_key[1],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[1],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     
        self.logPost('''self.p_bst[1].put(self.p_key[1],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[1]=True
        self.p_key_used[1]=True
    def guard60(self):
        return (self.p_int[0] != None) and (self.p_bst[1] != None) and (self.p_key[1] != None) and ((self.p_bst[1].contains(self.p_key[1]) == False))
    
    def act61(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard61,self.act61))
        self.log('''self.p_bst[1].put(self.p_key[1],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[1],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     
        self.logPost('''self.p_bst[1].put(self.p_key[1],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[1]=True
        self.p_key_used[1]=True
    def guard61(self):
        return (self.p_int[1] != None) and (self.p_bst[1] != None) and (self.p_key[1] != None) and ((self.p_bst[1].contains(self.p_key[1]) == False))
    
    def act62(self):
        self.__test.append(('''self.p_bst[0].delete(self.p_key[0]) ''',self.guard62,self.act62))
        self.log('''self.p_bst[0].delete(self.p_key[0])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].delete(self.p_key[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()''']  == self.p_bst[0].size() + 1) and (self.p_bst[0].contains(self.p_key[0]) == False)  
        self.logPost('''self.p_bst[0].delete(self.p_key[0])''')
        self.p_bst_used[0]=True
        self.p_key_used[0]=True
    def guard62(self):
        return (self.p_bst[0] != None) and (self.p_key[0] != None) and (self.p_bst[0].contains(self.p_key[0]))
    
    def act63(self):
        self.__test.append(('''self.p_bst[0].delete(self.p_key[1]) ''',self.guard63,self.act63))
        self.log('''self.p_bst[0].delete(self.p_key[1])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].delete(self.p_key[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()''']  == self.p_bst[0].size() + 1) and (self.p_bst[0].contains(self.p_key[1]) == False)  
        self.logPost('''self.p_bst[0].delete(self.p_key[1])''')
        self.p_bst_used[0]=True
        self.p_key_used[1]=True
    def guard63(self):
        return (self.p_bst[0] != None) and (self.p_key[1] != None) and (self.p_bst[0].contains(self.p_key[1]))
    
    def act64(self):
        self.__test.append(('''self.p_bst[1].delete(self.p_key[0]) ''',self.guard64,self.act64))
        self.log('''self.p_bst[1].delete(self.p_key[0])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].delete(self.p_key[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()''']  == self.p_bst[1].size() + 1) and (self.p_bst[1].contains(self.p_key[0]) == False)  
        self.logPost('''self.p_bst[1].delete(self.p_key[0])''')
        self.p_bst_used[1]=True
        self.p_key_used[0]=True
    def guard64(self):
        return (self.p_bst[1] != None) and (self.p_key[0] != None) and (self.p_bst[1].contains(self.p_key[0]))
    
    def act65(self):
        self.__test.append(('''self.p_bst[1].delete(self.p_key[1]) ''',self.guard65,self.act65))
        self.log('''self.p_bst[1].delete(self.p_key[1])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].delete(self.p_key[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()''']  == self.p_bst[1].size() + 1) and (self.p_bst[1].contains(self.p_key[1]) == False)  
        self.logPost('''self.p_bst[1].delete(self.p_key[1])''')
        self.p_bst_used[1]=True
        self.p_key_used[1]=True
    def guard65(self):
        return (self.p_bst[1] != None) and (self.p_key[1] != None) and (self.p_bst[1].contains(self.p_key[1]))
    
    def act66(self):
        self.__test.append(('''self.p_bst[0].delete(self.p_key[0]) ''',self.guard66,self.act66))
        self.log('''self.p_bst[0].delete(self.p_key[0])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].delete(self.p_key[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[0].is_empty() 
        self.logPost('''self.p_bst[0].delete(self.p_key[0])''')
        self.p_bst_used[0]=True
        self.p_key_used[0]=True
    def guard66(self):
        return (self.p_bst[0] != None) and (self.p_key[0] != None) and ((checkroot(self.p_bst[0]) == 0))
    
    def act67(self):
        self.__test.append(('''self.p_bst[0].delete(self.p_key[1]) ''',self.guard67,self.act67))
        self.log('''self.p_bst[0].delete(self.p_key[1])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].delete(self.p_key[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[0].is_empty() 
        self.logPost('''self.p_bst[0].delete(self.p_key[1])''')
        self.p_bst_used[0]=True
        self.p_key_used[1]=True
    def guard67(self):
        return (self.p_bst[0] != None) and (self.p_key[1] != None) and ((checkroot(self.p_bst[0]) == 0))
    
    def act68(self):
        self.__test.append(('''self.p_bst[1].delete(self.p_key[0]) ''',self.guard68,self.act68))
        self.log('''self.p_bst[1].delete(self.p_key[0])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].delete(self.p_key[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[1].is_empty() 
        self.logPost('''self.p_bst[1].delete(self.p_key[0])''')
        self.p_bst_used[1]=True
        self.p_key_used[0]=True
    def guard68(self):
        return (self.p_bst[1] != None) and (self.p_key[0] != None) and ((checkroot(self.p_bst[1]) == 0))
    
    def act69(self):
        self.__test.append(('''self.p_bst[1].delete(self.p_key[1]) ''',self.guard69,self.act69))
        self.log('''self.p_bst[1].delete(self.p_key[1])''')
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].delete(self.p_key[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert self.p_bst[1].is_empty() 
        self.logPost('''self.p_bst[1].delete(self.p_key[1])''')
        self.p_bst_used[1]=True
        self.p_key_used[1]=True
    def guard69(self):
        return (self.p_bst[1] != None) and (self.p_key[1] != None) and ((checkroot(self.p_bst[1]) == 0))
    
    def act70(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard70,self.act70))
        self.log('''self.p_bst[0].put(self.p_key[0],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[0],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[0],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[0]=True
        self.p_key_used[0]=True
    def guard70(self):
        return (self.p_int[0] != None) and (self.p_bst[0] != None) and (self.p_key[0] != None) and ((self.p_bst[0].contains(self.p_key[0]) == True))
    
    def act71(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard71,self.act71))
        self.log('''self.p_bst[0].put(self.p_key[0],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[0],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[0],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[0]=True
        self.p_key_used[0]=True
    def guard71(self):
        return (self.p_int[1] != None) and (self.p_bst[0] != None) and (self.p_key[0] != None) and ((self.p_bst[0].contains(self.p_key[0]) == True))
    
    def act72(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard72,self.act72))
        self.log('''self.p_bst[0].put(self.p_key[1],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[1],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[1],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[0]=True
        self.p_key_used[1]=True
    def guard72(self):
        return (self.p_int[0] != None) and (self.p_bst[0] != None) and (self.p_key[1] != None) and ((self.p_bst[0].contains(self.p_key[1]) == True))
    
    def act73(self):
        self.__test.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard73,self.act73))
        self.log('''self.p_bst[0].put(self.p_key[1],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[0].put(self.p_key[1],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])
        self.logPost('''self.p_bst[0].put(self.p_key[1],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[0]=True
        self.p_key_used[1]=True
    def guard73(self):
        return (self.p_int[1] != None) and (self.p_bst[0] != None) and (self.p_key[1] != None) and ((self.p_bst[0].contains(self.p_key[1]) == True))
    
    def act74(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard74,self.act74))
        self.log('''self.p_bst[1].put(self.p_key[0],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[0],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[0],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[1]=True
        self.p_key_used[0]=True
    def guard74(self):
        return (self.p_int[0] != None) and (self.p_bst[1] != None) and (self.p_key[0] != None) and ((self.p_bst[1].contains(self.p_key[0]) == True))
    
    def act75(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard75,self.act75))
        self.log('''self.p_bst[1].put(self.p_key[0],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[0],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[0],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[1]=True
        self.p_key_used[0]=True
    def guard75(self):
        return (self.p_int[1] != None) and (self.p_bst[1] != None) and (self.p_key[0] != None) and ((self.p_bst[1].contains(self.p_key[0]) == True))
    
    def act76(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard76,self.act76))
        self.log('''self.p_bst[1].put(self.p_key[1],self.p_int[0])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[1],self.p_int[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[1],self.p_int[0])''')
        self.p_int_used[0]=True
        self.p_bst_used[1]=True
        self.p_key_used[1]=True
    def guard76(self):
        return (self.p_int[0] != None) and (self.p_bst[1] != None) and (self.p_key[1] != None) and ((self.p_bst[1].contains(self.p_key[1]) == True))
    
    def act77(self):
        self.__test.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard77,self.act77))
        self.log('''self.p_bst[1].put(self.p_key[1],self.p_int[1])''')
        __pre = {}
        __pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_bst[1].put(self.p_key[1],self.p_int[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert (__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])
        self.logPost('''self.p_bst[1].put(self.p_key[1],self.p_int[1])''')
        self.p_int_used[1]=True
        self.p_bst_used[1]=True
        self.p_key_used[1]=True
    def guard77(self):
        return (self.p_int[1] != None) and (self.p_bst[1] != None) and (self.p_key[1] != None) and ((self.p_bst[1].contains(self.p_key[1]) == True))
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__modules.append(r"binary_search_tree.py")
        self.__features = []
        self.__replayBacktrack = False
        self.__cov = coverage.coverage(branch=True, source=["binary_search_tree.py"])
        self.__collectCov = True
        self.__allBranches = set()
        self.__allStatements = set()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
        self.__oldCovData = None; print 'COV: CLEARING OLD DATA'
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_int = {}
        self.p_int_used = {}
        self.__pools.append("self.p_int")
        self.p_int[0] = None
        self.p_int_used[0] = True
        self.p_int[1] = None
        self.p_int_used[1] = True
        self.p_int[2] = None
        self.p_int_used[2] = True
        self.p_bst = {}
        self.p_bst_used = {}
        self.__pools.append("self.p_bst")
        self.p_bst[0] = None
        self.p_bst_used[0] = True
        self.p_bst[1] = None
        self.p_bst_used[1] = True
        self.p_bst[2] = None
        self.p_bst_used[2] = True
        self.p_key = {}
        self.p_key_used = {}
        self.__pools.append("self.p_key")
        self.p_key[0] = None
        self.p_key_used[0] = True
        self.p_key[1] = None
        self.p_key_used[1] = True
        self.p_key[2] = None
        self.p_key_used[2] = True
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
        self.__actions.append(('''self.p_key[0]= 0 ''',self.guard0,self.act0))

        self.__names['''self.p_key[0]= 0 '''] = ('''self.p_key[0]= 0 ''',self.guard0,self.act0)

        self.__orderings['''self.p_key[0]= 0 '''] = 1

        self.__okExcepts['''self.p_key[0]= 0 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 1 ''',self.guard1,self.act1))

        self.__names['''self.p_key[0]= 1 '''] = ('''self.p_key[0]= 1 ''',self.guard1,self.act1)

        self.__orderings['''self.p_key[0]= 1 '''] = 2

        self.__okExcepts['''self.p_key[0]= 1 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 2 ''',self.guard2,self.act2))

        self.__names['''self.p_key[0]= 2 '''] = ('''self.p_key[0]= 2 ''',self.guard2,self.act2)

        self.__orderings['''self.p_key[0]= 2 '''] = 3

        self.__okExcepts['''self.p_key[0]= 2 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 3 ''',self.guard3,self.act3))

        self.__names['''self.p_key[0]= 3 '''] = ('''self.p_key[0]= 3 ''',self.guard3,self.act3)

        self.__orderings['''self.p_key[0]= 3 '''] = 4

        self.__okExcepts['''self.p_key[0]= 3 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 4 ''',self.guard4,self.act4))

        self.__names['''self.p_key[0]= 4 '''] = ('''self.p_key[0]= 4 ''',self.guard4,self.act4)

        self.__orderings['''self.p_key[0]= 4 '''] = 5

        self.__okExcepts['''self.p_key[0]= 4 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 5 ''',self.guard5,self.act5))

        self.__names['''self.p_key[0]= 5 '''] = ('''self.p_key[0]= 5 ''',self.guard5,self.act5)

        self.__orderings['''self.p_key[0]= 5 '''] = 6

        self.__okExcepts['''self.p_key[0]= 5 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 6 ''',self.guard6,self.act6))

        self.__names['''self.p_key[0]= 6 '''] = ('''self.p_key[0]= 6 ''',self.guard6,self.act6)

        self.__orderings['''self.p_key[0]= 6 '''] = 7

        self.__okExcepts['''self.p_key[0]= 6 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 7 ''',self.guard7,self.act7))

        self.__names['''self.p_key[0]= 7 '''] = ('''self.p_key[0]= 7 ''',self.guard7,self.act7)

        self.__orderings['''self.p_key[0]= 7 '''] = 8

        self.__okExcepts['''self.p_key[0]= 7 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 8 ''',self.guard8,self.act8))

        self.__names['''self.p_key[0]= 8 '''] = ('''self.p_key[0]= 8 ''',self.guard8,self.act8)

        self.__orderings['''self.p_key[0]= 8 '''] = 9

        self.__okExcepts['''self.p_key[0]= 8 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 9 ''',self.guard9,self.act9))

        self.__names['''self.p_key[0]= 9 '''] = ('''self.p_key[0]= 9 ''',self.guard9,self.act9)

        self.__orderings['''self.p_key[0]= 9 '''] = 10

        self.__okExcepts['''self.p_key[0]= 9 '''] = ''''''

        self.__actions.append(('''self.p_key[0]= 10 ''',self.guard10,self.act10))

        self.__names['''self.p_key[0]= 10 '''] = ('''self.p_key[0]= 10 ''',self.guard10,self.act10)

        self.__orderings['''self.p_key[0]= 10 '''] = 11

        self.__okExcepts['''self.p_key[0]= 10 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 0 ''',self.guard11,self.act11))

        self.__names['''self.p_key[1]= 0 '''] = ('''self.p_key[1]= 0 ''',self.guard11,self.act11)

        self.__orderings['''self.p_key[1]= 0 '''] = 12

        self.__okExcepts['''self.p_key[1]= 0 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 1 ''',self.guard12,self.act12))

        self.__names['''self.p_key[1]= 1 '''] = ('''self.p_key[1]= 1 ''',self.guard12,self.act12)

        self.__orderings['''self.p_key[1]= 1 '''] = 13

        self.__okExcepts['''self.p_key[1]= 1 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 2 ''',self.guard13,self.act13))

        self.__names['''self.p_key[1]= 2 '''] = ('''self.p_key[1]= 2 ''',self.guard13,self.act13)

        self.__orderings['''self.p_key[1]= 2 '''] = 14

        self.__okExcepts['''self.p_key[1]= 2 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 3 ''',self.guard14,self.act14))

        self.__names['''self.p_key[1]= 3 '''] = ('''self.p_key[1]= 3 ''',self.guard14,self.act14)

        self.__orderings['''self.p_key[1]= 3 '''] = 15

        self.__okExcepts['''self.p_key[1]= 3 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 4 ''',self.guard15,self.act15))

        self.__names['''self.p_key[1]= 4 '''] = ('''self.p_key[1]= 4 ''',self.guard15,self.act15)

        self.__orderings['''self.p_key[1]= 4 '''] = 16

        self.__okExcepts['''self.p_key[1]= 4 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 5 ''',self.guard16,self.act16))

        self.__names['''self.p_key[1]= 5 '''] = ('''self.p_key[1]= 5 ''',self.guard16,self.act16)

        self.__orderings['''self.p_key[1]= 5 '''] = 17

        self.__okExcepts['''self.p_key[1]= 5 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 6 ''',self.guard17,self.act17))

        self.__names['''self.p_key[1]= 6 '''] = ('''self.p_key[1]= 6 ''',self.guard17,self.act17)

        self.__orderings['''self.p_key[1]= 6 '''] = 18

        self.__okExcepts['''self.p_key[1]= 6 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 7 ''',self.guard18,self.act18))

        self.__names['''self.p_key[1]= 7 '''] = ('''self.p_key[1]= 7 ''',self.guard18,self.act18)

        self.__orderings['''self.p_key[1]= 7 '''] = 19

        self.__okExcepts['''self.p_key[1]= 7 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 8 ''',self.guard19,self.act19))

        self.__names['''self.p_key[1]= 8 '''] = ('''self.p_key[1]= 8 ''',self.guard19,self.act19)

        self.__orderings['''self.p_key[1]= 8 '''] = 20

        self.__okExcepts['''self.p_key[1]= 8 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 9 ''',self.guard20,self.act20))

        self.__names['''self.p_key[1]= 9 '''] = ('''self.p_key[1]= 9 ''',self.guard20,self.act20)

        self.__orderings['''self.p_key[1]= 9 '''] = 21

        self.__okExcepts['''self.p_key[1]= 9 '''] = ''''''

        self.__actions.append(('''self.p_key[1]= 10 ''',self.guard21,self.act21))

        self.__names['''self.p_key[1]= 10 '''] = ('''self.p_key[1]= 10 ''',self.guard21,self.act21)

        self.__orderings['''self.p_key[1]= 10 '''] = 22

        self.__okExcepts['''self.p_key[1]= 10 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 0 ''',self.guard22,self.act22))

        self.__names['''self.p_int[0]= 0 '''] = ('''self.p_int[0]= 0 ''',self.guard22,self.act22)

        self.__orderings['''self.p_int[0]= 0 '''] = 23

        self.__okExcepts['''self.p_int[0]= 0 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 1 ''',self.guard23,self.act23))

        self.__names['''self.p_int[0]= 1 '''] = ('''self.p_int[0]= 1 ''',self.guard23,self.act23)

        self.__orderings['''self.p_int[0]= 1 '''] = 24

        self.__okExcepts['''self.p_int[0]= 1 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 2 ''',self.guard24,self.act24))

        self.__names['''self.p_int[0]= 2 '''] = ('''self.p_int[0]= 2 ''',self.guard24,self.act24)

        self.__orderings['''self.p_int[0]= 2 '''] = 25

        self.__okExcepts['''self.p_int[0]= 2 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 3 ''',self.guard25,self.act25))

        self.__names['''self.p_int[0]= 3 '''] = ('''self.p_int[0]= 3 ''',self.guard25,self.act25)

        self.__orderings['''self.p_int[0]= 3 '''] = 26

        self.__okExcepts['''self.p_int[0]= 3 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 4 ''',self.guard26,self.act26))

        self.__names['''self.p_int[0]= 4 '''] = ('''self.p_int[0]= 4 ''',self.guard26,self.act26)

        self.__orderings['''self.p_int[0]= 4 '''] = 27

        self.__okExcepts['''self.p_int[0]= 4 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 5 ''',self.guard27,self.act27))

        self.__names['''self.p_int[0]= 5 '''] = ('''self.p_int[0]= 5 ''',self.guard27,self.act27)

        self.__orderings['''self.p_int[0]= 5 '''] = 28

        self.__okExcepts['''self.p_int[0]= 5 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 6 ''',self.guard28,self.act28))

        self.__names['''self.p_int[0]= 6 '''] = ('''self.p_int[0]= 6 ''',self.guard28,self.act28)

        self.__orderings['''self.p_int[0]= 6 '''] = 29

        self.__okExcepts['''self.p_int[0]= 6 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 7 ''',self.guard29,self.act29))

        self.__names['''self.p_int[0]= 7 '''] = ('''self.p_int[0]= 7 ''',self.guard29,self.act29)

        self.__orderings['''self.p_int[0]= 7 '''] = 30

        self.__okExcepts['''self.p_int[0]= 7 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 8 ''',self.guard30,self.act30))

        self.__names['''self.p_int[0]= 8 '''] = ('''self.p_int[0]= 8 ''',self.guard30,self.act30)

        self.__orderings['''self.p_int[0]= 8 '''] = 31

        self.__okExcepts['''self.p_int[0]= 8 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 9 ''',self.guard31,self.act31))

        self.__names['''self.p_int[0]= 9 '''] = ('''self.p_int[0]= 9 ''',self.guard31,self.act31)

        self.__orderings['''self.p_int[0]= 9 '''] = 32

        self.__okExcepts['''self.p_int[0]= 9 '''] = ''''''

        self.__actions.append(('''self.p_int[0]= 10 ''',self.guard32,self.act32))

        self.__names['''self.p_int[0]= 10 '''] = ('''self.p_int[0]= 10 ''',self.guard32,self.act32)

        self.__orderings['''self.p_int[0]= 10 '''] = 33

        self.__okExcepts['''self.p_int[0]= 10 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 0 ''',self.guard33,self.act33))

        self.__names['''self.p_int[1]= 0 '''] = ('''self.p_int[1]= 0 ''',self.guard33,self.act33)

        self.__orderings['''self.p_int[1]= 0 '''] = 34

        self.__okExcepts['''self.p_int[1]= 0 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 1 ''',self.guard34,self.act34))

        self.__names['''self.p_int[1]= 1 '''] = ('''self.p_int[1]= 1 ''',self.guard34,self.act34)

        self.__orderings['''self.p_int[1]= 1 '''] = 35

        self.__okExcepts['''self.p_int[1]= 1 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 2 ''',self.guard35,self.act35))

        self.__names['''self.p_int[1]= 2 '''] = ('''self.p_int[1]= 2 ''',self.guard35,self.act35)

        self.__orderings['''self.p_int[1]= 2 '''] = 36

        self.__okExcepts['''self.p_int[1]= 2 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 3 ''',self.guard36,self.act36))

        self.__names['''self.p_int[1]= 3 '''] = ('''self.p_int[1]= 3 ''',self.guard36,self.act36)

        self.__orderings['''self.p_int[1]= 3 '''] = 37

        self.__okExcepts['''self.p_int[1]= 3 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 4 ''',self.guard37,self.act37))

        self.__names['''self.p_int[1]= 4 '''] = ('''self.p_int[1]= 4 ''',self.guard37,self.act37)

        self.__orderings['''self.p_int[1]= 4 '''] = 38

        self.__okExcepts['''self.p_int[1]= 4 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 5 ''',self.guard38,self.act38))

        self.__names['''self.p_int[1]= 5 '''] = ('''self.p_int[1]= 5 ''',self.guard38,self.act38)

        self.__orderings['''self.p_int[1]= 5 '''] = 39

        self.__okExcepts['''self.p_int[1]= 5 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 6 ''',self.guard39,self.act39))

        self.__names['''self.p_int[1]= 6 '''] = ('''self.p_int[1]= 6 ''',self.guard39,self.act39)

        self.__orderings['''self.p_int[1]= 6 '''] = 40

        self.__okExcepts['''self.p_int[1]= 6 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 7 ''',self.guard40,self.act40))

        self.__names['''self.p_int[1]= 7 '''] = ('''self.p_int[1]= 7 ''',self.guard40,self.act40)

        self.__orderings['''self.p_int[1]= 7 '''] = 41

        self.__okExcepts['''self.p_int[1]= 7 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 8 ''',self.guard41,self.act41))

        self.__names['''self.p_int[1]= 8 '''] = ('''self.p_int[1]= 8 ''',self.guard41,self.act41)

        self.__orderings['''self.p_int[1]= 8 '''] = 42

        self.__okExcepts['''self.p_int[1]= 8 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 9 ''',self.guard42,self.act42))

        self.__names['''self.p_int[1]= 9 '''] = ('''self.p_int[1]= 9 ''',self.guard42,self.act42)

        self.__orderings['''self.p_int[1]= 9 '''] = 43

        self.__okExcepts['''self.p_int[1]= 9 '''] = ''''''

        self.__actions.append(('''self.p_int[1]= 10 ''',self.guard43,self.act43))

        self.__names['''self.p_int[1]= 10 '''] = ('''self.p_int[1]= 10 ''',self.guard43,self.act43)

        self.__orderings['''self.p_int[1]= 10 '''] = 44

        self.__okExcepts['''self.p_int[1]= 10 '''] = ''''''

        self.__actions.append(('''self.p_bst[0]= binary_search_tree.BinarySearchTree()  ''',self.guard44,self.act44))

        self.__names['''self.p_bst[0]= binary_search_tree.BinarySearchTree()  '''] = ('''self.p_bst[0]= binary_search_tree.BinarySearchTree()  ''',self.guard44,self.act44)

        self.__orderings['''self.p_bst[0]= binary_search_tree.BinarySearchTree()  '''] = 45

        self.__okExcepts['''self.p_bst[0]= binary_search_tree.BinarySearchTree()  '''] = ''''''

        self.__actions.append(('''self.p_bst[1]= binary_search_tree.BinarySearchTree()  ''',self.guard45,self.act45))

        self.__names['''self.p_bst[1]= binary_search_tree.BinarySearchTree()  '''] = ('''self.p_bst[1]= binary_search_tree.BinarySearchTree()  ''',self.guard45,self.act45)

        self.__orderings['''self.p_bst[1]= binary_search_tree.BinarySearchTree()  '''] = 46

        self.__okExcepts['''self.p_bst[1]= binary_search_tree.BinarySearchTree()  '''] = ''''''

        self.__actions.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard46,self.act46))

        self.__names['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = ('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard46,self.act46)

        self.__orderings['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = 47

        self.__okExcepts['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = r"self.p_bst[0].contains(self.p_key[0]) and checktreeBST(self.p_bst[0])"

        self.__actions.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard47,self.act47))

        self.__names['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = ('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard47,self.act47)

        self.__orderings['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = 48

        self.__okExcepts['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = r"self.p_bst[0].contains(self.p_key[0]) and checktreeBST(self.p_bst[0])"

        self.__actions.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard48,self.act48))

        self.__names['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = ('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard48,self.act48)

        self.__orderings['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = 49

        self.__okExcepts['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = r"self.p_bst[0].contains(self.p_key[1]) and checktreeBST(self.p_bst[0])"

        self.__actions.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard49,self.act49))

        self.__names['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = ('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard49,self.act49)

        self.__orderings['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = 50

        self.__okExcepts['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = r"self.p_bst[0].contains(self.p_key[1]) and checktreeBST(self.p_bst[0])"

        self.__actions.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard50,self.act50))

        self.__names['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = ('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard50,self.act50)

        self.__orderings['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = 51

        self.__okExcepts['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = r"self.p_bst[1].contains(self.p_key[0]) and checktreeBST(self.p_bst[1])"

        self.__actions.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard51,self.act51))

        self.__names['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = ('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard51,self.act51)

        self.__orderings['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = 52

        self.__okExcepts['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = r"self.p_bst[1].contains(self.p_key[0]) and checktreeBST(self.p_bst[1])"

        self.__actions.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard52,self.act52))

        self.__names['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = ('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard52,self.act52)

        self.__orderings['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = 53

        self.__okExcepts['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = r"self.p_bst[1].contains(self.p_key[1]) and checktreeBST(self.p_bst[1])"

        self.__actions.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard53,self.act53))

        self.__names['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = ('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard53,self.act53)

        self.__orderings['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = 54

        self.__okExcepts['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = r"self.p_bst[1].contains(self.p_key[1]) and checktreeBST(self.p_bst[1])"

        self.__actions.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard54,self.act54))

        self.__names['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = ('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard54,self.act54)

        self.__orderings['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = 55

        self.__okExcepts['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = r"(__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     "

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard55,self.act55))

        self.__names['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = ('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard55,self.act55)

        self.__orderings['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = 56

        self.__okExcepts['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = r"(__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     "

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard56,self.act56))

        self.__names['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = ('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard56,self.act56)

        self.__orderings['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = 57

        self.__okExcepts['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = r"(__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     "

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard57,self.act57))

        self.__names['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = ('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard57,self.act57)

        self.__orderings['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = 58

        self.__okExcepts['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = r"(__pre['''self.p_bst[0].size()'''] + 1) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])     "

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard58,self.act58))

        self.__names['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = ('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard58,self.act58)

        self.__orderings['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = 59

        self.__okExcepts['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = r"(__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     "

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard59,self.act59))

        self.__names['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = ('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard59,self.act59)

        self.__orderings['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = 60

        self.__okExcepts['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = r"(__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     "

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard60,self.act60))

        self.__names['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = ('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard60,self.act60)

        self.__orderings['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = 61

        self.__okExcepts['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = r"(__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     "

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard61,self.act61))

        self.__names['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = ('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard61,self.act61)

        self.__orderings['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = 62

        self.__okExcepts['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = r"(__pre['''self.p_bst[1].size()'''] + 1) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])     "

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[0].delete(self.p_key[0]) ''',self.guard62,self.act62))

        self.__names['''self.p_bst[0].delete(self.p_key[0]) '''] = ('''self.p_bst[0].delete(self.p_key[0]) ''',self.guard62,self.act62)

        self.__orderings['''self.p_bst[0].delete(self.p_key[0]) '''] = 63

        self.__okExcepts['''self.p_bst[0].delete(self.p_key[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].delete(self.p_key[0]) '''] = r"(__pre['''self.p_bst[0].size()''']  == self.p_bst[0].size() + 1) and (self.p_bst[0].contains(self.p_key[0]) == False)  "

        self.__preCode['''self.p_bst[0].delete(self.p_key[0]) '''] = []

        self.__preCode['''self.p_bst[0].delete(self.p_key[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].delete(self.p_key[0]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].delete(self.p_key[1]) ''',self.guard63,self.act63))

        self.__names['''self.p_bst[0].delete(self.p_key[1]) '''] = ('''self.p_bst[0].delete(self.p_key[1]) ''',self.guard63,self.act63)

        self.__orderings['''self.p_bst[0].delete(self.p_key[1]) '''] = 64

        self.__okExcepts['''self.p_bst[0].delete(self.p_key[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].delete(self.p_key[1]) '''] = r"(__pre['''self.p_bst[0].size()''']  == self.p_bst[0].size() + 1) and (self.p_bst[0].contains(self.p_key[1]) == False)  "

        self.__preCode['''self.p_bst[0].delete(self.p_key[1]) '''] = []

        self.__preCode['''self.p_bst[0].delete(self.p_key[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].delete(self.p_key[1]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[1].delete(self.p_key[0]) ''',self.guard64,self.act64))

        self.__names['''self.p_bst[1].delete(self.p_key[0]) '''] = ('''self.p_bst[1].delete(self.p_key[0]) ''',self.guard64,self.act64)

        self.__orderings['''self.p_bst[1].delete(self.p_key[0]) '''] = 65

        self.__okExcepts['''self.p_bst[1].delete(self.p_key[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].delete(self.p_key[0]) '''] = r"(__pre['''self.p_bst[1].size()''']  == self.p_bst[1].size() + 1) and (self.p_bst[1].contains(self.p_key[0]) == False)  "

        self.__preCode['''self.p_bst[1].delete(self.p_key[0]) '''] = []

        self.__preCode['''self.p_bst[1].delete(self.p_key[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].delete(self.p_key[0]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].delete(self.p_key[1]) ''',self.guard65,self.act65))

        self.__names['''self.p_bst[1].delete(self.p_key[1]) '''] = ('''self.p_bst[1].delete(self.p_key[1]) ''',self.guard65,self.act65)

        self.__orderings['''self.p_bst[1].delete(self.p_key[1]) '''] = 66

        self.__okExcepts['''self.p_bst[1].delete(self.p_key[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].delete(self.p_key[1]) '''] = r"(__pre['''self.p_bst[1].size()''']  == self.p_bst[1].size() + 1) and (self.p_bst[1].contains(self.p_key[1]) == False)  "

        self.__preCode['''self.p_bst[1].delete(self.p_key[1]) '''] = []

        self.__preCode['''self.p_bst[1].delete(self.p_key[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].delete(self.p_key[1]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[0].delete(self.p_key[0]) ''',self.guard66,self.act66))

        self.__names['''self.p_bst[0].delete(self.p_key[0]) '''] = ('''self.p_bst[0].delete(self.p_key[0]) ''',self.guard66,self.act66)

        self.__orderings['''self.p_bst[0].delete(self.p_key[0]) '''] = 67

        self.__okExcepts['''self.p_bst[0].delete(self.p_key[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].delete(self.p_key[0]) '''] = r"self.p_bst[0].is_empty() "

        self.__actions.append(('''self.p_bst[0].delete(self.p_key[1]) ''',self.guard67,self.act67))

        self.__names['''self.p_bst[0].delete(self.p_key[1]) '''] = ('''self.p_bst[0].delete(self.p_key[1]) ''',self.guard67,self.act67)

        self.__orderings['''self.p_bst[0].delete(self.p_key[1]) '''] = 68

        self.__okExcepts['''self.p_bst[0].delete(self.p_key[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].delete(self.p_key[1]) '''] = r"self.p_bst[0].is_empty() "

        self.__actions.append(('''self.p_bst[1].delete(self.p_key[0]) ''',self.guard68,self.act68))

        self.__names['''self.p_bst[1].delete(self.p_key[0]) '''] = ('''self.p_bst[1].delete(self.p_key[0]) ''',self.guard68,self.act68)

        self.__orderings['''self.p_bst[1].delete(self.p_key[0]) '''] = 69

        self.__okExcepts['''self.p_bst[1].delete(self.p_key[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].delete(self.p_key[0]) '''] = r"self.p_bst[1].is_empty() "

        self.__actions.append(('''self.p_bst[1].delete(self.p_key[1]) ''',self.guard69,self.act69))

        self.__names['''self.p_bst[1].delete(self.p_key[1]) '''] = ('''self.p_bst[1].delete(self.p_key[1]) ''',self.guard69,self.act69)

        self.__orderings['''self.p_bst[1].delete(self.p_key[1]) '''] = 70

        self.__okExcepts['''self.p_bst[1].delete(self.p_key[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].delete(self.p_key[1]) '''] = r"self.p_bst[1].is_empty() "

        self.__actions.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard70,self.act70))

        self.__names['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = ('''self.p_bst[0].put(self.p_key[0],self.p_int[0]) ''',self.guard70,self.act70)

        self.__orderings['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = 71

        self.__okExcepts['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = r"(__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])"

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard71,self.act71))

        self.__names['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = ('''self.p_bst[0].put(self.p_key[0],self.p_int[1]) ''',self.guard71,self.act71)

        self.__orderings['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = 72

        self.__okExcepts['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = r"(__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])"

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard72,self.act72))

        self.__names['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = ('''self.p_bst[0].put(self.p_key[1],self.p_int[0]) ''',self.guard72,self.act72)

        self.__orderings['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = 73

        self.__okExcepts['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = r"(__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])"

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard73,self.act73))

        self.__names['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = ('''self.p_bst[0].put(self.p_key[1],self.p_int[1]) ''',self.guard73,self.act73)

        self.__orderings['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = 74

        self.__okExcepts['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = r"(__pre['''self.p_bst[0].size()'''] ) == self.p_bst[0].size() and checktreeBST(self.p_bst[0])"

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[0].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre['''self.p_bst[0].size()'''] = self.p_bst[0].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard74,self.act74))

        self.__names['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = ('''self.p_bst[1].put(self.p_key[0],self.p_int[0]) ''',self.guard74,self.act74)

        self.__orderings['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = 75

        self.__okExcepts['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = r"(__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])"

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[0]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard75,self.act75))

        self.__names['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = ('''self.p_bst[1].put(self.p_key[0],self.p_int[1]) ''',self.guard75,self.act75)

        self.__orderings['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = 76

        self.__okExcepts['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = r"(__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])"

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[0],self.p_int[1]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard76,self.act76))

        self.__names['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = ('''self.p_bst[1].put(self.p_key[1],self.p_int[0]) ''',self.guard76,self.act76)

        self.__orderings['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = 77

        self.__okExcepts['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = r"(__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])"

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[0]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions.append(('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard77,self.act77))

        self.__names['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = ('''self.p_bst[1].put(self.p_key[1],self.p_int[1]) ''',self.guard77,self.act77)

        self.__orderings['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = 78

        self.__okExcepts['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = ''''''

        self.__propCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = r"(__pre['''self.p_bst[1].size()'''] ) == self.p_bst[1].size() and checktreeBST(self.p_bst[1])"

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''] = []

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_bst[1].put(self.p_key[1],self.p_int[1]) '''].append(r"__pre['''self.p_bst[1].size()'''] = self.p_bst[1].size()")

        self.__actions_backup = list(self.__actions)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
        self.cleanCov()
    # BEGIN RELOAD CODE
        reload(binary_search_tree)
    # END RELOAD CODE
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_int = {}
        self.p_int_used = {}
        self.__pools.append("self.p_int")
        self.p_int[0] = None
        self.p_int_used[0] = True
        self.p_int[1] = None
        self.p_int_used[1] = True
        self.p_int[2] = None
        self.p_int_used[2] = True
        self.p_bst = {}
        self.p_bst_used = {}
        self.__pools.append("self.p_bst")
        self.p_bst[0] = None
        self.p_bst_used[0] = True
        self.p_bst[1] = None
        self.p_bst_used[1] = True
        self.p_bst[2] = None
        self.p_bst_used[2] = True
        self.p_key = {}
        self.p_key_used = {}
        self.__pools.append("self.p_key")
        self.p_key[0] = None
        self.p_key_used[0] = True
        self.p_key[1] = None
        self.p_key_used[1] = True
        self.p_key[2] = None
        self.p_key_used[2] = True
        try:
            test_after_restart(self)
        except:
            pass
    def log(self, name):
        if self.__log == None:
            return
        if (self.__log == 'All') or (self.__log >= 1):
            try:
                self.__logAction(name,"""self.p_int[0]		""",self.p_int[0]		,False)
            except:
                pass
        if (self.__log == 'All') or (self.__log >= 1):
            try:
                self.__logAction(name,"""self.p_int[1]		""",self.p_int[1]		,False)
            except:
                pass
    def logPost(self, name):
        if self.__log == None:
            return
    def state(self):
        if self.__replayBacktrack:
            return self.captureReplay(self.__test)
        return [ copy.deepcopy(self.p_int),copy.deepcopy(self.p_int_used),copy.deepcopy(self.p_bst),copy.deepcopy(self.p_bst_used),copy.deepcopy(self.p_key),copy.deepcopy(self.p_key_used)]
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_int = copy.deepcopy(old[0])
        self.p_int_used = copy.deepcopy(old[1])
        self.p_bst = copy.deepcopy(old[2])
        self.p_bst_used = copy.deepcopy(old[3])
        self.p_key = copy.deepcopy(old[4])
        self.p_key_used = copy.deepcopy(old[5])
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
        while True:
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
    
    def reduceLengthStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING REDUCE LENGTH STEP"
        # Replace any action with another action, if that allows test to be further reduced
        enableChange = self.getEnabled(test,checkEnabled)
        
        for i in xrange(0,len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue        
            for name2 in enableChange[i]:
                if name1 != name2:
                    if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                    if pred(testC):
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
                    if pred(testC):
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
                    if (testC != test) and pred(testC):
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
                        if (testC != test) and pred(testC):
                            if verbose:
                                print "NORMALIZER: RULE ReplacePool:",p,"WITH",new,"FROM",pos,"TO",pos2
                            return (True, testC)
        return (False, test)
    
    
    def replaceSingleStep(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, checkEnabled = False, distLimit = None):
        if verbose == "VERY":
            print "STARTING REPLACE SINGLE STEP"        
        # Replace any single action with a lower-numbered action
        enableChange = self.getEnabled(test,checkEnabled)    
        
        for i in xrange(0,len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue        
            for name2 in enableChange[i]:
                if self.__orderings[name1] > self.__orderings[name2]:
                    if (distLimit != None) and (self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i+1:]
                    if pred(testC):
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
                                if pred(testC):
                                    if verbose:
                                        print "NORMALIZER: RULE SwapPool:",p1,"AND",p2,"BETWEEN STEP",pos1,"AND",pos2
                                    return (True, testC)
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
    
    def normalize(self, test, pred, pruneGuards = False, keepLast = True, verbose = False, speed = "FAST", checkEnabled = False, distLimit = None, reorder=True):
        """
        Attempts to produce a normalized test case
        """
        try:
            test_before_normalize(self)
        except:
            pass
    
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
        simplifiers = [self.replaceAllStep, self.replacePoolStep, self.replaceSingleStep, self.swapPoolStep, self.swapActionOrderStep, self.reduceLengthStep]
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
        while changed:
            stest = self.captureReplay(test)
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
    def __updateCov(self):
        self.__newBranches = set()
        self.__newStatements = set()
        newCov = self.__cov.get_data()
        if self.__oldCovData == None:
            self.__oldCovData = coverage.CoverageData()
        self.__oldCovData.update(newCov)
        if newCov.measured_files() == None:
            return
        for src_file in newCov.measured_files():
            thisArcs = newCov.arcs(src_file)
            if thisArcs == None:
                continue # assume if we have arcs we have lines
            for arc in thisArcs:
                branch = (src_file, arc)
                if branch not in self.__allBranches:
                    self.__allBranches.add(branch)
                    self.__newBranches.add(branch)
                    self.__newCurrBranches.add(branch)
                if branch not in self.__currBranches:
                    self.__currBranches.add(branch)
            for line in newCov.lines(src_file):
                statement = (src_file, line)
                if statement not in self.__allStatements:
                    self.__allStatements.add(statement)
                    self.__newStatements.add(statement)
                    self.__newCurrStatements.add(statement)
                if statement not in self.__currStatements:
                    self.__currStatements.add(statement)
                    
    def internalReport(self):
        print "TSTL INTERNAL COVERAGE REPORT:"
        for src_file in self.__oldCovData.measured_files():
            adata = self.__oldCovData.arcs(src_file)
            print src_file,"ARCS:",len(adata),sorted(adata)
            for (f,a) in self.__allBranches:
                if f == src_file:
                    if a not in adata:
                        print "WARNING:",a,"VISITED BUT MISSING FROM COVERAGEDATA"
            for a in adata:
                if (src_file,a) not in self.__allBranches:
                    print "WARNING:",a,"IN COVERAGEDATA BUT NOT IN TSTL COVERAGE"
            ldata = list(set(self.__oldCovData.lines(src_file)))
            print src_file,"LINES:",len(ldata),sorted(ldata)
            for (f,l) in self.__allStatements:
                if f == src_file:
                    if l not in ldata:
                        print "WARNING:",l,"VISITED BUT MISSING FROM COVERAGEDATA"
            for l in ldata:
                if (src_file,l) not in self.__allStatements:
                    print "WARNING",l,"IN COVERAGEDATA BUT NOT IN TSTL COVERAGE"
        for (f,l) in self.__allStatements:
            if f not in self.__oldCovData.measured_files():
                print "WARNING:",(f,l),"IS NOT IN COVERAGEDATA"
        print "TSTL BRANCH COUNT:",len(self.__allBranches)                
        print "TSTL STATEMENT COUNT:",len(self.__allStatements)
                    
    def cleanCov(self):
        if self.__oldCovData == None:
            self.__oldCovData = coverage.CoverageData()
        self.__oldCovData.update(self.__cov.get_data())
        self.__cov.erase()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()    
                        
    def resetCov(self):
        self.__cov.erase()
        self.__oldCovData = None
        self.__allBranches = set()
        self.__allStatements = set()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()    
    
    def report(self, filename):
        if self.__oldCovData != None:
            self.__oldCovData.write_file(filename)
            self.__cov.combine([filename])
        outf = open(filename,'w')
        r = -1
        try:
            r = self.__cov.report(morfs=self.__modules, file=outf)
        finally:
            outf.close()
            return r
    
    def htmlReport(self, dir):
        if self.__oldCovData != None:
            self.__oldCovData.write_file(dir + "/.tmpcov")
            self.__cov.combine([dir + "/.tmpcov"])    
        r = -1
        try:
            r = self.__cov.html_report(morfs=self.__modules, directory=dir,
                                          title="TSTL Coverage Report")
        finally:
            return r
    
    def allBranches(self):
        return self.__allBranches
    
    def allStatements(self):
        return self.__allStatements
    
    def currBranches(self):
        return self.__currBranches
    
    def currStatements(self):
        return self.__currStatements
    
    def newBranches(self):
        return self.__newBranches
    
    def newStatements(self):
        return self.__newStatements
    
    def newCurrBranches(self):
        return self.__newCurrBranches
    
    def newCurrStatements(self):
        return self.__newCurrStatements
    
    def startCoverage(self):
        self.__collectCov = True
    
    def stopCoverage(self):
        self.__collectCov = False    
    
    def coversBranches(self, branches, catchUncaught=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught)
            except:
                pass
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            return True
        return coverPred
    
    def coversStatements(self, statements, catchUncaught=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught)
            except:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            return True
        return coverPred
    
    def coversAll(self, statements, branches, catchUncaught=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught)
            except:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            return True
        return coverPred
