import copy
import traceback
import re
import sys
from itertools import chain, combinations
import coverage
# BEGIN STANDALONE CODE
import linkedlist
import math
import time
def countLength(self):
    cot = 0
    head=self.head
    if head==None:
        return cot
    else:
        while head!=None:
            head=head.next
            cot = cot + 1
        return cot

def lengthHead(head):
    ncot=0;
    if not head:
        return ncot
    while head:
        ncot+=1
        head=head.next
    return ncot

def findFstValue (self):
    head=self.head
    if head == None:
        return None
    else:   
        return head.val

def findSecValue (self):
    pp=self.head
    if pp ==None:
        return None
    elif pp.next ==None:
        return None
    else:   
        return pp.next.val  

def findTrdValue (self):
    pp=self.head
    if pp ==None:
        return None
    elif pp.next ==None:
        return None
    elif pp.next.next ==None:
        return None
    else:            
        return pp.next.next.val          

def findLstValue (self):
    head=self.head
    if head == None:
		return None
    else:
        while(head.next!=None):
            head=head.next
        return head.val

def findFstDuplicates(self): 
    head = self.head
    if head==None or head.next==None:
        return False
    else:
        while head.next:
            if head.val==head.next.val:
                return head.val
            else:
                head=head.next 
                if not head.next:
                    return False  

def nprintList (self): 
    print "{{{{{{{{{{{{{{{{{{{{{{{{{{{"   
    head = self.head 
    if head == None :
        return None
    else:
        while head:
            print head.val
            head=head.next
    print "}}}}}}}}}}}}}}}}}}}}}}}}}}}}"

# END STANDALONE CODE
class sut(object):
    def act0(self):
        self.__test.append(('''self.p_INT[0] =1  ''',self.guard0,self.act0))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =1 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard0(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        self.__test.append(('''self.p_INT[0] =2  ''',self.guard1,self.act1))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =2 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard1(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        self.__test.append(('''self.p_INT[0] =3  ''',self.guard2,self.act2))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =3 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard2(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        self.__test.append(('''self.p_INT[0] =4  ''',self.guard3,self.act3))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =4 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard3(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act4(self):
        self.__test.append(('''self.p_INT[0] =5  ''',self.guard4,self.act4))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =5 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard4(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act5(self):
        self.__test.append(('''self.p_INT[0] =6  ''',self.guard5,self.act5))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =6 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard5(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act6(self):
        self.__test.append(('''self.p_INT[0] =7  ''',self.guard6,self.act6))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =7 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard6(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act7(self):
        self.__test.append(('''self.p_INT[0] =8  ''',self.guard7,self.act7))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =8 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard7(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act8(self):
        self.__test.append(('''self.p_INT[0] =9  ''',self.guard8,self.act8))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =9 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard8(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act9(self):
        self.__test.append(('''self.p_INT[0] =10  ''',self.guard9,self.act9))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[0] =10 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=False
    def guard9(self):
        return (((self.p_INT_used[0]) or (self.p_INT[0] == None) or (self.__relaxUsedRestriction)))
    
    def act10(self):
        self.__test.append(('''self.p_INT[1] =1  ''',self.guard10,self.act10))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =1 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard10(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act11(self):
        self.__test.append(('''self.p_INT[1] =2  ''',self.guard11,self.act11))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =2 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard11(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act12(self):
        self.__test.append(('''self.p_INT[1] =3  ''',self.guard12,self.act12))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =3 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard12(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act13(self):
        self.__test.append(('''self.p_INT[1] =4  ''',self.guard13,self.act13))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =4 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard13(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act14(self):
        self.__test.append(('''self.p_INT[1] =5  ''',self.guard14,self.act14))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =5 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard14(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act15(self):
        self.__test.append(('''self.p_INT[1] =6  ''',self.guard15,self.act15))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =6 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard15(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act16(self):
        self.__test.append(('''self.p_INT[1] =7  ''',self.guard16,self.act16))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =7 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard16(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act17(self):
        self.__test.append(('''self.p_INT[1] =8  ''',self.guard17,self.act17))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =8 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard17(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act18(self):
        self.__test.append(('''self.p_INT[1] =9  ''',self.guard18,self.act18))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =9 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard18(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act19(self):
        self.__test.append(('''self.p_INT[1] =10  ''',self.guard19,self.act19))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[1] =10 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=False
    def guard19(self):
        return (((self.p_INT_used[1]) or (self.p_INT[1] == None) or (self.__relaxUsedRestriction)))
    
    def act20(self):
        self.__test.append(('''self.p_INT[2] =1  ''',self.guard20,self.act20))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =1 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard20(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act21(self):
        self.__test.append(('''self.p_INT[2] =2  ''',self.guard21,self.act21))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =2 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard21(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act22(self):
        self.__test.append(('''self.p_INT[2] =3  ''',self.guard22,self.act22))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =3 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard22(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act23(self):
        self.__test.append(('''self.p_INT[2] =4  ''',self.guard23,self.act23))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =4 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard23(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act24(self):
        self.__test.append(('''self.p_INT[2] =5  ''',self.guard24,self.act24))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =5 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard24(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act25(self):
        self.__test.append(('''self.p_INT[2] =6  ''',self.guard25,self.act25))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =6 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard25(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act26(self):
        self.__test.append(('''self.p_INT[2] =7  ''',self.guard26,self.act26))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =7 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard26(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act27(self):
        self.__test.append(('''self.p_INT[2] =8  ''',self.guard27,self.act27))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =8 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard27(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act28(self):
        self.__test.append(('''self.p_INT[2] =9  ''',self.guard28,self.act28))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =9 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard28(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act29(self):
        self.__test.append(('''self.p_INT[2] =10  ''',self.guard29,self.act29))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_INT[2] =10 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=False
    def guard29(self):
        return (((self.p_INT_used[2]) or (self.p_INT[2] == None) or (self.__relaxUsedRestriction)))
    
    def act30(self):
        self.__test.append(('''self.p_CHAR[0] = 'a' ''',self.guard30,self.act30))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 'a'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard30(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act31(self):
        self.__test.append(('''self.p_CHAR[0] = 'b' ''',self.guard31,self.act31))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 'b'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard31(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act32(self):
        self.__test.append(('''self.p_CHAR[0] = 'c' ''',self.guard32,self.act32))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 'c'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard32(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act33(self):
        self.__test.append(('''self.p_CHAR[0] = 'd' ''',self.guard33,self.act33))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 'd'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard33(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act34(self):
        self.__test.append(('''self.p_CHAR[0] = '*' ''',self.guard34,self.act34))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = '*'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard34(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act35(self):
        self.__test.append(('''self.p_CHAR[0] = '$' ''',self.guard35,self.act35))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = '$'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard35(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act36(self):
        self.__test.append(('''self.p_CHAR[0] = 'hello good' ''',self.guard36,self.act36))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 'hello good'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard36(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act37(self):
        self.__test.append(('''self.p_CHAR[0] = 100 ''',self.guard37,self.act37))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 100

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard37(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act38(self):
        self.__test.append(('''self.p_CHAR[0] = 200.1 ''',self.guard38,self.act38))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[0] = 200.1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[0]=False
    def guard38(self):
        return (((self.p_CHAR_used[0]) or (self.p_CHAR[0] == None) or (self.__relaxUsedRestriction)))
    
    def act39(self):
        self.__test.append(('''self.p_CHAR[1] = 'a' ''',self.guard39,self.act39))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 'a'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard39(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act40(self):
        self.__test.append(('''self.p_CHAR[1] = 'b' ''',self.guard40,self.act40))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 'b'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard40(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act41(self):
        self.__test.append(('''self.p_CHAR[1] = 'c' ''',self.guard41,self.act41))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 'c'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard41(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act42(self):
        self.__test.append(('''self.p_CHAR[1] = 'd' ''',self.guard42,self.act42))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 'd'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard42(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act43(self):
        self.__test.append(('''self.p_CHAR[1] = '*' ''',self.guard43,self.act43))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = '*'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard43(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act44(self):
        self.__test.append(('''self.p_CHAR[1] = '$' ''',self.guard44,self.act44))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = '$'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard44(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act45(self):
        self.__test.append(('''self.p_CHAR[1] = 'hello good' ''',self.guard45,self.act45))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 'hello good'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard45(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act46(self):
        self.__test.append(('''self.p_CHAR[1] = 100 ''',self.guard46,self.act46))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 100

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard46(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act47(self):
        self.__test.append(('''self.p_CHAR[1] = 200.1 ''',self.guard47,self.act47))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[1] = 200.1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[1]=False
    def guard47(self):
        return (((self.p_CHAR_used[1]) or (self.p_CHAR[1] == None) or (self.__relaxUsedRestriction)))
    
    def act48(self):
        self.__test.append(('''self.p_CHAR[2] = 'a' ''',self.guard48,self.act48))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 'a'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard48(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act49(self):
        self.__test.append(('''self.p_CHAR[2] = 'b' ''',self.guard49,self.act49))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 'b'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard49(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act50(self):
        self.__test.append(('''self.p_CHAR[2] = 'c' ''',self.guard50,self.act50))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 'c'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard50(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act51(self):
        self.__test.append(('''self.p_CHAR[2] = 'd' ''',self.guard51,self.act51))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 'd'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard51(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act52(self):
        self.__test.append(('''self.p_CHAR[2] = '*' ''',self.guard52,self.act52))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = '*'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard52(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act53(self):
        self.__test.append(('''self.p_CHAR[2] = '$' ''',self.guard53,self.act53))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = '$'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard53(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act54(self):
        self.__test.append(('''self.p_CHAR[2] = 'hello good' ''',self.guard54,self.act54))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 'hello good'

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard54(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act55(self):
        self.__test.append(('''self.p_CHAR[2] = 100 ''',self.guard55,self.act55))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 100

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard55(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act56(self):
        self.__test.append(('''self.p_CHAR[2] = 200.1 ''',self.guard56,self.act56))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_CHAR[2] = 200.1

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_CHAR_used[2]=False
    def guard56(self):
        return (((self.p_CHAR_used[2]) or (self.p_CHAR[2] == None) or (self.__relaxUsedRestriction)))
    
    def act57(self):
        self.__test.append(('''self.p_LIST[0]=[] ''',self.guard57,self.act57))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[0]=[]

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LIST_used[0]=False
    def guard57(self):
        return (((self.p_LIST_used[0]) or (self.p_LIST[0] == None) or (self.__relaxUsedRestriction)))
    
    def act58(self):
        self.__test.append(('''self.p_LIST[1]=[] ''',self.guard58,self.act58))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[1]=[]

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LIST_used[1]=False
    def guard58(self):
        return (((self.p_LIST_used[1]) or (self.p_LIST[1] == None) or (self.__relaxUsedRestriction)))
    
    def act59(self):
        self.__test.append(('''self.p_LIST[2]=[] ''',self.guard59,self.act59))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[2]=[]

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LIST_used[2]=False
    def guard59(self):
        return (((self.p_LIST_used[2]) or (self.p_LIST[2] == None) or (self.__relaxUsedRestriction)))
    
    def act60(self):
        self.__test.append(('''self.p_LIST[0].append(self.p_INT[0]) ''',self.guard60,self.act60))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[0].append(self.p_INT[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
    def guard60(self):
        return (self.p_INT[0] != None) and (self.p_LIST[0] != None)
    
    def act61(self):
        self.__test.append(('''self.p_LIST[0].append(self.p_INT[1]) ''',self.guard61,self.act61))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[0].append(self.p_INT[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
    def guard61(self):
        return (self.p_INT[1] != None) and (self.p_LIST[0] != None)
    
    def act62(self):
        self.__test.append(('''self.p_LIST[0].append(self.p_INT[2]) ''',self.guard62,self.act62))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[0].append(self.p_INT[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
    def guard62(self):
        return (self.p_INT[2] != None) and (self.p_LIST[0] != None)
    
    def act63(self):
        self.__test.append(('''self.p_LIST[1].append(self.p_INT[0]) ''',self.guard63,self.act63))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[1].append(self.p_INT[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
    def guard63(self):
        return (self.p_INT[0] != None) and (self.p_LIST[1] != None)
    
    def act64(self):
        self.__test.append(('''self.p_LIST[1].append(self.p_INT[1]) ''',self.guard64,self.act64))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[1].append(self.p_INT[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
    def guard64(self):
        return (self.p_INT[1] != None) and (self.p_LIST[1] != None)
    
    def act65(self):
        self.__test.append(('''self.p_LIST[1].append(self.p_INT[2]) ''',self.guard65,self.act65))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[1].append(self.p_INT[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
    def guard65(self):
        return (self.p_INT[2] != None) and (self.p_LIST[1] != None)
    
    def act66(self):
        self.__test.append(('''self.p_LIST[2].append(self.p_INT[0]) ''',self.guard66,self.act66))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[2].append(self.p_INT[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
    def guard66(self):
        return (self.p_INT[0] != None) and (self.p_LIST[2] != None)
    
    def act67(self):
        self.__test.append(('''self.p_LIST[2].append(self.p_INT[1]) ''',self.guard67,self.act67))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[2].append(self.p_INT[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
    def guard67(self):
        return (self.p_INT[1] != None) and (self.p_LIST[2] != None)
    
    def act68(self):
        self.__test.append(('''self.p_LIST[2].append(self.p_INT[2]) ''',self.guard68,self.act68))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIST[2].append(self.p_INT[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
    def guard68(self):
        return (self.p_INT[2] != None) and (self.p_LIST[2] != None)
    
    def act69(self):
        self.__test.append(('''self.p_LINKED[0]=linkedlist.linkedList() ''',self.guard69,self.act69))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[0]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[0]=False
    def guard69(self):
        return (((self.p_LINKED_used[0]) or (self.p_LINKED[0] == None) or (self.__relaxUsedRestriction)))
    
    def act70(self):
        self.__test.append(('''self.p_LINKED[1]=linkedlist.linkedList() ''',self.guard70,self.act70))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[1]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[1]=False
    def guard70(self):
        return (((self.p_LINKED_used[1]) or (self.p_LINKED[1] == None) or (self.__relaxUsedRestriction)))
    
    def act71(self):
        self.__test.append(('''self.p_LINKED[2]=linkedlist.linkedList() ''',self.guard71,self.act71))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[2]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[2]=False
    def guard71(self):
        return (((self.p_LINKED_used[2]) or (self.p_LINKED[2] == None) or (self.__relaxUsedRestriction)))
    
    def act72(self):
        self.__test.append(('''self.p_LINKED[3]=linkedlist.linkedList() ''',self.guard72,self.act72))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[3]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[3]=False
    def guard72(self):
        return (((self.p_LINKED_used[3]) or (self.p_LINKED[3] == None) or (self.__relaxUsedRestriction)))
    
    def act73(self):
        self.__test.append(('''self.p_LINKK[0]=linkedlist.linkedList() ''',self.guard73,self.act73))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKK_used[0]=False
    def guard73(self):
        return (((self.p_LINKK_used[0]) or (self.p_LINKK[0] == None) or (self.__relaxUsedRestriction)))
    
    def act74(self):
        self.__test.append(('''self.p_LINKK[1]=linkedlist.linkedList() ''',self.guard74,self.act74))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKK_used[1]=False
    def guard74(self):
        return (((self.p_LINKK_used[1]) or (self.p_LINKK[1] == None) or (self.__relaxUsedRestriction)))
    
    def act75(self):
        self.__test.append(('''self.p_LINKK[2]=linkedlist.linkedList() ''',self.guard75,self.act75))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKK_used[2]=False
    def guard75(self):
        return (((self.p_LINKK_used[2]) or (self.p_LINKK[2] == None) or (self.__relaxUsedRestriction)))
    
    def act76(self):
        self.__test.append(('''self.p_LIN[0]=linkedlist.linkedList() ''',self.guard76,self.act76))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIN[0]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LIN_used[0]=False
    def guard76(self):
        return (((self.p_LIN_used[0]) or (self.p_LIN[0] == None) or (self.__relaxUsedRestriction)))
    
    def act77(self):
        self.__test.append(('''self.p_LIN[1]=linkedlist.linkedList() ''',self.guard77,self.act77))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIN[1]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LIN_used[1]=False
    def guard77(self):
        return (((self.p_LIN_used[1]) or (self.p_LIN[1] == None) or (self.__relaxUsedRestriction)))
    
    def act78(self):
        self.__test.append(('''self.p_LIN[2]=linkedlist.linkedList() ''',self.guard78,self.act78))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LIN[2]=linkedlist.linkedList()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LIN_used[2]=False
    def guard78(self):
        return (((self.p_LIN_used[2]) or (self.p_LIN[2] == None) or (self.__relaxUsedRestriction)))
    
    def act79(self):
        self.__test.append(('''self.p_LINKED[0].insert(self.p_CHAR[0]) ''',self.guard79,self.act79))
        __pre = {}
        __pre['''countLength(self.p_LINKED[0])'''] = countLength(self.p_LINKED[0])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[0])==__pre['''countLength(self.p_LINKED[0])''']+1)
        self.p_LINKED_used[0]=True
        self.p_CHAR_used[0]=True
    def guard79(self):
        return (self.p_LINKED[0] != None) and (self.p_CHAR[0] != None)
    
    def act80(self):
        self.__test.append(('''self.p_LINKED[0].insert(self.p_CHAR[1]) ''',self.guard80,self.act80))
        __pre = {}
        __pre['''countLength(self.p_LINKED[0])'''] = countLength(self.p_LINKED[0])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[0])==__pre['''countLength(self.p_LINKED[0])''']+1)
        self.p_LINKED_used[0]=True
        self.p_CHAR_used[1]=True
    def guard80(self):
        return (self.p_LINKED[0] != None) and (self.p_CHAR[1] != None)
    
    def act81(self):
        self.__test.append(('''self.p_LINKED[0].insert(self.p_CHAR[2]) ''',self.guard81,self.act81))
        __pre = {}
        __pre['''countLength(self.p_LINKED[0])'''] = countLength(self.p_LINKED[0])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[0])==__pre['''countLength(self.p_LINKED[0])''']+1)
        self.p_LINKED_used[0]=True
        self.p_CHAR_used[2]=True
    def guard81(self):
        return (self.p_LINKED[0] != None) and (self.p_CHAR[2] != None)
    
    def act82(self):
        self.__test.append(('''self.p_LINKED[1].insert(self.p_CHAR[0]) ''',self.guard82,self.act82))
        __pre = {}
        __pre['''countLength(self.p_LINKED[1])'''] = countLength(self.p_LINKED[1])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[1])==__pre['''countLength(self.p_LINKED[1])''']+1)
        self.p_LINKED_used[1]=True
        self.p_CHAR_used[0]=True
    def guard82(self):
        return (self.p_LINKED[1] != None) and (self.p_CHAR[0] != None)
    
    def act83(self):
        self.__test.append(('''self.p_LINKED[1].insert(self.p_CHAR[1]) ''',self.guard83,self.act83))
        __pre = {}
        __pre['''countLength(self.p_LINKED[1])'''] = countLength(self.p_LINKED[1])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[1])==__pre['''countLength(self.p_LINKED[1])''']+1)
        self.p_LINKED_used[1]=True
        self.p_CHAR_used[1]=True
    def guard83(self):
        return (self.p_LINKED[1] != None) and (self.p_CHAR[1] != None)
    
    def act84(self):
        self.__test.append(('''self.p_LINKED[1].insert(self.p_CHAR[2]) ''',self.guard84,self.act84))
        __pre = {}
        __pre['''countLength(self.p_LINKED[1])'''] = countLength(self.p_LINKED[1])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[1])==__pre['''countLength(self.p_LINKED[1])''']+1)
        self.p_LINKED_used[1]=True
        self.p_CHAR_used[2]=True
    def guard84(self):
        return (self.p_LINKED[1] != None) and (self.p_CHAR[2] != None)
    
    def act85(self):
        self.__test.append(('''self.p_LINKED[2].insert(self.p_CHAR[0]) ''',self.guard85,self.act85))
        __pre = {}
        __pre['''countLength(self.p_LINKED[2])'''] = countLength(self.p_LINKED[2])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[2])==__pre['''countLength(self.p_LINKED[2])''']+1)
        self.p_LINKED_used[2]=True
        self.p_CHAR_used[0]=True
    def guard85(self):
        return (self.p_LINKED[2] != None) and (self.p_CHAR[0] != None)
    
    def act86(self):
        self.__test.append(('''self.p_LINKED[2].insert(self.p_CHAR[1]) ''',self.guard86,self.act86))
        __pre = {}
        __pre['''countLength(self.p_LINKED[2])'''] = countLength(self.p_LINKED[2])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[2])==__pre['''countLength(self.p_LINKED[2])''']+1)
        self.p_LINKED_used[2]=True
        self.p_CHAR_used[1]=True
    def guard86(self):
        return (self.p_LINKED[2] != None) and (self.p_CHAR[1] != None)
    
    def act87(self):
        self.__test.append(('''self.p_LINKED[2].insert(self.p_CHAR[2]) ''',self.guard87,self.act87))
        __pre = {}
        __pre['''countLength(self.p_LINKED[2])'''] = countLength(self.p_LINKED[2])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[2])==__pre['''countLength(self.p_LINKED[2])''']+1)
        self.p_LINKED_used[2]=True
        self.p_CHAR_used[2]=True
    def guard87(self):
        return (self.p_LINKED[2] != None) and (self.p_CHAR[2] != None)
    
    def act88(self):
        self.__test.append(('''self.p_LINKED[3].insert(self.p_CHAR[0]) ''',self.guard88,self.act88))
        __pre = {}
        __pre['''countLength(self.p_LINKED[3])'''] = countLength(self.p_LINKED[3])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[3].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[3])==__pre['''countLength(self.p_LINKED[3])''']+1)
        self.p_LINKED_used[3]=True
        self.p_CHAR_used[0]=True
    def guard88(self):
        return (self.p_LINKED[3] != None) and (self.p_CHAR[0] != None)
    
    def act89(self):
        self.__test.append(('''self.p_LINKED[3].insert(self.p_CHAR[1]) ''',self.guard89,self.act89))
        __pre = {}
        __pre['''countLength(self.p_LINKED[3])'''] = countLength(self.p_LINKED[3])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[3].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[3])==__pre['''countLength(self.p_LINKED[3])''']+1)
        self.p_LINKED_used[3]=True
        self.p_CHAR_used[1]=True
    def guard89(self):
        return (self.p_LINKED[3] != None) and (self.p_CHAR[1] != None)
    
    def act90(self):
        self.__test.append(('''self.p_LINKED[3].insert(self.p_CHAR[2]) ''',self.guard90,self.act90))
        __pre = {}
        __pre['''countLength(self.p_LINKED[3])'''] = countLength(self.p_LINKED[3])
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKED[3].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (countLength(self.p_LINKED[3])==__pre['''countLength(self.p_LINKED[3])''']+1)
        self.p_LINKED_used[3]=True
        self.p_CHAR_used[2]=True
    def guard90(self):
        return (self.p_LINKED[3] != None) and (self.p_CHAR[2] != None)
    
    def act91(self):
        self.__test.append(('''print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  " ''',self.guard91,self.act91))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[0]=True
    def guard91(self):
        return (self.p_LINKED[0] != None) and (countLength(self.p_LINKED[0]) == 6)
    
    def act92(self):
        self.__test.append(('''print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  " ''',self.guard92,self.act92))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[1]=True
    def guard92(self):
        return (self.p_LINKED[1] != None) and (countLength(self.p_LINKED[1]) == 6)
    
    def act93(self):
        self.__test.append(('''print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  " ''',self.guard93,self.act93))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[2]=True
    def guard93(self):
        return (self.p_LINKED[2] != None) and (countLength(self.p_LINKED[2]) == 6)
    
    def act94(self):
        self.__test.append(('''print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  " ''',self.guard94,self.act94))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[3]=True
    def guard94(self):
        return (self.p_LINKED[3] != None) and (countLength(self.p_LINKED[3]) == 6)
    
    def act95(self):
        self.__test.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? " ''',self.guard95,self.act95))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[0]=True
    def guard95(self):
        return (self.p_LINKED[0] != None) and (countLength(self.p_LINKED[0]) == 6)
    
    def act96(self):
        self.__test.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? " ''',self.guard96,self.act96))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[1]=True
    def guard96(self):
        return (self.p_LINKED[1] != None) and (countLength(self.p_LINKED[1]) == 6)
    
    def act97(self):
        self.__test.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? " ''',self.guard97,self.act97))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[2]=True
    def guard97(self):
        return (self.p_LINKED[2] != None) and (countLength(self.p_LINKED[2]) == 6)
    
    def act98(self):
        self.__test.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? " ''',self.guard98,self.act98))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? "

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_LINKED_used[3]=True
    def guard98(self):
        return (self.p_LINKED[3] != None) and (countLength(self.p_LINKED[3]) == 6)
    
    def act99(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard99,self.act99))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard99(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act100(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard100,self.act100))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard100(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act101(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard101,self.act101))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard101(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act102(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard102,self.act102))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard102(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act103(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard103,self.act103))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard103(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act104(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard104,self.act104))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard104(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act105(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard105,self.act105))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard105(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act106(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard106,self.act106))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard106(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act107(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard107,self.act107))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard107(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act108(self):
        self.__test.append(('''print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4) ''',self.guard108,self.act108))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard108(self):
        return (self.p_LINKK[0] != None) and (countLength(self.p_LINKK[0]) == 4)
    
    def act109(self):
        self.__test.append(('''print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4) ''',self.guard109,self.act109))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard109(self):
        return (self.p_LINKK[1] != None) and (countLength(self.p_LINKK[1]) == 4)
    
    def act110(self):
        self.__test.append(('''print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4) ''',self.guard110,self.act110))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard110(self):
        return (self.p_LINKK[2] != None) and (countLength(self.p_LINKK[2]) == 4)
    
    def act111(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard111,self.act111))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard111(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act112(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard112,self.act112))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard112(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act113(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard113,self.act113))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard113(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act114(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard114,self.act114))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard114(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act115(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard115,self.act115))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard115(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act116(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard116,self.act116))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard116(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act117(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard117,self.act117))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard117(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act118(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard118,self.act118))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard118(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act119(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard119,self.act119))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard119(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act120(self):
        self.__test.append(('''self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard120,self.act120))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard120(self):
        return (self.p_LINKK[0] != None) and (self.p_LINKK[0] != None) and (countLength(self.p_LINKK[0]) == 4)
    
    def act121(self):
        self.__test.append(('''self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard121,self.act121))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard121(self):
        return (self.p_LINKK[0] != None) and (self.p_LINKK[1] != None) and (countLength(self.p_LINKK[0]) == 4)
    
    def act122(self):
        self.__test.append(('''self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard122,self.act122))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard122(self):
        return (self.p_LINKK[0] != None) and (self.p_LINKK[2] != None) and (countLength(self.p_LINKK[0]) == 4)
    
    def act123(self):
        self.__test.append(('''self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard123,self.act123))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard123(self):
        return (self.p_LINKK[1] != None) and (self.p_LINKK[0] != None) and (countLength(self.p_LINKK[1]) == 4)
    
    def act124(self):
        self.__test.append(('''self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard124,self.act124))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard124(self):
        return (self.p_LINKK[1] != None) and (self.p_LINKK[1] != None) and (countLength(self.p_LINKK[1]) == 4)
    
    def act125(self):
        self.__test.append(('''self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard125,self.act125))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard125(self):
        return (self.p_LINKK[1] != None) and (self.p_LINKK[2] != None) and (countLength(self.p_LINKK[1]) == 4)
    
    def act126(self):
        self.__test.append(('''self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard126,self.act126))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard126(self):
        return (self.p_LINKK[2] != None) and (self.p_LINKK[0] != None) and (countLength(self.p_LINKK[2]) == 4)
    
    def act127(self):
        self.__test.append(('''self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard127,self.act127))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard127(self):
        return (self.p_LINKK[2] != None) and (self.p_LINKK[1] != None) and (countLength(self.p_LINKK[2]) == 4)
    
    def act128(self):
        self.__test.append(('''self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard128,self.act128))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard128(self):
        return (self.p_LINKK[2] != None) and (self.p_LINKK[2] != None) and (countLength(self.p_LINKK[2]) == 4)
    
    def act129(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard129,self.act129))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard129(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act130(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard130,self.act130))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard130(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act131(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard131,self.act131))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard131(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act132(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard132,self.act132))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard132(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act133(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard133,self.act133))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard133(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act134(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard134,self.act134))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard134(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act135(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard135,self.act135))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard135(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act136(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard136,self.act136))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard136(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act137(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard137,self.act137))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard137(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act138(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard138,self.act138))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard138(self):
        return (self.p_LINKK[0] != None) and (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[0]) == 5) and (findFstDuplicates(self.p_LINKK[0]) !=False) )
    
    def act139(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard139,self.act139))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard139(self):
        return (self.p_LINKK[0] != None) and (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[0]) == 5) and (findFstDuplicates(self.p_LINKK[1]) !=False) )
    
    def act140(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard140,self.act140))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard140(self):
        return (self.p_LINKK[0] != None) and (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[0]) == 5) and (findFstDuplicates(self.p_LINKK[2]) !=False) )
    
    def act141(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard141,self.act141))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard141(self):
        return (self.p_LINKK[1] != None) and (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[1]) == 5) and (findFstDuplicates(self.p_LINKK[0]) !=False) )
    
    def act142(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard142,self.act142))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard142(self):
        return (self.p_LINKK[1] != None) and (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[1]) == 5) and (findFstDuplicates(self.p_LINKK[1]) !=False) )
    
    def act143(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard143,self.act143))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard143(self):
        return (self.p_LINKK[1] != None) and (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[1]) == 5) and (findFstDuplicates(self.p_LINKK[2]) !=False) )
    
    def act144(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard144,self.act144))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard144(self):
        return (self.p_LINKK[2] != None) and (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[2]) == 5) and (findFstDuplicates(self.p_LINKK[0]) !=False) )
    
    def act145(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard145,self.act145))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard145(self):
        return (self.p_LINKK[2] != None) and (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[2]) == 5) and (findFstDuplicates(self.p_LINKK[1]) !=False) )
    
    def act146(self):
        self.__test.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard146,self.act146))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard146(self):
        return (self.p_LINKK[2] != None) and (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[2]) == 5) and (findFstDuplicates(self.p_LINKK[2]) !=False) )
    
    def act147(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard147,self.act147))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard147(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act148(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard148,self.act148))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard148(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act149(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard149,self.act149))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard149(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act150(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard150,self.act150))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard150(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act151(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard151,self.act151))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard151(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act152(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard152,self.act152))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard152(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act153(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard153,self.act153))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard153(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act154(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard154,self.act154))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard154(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act155(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard155,self.act155))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard155(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act156(self):
        self.__test.append(('''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); ''',self.guard156,self.act156))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1));

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert findLstValue(self.p_LINKK[0])==(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)).val
    def guard156(self):
        return (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[0]) == 6))
    
    def act157(self):
        self.__test.append(('''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); ''',self.guard157,self.act157))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1));

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert findLstValue(self.p_LINKK[1])==(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)).val
    def guard157(self):
        return (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[1]) == 6))
    
    def act158(self):
        self.__test.append(('''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); ''',self.guard158,self.act158))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1));

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert findLstValue(self.p_LINKK[2])==(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)).val
    def guard158(self):
        return (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[2]) == 6))
    
    def act159(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard159,self.act159))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard159(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act160(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard160,self.act160))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard160(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act161(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard161,self.act161))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard161(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act162(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard162,self.act162))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard162(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act163(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard163,self.act163))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard163(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act164(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard164,self.act164))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard164(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act165(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard165,self.act165))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard165(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act166(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard166,self.act166))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard166(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act167(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard167,self.act167))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard167(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act168(self):
        self.__test.append((''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); ''',self.guard168,self.act168))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   findSecValue(self.p_LINKK[0]) == a
    def guard168(self):
        return (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[0]) == 5))
    
    def act169(self):
        self.__test.append((''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); ''',self.guard169,self.act169))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   findSecValue(self.p_LINKK[1]) == a
    def guard169(self):
        return (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[1]) == 5))
    
    def act170(self):
        self.__test.append((''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); ''',self.guard170,self.act170))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   findSecValue(self.p_LINKK[2]) == a
    def guard170(self):
        return (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[2]) == 5))
    
    def act171(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard171,self.act171))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard171(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act172(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard172,self.act172))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard172(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act173(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard173,self.act173))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard173(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act174(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard174,self.act174))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard174(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act175(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard175,self.act175))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard175(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act176(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard176,self.act176))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard176(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act177(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard177,self.act177))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard177(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act178(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard178,self.act178))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard178(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act179(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard179,self.act179))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard179(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act180(self):
        self.__test.append((''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard180,self.act180))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard180(self):
        return (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[0]) == 5))
    
    def act181(self):
        self.__test.append((''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard181,self.act181))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard181(self):
        return (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[1]) == 5))
    
    def act182(self):
        self.__test.append((''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard182,self.act182))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
    def guard182(self):
        return (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[2]) == 5))
    
    def act183(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard183,self.act183))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[0]=True
    def guard183(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[0] != None)
    
    def act184(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard184,self.act184))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[0]=True
    def guard184(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[0] != None)
    
    def act185(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard185,self.act185))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[0]=True
    def guard185(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[0] != None)
    
    def act186(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard186,self.act186))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[1]=True
    def guard186(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[1] != None)
    
    def act187(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard187,self.act187))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[1]=True
    def guard187(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[1] != None)
    
    def act188(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard188,self.act188))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[1]=True
    def guard188(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[1] != None)
    
    def act189(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard189,self.act189))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LINKK_used[2]=True
    def guard189(self):
        return (self.p_INT[0] != None) and (self.p_LINKK[2] != None)
    
    def act190(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard190,self.act190))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LINKK_used[2]=True
    def guard190(self):
        return (self.p_INT[1] != None) and (self.p_LINKK[2] != None)
    
    def act191(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard191,self.act191))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]) 

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LINKK_used[2]=True
    def guard191(self):
        return (self.p_INT[2] != None) and (self.p_LINKK[2] != None)
    
    def act192(self):
        self.__test.append((''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); ''',self.guard192,self.act192))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (a == c.next.val) and (b==c.next.next.next.val)
    def guard192(self):
        return (self.p_LINKK[0] != None) and ((countLength(self.p_LINKK[0]) == 5))
    
    def act193(self):
        self.__test.append((''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); ''',self.guard193,self.act193))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (a == c.next.val) and (b==c.next.next.next.val)
    def guard193(self):
        return (self.p_LINKK[1] != None) and ((countLength(self.p_LINKK[1]) == 5))
    
    def act194(self):
        self.__test.append((''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); ''',self.guard194,self.act194))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
             a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead());

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert   (a == c.next.val) and (b==c.next.next.next.val)
    def guard194(self):
        return (self.p_LINKK[2] != None) and ((countLength(self.p_LINKK[2]) == 5))
    
    def act195(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard195,self.act195))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard195(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act196(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard196,self.act196))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard196(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act197(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard197,self.act197))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard197(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act198(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard198,self.act198))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard198(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act199(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard199,self.act199))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard199(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act200(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard200,self.act200))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard200(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act201(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard201,self.act201))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard201(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act202(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard202,self.act202))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard202(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act203(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard203,self.act203))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard203(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act204(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard204,self.act204))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard204(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act205(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard205,self.act205))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard205(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act206(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard206,self.act206))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard206(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act207(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard207,self.act207))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard207(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act208(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard208,self.act208))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard208(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act209(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard209,self.act209))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard209(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act210(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard210,self.act210))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard210(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act211(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard211,self.act211))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard211(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act212(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard212,self.act212))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard212(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act213(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard213,self.act213))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard213(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act214(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard214,self.act214))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard214(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act215(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard215,self.act215))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard215(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act216(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard216,self.act216))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard216(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act217(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard217,self.act217))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard217(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act218(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard218,self.act218))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard218(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act219(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard219,self.act219))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[0]=True
    def guard219(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[0] != None)
    
    def act220(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard220,self.act220))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[0]=True
    def guard220(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[0] != None)
    
    def act221(self):
        self.__test.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard221,self.act221))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[0]=True
    def guard221(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[0] != None)
    
    def act222(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard222,self.act222))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard222(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act223(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard223,self.act223))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard223(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act224(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard224,self.act224))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard224(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act225(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard225,self.act225))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard225(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act226(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard226,self.act226))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard226(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act227(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard227,self.act227))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard227(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act228(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard228,self.act228))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard228(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act229(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard229,self.act229))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard229(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act230(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard230,self.act230))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard230(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act231(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard231,self.act231))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard231(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act232(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard232,self.act232))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard232(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act233(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard233,self.act233))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard233(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act234(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard234,self.act234))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard234(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act235(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard235,self.act235))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard235(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act236(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard236,self.act236))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard236(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act237(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard237,self.act237))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard237(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act238(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard238,self.act238))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard238(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act239(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard239,self.act239))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard239(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act240(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard240,self.act240))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard240(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act241(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard241,self.act241))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard241(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act242(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard242,self.act242))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard242(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act243(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard243,self.act243))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard243(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act244(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard244,self.act244))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard244(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act245(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard245,self.act245))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard245(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act246(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard246,self.act246))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[1]=True
    def guard246(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[1] != None)
    
    def act247(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard247,self.act247))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[1]=True
    def guard247(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[1] != None)
    
    def act248(self):
        self.__test.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard248,self.act248))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[1]=True
    def guard248(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[1] != None)
    
    def act249(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard249,self.act249))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard249(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act250(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard250,self.act250))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard250(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act251(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard251,self.act251))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard251(self):
        return (self.p_INT[0] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act252(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard252,self.act252))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard252(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act253(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard253,self.act253))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard253(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act254(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard254,self.act254))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard254(self):
        return (self.p_INT[0] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act255(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard255,self.act255))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard255(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act256(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard256,self.act256))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard256(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act257(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard257,self.act257))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[0]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard257(self):
        return (self.p_INT[0] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act258(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard258,self.act258))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard258(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act259(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard259,self.act259))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard259(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act260(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard260,self.act260))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard260(self):
        return (self.p_INT[1] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act261(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard261,self.act261))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard261(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act262(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard262,self.act262))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard262(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act263(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard263,self.act263))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard263(self):
        return (self.p_INT[1] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act264(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard264,self.act264))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard264(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act265(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard265,self.act265))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard265(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act266(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard266,self.act266))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[1]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard266(self):
        return (self.p_INT[1] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act267(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard267,self.act267))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard267(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act268(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard268,self.act268))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard268(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act269(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard269,self.act269))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[0]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard269(self):
        return (self.p_INT[2] != None) and (self.p_LIN[0] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act270(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard270,self.act270))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard270(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act271(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard271,self.act271))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard271(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act272(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard272,self.act272))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[1]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard272(self):
        return (self.p_INT[2] != None) and (self.p_LIN[1] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act273(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard273,self.act273))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[0]=True
        self.p_LINKK_used[2]=True
    def guard273(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[0] != None) and (self.p_LINKK[2] != None)
    
    def act274(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard274,self.act274))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[1]=True
        self.p_LINKK_used[2]=True
    def guard274(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[1] != None) and (self.p_LINKK[2] != None)
    
    def act275(self):
        self.__test.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard275,self.act275))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_INT_used[2]=True
        self.p_LIN_used[2]=True
        self.p_CHAR_used[2]=True
        self.p_LINKK_used[2]=True
    def guard275(self):
        return (self.p_INT[2] != None) and (self.p_LIN[2] != None) and (self.p_CHAR[2] != None) and (self.p_LINKK[2] != None)
    
    def act276(self):
        self.__test.append(('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard276,self.act276))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard276(self):
        return (self.p_LIN[0] != None) and (self.p_LINKK[0] != None) and ((countLength(self.p_LIN[0])==4) and (countLength(self.p_LINKK[0])==5))
    
    def act277(self):
        self.__test.append(('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard277,self.act277))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard277(self):
        return (self.p_LIN[0] != None) and (self.p_LINKK[1] != None) and ((countLength(self.p_LIN[0])==4) and (countLength(self.p_LINKK[1])==5))
    
    def act278(self):
        self.__test.append(('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard278,self.act278))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard278(self):
        return (self.p_LIN[0] != None) and (self.p_LINKK[2] != None) and ((countLength(self.p_LIN[0])==4) and (countLength(self.p_LINKK[2])==5))
    
    def act279(self):
        self.__test.append(('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard279,self.act279))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard279(self):
        return (self.p_LIN[1] != None) and (self.p_LINKK[0] != None) and ((countLength(self.p_LIN[1])==4) and (countLength(self.p_LINKK[0])==5))
    
    def act280(self):
        self.__test.append(('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard280,self.act280))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard280(self):
        return (self.p_LIN[1] != None) and (self.p_LINKK[1] != None) and ((countLength(self.p_LIN[1])==4) and (countLength(self.p_LINKK[1])==5))
    
    def act281(self):
        self.__test.append(('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard281,self.act281))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard281(self):
        return (self.p_LIN[1] != None) and (self.p_LINKK[2] != None) and ((countLength(self.p_LIN[1])==4) and (countLength(self.p_LINKK[2])==5))
    
    def act282(self):
        self.__test.append(('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard282,self.act282))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard282(self):
        return (self.p_LIN[2] != None) and (self.p_LINKK[0] != None) and ((countLength(self.p_LIN[2])==4) and (countLength(self.p_LINKK[0])==5))
    
    def act283(self):
        self.__test.append(('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard283,self.act283))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard283(self):
        return (self.p_LIN[2] != None) and (self.p_LINKK[1] != None) and ((countLength(self.p_LIN[2])==4) and (countLength(self.p_LINKK[1])==5))
    
    def act284(self):
        self.__test.append(('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard284,self.act284))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x);

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        assert  lengthHead(x)==9
    def guard284(self):
        return (self.p_LIN[2] != None) and (self.p_LINKK[2] != None) and ((countLength(self.p_LIN[2])==4) and (countLength(self.p_LINKK[2])==5))
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__modules.append(r"linkedlist.py")
        self.__features = []
        self.__replayBacktrack = False
        self.__cov = coverage.coverage(branch=True, source=["linkedlist.py"])
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
        self.p_INT = {}
        self.p_INT_used = {}
        self.__pools.append("self.p_INT")
        self.p_INT[0] = None
        self.p_INT_used[0] = True
        self.p_INT[1] = None
        self.p_INT_used[1] = True
        self.p_INT[2] = None
        self.p_INT_used[2] = True
        self.p_INT[3] = None
        self.p_INT_used[3] = True
        self.p_LIST = {}
        self.p_LIST_used = {}
        self.__pools.append("self.p_LIST")
        self.p_LIST[0] = None
        self.p_LIST_used[0] = True
        self.p_LIST[1] = None
        self.p_LIST_used[1] = True
        self.p_LIST[2] = None
        self.p_LIST_used[2] = True
        self.p_LIST[3] = None
        self.p_LIST_used[3] = True
        self.p_LIN = {}
        self.p_LIN_used = {}
        self.__pools.append("self.p_LIN")
        self.p_LIN[0] = None
        self.p_LIN_used[0] = True
        self.p_LIN[1] = None
        self.p_LIN_used[1] = True
        self.p_LIN[2] = None
        self.p_LIN_used[2] = True
        self.p_LIN[3] = None
        self.p_LIN_used[3] = True
        self.p_LINKED = {}
        self.p_LINKED_used = {}
        self.__pools.append("self.p_LINKED")
        self.p_LINKED[0] = None
        self.p_LINKED_used[0] = True
        self.p_LINKED[1] = None
        self.p_LINKED_used[1] = True
        self.p_LINKED[2] = None
        self.p_LINKED_used[2] = True
        self.p_LINKED[3] = None
        self.p_LINKED_used[3] = True
        self.p_LINKED[4] = None
        self.p_LINKED_used[4] = True
        self.p_CHAR = {}
        self.p_CHAR_used = {}
        self.__pools.append("self.p_CHAR")
        self.p_CHAR[0] = None
        self.p_CHAR_used[0] = True
        self.p_CHAR[1] = None
        self.p_CHAR_used[1] = True
        self.p_CHAR[2] = None
        self.p_CHAR_used[2] = True
        self.p_CHAR[3] = None
        self.p_CHAR_used[3] = True
        self.p_LINKK = {}
        self.p_LINKK_used = {}
        self.__pools.append("self.p_LINKK")
        self.p_LINKK[0] = None
        self.p_LINKK_used[0] = True
        self.p_LINKK[1] = None
        self.p_LINKK_used[1] = True
        self.p_LINKK[2] = None
        self.p_LINKK_used[2] = True
        self.p_LINKK[3] = None
        self.p_LINKK_used[3] = True
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
        self.__actions.append(('''self.p_INT[0] =1  ''',self.guard0,self.act0))

        self.__names['''self.p_INT[0] =1  '''] = ('''self.p_INT[0] =1  ''',self.guard0,self.act0)

        self.__orderings['''self.p_INT[0] =1  '''] = 1

        self.__okExcepts['''self.p_INT[0] =1  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =2  ''',self.guard1,self.act1))

        self.__names['''self.p_INT[0] =2  '''] = ('''self.p_INT[0] =2  ''',self.guard1,self.act1)

        self.__orderings['''self.p_INT[0] =2  '''] = 2

        self.__okExcepts['''self.p_INT[0] =2  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =3  ''',self.guard2,self.act2))

        self.__names['''self.p_INT[0] =3  '''] = ('''self.p_INT[0] =3  ''',self.guard2,self.act2)

        self.__orderings['''self.p_INT[0] =3  '''] = 3

        self.__okExcepts['''self.p_INT[0] =3  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =4  ''',self.guard3,self.act3))

        self.__names['''self.p_INT[0] =4  '''] = ('''self.p_INT[0] =4  ''',self.guard3,self.act3)

        self.__orderings['''self.p_INT[0] =4  '''] = 4

        self.__okExcepts['''self.p_INT[0] =4  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =5  ''',self.guard4,self.act4))

        self.__names['''self.p_INT[0] =5  '''] = ('''self.p_INT[0] =5  ''',self.guard4,self.act4)

        self.__orderings['''self.p_INT[0] =5  '''] = 5

        self.__okExcepts['''self.p_INT[0] =5  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =6  ''',self.guard5,self.act5))

        self.__names['''self.p_INT[0] =6  '''] = ('''self.p_INT[0] =6  ''',self.guard5,self.act5)

        self.__orderings['''self.p_INT[0] =6  '''] = 6

        self.__okExcepts['''self.p_INT[0] =6  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =7  ''',self.guard6,self.act6))

        self.__names['''self.p_INT[0] =7  '''] = ('''self.p_INT[0] =7  ''',self.guard6,self.act6)

        self.__orderings['''self.p_INT[0] =7  '''] = 7

        self.__okExcepts['''self.p_INT[0] =7  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =8  ''',self.guard7,self.act7))

        self.__names['''self.p_INT[0] =8  '''] = ('''self.p_INT[0] =8  ''',self.guard7,self.act7)

        self.__orderings['''self.p_INT[0] =8  '''] = 8

        self.__okExcepts['''self.p_INT[0] =8  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =9  ''',self.guard8,self.act8))

        self.__names['''self.p_INT[0] =9  '''] = ('''self.p_INT[0] =9  ''',self.guard8,self.act8)

        self.__orderings['''self.p_INT[0] =9  '''] = 9

        self.__okExcepts['''self.p_INT[0] =9  '''] = ''''''

        self.__actions.append(('''self.p_INT[0] =10  ''',self.guard9,self.act9))

        self.__names['''self.p_INT[0] =10  '''] = ('''self.p_INT[0] =10  ''',self.guard9,self.act9)

        self.__orderings['''self.p_INT[0] =10  '''] = 10

        self.__okExcepts['''self.p_INT[0] =10  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =1  ''',self.guard10,self.act10))

        self.__names['''self.p_INT[1] =1  '''] = ('''self.p_INT[1] =1  ''',self.guard10,self.act10)

        self.__orderings['''self.p_INT[1] =1  '''] = 11

        self.__okExcepts['''self.p_INT[1] =1  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =2  ''',self.guard11,self.act11))

        self.__names['''self.p_INT[1] =2  '''] = ('''self.p_INT[1] =2  ''',self.guard11,self.act11)

        self.__orderings['''self.p_INT[1] =2  '''] = 12

        self.__okExcepts['''self.p_INT[1] =2  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =3  ''',self.guard12,self.act12))

        self.__names['''self.p_INT[1] =3  '''] = ('''self.p_INT[1] =3  ''',self.guard12,self.act12)

        self.__orderings['''self.p_INT[1] =3  '''] = 13

        self.__okExcepts['''self.p_INT[1] =3  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =4  ''',self.guard13,self.act13))

        self.__names['''self.p_INT[1] =4  '''] = ('''self.p_INT[1] =4  ''',self.guard13,self.act13)

        self.__orderings['''self.p_INT[1] =4  '''] = 14

        self.__okExcepts['''self.p_INT[1] =4  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =5  ''',self.guard14,self.act14))

        self.__names['''self.p_INT[1] =5  '''] = ('''self.p_INT[1] =5  ''',self.guard14,self.act14)

        self.__orderings['''self.p_INT[1] =5  '''] = 15

        self.__okExcepts['''self.p_INT[1] =5  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =6  ''',self.guard15,self.act15))

        self.__names['''self.p_INT[1] =6  '''] = ('''self.p_INT[1] =6  ''',self.guard15,self.act15)

        self.__orderings['''self.p_INT[1] =6  '''] = 16

        self.__okExcepts['''self.p_INT[1] =6  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =7  ''',self.guard16,self.act16))

        self.__names['''self.p_INT[1] =7  '''] = ('''self.p_INT[1] =7  ''',self.guard16,self.act16)

        self.__orderings['''self.p_INT[1] =7  '''] = 17

        self.__okExcepts['''self.p_INT[1] =7  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =8  ''',self.guard17,self.act17))

        self.__names['''self.p_INT[1] =8  '''] = ('''self.p_INT[1] =8  ''',self.guard17,self.act17)

        self.__orderings['''self.p_INT[1] =8  '''] = 18

        self.__okExcepts['''self.p_INT[1] =8  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =9  ''',self.guard18,self.act18))

        self.__names['''self.p_INT[1] =9  '''] = ('''self.p_INT[1] =9  ''',self.guard18,self.act18)

        self.__orderings['''self.p_INT[1] =9  '''] = 19

        self.__okExcepts['''self.p_INT[1] =9  '''] = ''''''

        self.__actions.append(('''self.p_INT[1] =10  ''',self.guard19,self.act19))

        self.__names['''self.p_INT[1] =10  '''] = ('''self.p_INT[1] =10  ''',self.guard19,self.act19)

        self.__orderings['''self.p_INT[1] =10  '''] = 20

        self.__okExcepts['''self.p_INT[1] =10  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =1  ''',self.guard20,self.act20))

        self.__names['''self.p_INT[2] =1  '''] = ('''self.p_INT[2] =1  ''',self.guard20,self.act20)

        self.__orderings['''self.p_INT[2] =1  '''] = 21

        self.__okExcepts['''self.p_INT[2] =1  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =2  ''',self.guard21,self.act21))

        self.__names['''self.p_INT[2] =2  '''] = ('''self.p_INT[2] =2  ''',self.guard21,self.act21)

        self.__orderings['''self.p_INT[2] =2  '''] = 22

        self.__okExcepts['''self.p_INT[2] =2  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =3  ''',self.guard22,self.act22))

        self.__names['''self.p_INT[2] =3  '''] = ('''self.p_INT[2] =3  ''',self.guard22,self.act22)

        self.__orderings['''self.p_INT[2] =3  '''] = 23

        self.__okExcepts['''self.p_INT[2] =3  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =4  ''',self.guard23,self.act23))

        self.__names['''self.p_INT[2] =4  '''] = ('''self.p_INT[2] =4  ''',self.guard23,self.act23)

        self.__orderings['''self.p_INT[2] =4  '''] = 24

        self.__okExcepts['''self.p_INT[2] =4  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =5  ''',self.guard24,self.act24))

        self.__names['''self.p_INT[2] =5  '''] = ('''self.p_INT[2] =5  ''',self.guard24,self.act24)

        self.__orderings['''self.p_INT[2] =5  '''] = 25

        self.__okExcepts['''self.p_INT[2] =5  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =6  ''',self.guard25,self.act25))

        self.__names['''self.p_INT[2] =6  '''] = ('''self.p_INT[2] =6  ''',self.guard25,self.act25)

        self.__orderings['''self.p_INT[2] =6  '''] = 26

        self.__okExcepts['''self.p_INT[2] =6  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =7  ''',self.guard26,self.act26))

        self.__names['''self.p_INT[2] =7  '''] = ('''self.p_INT[2] =7  ''',self.guard26,self.act26)

        self.__orderings['''self.p_INT[2] =7  '''] = 27

        self.__okExcepts['''self.p_INT[2] =7  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =8  ''',self.guard27,self.act27))

        self.__names['''self.p_INT[2] =8  '''] = ('''self.p_INT[2] =8  ''',self.guard27,self.act27)

        self.__orderings['''self.p_INT[2] =8  '''] = 28

        self.__okExcepts['''self.p_INT[2] =8  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =9  ''',self.guard28,self.act28))

        self.__names['''self.p_INT[2] =9  '''] = ('''self.p_INT[2] =9  ''',self.guard28,self.act28)

        self.__orderings['''self.p_INT[2] =9  '''] = 29

        self.__okExcepts['''self.p_INT[2] =9  '''] = ''''''

        self.__actions.append(('''self.p_INT[2] =10  ''',self.guard29,self.act29))

        self.__names['''self.p_INT[2] =10  '''] = ('''self.p_INT[2] =10  ''',self.guard29,self.act29)

        self.__orderings['''self.p_INT[2] =10  '''] = 30

        self.__okExcepts['''self.p_INT[2] =10  '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 'a' ''',self.guard30,self.act30))

        self.__names['''self.p_CHAR[0] = 'a' '''] = ('''self.p_CHAR[0] = 'a' ''',self.guard30,self.act30)

        self.__orderings['''self.p_CHAR[0] = 'a' '''] = 31

        self.__okExcepts['''self.p_CHAR[0] = 'a' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 'b' ''',self.guard31,self.act31))

        self.__names['''self.p_CHAR[0] = 'b' '''] = ('''self.p_CHAR[0] = 'b' ''',self.guard31,self.act31)

        self.__orderings['''self.p_CHAR[0] = 'b' '''] = 32

        self.__okExcepts['''self.p_CHAR[0] = 'b' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 'c' ''',self.guard32,self.act32))

        self.__names['''self.p_CHAR[0] = 'c' '''] = ('''self.p_CHAR[0] = 'c' ''',self.guard32,self.act32)

        self.__orderings['''self.p_CHAR[0] = 'c' '''] = 33

        self.__okExcepts['''self.p_CHAR[0] = 'c' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 'd' ''',self.guard33,self.act33))

        self.__names['''self.p_CHAR[0] = 'd' '''] = ('''self.p_CHAR[0] = 'd' ''',self.guard33,self.act33)

        self.__orderings['''self.p_CHAR[0] = 'd' '''] = 34

        self.__okExcepts['''self.p_CHAR[0] = 'd' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = '*' ''',self.guard34,self.act34))

        self.__names['''self.p_CHAR[0] = '*' '''] = ('''self.p_CHAR[0] = '*' ''',self.guard34,self.act34)

        self.__orderings['''self.p_CHAR[0] = '*' '''] = 35

        self.__okExcepts['''self.p_CHAR[0] = '*' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = '$' ''',self.guard35,self.act35))

        self.__names['''self.p_CHAR[0] = '$' '''] = ('''self.p_CHAR[0] = '$' ''',self.guard35,self.act35)

        self.__orderings['''self.p_CHAR[0] = '$' '''] = 36

        self.__okExcepts['''self.p_CHAR[0] = '$' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 'hello good' ''',self.guard36,self.act36))

        self.__names['''self.p_CHAR[0] = 'hello good' '''] = ('''self.p_CHAR[0] = 'hello good' ''',self.guard36,self.act36)

        self.__orderings['''self.p_CHAR[0] = 'hello good' '''] = 37

        self.__okExcepts['''self.p_CHAR[0] = 'hello good' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 100 ''',self.guard37,self.act37))

        self.__names['''self.p_CHAR[0] = 100 '''] = ('''self.p_CHAR[0] = 100 ''',self.guard37,self.act37)

        self.__orderings['''self.p_CHAR[0] = 100 '''] = 38

        self.__okExcepts['''self.p_CHAR[0] = 100 '''] = ''''''

        self.__actions.append(('''self.p_CHAR[0] = 200.1 ''',self.guard38,self.act38))

        self.__names['''self.p_CHAR[0] = 200.1 '''] = ('''self.p_CHAR[0] = 200.1 ''',self.guard38,self.act38)

        self.__orderings['''self.p_CHAR[0] = 200.1 '''] = 39

        self.__okExcepts['''self.p_CHAR[0] = 200.1 '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 'a' ''',self.guard39,self.act39))

        self.__names['''self.p_CHAR[1] = 'a' '''] = ('''self.p_CHAR[1] = 'a' ''',self.guard39,self.act39)

        self.__orderings['''self.p_CHAR[1] = 'a' '''] = 40

        self.__okExcepts['''self.p_CHAR[1] = 'a' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 'b' ''',self.guard40,self.act40))

        self.__names['''self.p_CHAR[1] = 'b' '''] = ('''self.p_CHAR[1] = 'b' ''',self.guard40,self.act40)

        self.__orderings['''self.p_CHAR[1] = 'b' '''] = 41

        self.__okExcepts['''self.p_CHAR[1] = 'b' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 'c' ''',self.guard41,self.act41))

        self.__names['''self.p_CHAR[1] = 'c' '''] = ('''self.p_CHAR[1] = 'c' ''',self.guard41,self.act41)

        self.__orderings['''self.p_CHAR[1] = 'c' '''] = 42

        self.__okExcepts['''self.p_CHAR[1] = 'c' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 'd' ''',self.guard42,self.act42))

        self.__names['''self.p_CHAR[1] = 'd' '''] = ('''self.p_CHAR[1] = 'd' ''',self.guard42,self.act42)

        self.__orderings['''self.p_CHAR[1] = 'd' '''] = 43

        self.__okExcepts['''self.p_CHAR[1] = 'd' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = '*' ''',self.guard43,self.act43))

        self.__names['''self.p_CHAR[1] = '*' '''] = ('''self.p_CHAR[1] = '*' ''',self.guard43,self.act43)

        self.__orderings['''self.p_CHAR[1] = '*' '''] = 44

        self.__okExcepts['''self.p_CHAR[1] = '*' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = '$' ''',self.guard44,self.act44))

        self.__names['''self.p_CHAR[1] = '$' '''] = ('''self.p_CHAR[1] = '$' ''',self.guard44,self.act44)

        self.__orderings['''self.p_CHAR[1] = '$' '''] = 45

        self.__okExcepts['''self.p_CHAR[1] = '$' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 'hello good' ''',self.guard45,self.act45))

        self.__names['''self.p_CHAR[1] = 'hello good' '''] = ('''self.p_CHAR[1] = 'hello good' ''',self.guard45,self.act45)

        self.__orderings['''self.p_CHAR[1] = 'hello good' '''] = 46

        self.__okExcepts['''self.p_CHAR[1] = 'hello good' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 100 ''',self.guard46,self.act46))

        self.__names['''self.p_CHAR[1] = 100 '''] = ('''self.p_CHAR[1] = 100 ''',self.guard46,self.act46)

        self.__orderings['''self.p_CHAR[1] = 100 '''] = 47

        self.__okExcepts['''self.p_CHAR[1] = 100 '''] = ''''''

        self.__actions.append(('''self.p_CHAR[1] = 200.1 ''',self.guard47,self.act47))

        self.__names['''self.p_CHAR[1] = 200.1 '''] = ('''self.p_CHAR[1] = 200.1 ''',self.guard47,self.act47)

        self.__orderings['''self.p_CHAR[1] = 200.1 '''] = 48

        self.__okExcepts['''self.p_CHAR[1] = 200.1 '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 'a' ''',self.guard48,self.act48))

        self.__names['''self.p_CHAR[2] = 'a' '''] = ('''self.p_CHAR[2] = 'a' ''',self.guard48,self.act48)

        self.__orderings['''self.p_CHAR[2] = 'a' '''] = 49

        self.__okExcepts['''self.p_CHAR[2] = 'a' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 'b' ''',self.guard49,self.act49))

        self.__names['''self.p_CHAR[2] = 'b' '''] = ('''self.p_CHAR[2] = 'b' ''',self.guard49,self.act49)

        self.__orderings['''self.p_CHAR[2] = 'b' '''] = 50

        self.__okExcepts['''self.p_CHAR[2] = 'b' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 'c' ''',self.guard50,self.act50))

        self.__names['''self.p_CHAR[2] = 'c' '''] = ('''self.p_CHAR[2] = 'c' ''',self.guard50,self.act50)

        self.__orderings['''self.p_CHAR[2] = 'c' '''] = 51

        self.__okExcepts['''self.p_CHAR[2] = 'c' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 'd' ''',self.guard51,self.act51))

        self.__names['''self.p_CHAR[2] = 'd' '''] = ('''self.p_CHAR[2] = 'd' ''',self.guard51,self.act51)

        self.__orderings['''self.p_CHAR[2] = 'd' '''] = 52

        self.__okExcepts['''self.p_CHAR[2] = 'd' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = '*' ''',self.guard52,self.act52))

        self.__names['''self.p_CHAR[2] = '*' '''] = ('''self.p_CHAR[2] = '*' ''',self.guard52,self.act52)

        self.__orderings['''self.p_CHAR[2] = '*' '''] = 53

        self.__okExcepts['''self.p_CHAR[2] = '*' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = '$' ''',self.guard53,self.act53))

        self.__names['''self.p_CHAR[2] = '$' '''] = ('''self.p_CHAR[2] = '$' ''',self.guard53,self.act53)

        self.__orderings['''self.p_CHAR[2] = '$' '''] = 54

        self.__okExcepts['''self.p_CHAR[2] = '$' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 'hello good' ''',self.guard54,self.act54))

        self.__names['''self.p_CHAR[2] = 'hello good' '''] = ('''self.p_CHAR[2] = 'hello good' ''',self.guard54,self.act54)

        self.__orderings['''self.p_CHAR[2] = 'hello good' '''] = 55

        self.__okExcepts['''self.p_CHAR[2] = 'hello good' '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 100 ''',self.guard55,self.act55))

        self.__names['''self.p_CHAR[2] = 100 '''] = ('''self.p_CHAR[2] = 100 ''',self.guard55,self.act55)

        self.__orderings['''self.p_CHAR[2] = 100 '''] = 56

        self.__okExcepts['''self.p_CHAR[2] = 100 '''] = ''''''

        self.__actions.append(('''self.p_CHAR[2] = 200.1 ''',self.guard56,self.act56))

        self.__names['''self.p_CHAR[2] = 200.1 '''] = ('''self.p_CHAR[2] = 200.1 ''',self.guard56,self.act56)

        self.__orderings['''self.p_CHAR[2] = 200.1 '''] = 57

        self.__okExcepts['''self.p_CHAR[2] = 200.1 '''] = ''''''

        self.__actions.append(('''self.p_LIST[0]=[] ''',self.guard57,self.act57))

        self.__names['''self.p_LIST[0]=[] '''] = ('''self.p_LIST[0]=[] ''',self.guard57,self.act57)

        self.__orderings['''self.p_LIST[0]=[] '''] = 58

        self.__okExcepts['''self.p_LIST[0]=[] '''] = ''''''

        self.__actions.append(('''self.p_LIST[1]=[] ''',self.guard58,self.act58))

        self.__names['''self.p_LIST[1]=[] '''] = ('''self.p_LIST[1]=[] ''',self.guard58,self.act58)

        self.__orderings['''self.p_LIST[1]=[] '''] = 59

        self.__okExcepts['''self.p_LIST[1]=[] '''] = ''''''

        self.__actions.append(('''self.p_LIST[2]=[] ''',self.guard59,self.act59))

        self.__names['''self.p_LIST[2]=[] '''] = ('''self.p_LIST[2]=[] ''',self.guard59,self.act59)

        self.__orderings['''self.p_LIST[2]=[] '''] = 60

        self.__okExcepts['''self.p_LIST[2]=[] '''] = ''''''

        self.__actions.append(('''self.p_LIST[0].append(self.p_INT[0]) ''',self.guard60,self.act60))

        self.__names['''self.p_LIST[0].append(self.p_INT[0]) '''] = ('''self.p_LIST[0].append(self.p_INT[0]) ''',self.guard60,self.act60)

        self.__orderings['''self.p_LIST[0].append(self.p_INT[0]) '''] = 61

        self.__okExcepts['''self.p_LIST[0].append(self.p_INT[0]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[0].append(self.p_INT[1]) ''',self.guard61,self.act61))

        self.__names['''self.p_LIST[0].append(self.p_INT[1]) '''] = ('''self.p_LIST[0].append(self.p_INT[1]) ''',self.guard61,self.act61)

        self.__orderings['''self.p_LIST[0].append(self.p_INT[1]) '''] = 62

        self.__okExcepts['''self.p_LIST[0].append(self.p_INT[1]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[0].append(self.p_INT[2]) ''',self.guard62,self.act62))

        self.__names['''self.p_LIST[0].append(self.p_INT[2]) '''] = ('''self.p_LIST[0].append(self.p_INT[2]) ''',self.guard62,self.act62)

        self.__orderings['''self.p_LIST[0].append(self.p_INT[2]) '''] = 63

        self.__okExcepts['''self.p_LIST[0].append(self.p_INT[2]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[1].append(self.p_INT[0]) ''',self.guard63,self.act63))

        self.__names['''self.p_LIST[1].append(self.p_INT[0]) '''] = ('''self.p_LIST[1].append(self.p_INT[0]) ''',self.guard63,self.act63)

        self.__orderings['''self.p_LIST[1].append(self.p_INT[0]) '''] = 64

        self.__okExcepts['''self.p_LIST[1].append(self.p_INT[0]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[1].append(self.p_INT[1]) ''',self.guard64,self.act64))

        self.__names['''self.p_LIST[1].append(self.p_INT[1]) '''] = ('''self.p_LIST[1].append(self.p_INT[1]) ''',self.guard64,self.act64)

        self.__orderings['''self.p_LIST[1].append(self.p_INT[1]) '''] = 65

        self.__okExcepts['''self.p_LIST[1].append(self.p_INT[1]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[1].append(self.p_INT[2]) ''',self.guard65,self.act65))

        self.__names['''self.p_LIST[1].append(self.p_INT[2]) '''] = ('''self.p_LIST[1].append(self.p_INT[2]) ''',self.guard65,self.act65)

        self.__orderings['''self.p_LIST[1].append(self.p_INT[2]) '''] = 66

        self.__okExcepts['''self.p_LIST[1].append(self.p_INT[2]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[2].append(self.p_INT[0]) ''',self.guard66,self.act66))

        self.__names['''self.p_LIST[2].append(self.p_INT[0]) '''] = ('''self.p_LIST[2].append(self.p_INT[0]) ''',self.guard66,self.act66)

        self.__orderings['''self.p_LIST[2].append(self.p_INT[0]) '''] = 67

        self.__okExcepts['''self.p_LIST[2].append(self.p_INT[0]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[2].append(self.p_INT[1]) ''',self.guard67,self.act67))

        self.__names['''self.p_LIST[2].append(self.p_INT[1]) '''] = ('''self.p_LIST[2].append(self.p_INT[1]) ''',self.guard67,self.act67)

        self.__orderings['''self.p_LIST[2].append(self.p_INT[1]) '''] = 68

        self.__okExcepts['''self.p_LIST[2].append(self.p_INT[1]) '''] = ''''''

        self.__actions.append(('''self.p_LIST[2].append(self.p_INT[2]) ''',self.guard68,self.act68))

        self.__names['''self.p_LIST[2].append(self.p_INT[2]) '''] = ('''self.p_LIST[2].append(self.p_INT[2]) ''',self.guard68,self.act68)

        self.__orderings['''self.p_LIST[2].append(self.p_INT[2]) '''] = 69

        self.__okExcepts['''self.p_LIST[2].append(self.p_INT[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKED[0]=linkedlist.linkedList() ''',self.guard69,self.act69))

        self.__names['''self.p_LINKED[0]=linkedlist.linkedList() '''] = ('''self.p_LINKED[0]=linkedlist.linkedList() ''',self.guard69,self.act69)

        self.__orderings['''self.p_LINKED[0]=linkedlist.linkedList() '''] = 70

        self.__okExcepts['''self.p_LINKED[0]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKED[1]=linkedlist.linkedList() ''',self.guard70,self.act70))

        self.__names['''self.p_LINKED[1]=linkedlist.linkedList() '''] = ('''self.p_LINKED[1]=linkedlist.linkedList() ''',self.guard70,self.act70)

        self.__orderings['''self.p_LINKED[1]=linkedlist.linkedList() '''] = 71

        self.__okExcepts['''self.p_LINKED[1]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKED[2]=linkedlist.linkedList() ''',self.guard71,self.act71))

        self.__names['''self.p_LINKED[2]=linkedlist.linkedList() '''] = ('''self.p_LINKED[2]=linkedlist.linkedList() ''',self.guard71,self.act71)

        self.__orderings['''self.p_LINKED[2]=linkedlist.linkedList() '''] = 72

        self.__okExcepts['''self.p_LINKED[2]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKED[3]=linkedlist.linkedList() ''',self.guard72,self.act72))

        self.__names['''self.p_LINKED[3]=linkedlist.linkedList() '''] = ('''self.p_LINKED[3]=linkedlist.linkedList() ''',self.guard72,self.act72)

        self.__orderings['''self.p_LINKED[3]=linkedlist.linkedList() '''] = 73

        self.__okExcepts['''self.p_LINKED[3]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0]=linkedlist.linkedList() ''',self.guard73,self.act73))

        self.__names['''self.p_LINKK[0]=linkedlist.linkedList() '''] = ('''self.p_LINKK[0]=linkedlist.linkedList() ''',self.guard73,self.act73)

        self.__orderings['''self.p_LINKK[0]=linkedlist.linkedList() '''] = 74

        self.__okExcepts['''self.p_LINKK[0]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1]=linkedlist.linkedList() ''',self.guard74,self.act74))

        self.__names['''self.p_LINKK[1]=linkedlist.linkedList() '''] = ('''self.p_LINKK[1]=linkedlist.linkedList() ''',self.guard74,self.act74)

        self.__orderings['''self.p_LINKK[1]=linkedlist.linkedList() '''] = 75

        self.__okExcepts['''self.p_LINKK[1]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2]=linkedlist.linkedList() ''',self.guard75,self.act75))

        self.__names['''self.p_LINKK[2]=linkedlist.linkedList() '''] = ('''self.p_LINKK[2]=linkedlist.linkedList() ''',self.guard75,self.act75)

        self.__orderings['''self.p_LINKK[2]=linkedlist.linkedList() '''] = 76

        self.__okExcepts['''self.p_LINKK[2]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LIN[0]=linkedlist.linkedList() ''',self.guard76,self.act76))

        self.__names['''self.p_LIN[0]=linkedlist.linkedList() '''] = ('''self.p_LIN[0]=linkedlist.linkedList() ''',self.guard76,self.act76)

        self.__orderings['''self.p_LIN[0]=linkedlist.linkedList() '''] = 77

        self.__okExcepts['''self.p_LIN[0]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LIN[1]=linkedlist.linkedList() ''',self.guard77,self.act77))

        self.__names['''self.p_LIN[1]=linkedlist.linkedList() '''] = ('''self.p_LIN[1]=linkedlist.linkedList() ''',self.guard77,self.act77)

        self.__orderings['''self.p_LIN[1]=linkedlist.linkedList() '''] = 78

        self.__okExcepts['''self.p_LIN[1]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LIN[2]=linkedlist.linkedList() ''',self.guard78,self.act78))

        self.__names['''self.p_LIN[2]=linkedlist.linkedList() '''] = ('''self.p_LIN[2]=linkedlist.linkedList() ''',self.guard78,self.act78)

        self.__orderings['''self.p_LIN[2]=linkedlist.linkedList() '''] = 79

        self.__okExcepts['''self.p_LIN[2]=linkedlist.linkedList() '''] = ''''''

        self.__actions.append(('''self.p_LINKED[0].insert(self.p_CHAR[0]) ''',self.guard79,self.act79))

        self.__names['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKED[0].insert(self.p_CHAR[0]) ''',self.guard79,self.act79)

        self.__orderings['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''] = 80

        self.__okExcepts['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__propCode['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''] = r"  (countLength(self.p_LINKED[0])==__pre['''countLength(self.p_LINKED[0])''']+1)"

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''] = []

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[0]) '''].append(r"__pre['''countLength(self.p_LINKED[0])'''] = countLength(self.p_LINKED[0])")

        self.__actions.append(('''self.p_LINKED[0].insert(self.p_CHAR[1]) ''',self.guard80,self.act80))

        self.__names['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKED[0].insert(self.p_CHAR[1]) ''',self.guard80,self.act80)

        self.__orderings['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''] = 81

        self.__okExcepts['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__propCode['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''] = r"  (countLength(self.p_LINKED[0])==__pre['''countLength(self.p_LINKED[0])''']+1)"

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''] = []

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[1]) '''].append(r"__pre['''countLength(self.p_LINKED[0])'''] = countLength(self.p_LINKED[0])")

        self.__actions.append(('''self.p_LINKED[0].insert(self.p_CHAR[2]) ''',self.guard81,self.act81))

        self.__names['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKED[0].insert(self.p_CHAR[2]) ''',self.guard81,self.act81)

        self.__orderings['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''] = 82

        self.__okExcepts['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__propCode['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''] = r"  (countLength(self.p_LINKED[0])==__pre['''countLength(self.p_LINKED[0])''']+1)"

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''] = []

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[0].insert(self.p_CHAR[2]) '''].append(r"__pre['''countLength(self.p_LINKED[0])'''] = countLength(self.p_LINKED[0])")

        self.__actions.append(('''self.p_LINKED[1].insert(self.p_CHAR[0]) ''',self.guard82,self.act82))

        self.__names['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKED[1].insert(self.p_CHAR[0]) ''',self.guard82,self.act82)

        self.__orderings['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''] = 83

        self.__okExcepts['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__propCode['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''] = r"  (countLength(self.p_LINKED[1])==__pre['''countLength(self.p_LINKED[1])''']+1)"

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''] = []

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[0]) '''].append(r"__pre['''countLength(self.p_LINKED[1])'''] = countLength(self.p_LINKED[1])")

        self.__actions.append(('''self.p_LINKED[1].insert(self.p_CHAR[1]) ''',self.guard83,self.act83))

        self.__names['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKED[1].insert(self.p_CHAR[1]) ''',self.guard83,self.act83)

        self.__orderings['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''] = 84

        self.__okExcepts['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__propCode['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''] = r"  (countLength(self.p_LINKED[1])==__pre['''countLength(self.p_LINKED[1])''']+1)"

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''] = []

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[1]) '''].append(r"__pre['''countLength(self.p_LINKED[1])'''] = countLength(self.p_LINKED[1])")

        self.__actions.append(('''self.p_LINKED[1].insert(self.p_CHAR[2]) ''',self.guard84,self.act84))

        self.__names['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKED[1].insert(self.p_CHAR[2]) ''',self.guard84,self.act84)

        self.__orderings['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''] = 85

        self.__okExcepts['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__propCode['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''] = r"  (countLength(self.p_LINKED[1])==__pre['''countLength(self.p_LINKED[1])''']+1)"

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''] = []

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[1].insert(self.p_CHAR[2]) '''].append(r"__pre['''countLength(self.p_LINKED[1])'''] = countLength(self.p_LINKED[1])")

        self.__actions.append(('''self.p_LINKED[2].insert(self.p_CHAR[0]) ''',self.guard85,self.act85))

        self.__names['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKED[2].insert(self.p_CHAR[0]) ''',self.guard85,self.act85)

        self.__orderings['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''] = 86

        self.__okExcepts['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__propCode['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''] = r"  (countLength(self.p_LINKED[2])==__pre['''countLength(self.p_LINKED[2])''']+1)"

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''] = []

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[0]) '''].append(r"__pre['''countLength(self.p_LINKED[2])'''] = countLength(self.p_LINKED[2])")

        self.__actions.append(('''self.p_LINKED[2].insert(self.p_CHAR[1]) ''',self.guard86,self.act86))

        self.__names['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKED[2].insert(self.p_CHAR[1]) ''',self.guard86,self.act86)

        self.__orderings['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''] = 87

        self.__okExcepts['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__propCode['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''] = r"  (countLength(self.p_LINKED[2])==__pre['''countLength(self.p_LINKED[2])''']+1)"

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''] = []

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[1]) '''].append(r"__pre['''countLength(self.p_LINKED[2])'''] = countLength(self.p_LINKED[2])")

        self.__actions.append(('''self.p_LINKED[2].insert(self.p_CHAR[2]) ''',self.guard87,self.act87))

        self.__names['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKED[2].insert(self.p_CHAR[2]) ''',self.guard87,self.act87)

        self.__orderings['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''] = 88

        self.__okExcepts['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__propCode['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''] = r"  (countLength(self.p_LINKED[2])==__pre['''countLength(self.p_LINKED[2])''']+1)"

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''] = []

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[2].insert(self.p_CHAR[2]) '''].append(r"__pre['''countLength(self.p_LINKED[2])'''] = countLength(self.p_LINKED[2])")

        self.__actions.append(('''self.p_LINKED[3].insert(self.p_CHAR[0]) ''',self.guard88,self.act88))

        self.__names['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKED[3].insert(self.p_CHAR[0]) ''',self.guard88,self.act88)

        self.__orderings['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''] = 89

        self.__okExcepts['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''] = ''''''

        self.__propCode['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''] = r"  (countLength(self.p_LINKED[3])==__pre['''countLength(self.p_LINKED[3])''']+1)"

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''] = []

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[0]) '''].append(r"__pre['''countLength(self.p_LINKED[3])'''] = countLength(self.p_LINKED[3])")

        self.__actions.append(('''self.p_LINKED[3].insert(self.p_CHAR[1]) ''',self.guard89,self.act89))

        self.__names['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKED[3].insert(self.p_CHAR[1]) ''',self.guard89,self.act89)

        self.__orderings['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''] = 90

        self.__okExcepts['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''] = ''''''

        self.__propCode['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''] = r"  (countLength(self.p_LINKED[3])==__pre['''countLength(self.p_LINKED[3])''']+1)"

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''] = []

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[1]) '''].append(r"__pre['''countLength(self.p_LINKED[3])'''] = countLength(self.p_LINKED[3])")

        self.__actions.append(('''self.p_LINKED[3].insert(self.p_CHAR[2]) ''',self.guard90,self.act90))

        self.__names['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKED[3].insert(self.p_CHAR[2]) ''',self.guard90,self.act90)

        self.__orderings['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''] = 91

        self.__okExcepts['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''] = ''''''

        self.__propCode['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''] = r"  (countLength(self.p_LINKED[3])==__pre['''countLength(self.p_LINKED[3])''']+1)"

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''] = []

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''].append(r"__pre = {}")

        self.__preCode['''self.p_LINKED[3].insert(self.p_CHAR[2]) '''].append(r"__pre['''countLength(self.p_LINKED[3])'''] = countLength(self.p_LINKED[3])")

        self.__actions.append(('''print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  " ''',self.guard91,self.act91))

        self.__names['''print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  " '''] = ('''print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  " ''',self.guard91,self.act91)

        self.__orderings['''print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  " '''] = 92

        self.__okExcepts['''print " % % % % % % % % % %  "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].ReversePrint(self.p_LINKED[0].getHead()); print "%        %        %  " '''] = ''''''

        self.__actions.append(('''print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  " ''',self.guard92,self.act92))

        self.__names['''print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  " '''] = ('''print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  " ''',self.guard92,self.act92)

        self.__orderings['''print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  " '''] = 93

        self.__okExcepts['''print " % % % % % % % % % %  "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].ReversePrint(self.p_LINKED[1].getHead()); print "%        %        %  " '''] = ''''''

        self.__actions.append(('''print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  " ''',self.guard93,self.act93))

        self.__names['''print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  " '''] = ('''print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  " ''',self.guard93,self.act93)

        self.__orderings['''print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  " '''] = 94

        self.__okExcepts['''print " % % % % % % % % % %  "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].ReversePrint(self.p_LINKED[2].getHead()); print "%        %        %  " '''] = ''''''

        self.__actions.append(('''print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  " ''',self.guard94,self.act94))

        self.__names['''print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  " '''] = ('''print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  " ''',self.guard94,self.act94)

        self.__orderings['''print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  " '''] = 95

        self.__okExcepts['''print " % % % % % % % % % %  "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].ReversePrint(self.p_LINKED[3].getHead()); print "%        %        %  " '''] = ''''''

        self.__actions.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? " ''',self.guard95,self.act95))

        self.__names['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? " '''] = ('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? " ''',self.guard95,self.act95)

        self.__orderings['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? " '''] = 96

        self.__okExcepts['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[0].printList(self.p_LINKED[0].getHead());self.p_LINKED[0].printList(self.p_LINKED[0].reverseList(self.p_LINKED[0].getHead())); print "?         ?        ? " '''] = ''''''

        self.__actions.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? " ''',self.guard96,self.act96))

        self.__names['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? " '''] = ('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? " ''',self.guard96,self.act96)

        self.__orderings['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? " '''] = 97

        self.__okExcepts['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[1].printList(self.p_LINKED[1].getHead());self.p_LINKED[1].printList(self.p_LINKED[1].reverseList(self.p_LINKED[1].getHead())); print "?         ?        ? " '''] = ''''''

        self.__actions.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? " ''',self.guard97,self.act97))

        self.__names['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? " '''] = ('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? " ''',self.guard97,self.act97)

        self.__orderings['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? " '''] = 98

        self.__okExcepts['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[2].printList(self.p_LINKED[2].getHead());self.p_LINKED[2].printList(self.p_LINKED[2].reverseList(self.p_LINKED[2].getHead())); print "?         ?        ? " '''] = ''''''

        self.__actions.append(('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? " ''',self.guard98,self.act98))

        self.__names['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? " '''] = ('''print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? " ''',self.guard98,self.act98)

        self.__orderings['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? " '''] = 99

        self.__okExcepts['''print "? ? ? ? ? ? ? ? "; self.p_LINKED[3].printList(self.p_LINKED[3].getHead());self.p_LINKED[3].printList(self.p_LINKED[3].reverseList(self.p_LINKED[3].getHead())); print "?         ?        ? " '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard99,self.act99))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard99,self.act99)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 100

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard100,self.act100))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard100,self.act100)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 101

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard101,self.act101))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard101,self.act101)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 102

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard102,self.act102))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard102,self.act102)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 103

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard103,self.act103))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard103,self.act103)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 104

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard104,self.act104))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard104,self.act104)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 105

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard105,self.act105))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard105,self.act105)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 106

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard106,self.act106))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard106,self.act106)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 107

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard107,self.act107))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard107,self.act107)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 108

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4) ''',self.guard108,self.act108))

        self.__names['''print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4) '''] = ('''print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4) ''',self.guard108,self.act108)

        self.__orderings['''print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4) '''] = 109

        self.__okExcepts['''print "-------------------"; self.p_LINKK[0].printList(self.p_LINKK[0].getHead());self.p_LINKK[0].removeElements(self.p_LINKK[0].getHead(),findLstValue(self.p_LINKK[0])); self.p_LINKK[0].printList(self.p_LINKK[0].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[0]) < 4) '''] = ''''''

        self.__actions.append(('''print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4) ''',self.guard109,self.act109))

        self.__names['''print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4) '''] = ('''print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4) ''',self.guard109,self.act109)

        self.__orderings['''print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4) '''] = 110

        self.__okExcepts['''print "-------------------"; self.p_LINKK[1].printList(self.p_LINKK[1].getHead());self.p_LINKK[1].removeElements(self.p_LINKK[1].getHead(),findLstValue(self.p_LINKK[1])); self.p_LINKK[1].printList(self.p_LINKK[1].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[1]) < 4) '''] = ''''''

        self.__actions.append(('''print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4) ''',self.guard110,self.act110))

        self.__names['''print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4) '''] = ('''print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4) ''',self.guard110,self.act110)

        self.__orderings['''print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4) '''] = 111

        self.__okExcepts['''print "-------------------"; self.p_LINKK[2].printList(self.p_LINKK[2].getHead());self.p_LINKK[2].removeElements(self.p_LINKK[2].getHead(),findLstValue(self.p_LINKK[2])); self.p_LINKK[2].printList(self.p_LINKK[2].getHead()); print "-       -     -     - "; #=>  # (countLength(self.p_LINKK[2]) < 4) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard111,self.act111))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard111,self.act111)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 112

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard112,self.act112))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard112,self.act112)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 113

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard113,self.act113))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard113,self.act113)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 114

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard114,self.act114))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard114,self.act114)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 115

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard115,self.act115))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard115,self.act115)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 116

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard116,self.act116))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard116,self.act116)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 117

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard117,self.act117))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard117,self.act117)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 118

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard118,self.act118))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard118,self.act118)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 119

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard119,self.act119))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard119,self.act119)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 120

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard120,self.act120))

        self.__names['''self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead()); '''] = ('''self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard120,self.act120)

        self.__orderings['''self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead()); '''] = 121

        self.__okExcepts['''self.p_LINKK[0].deleteNode((self.p_LINKK[0]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard121,self.act121))

        self.__names['''self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead()); '''] = ('''self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard121,self.act121)

        self.__orderings['''self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead()); '''] = 122

        self.__okExcepts['''self.p_LINKK[1].deleteNode((self.p_LINKK[0]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard122,self.act122))

        self.__names['''self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead()); '''] = ('''self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead()); ''',self.guard122,self.act122)

        self.__orderings['''self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead()); '''] = 123

        self.__okExcepts['''self.p_LINKK[2].deleteNode((self.p_LINKK[0]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard123,self.act123))

        self.__names['''self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead()); '''] = ('''self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard123,self.act123)

        self.__orderings['''self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead()); '''] = 124

        self.__okExcepts['''self.p_LINKK[0].deleteNode((self.p_LINKK[1]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard124,self.act124))

        self.__names['''self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead()); '''] = ('''self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard124,self.act124)

        self.__orderings['''self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead()); '''] = 125

        self.__okExcepts['''self.p_LINKK[1].deleteNode((self.p_LINKK[1]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard125,self.act125))

        self.__names['''self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead()); '''] = ('''self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead()); ''',self.guard125,self.act125)

        self.__orderings['''self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead()); '''] = 126

        self.__okExcepts['''self.p_LINKK[2].deleteNode((self.p_LINKK[1]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard126,self.act126))

        self.__names['''self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead()); '''] = ('''self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard126,self.act126)

        self.__orderings['''self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead()); '''] = 127

        self.__okExcepts['''self.p_LINKK[0].deleteNode((self.p_LINKK[2]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard127,self.act127))

        self.__names['''self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead()); '''] = ('''self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard127,self.act127)

        self.__orderings['''self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead()); '''] = 128

        self.__okExcepts['''self.p_LINKK[1].deleteNode((self.p_LINKK[2]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard128,self.act128))

        self.__names['''self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead()); '''] = ('''self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead()); ''',self.guard128,self.act128)

        self.__orderings['''self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead()); '''] = 129

        self.__okExcepts['''self.p_LINKK[2].deleteNode((self.p_LINKK[2]).getHead()); '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard129,self.act129))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard129,self.act129)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 130

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard130,self.act130))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard130,self.act130)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 131

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard131,self.act131))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard131,self.act131)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 132

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard132,self.act132))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard132,self.act132)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 133

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard133,self.act133))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard133,self.act133)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 134

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard134,self.act134))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard134,self.act134)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 135

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard135,self.act135))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard135,self.act135)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 136

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard136,self.act136))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard136,self.act136)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 137

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard137,self.act137))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard137,self.act137)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 138

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard138,self.act138))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard138,self.act138)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = 139

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard139,self.act139))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard139,self.act139)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = 140

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard140,self.act140))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False ''',self.guard140,self.act140)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = 141

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[0]); self.p_LINKK[0].deleteDuplicates(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[0]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard141,self.act141))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard141,self.act141)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = 142

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard142,self.act142))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard142,self.act142)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = 143

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard143,self.act143))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False ''',self.guard143,self.act143)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = 144

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[1]); self.p_LINKK[1].deleteDuplicates(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[1]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard144,self.act144))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard144,self.act144)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = 145

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard145,self.act145))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard145,self.act145)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = 146

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = ''''''

        self.__actions.append(('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard146,self.act146))

        self.__names['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = ('''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False ''',self.guard146,self.act146)

        self.__orderings['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = 147

        self.__okExcepts['''print "--$--$---$---$----$----"; nprintList(self.p_LINKK[2]); self.p_LINKK[2].deleteDuplicates(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); print "--$    ---$     ---$    ---$" #=> # findFstDuplicates(self.p_LINKK[2]) ==False '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard147,self.act147))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard147,self.act147)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 148

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard148,self.act148))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard148,self.act148)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 149

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard149,self.act149))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard149,self.act149)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 150

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard150,self.act150))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard150,self.act150)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 151

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard151,self.act151))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard151,self.act151)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 152

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard152,self.act152))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard152,self.act152)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 153

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard153,self.act153))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard153,self.act153)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 154

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard154,self.act154))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard154,self.act154)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 155

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard155,self.act155))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard155,self.act155)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 156

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); ''',self.guard156,self.act156))

        self.__names['''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); '''] = ('''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); ''',self.guard156,self.act156)

        self.__orderings['''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); '''] = 157

        self.__okExcepts['''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[0]);self.p_LINKK[0].printList(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)); '''] = r"findLstValue(self.p_LINKK[0])==(self.p_LINKK[0].rotateRight(self.p_LINKK[0].getHead(),1)).val"

        self.__actions.append(('''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); ''',self.guard157,self.act157))

        self.__names['''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); '''] = ('''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); ''',self.guard157,self.act157)

        self.__orderings['''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); '''] = 158

        self.__okExcepts['''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[1]);self.p_LINKK[1].printList(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)); '''] = r"findLstValue(self.p_LINKK[1])==(self.p_LINKK[1].rotateRight(self.p_LINKK[1].getHead(),1)).val"

        self.__actions.append(('''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); ''',self.guard158,self.act158))

        self.__names['''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); '''] = ('''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); ''',self.guard158,self.act158)

        self.__orderings['''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); '''] = 159

        self.__okExcepts['''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[2]);self.p_LINKK[2].printList(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)); '''] = r"findLstValue(self.p_LINKK[2])==(self.p_LINKK[2].rotateRight(self.p_LINKK[2].getHead(),1)).val"

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard159,self.act159))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard159,self.act159)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 160

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard160,self.act160))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard160,self.act160)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 161

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard161,self.act161))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard161,self.act161)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 162

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard162,self.act162))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard162,self.act162)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 163

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard163,self.act163))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard163,self.act163)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 164

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard164,self.act164))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard164,self.act164)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 165

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard165,self.act165))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard165,self.act165)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 166

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard166,self.act166))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard166,self.act166)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 167

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard167,self.act167))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard167,self.act167)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 168

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append((''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); ''',self.guard168,self.act168))

        self.__names[''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); '''] = (''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); ''',self.guard168,self.act168)

        self.__orderings[''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); '''] = 169

        self.__okExcepts[''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); '''] = ''''''

        self.__propCode[''' a= findLstValue(self.p_LINKK[0]); nprintList(self.p_LINKK[0]);self.p_LINKK[0].reorderList(self.p_LINKK[0].getHead());nprintList(self.p_LINKK[0]); '''] = r"  findSecValue(self.p_LINKK[0]) == a"

        self.__actions.append((''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); ''',self.guard169,self.act169))

        self.__names[''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); '''] = (''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); ''',self.guard169,self.act169)

        self.__orderings[''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); '''] = 170

        self.__okExcepts[''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); '''] = ''''''

        self.__propCode[''' a= findLstValue(self.p_LINKK[1]); nprintList(self.p_LINKK[1]);self.p_LINKK[1].reorderList(self.p_LINKK[1].getHead());nprintList(self.p_LINKK[1]); '''] = r"  findSecValue(self.p_LINKK[1]) == a"

        self.__actions.append((''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); ''',self.guard170,self.act170))

        self.__names[''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); '''] = (''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); ''',self.guard170,self.act170)

        self.__orderings[''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); '''] = 171

        self.__okExcepts[''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); '''] = ''''''

        self.__propCode[''' a= findLstValue(self.p_LINKK[2]); nprintList(self.p_LINKK[2]);self.p_LINKK[2].reorderList(self.p_LINKK[2].getHead());nprintList(self.p_LINKK[2]); '''] = r"  findSecValue(self.p_LINKK[2]) == a"

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard171,self.act171))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard171,self.act171)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 172

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard172,self.act172))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard172,self.act172)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 173

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard173,self.act173))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard173,self.act173)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 174

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard174,self.act174))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard174,self.act174)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 175

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard175,self.act175))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard175,self.act175)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 176

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard176,self.act176))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard176,self.act176)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 177

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard177,self.act177))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard177,self.act177)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 178

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard178,self.act178))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard178,self.act178)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 179

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard179,self.act179))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard179,self.act179)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 180

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append((''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard180,self.act180))

        self.__names[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = (''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard180,self.act180)

        self.__orderings[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = 181

        self.__okExcepts[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs1(self.p_LINKK[0].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = ''''''

        self.__actions.append((''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard181,self.act181))

        self.__names[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = (''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard181,self.act181)

        self.__orderings[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = 182

        self.__okExcepts[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs1(self.p_LINKK[1].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = ''''''

        self.__actions.append((''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard182,self.act182))

        self.__names[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = (''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) ''',self.guard182,self.act182)

        self.__orderings[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = 183

        self.__okExcepts[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs1(self.p_LINKK[2].getHead()); #=>  # (a == c.next.val) and (b==c.next.next.next.val) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard183,self.act183))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[0])  ''',self.guard183,self.act183)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = 184

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard184,self.act184))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[1])  ''',self.guard184,self.act184)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = 185

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard185,self.act185))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[0].insert(self.p_INT[2])  ''',self.guard185,self.act185)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = 186

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard186,self.act186))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[0])  ''',self.guard186,self.act186)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = 187

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard187,self.act187))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[1])  ''',self.guard187,self.act187)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = 188

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard188,self.act188))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[1].insert(self.p_INT[2])  ''',self.guard188,self.act188)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = 189

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard189,self.act189))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[0])  ''',self.guard189,self.act189)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = 190

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard190,self.act190))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[1])  ''',self.guard190,self.act190)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = 191

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1])  '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard191,self.act191))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ('''self.p_LINKK[2].insert(self.p_INT[2])  ''',self.guard191,self.act191)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = 192

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2])  '''] = ''''''

        self.__actions.append((''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); ''',self.guard192,self.act192))

        self.__names[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); '''] = (''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); ''',self.guard192,self.act192)

        self.__orderings[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); '''] = 193

        self.__okExcepts[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); '''] = ''''''

        self.__propCode[''' a= findFstValue(self.p_LINKK[0]);b=findTrdValue(self.p_LINKK[0]);c=self.p_LINKK[0].swapPairs(self.p_LINKK[0].getHead()); '''] = r"  (a == c.next.val) and (b==c.next.next.next.val)"

        self.__actions.append((''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); ''',self.guard193,self.act193))

        self.__names[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); '''] = (''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); ''',self.guard193,self.act193)

        self.__orderings[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); '''] = 194

        self.__okExcepts[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); '''] = ''''''

        self.__propCode[''' a= findFstValue(self.p_LINKK[1]);b=findTrdValue(self.p_LINKK[1]);c=self.p_LINKK[1].swapPairs(self.p_LINKK[1].getHead()); '''] = r"  (a == c.next.val) and (b==c.next.next.next.val)"

        self.__actions.append((''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); ''',self.guard194,self.act194))

        self.__names[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); '''] = (''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); ''',self.guard194,self.act194)

        self.__orderings[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); '''] = 195

        self.__okExcepts[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); '''] = ''''''

        self.__propCode[''' a= findFstValue(self.p_LINKK[2]);b=findTrdValue(self.p_LINKK[2]);c=self.p_LINKK[2].swapPairs(self.p_LINKK[2].getHead()); '''] = r"  (a == c.next.val) and (b==c.next.next.next.val)"

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard195,self.act195))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard195,self.act195)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 196

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard196,self.act196))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard196,self.act196)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 197

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard197,self.act197))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard197,self.act197)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 198

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard198,self.act198))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard198,self.act198)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 199

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard199,self.act199))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard199,self.act199)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 200

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard200,self.act200))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard200,self.act200)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 201

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard201,self.act201))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard201,self.act201)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 202

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard202,self.act202))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard202,self.act202)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 203

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard203,self.act203))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard203,self.act203)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 204

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard204,self.act204))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard204,self.act204)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 205

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard205,self.act205))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard205,self.act205)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 206

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard206,self.act206))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard206,self.act206)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 207

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard207,self.act207))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard207,self.act207)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 208

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard208,self.act208))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard208,self.act208)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 209

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard209,self.act209))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard209,self.act209)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 210

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard210,self.act210))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard210,self.act210)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 211

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard211,self.act211))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard211,self.act211)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 212

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard212,self.act212))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard212,self.act212)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 213

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard213,self.act213))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard213,self.act213)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 214

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard214,self.act214))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard214,self.act214)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 215

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard215,self.act215))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard215,self.act215)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 216

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard216,self.act216))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard216,self.act216)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 217

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard217,self.act217))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard217,self.act217)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 218

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard218,self.act218))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard218,self.act218)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 219

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard219,self.act219))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard219,self.act219)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 220

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard220,self.act220))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard220,self.act220)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 221

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard221,self.act221))

        self.__names['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard221,self.act221)

        self.__orderings['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 222

        self.__okExcepts['''self.p_LINKK[0].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard222,self.act222))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard222,self.act222)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 223

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard223,self.act223))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard223,self.act223)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 224

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard224,self.act224))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard224,self.act224)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 225

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard225,self.act225))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard225,self.act225)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 226

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard226,self.act226))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard226,self.act226)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 227

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard227,self.act227))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard227,self.act227)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 228

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard228,self.act228))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard228,self.act228)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 229

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard229,self.act229))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard229,self.act229)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 230

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard230,self.act230))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard230,self.act230)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 231

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard231,self.act231))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard231,self.act231)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 232

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard232,self.act232))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard232,self.act232)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 233

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard233,self.act233))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard233,self.act233)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 234

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard234,self.act234))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard234,self.act234)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 235

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard235,self.act235))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard235,self.act235)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 236

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard236,self.act236))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard236,self.act236)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 237

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard237,self.act237))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard237,self.act237)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 238

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard238,self.act238))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard238,self.act238)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 239

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard239,self.act239))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard239,self.act239)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 240

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard240,self.act240))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard240,self.act240)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 241

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard241,self.act241))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard241,self.act241)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 242

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard242,self.act242))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard242,self.act242)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 243

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard243,self.act243))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard243,self.act243)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 244

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard244,self.act244))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard244,self.act244)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 245

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard245,self.act245))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard245,self.act245)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 246

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard246,self.act246))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard246,self.act246)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 247

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard247,self.act247))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard247,self.act247)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 248

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard248,self.act248))

        self.__names['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard248,self.act248)

        self.__orderings['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 249

        self.__okExcepts['''self.p_LINKK[1].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard249,self.act249))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard249,self.act249)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 250

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard250,self.act250))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard250,self.act250)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 251

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard251,self.act251))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard251,self.act251)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 252

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard252,self.act252))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard252,self.act252)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 253

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard253,self.act253))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard253,self.act253)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 254

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard254,self.act254))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard254,self.act254)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 255

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard255,self.act255))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard255,self.act255)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 256

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard256,self.act256))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard256,self.act256)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 257

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard257,self.act257))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard257,self.act257)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 258

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[0]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard258,self.act258))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard258,self.act258)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 259

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard259,self.act259))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard259,self.act259)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 260

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard260,self.act260))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard260,self.act260)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 261

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard261,self.act261))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard261,self.act261)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 262

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard262,self.act262))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard262,self.act262)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 263

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard263,self.act263))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard263,self.act263)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 264

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard264,self.act264))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard264,self.act264)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 265

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard265,self.act265))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard265,self.act265)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 266

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard266,self.act266))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard266,self.act266)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 267

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[1]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard267,self.act267))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) ''',self.guard267,self.act267)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = 268

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard268,self.act268))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) ''',self.guard268,self.act268)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = 269

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard269,self.act269))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) ''',self.guard269,self.act269)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = 270

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[0].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard270,self.act270))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) ''',self.guard270,self.act270)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = 271

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard271,self.act271))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) ''',self.guard271,self.act271)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = 272

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard272,self.act272))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) ''',self.guard272,self.act272)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = 273

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[1].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard273,self.act273))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) ''',self.guard273,self.act273)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = 274

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[0]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard274,self.act274))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) ''',self.guard274,self.act274)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = 275

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[1]) '''] = ''''''

        self.__actions.append(('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard275,self.act275))

        self.__names['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ('''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) ''',self.guard275,self.act275)

        self.__orderings['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = 276

        self.__okExcepts['''self.p_LINKK[2].insert(self.p_INT[2]);self.p_LIN[2].insert(self.p_CHAR[2]) '''] = ''''''

        self.__actions.append(('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard276,self.act276))

        self.__names['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = ('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard276,self.act276)

        self.__orderings['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = 277

        self.__okExcepts['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard277,self.act277))

        self.__names['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = ('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard277,self.act277)

        self.__orderings['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = 278

        self.__okExcepts['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard278,self.act278))

        self.__names['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = ('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard278,self.act278)

        self.__orderings['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = 279

        self.__okExcepts['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[0]);headA=self.p_LIN[0].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard279,self.act279))

        self.__names['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = ('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard279,self.act279)

        self.__orderings['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = 280

        self.__okExcepts['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard280,self.act280))

        self.__names['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = ('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard280,self.act280)

        self.__orderings['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = 281

        self.__okExcepts['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard281,self.act281))

        self.__names['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = ('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard281,self.act281)

        self.__orderings['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = 282

        self.__okExcepts['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[1]);headA=self.p_LIN[1].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard282,self.act282))

        self.__names['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = ('''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); ''',self.guard282,self.act282)

        self.__orderings['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = 283

        self.__okExcepts['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[0]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[0].getHead(); print "LOGGGG";x=self.p_LINKK[0].mergeTwoLists(headB,headA); self.p_LINKK[0].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard283,self.act283))

        self.__names['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = ('''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); ''',self.guard283,self.act283)

        self.__orderings['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = 284

        self.__okExcepts['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[1]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[1].getHead(); print "LOGGGG";x=self.p_LINKK[1].mergeTwoLists(headB,headA); self.p_LINKK[1].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions.append(('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard284,self.act284))

        self.__names['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = ('''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); ''',self.guard284,self.act284)

        self.__orderings['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = 285

        self.__okExcepts['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = ''''''

        self.__propCode['''nprintList(self.p_LINKK[2]);nprintList(self.p_LIN[2]);headA=self.p_LIN[2].getHead(); headB= self.p_LINKK[2].getHead(); print "LOGGGG";x=self.p_LINKK[2].mergeTwoLists(headB,headA); self.p_LINKK[2].printList(x); '''] = r" lengthHead(x)==9"

        self.__actions_backup = list(self.__actions)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
        self.cleanCov()
    # BEGIN RELOAD CODE
        reload(linkedlist)
        reload(math)
        reload(time)
    # END RELOAD CODE
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_INT = {}
        self.p_INT_used = {}
        self.__pools.append("self.p_INT")
        self.p_INT[0] = None
        self.p_INT_used[0] = True
        self.p_INT[1] = None
        self.p_INT_used[1] = True
        self.p_INT[2] = None
        self.p_INT_used[2] = True
        self.p_INT[3] = None
        self.p_INT_used[3] = True
        self.p_LIST = {}
        self.p_LIST_used = {}
        self.__pools.append("self.p_LIST")
        self.p_LIST[0] = None
        self.p_LIST_used[0] = True
        self.p_LIST[1] = None
        self.p_LIST_used[1] = True
        self.p_LIST[2] = None
        self.p_LIST_used[2] = True
        self.p_LIST[3] = None
        self.p_LIST_used[3] = True
        self.p_LIN = {}
        self.p_LIN_used = {}
        self.__pools.append("self.p_LIN")
        self.p_LIN[0] = None
        self.p_LIN_used[0] = True
        self.p_LIN[1] = None
        self.p_LIN_used[1] = True
        self.p_LIN[2] = None
        self.p_LIN_used[2] = True
        self.p_LIN[3] = None
        self.p_LIN_used[3] = True
        self.p_LINKED = {}
        self.p_LINKED_used = {}
        self.__pools.append("self.p_LINKED")
        self.p_LINKED[0] = None
        self.p_LINKED_used[0] = True
        self.p_LINKED[1] = None
        self.p_LINKED_used[1] = True
        self.p_LINKED[2] = None
        self.p_LINKED_used[2] = True
        self.p_LINKED[3] = None
        self.p_LINKED_used[3] = True
        self.p_LINKED[4] = None
        self.p_LINKED_used[4] = True
        self.p_CHAR = {}
        self.p_CHAR_used = {}
        self.__pools.append("self.p_CHAR")
        self.p_CHAR[0] = None
        self.p_CHAR_used[0] = True
        self.p_CHAR[1] = None
        self.p_CHAR_used[1] = True
        self.p_CHAR[2] = None
        self.p_CHAR_used[2] = True
        self.p_CHAR[3] = None
        self.p_CHAR_used[3] = True
        self.p_LINKK = {}
        self.p_LINKK_used = {}
        self.__pools.append("self.p_LINKK")
        self.p_LINKK[0] = None
        self.p_LINKK_used[0] = True
        self.p_LINKK[1] = None
        self.p_LINKK_used[1] = True
        self.p_LINKK[2] = None
        self.p_LINKK_used[2] = True
        self.p_LINKK[3] = None
        self.p_LINKK_used[3] = True
        try:
            test_after_restart(self)
        except:
            pass
    def log(self, name):
        pass
    def logPost(self, name):
        pass
    def state(self):
        if self.__replayBacktrack:
            return self.captureReplay(self.__test)
        return [ copy.deepcopy(self.p_INT),copy.deepcopy(self.p_INT_used),copy.deepcopy(self.p_LIST),copy.deepcopy(self.p_LIST_used),copy.deepcopy(self.p_LIN),copy.deepcopy(self.p_LIN_used),copy.deepcopy(self.p_LINKED),copy.deepcopy(self.p_LINKED_used),copy.deepcopy(self.p_CHAR),copy.deepcopy(self.p_CHAR_used),copy.deepcopy(self.p_LINKK),copy.deepcopy(self.p_LINKK_used)]
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_INT = copy.deepcopy(old[0])
        self.p_INT_used = copy.deepcopy(old[1])
        self.p_LIST = copy.deepcopy(old[2])
        self.p_LIST_used = copy.deepcopy(old[3])
        self.p_LIN = copy.deepcopy(old[4])
        self.p_LIN_used = copy.deepcopy(old[5])
        self.p_LINKED = copy.deepcopy(old[6])
        self.p_LINKED_used = copy.deepcopy(old[7])
        self.p_CHAR = copy.deepcopy(old[8])
        self.p_CHAR_used = copy.deepcopy(old[9])
        self.p_LINKK = copy.deepcopy(old[10])
        self.p_LINKK_used = copy.deepcopy(old[11])
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
