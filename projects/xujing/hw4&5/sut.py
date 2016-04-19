import copy
import traceback
import re
import sys
from itertools import chain, combinations
# BEGIN STANDALONE CODE
import examine as examine
def check(object):
	if object==None:
		print("None")
	else: 
		print(object)
# END STANDALONE CODE
class sut(object):
    def act0(self):
        self.__test.append(('''self.p_strtest[0] =[] ''',self.guard0,self.act0))
        try:
            self.p_strtest[0] =[]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[0]=False
    def guard0(self):
        return (((self.p_strtest_used[0]) or (self.p_strtest[0] == None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        self.__test.append(('''self.p_strtest[1] =[] ''',self.guard1,self.act1))
        try:
            self.p_strtest[1] =[]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[1]=False
    def guard1(self):
        return (((self.p_strtest_used[1]) or (self.p_strtest[1] == None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        self.__test.append(('''self.p_strtest[2] =[] ''',self.guard2,self.act2))
        try:
            self.p_strtest[2] =[]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[2]=False
    def guard2(self):
        return (((self.p_strtest_used[2]) or (self.p_strtest[2] == None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        self.__test.append(('''self.p_strtest[0] +=[{'key1': 'val1'}] ''',self.guard3,self.act3))
        try:
            self.p_strtest[0] +=[{'key1': 'val1'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[0]=True
    def guard3(self):
        return (self.p_strtest[0] != None)
    
    def act4(self):
        self.__test.append(('''self.p_strtest[1] +=[{'key1': 'val1'}] ''',self.guard4,self.act4))
        try:
            self.p_strtest[1] +=[{'key1': 'val1'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[1]=True
    def guard4(self):
        return (self.p_strtest[1] != None)
    
    def act5(self):
        self.__test.append(('''self.p_strtest[2] +=[{'key1': 'val1'}] ''',self.guard5,self.act5))
        try:
            self.p_strtest[2] +=[{'key1': 'val1'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[2]=True
    def guard5(self):
        return (self.p_strtest[2] != None)
    
    def act6(self):
        self.__test.append(('''self.p_strtest[0] +=['coding', 'snowboarding'] ''',self.guard6,self.act6))
        try:
            self.p_strtest[0] +=['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[0]=True
    def guard6(self):
        return (self.p_strtest[0] != None)
    
    def act7(self):
        self.__test.append(('''self.p_strtest[1] +=['coding', 'snowboarding'] ''',self.guard7,self.act7))
        try:
            self.p_strtest[1] +=['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[1]=True
    def guard7(self):
        return (self.p_strtest[1] != None)
    
    def act8(self):
        self.__test.append(('''self.p_strtest[2] +=['coding', 'snowboarding'] ''',self.guard8,self.act8))
        try:
            self.p_strtest[2] +=['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[2]=True
    def guard8(self):
        return (self.p_strtest[2] != None)
    
    def act9(self):
        self.__test.append(('''print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0]) ''',self.guard9,self.act9))
        try:
            print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[0]=True
        self.p_strtest_used[0]=True
    def guard9(self):
        return (self.p_strtest[0] != None) and (self.p_strtest[0] != None)
    
    def act10(self):
        self.__test.append(('''print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1]) ''',self.guard10,self.act10))
        try:
            print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[0]=True
        self.p_strtest_used[1]=True
    def guard10(self):
        return (self.p_strtest[0] != None) and (self.p_strtest[1] != None)
    
    def act11(self):
        self.__test.append(('''print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2]) ''',self.guard11,self.act11))
        try:
            print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[0]=True
        self.p_strtest_used[2]=True
    def guard11(self):
        return (self.p_strtest[0] != None) and (self.p_strtest[2] != None)
    
    def act12(self):
        self.__test.append(('''print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0]) ''',self.guard12,self.act12))
        try:
            print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[1]=True
        self.p_strtest_used[0]=True
    def guard12(self):
        return (self.p_strtest[1] != None) and (self.p_strtest[0] != None)
    
    def act13(self):
        self.__test.append(('''print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1]) ''',self.guard13,self.act13))
        try:
            print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[1]=True
        self.p_strtest_used[1]=True
    def guard13(self):
        return (self.p_strtest[1] != None) and (self.p_strtest[1] != None)
    
    def act14(self):
        self.__test.append(('''print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2]) ''',self.guard14,self.act14))
        try:
            print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[1]=True
        self.p_strtest_used[2]=True
    def guard14(self):
        return (self.p_strtest[1] != None) and (self.p_strtest[2] != None)
    
    def act15(self):
        self.__test.append(('''print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0]) ''',self.guard15,self.act15))
        try:
            print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[2]=True
        self.p_strtest_used[0]=True
    def guard15(self):
        return (self.p_strtest[2] != None) and (self.p_strtest[0] != None)
    
    def act16(self):
        self.__test.append(('''print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1]) ''',self.guard16,self.act16))
        try:
            print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[2]=True
        self.p_strtest_used[1]=True
    def guard16(self):
        return (self.p_strtest[2] != None) and (self.p_strtest[1] != None)
    
    def act17(self):
        self.__test.append(('''print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2]) ''',self.guard17,self.act17))
        try:
            print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strtest_used[2]=True
        self.p_strtest_used[2]=True
    def guard17(self):
        return (self.p_strtest[2] != None) and (self.p_strtest[2] != None)
    
    def act18(self):
        self.__test.append(('''self.p_strname[0] = ['coding', 'snowboarding'] ''',self.guard18,self.act18))
        try:
            self.p_strname[0] = ['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strname_used[0]=False
    def guard18(self):
        return (((self.p_strname_used[0]) or (self.p_strname[0] == None) or (self.__relaxUsedRestriction)))
    
    def act19(self):
        self.__test.append(('''self.p_strname[1] = ['coding', 'snowboarding'] ''',self.guard19,self.act19))
        try:
            self.p_strname[1] = ['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strname_used[1]=False
    def guard19(self):
        return (((self.p_strname_used[1]) or (self.p_strname[1] == None) or (self.__relaxUsedRestriction)))
    
    def act20(self):
        self.__test.append(('''self.p_strname[2] = ['coding', 'snowboarding'] ''',self.guard20,self.act20))
        try:
            self.p_strname[2] = ['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strname_used[2]=False
    def guard20(self):
        return (((self.p_strname_used[2]) or (self.p_strname[2] == None) or (self.__relaxUsedRestriction)))
    
    def act21(self):
        self.__test.append(('''self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard21,self.act21))
        try:
            self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=False
    def guard21(self):
        return (((self.p_list1_used[0]) or (self.p_list1[0] == None) or (self.__relaxUsedRestriction)))
    
    def act22(self):
        self.__test.append(('''self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard22,self.act22))
        try:
            self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=False
    def guard22(self):
        return (((self.p_list1_used[1]) or (self.p_list1[1] == None) or (self.__relaxUsedRestriction)))
    
    def act23(self):
        self.__test.append(('''self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard23,self.act23))
        try:
            self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=False
    def guard23(self):
        return (((self.p_list1_used[2]) or (self.p_list1[2] == None) or (self.__relaxUsedRestriction)))
    
    def act24(self):
        self.__test.append(('''print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0]) ''',self.guard24,self.act24))
        try:
            print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
    def guard24(self):
        return (self.p_list1[0] != None)
    
    def act25(self):
        self.__test.append(('''print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1]) ''',self.guard25,self.act25))
        try:
            print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
    def guard25(self):
        return (self.p_list1[1] != None)
    
    def act26(self):
        self.__test.append(('''print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2]) ''',self.guard26,self.act26))
        try:
            print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
    def guard26(self):
        return (self.p_list1[2] != None)
    
    def act27(self):
        self.__test.append(('''print (examine.Structure([None])).__add__(examine.Structure([])) ''',self.guard27,self.act27))
        try:
            print (examine.Structure([None])).__add__(examine.Structure([]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
    def guard27(self):
        return True
    
    def act28(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard28,self.act28))
        try:
            self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[0]=True
    def guard28(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act29(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard29,self.act29))
        try:
            self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[1]=True
    def guard29(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act30(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard30,self.act30))
        try:
            self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[2]=True
    def guard30(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act31(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard31,self.act31))
        try:
            self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[0]=True
    def guard31(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act32(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard32,self.act32))
        try:
            self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[1]=True
    def guard32(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act33(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard33,self.act33))
        try:
            self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[2]=True
    def guard33(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act34(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard34,self.act34))
        try:
            self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[0]=True
    def guard34(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act35(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard35,self.act35))
        try:
            self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[1]=True
    def guard35(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act36(self):
        self.__test.append(('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard36,self.act36))
        try:
            self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[0]=False
        self.p_strname_used[2]=True
    def guard36(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[0]) or (self.p_datalist[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act37(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard37,self.act37))
        try:
            self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[0]=True
    def guard37(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act38(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard38,self.act38))
        try:
            self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[1]=True
    def guard38(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act39(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard39,self.act39))
        try:
            self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[2]=True
    def guard39(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act40(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard40,self.act40))
        try:
            self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[0]=True
    def guard40(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act41(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard41,self.act41))
        try:
            self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[1]=True
    def guard41(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act42(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard42,self.act42))
        try:
            self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[2]=True
    def guard42(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act43(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard43,self.act43))
        try:
            self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[0]=True
    def guard43(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act44(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard44,self.act44))
        try:
            self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[1]=True
    def guard44(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act45(self):
        self.__test.append(('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard45,self.act45))
        try:
            self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[1]=False
        self.p_strname_used[2]=True
    def guard45(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[1]) or (self.p_datalist[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act46(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard46,self.act46))
        try:
            self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[0]=True
    def guard46(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act47(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard47,self.act47))
        try:
            self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[1]=True
    def guard47(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act48(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard48,self.act48))
        try:
            self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[2]=True
    def guard48(self):
        return (self.p_list1[0] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act49(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard49,self.act49))
        try:
            self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[0]=True
    def guard49(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act50(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard50,self.act50))
        try:
            self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[1]=True
    def guard50(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act51(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard51,self.act51))
        try:
            self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[2]=True
    def guard51(self):
        return (self.p_list1[1] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act52(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard52,self.act52))
        try:
            self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[0]=True
    def guard52(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act53(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard53,self.act53))
        try:
            self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[1]=True
    def guard53(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act54(self):
        self.__test.append(('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard54,self.act54))
        try:
            self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_datalist_used[2]=False
        self.p_strname_used[2]=True
    def guard54(self):
        return (self.p_list1[2] != None) and (((self.p_datalist_used[2]) or (self.p_datalist[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act55(self):
        self.__test.append(('''self.p_exams[0] = ['self.p_list1[0]'] ''',self.guard55,self.act55))
        try:
            self.p_exams[0] = ['self.p_list1[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_exams_used[0]=False
    def guard55(self):
        return (self.p_list1[0] != None) and (((self.p_exams_used[0]) or (self.p_exams[0] == None) or (self.__relaxUsedRestriction)))
    
    def act56(self):
        self.__test.append(('''self.p_exams[0] = ['self.p_list1[1]'] ''',self.guard56,self.act56))
        try:
            self.p_exams[0] = ['self.p_list1[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_exams_used[0]=False
    def guard56(self):
        return (self.p_list1[1] != None) and (((self.p_exams_used[0]) or (self.p_exams[0] == None) or (self.__relaxUsedRestriction)))
    
    def act57(self):
        self.__test.append(('''self.p_exams[0] = ['self.p_list1[2]'] ''',self.guard57,self.act57))
        try:
            self.p_exams[0] = ['self.p_list1[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_exams_used[0]=False
    def guard57(self):
        return (self.p_list1[2] != None) and (((self.p_exams_used[0]) or (self.p_exams[0] == None) or (self.__relaxUsedRestriction)))
    
    def act58(self):
        self.__test.append(('''self.p_exams[1] = ['self.p_list1[0]'] ''',self.guard58,self.act58))
        try:
            self.p_exams[1] = ['self.p_list1[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_exams_used[1]=False
    def guard58(self):
        return (self.p_list1[0] != None) and (((self.p_exams_used[1]) or (self.p_exams[1] == None) or (self.__relaxUsedRestriction)))
    
    def act59(self):
        self.__test.append(('''self.p_exams[1] = ['self.p_list1[1]'] ''',self.guard59,self.act59))
        try:
            self.p_exams[1] = ['self.p_list1[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_exams_used[1]=False
    def guard59(self):
        return (self.p_list1[1] != None) and (((self.p_exams_used[1]) or (self.p_exams[1] == None) or (self.__relaxUsedRestriction)))
    
    def act60(self):
        self.__test.append(('''self.p_exams[1] = ['self.p_list1[2]'] ''',self.guard60,self.act60))
        try:
            self.p_exams[1] = ['self.p_list1[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_exams_used[1]=False
    def guard60(self):
        return (self.p_list1[2] != None) and (((self.p_exams_used[1]) or (self.p_exams[1] == None) or (self.__relaxUsedRestriction)))
    
    def act61(self):
        self.__test.append(('''self.p_exams[2] = ['self.p_list1[0]'] ''',self.guard61,self.act61))
        try:
            self.p_exams[2] = ['self.p_list1[0]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_exams_used[2]=False
    def guard61(self):
        return (self.p_list1[0] != None) and (((self.p_exams_used[2]) or (self.p_exams[2] == None) or (self.__relaxUsedRestriction)))
    
    def act62(self):
        self.__test.append(('''self.p_exams[2] = ['self.p_list1[1]'] ''',self.guard62,self.act62))
        try:
            self.p_exams[2] = ['self.p_list1[1]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_exams_used[2]=False
    def guard62(self):
        return (self.p_list1[1] != None) and (((self.p_exams_used[2]) or (self.p_exams[2] == None) or (self.__relaxUsedRestriction)))
    
    def act63(self):
        self.__test.append(('''self.p_exams[2] = ['self.p_list1[2]'] ''',self.guard63,self.act63))
        try:
            self.p_exams[2] = ['self.p_list1[2]']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_exams_used[2]=False
    def guard63(self):
        return (self.p_list1[2] != None) and (((self.p_exams_used[2]) or (self.p_exams[2] == None) or (self.__relaxUsedRestriction)))
    
    def act64(self):
        self.__test.append(('''self.p_exams[0].append(self.p_datalist[0]) ''',self.guard64,self.act64))
        try:
            self.p_exams[0].append(self.p_datalist[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[0]=True
    def guard64(self):
        return (self.p_datalist[0] != None) and (self.p_exams[0] != None)
    
    def act65(self):
        self.__test.append(('''self.p_exams[0].append(self.p_datalist[1]) ''',self.guard65,self.act65))
        try:
            self.p_exams[0].append(self.p_datalist[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[1]=True
    def guard65(self):
        return (self.p_datalist[1] != None) and (self.p_exams[0] != None)
    
    def act66(self):
        self.__test.append(('''self.p_exams[0].append(self.p_datalist[2]) ''',self.guard66,self.act66))
        try:
            self.p_exams[0].append(self.p_datalist[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[2]=True
    def guard66(self):
        return (self.p_datalist[2] != None) and (self.p_exams[0] != None)
    
    def act67(self):
        self.__test.append(('''self.p_exams[1].append(self.p_datalist[0]) ''',self.guard67,self.act67))
        try:
            self.p_exams[1].append(self.p_datalist[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[0]=True
    def guard67(self):
        return (self.p_datalist[0] != None) and (self.p_exams[1] != None)
    
    def act68(self):
        self.__test.append(('''self.p_exams[1].append(self.p_datalist[1]) ''',self.guard68,self.act68))
        try:
            self.p_exams[1].append(self.p_datalist[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[1]=True
    def guard68(self):
        return (self.p_datalist[1] != None) and (self.p_exams[1] != None)
    
    def act69(self):
        self.__test.append(('''self.p_exams[1].append(self.p_datalist[2]) ''',self.guard69,self.act69))
        try:
            self.p_exams[1].append(self.p_datalist[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[2]=True
    def guard69(self):
        return (self.p_datalist[2] != None) and (self.p_exams[1] != None)
    
    def act70(self):
        self.__test.append(('''self.p_exams[2].append(self.p_datalist[0]) ''',self.guard70,self.act70))
        try:
            self.p_exams[2].append(self.p_datalist[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[0]=True
    def guard70(self):
        return (self.p_datalist[0] != None) and (self.p_exams[2] != None)
    
    def act71(self):
        self.__test.append(('''self.p_exams[2].append(self.p_datalist[1]) ''',self.guard71,self.act71))
        try:
            self.p_exams[2].append(self.p_datalist[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[1]=True
    def guard71(self):
        return (self.p_datalist[1] != None) and (self.p_exams[2] != None)
    
    def act72(self):
        self.__test.append(('''self.p_exams[2].append(self.p_datalist[2]) ''',self.guard72,self.act72))
        try:
            self.p_exams[2].append(self.p_datalist[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_datalist_used[2]=True
    def guard72(self):
        return (self.p_datalist[2] != None) and (self.p_exams[2] != None)
    
    def act73(self):
        self.__test.append(('''self.p_strname[0] = ['coding', 'snowboarding'] ''',self.guard73,self.act73))
        try:
            self.p_strname[0] = ['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strname_used[0]=False
    def guard73(self):
        return (((self.p_strname_used[0]) or (self.p_strname[0] == None) or (self.__relaxUsedRestriction)))
    
    def act74(self):
        self.__test.append(('''self.p_strname[1] = ['coding', 'snowboarding'] ''',self.guard74,self.act74))
        try:
            self.p_strname[1] = ['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strname_used[1]=False
    def guard74(self):
        return (((self.p_strname_used[1]) or (self.p_strname[1] == None) or (self.__relaxUsedRestriction)))
    
    def act75(self):
        self.__test.append(('''self.p_strname[2] = ['coding', 'snowboarding'] ''',self.guard75,self.act75))
        try:
            self.p_strname[2] = ['coding', 'snowboarding']

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strname_used[2]=False
    def guard75(self):
        return (((self.p_strname_used[2]) or (self.p_strname[2] == None) or (self.__relaxUsedRestriction)))
    
    def act76(self):
        self.__test.append(('''self.p_exam1[0]= examine.Structure(self.p_strname[0]) ''',self.guard76,self.act76))
        try:
            self.p_exam1[0]= examine.Structure(self.p_strname[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[0]=False
        self.p_strname_used[0]=True
    def guard76(self):
        return (((self.p_exam1_used[0]) or (self.p_exam1[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act77(self):
        self.__test.append(('''self.p_exam1[0]= examine.Structure(self.p_strname[1]) ''',self.guard77,self.act77))
        try:
            self.p_exam1[0]= examine.Structure(self.p_strname[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[0]=False
        self.p_strname_used[1]=True
    def guard77(self):
        return (((self.p_exam1_used[0]) or (self.p_exam1[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act78(self):
        self.__test.append(('''self.p_exam1[0]= examine.Structure(self.p_strname[2]) ''',self.guard78,self.act78))
        try:
            self.p_exam1[0]= examine.Structure(self.p_strname[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[0]=False
        self.p_strname_used[2]=True
    def guard78(self):
        return (((self.p_exam1_used[0]) or (self.p_exam1[0] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act79(self):
        self.__test.append(('''self.p_exam1[1]= examine.Structure(self.p_strname[0]) ''',self.guard79,self.act79))
        try:
            self.p_exam1[1]= examine.Structure(self.p_strname[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[1]=False
        self.p_strname_used[0]=True
    def guard79(self):
        return (((self.p_exam1_used[1]) or (self.p_exam1[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act80(self):
        self.__test.append(('''self.p_exam1[1]= examine.Structure(self.p_strname[1]) ''',self.guard80,self.act80))
        try:
            self.p_exam1[1]= examine.Structure(self.p_strname[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[1]=False
        self.p_strname_used[1]=True
    def guard80(self):
        return (((self.p_exam1_used[1]) or (self.p_exam1[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act81(self):
        self.__test.append(('''self.p_exam1[1]= examine.Structure(self.p_strname[2]) ''',self.guard81,self.act81))
        try:
            self.p_exam1[1]= examine.Structure(self.p_strname[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[1]=False
        self.p_strname_used[2]=True
    def guard81(self):
        return (((self.p_exam1_used[1]) or (self.p_exam1[1] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act82(self):
        self.__test.append(('''self.p_exam1[2]= examine.Structure(self.p_strname[0]) ''',self.guard82,self.act82))
        try:
            self.p_exam1[2]= examine.Structure(self.p_strname[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[2]=False
        self.p_strname_used[0]=True
    def guard82(self):
        return (((self.p_exam1_used[2]) or (self.p_exam1[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[0] != None)
    
    def act83(self):
        self.__test.append(('''self.p_exam1[2]= examine.Structure(self.p_strname[1]) ''',self.guard83,self.act83))
        try:
            self.p_exam1[2]= examine.Structure(self.p_strname[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[2]=False
        self.p_strname_used[1]=True
    def guard83(self):
        return (((self.p_exam1_used[2]) or (self.p_exam1[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[1] != None)
    
    def act84(self):
        self.__test.append(('''self.p_exam1[2]= examine.Structure(self.p_strname[2]) ''',self.guard84,self.act84))
        try:
            self.p_exam1[2]= examine.Structure(self.p_strname[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[2]=False
        self.p_strname_used[2]=True
    def guard84(self):
        return (((self.p_exam1_used[2]) or (self.p_exam1[2] == None) or (self.__relaxUsedRestriction))) and (self.p_strname[2] != None)
    
    def act85(self):
        self.__test.append(('''self.p_exam2[0]= examine.Structure(self.p_list1[0]) ''',self.guard85,self.act85))
        try:
            self.p_exam2[0]= examine.Structure(self.p_list1[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_exam2_used[0]=False
    def guard85(self):
        return (self.p_list1[0] != None) and (((self.p_exam2_used[0]) or (self.p_exam2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act86(self):
        self.__test.append(('''self.p_exam2[0]= examine.Structure(self.p_list1[1]) ''',self.guard86,self.act86))
        try:
            self.p_exam2[0]= examine.Structure(self.p_list1[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_exam2_used[0]=False
    def guard86(self):
        return (self.p_list1[1] != None) and (((self.p_exam2_used[0]) or (self.p_exam2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act87(self):
        self.__test.append(('''self.p_exam2[0]= examine.Structure(self.p_list1[2]) ''',self.guard87,self.act87))
        try:
            self.p_exam2[0]= examine.Structure(self.p_list1[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_exam2_used[0]=False
    def guard87(self):
        return (self.p_list1[2] != None) and (((self.p_exam2_used[0]) or (self.p_exam2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act88(self):
        self.__test.append(('''self.p_exam2[1]= examine.Structure(self.p_list1[0]) ''',self.guard88,self.act88))
        try:
            self.p_exam2[1]= examine.Structure(self.p_list1[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_exam2_used[1]=False
    def guard88(self):
        return (self.p_list1[0] != None) and (((self.p_exam2_used[1]) or (self.p_exam2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act89(self):
        self.__test.append(('''self.p_exam2[1]= examine.Structure(self.p_list1[1]) ''',self.guard89,self.act89))
        try:
            self.p_exam2[1]= examine.Structure(self.p_list1[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_exam2_used[1]=False
    def guard89(self):
        return (self.p_list1[1] != None) and (((self.p_exam2_used[1]) or (self.p_exam2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act90(self):
        self.__test.append(('''self.p_exam2[1]= examine.Structure(self.p_list1[2]) ''',self.guard90,self.act90))
        try:
            self.p_exam2[1]= examine.Structure(self.p_list1[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_exam2_used[1]=False
    def guard90(self):
        return (self.p_list1[2] != None) and (((self.p_exam2_used[1]) or (self.p_exam2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act91(self):
        self.__test.append(('''self.p_exam2[2]= examine.Structure(self.p_list1[0]) ''',self.guard91,self.act91))
        try:
            self.p_exam2[2]= examine.Structure(self.p_list1[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[0]=True
        self.p_exam2_used[2]=False
    def guard91(self):
        return (self.p_list1[0] != None) and (((self.p_exam2_used[2]) or (self.p_exam2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act92(self):
        self.__test.append(('''self.p_exam2[2]= examine.Structure(self.p_list1[1]) ''',self.guard92,self.act92))
        try:
            self.p_exam2[2]= examine.Structure(self.p_list1[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[1]=True
        self.p_exam2_used[2]=False
    def guard92(self):
        return (self.p_list1[1] != None) and (((self.p_exam2_used[2]) or (self.p_exam2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act93(self):
        self.__test.append(('''self.p_exam2[2]= examine.Structure(self.p_list1[2]) ''',self.guard93,self.act93))
        try:
            self.p_exam2[2]= examine.Structure(self.p_list1[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_list1_used[2]=True
        self.p_exam2_used[2]=False
    def guard93(self):
        return (self.p_list1[2] != None) and (((self.p_exam2_used[2]) or (self.p_exam2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act94(self):
        self.__test.append(('''self.p_exam3[0]= examine.Structure(self.p_exams[0]) ''',self.guard94,self.act94))
        try:
            self.p_exam3[0]= examine.Structure(self.p_exams[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[0]=True
        self.p_exam3_used[0]=False
    def guard94(self):
        return (self.p_exams[0] != None) and (((self.p_exam3_used[0]) or (self.p_exam3[0] == None) or (self.__relaxUsedRestriction)))
    
    def act95(self):
        self.__test.append(('''self.p_exam3[0]= examine.Structure(self.p_exams[1]) ''',self.guard95,self.act95))
        try:
            self.p_exam3[0]= examine.Structure(self.p_exams[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[1]=True
        self.p_exam3_used[0]=False
    def guard95(self):
        return (self.p_exams[1] != None) and (((self.p_exam3_used[0]) or (self.p_exam3[0] == None) or (self.__relaxUsedRestriction)))
    
    def act96(self):
        self.__test.append(('''self.p_exam3[0]= examine.Structure(self.p_exams[2]) ''',self.guard96,self.act96))
        try:
            self.p_exam3[0]= examine.Structure(self.p_exams[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[2]=True
        self.p_exam3_used[0]=False
    def guard96(self):
        return (self.p_exams[2] != None) and (((self.p_exam3_used[0]) or (self.p_exam3[0] == None) or (self.__relaxUsedRestriction)))
    
    def act97(self):
        self.__test.append(('''self.p_exam3[1]= examine.Structure(self.p_exams[0]) ''',self.guard97,self.act97))
        try:
            self.p_exam3[1]= examine.Structure(self.p_exams[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[0]=True
        self.p_exam3_used[1]=False
    def guard97(self):
        return (self.p_exams[0] != None) and (((self.p_exam3_used[1]) or (self.p_exam3[1] == None) or (self.__relaxUsedRestriction)))
    
    def act98(self):
        self.__test.append(('''self.p_exam3[1]= examine.Structure(self.p_exams[1]) ''',self.guard98,self.act98))
        try:
            self.p_exam3[1]= examine.Structure(self.p_exams[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[1]=True
        self.p_exam3_used[1]=False
    def guard98(self):
        return (self.p_exams[1] != None) and (((self.p_exam3_used[1]) or (self.p_exam3[1] == None) or (self.__relaxUsedRestriction)))
    
    def act99(self):
        self.__test.append(('''self.p_exam3[1]= examine.Structure(self.p_exams[2]) ''',self.guard99,self.act99))
        try:
            self.p_exam3[1]= examine.Structure(self.p_exams[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[2]=True
        self.p_exam3_used[1]=False
    def guard99(self):
        return (self.p_exams[2] != None) and (((self.p_exam3_used[1]) or (self.p_exam3[1] == None) or (self.__relaxUsedRestriction)))
    
    def act100(self):
        self.__test.append(('''self.p_exam3[2]= examine.Structure(self.p_exams[0]) ''',self.guard100,self.act100))
        try:
            self.p_exam3[2]= examine.Structure(self.p_exams[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[0]=True
        self.p_exam3_used[2]=False
    def guard100(self):
        return (self.p_exams[0] != None) and (((self.p_exam3_used[2]) or (self.p_exam3[2] == None) or (self.__relaxUsedRestriction)))
    
    def act101(self):
        self.__test.append(('''self.p_exam3[2]= examine.Structure(self.p_exams[1]) ''',self.guard101,self.act101))
        try:
            self.p_exam3[2]= examine.Structure(self.p_exams[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[1]=True
        self.p_exam3_used[2]=False
    def guard101(self):
        return (self.p_exams[1] != None) and (((self.p_exam3_used[2]) or (self.p_exam3[2] == None) or (self.__relaxUsedRestriction)))
    
    def act102(self):
        self.__test.append(('''self.p_exam3[2]= examine.Structure(self.p_exams[2]) ''',self.guard102,self.act102))
        try:
            self.p_exam3[2]= examine.Structure(self.p_exams[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exams_used[2]=True
        self.p_exam3_used[2]=False
    def guard102(self):
        return (self.p_exams[2] != None) and (((self.p_exam3_used[2]) or (self.p_exam3[2] == None) or (self.__relaxUsedRestriction)))
    
    def act103(self):
        self.__test.append(('''check(self.p_exam3[0].__add__(self.p_exam3[0])) ''',self.guard103,self.act103))
        try:
            check(self.p_exam3[0].__add__(self.p_exam3[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[0]=True
        self.p_exam3_used[0]=True
    def guard103(self):
        return (self.p_exam3[0] != None) and (self.p_exam3[0] != None)
    
    def act104(self):
        self.__test.append(('''check(self.p_exam3[0].__add__(self.p_exam3[1])) ''',self.guard104,self.act104))
        try:
            check(self.p_exam3[0].__add__(self.p_exam3[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[0]=True
        self.p_exam3_used[1]=True
    def guard104(self):
        return (self.p_exam3[0] != None) and (self.p_exam3[1] != None)
    
    def act105(self):
        self.__test.append(('''check(self.p_exam3[0].__add__(self.p_exam3[2])) ''',self.guard105,self.act105))
        try:
            check(self.p_exam3[0].__add__(self.p_exam3[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[0]=True
        self.p_exam3_used[2]=True
    def guard105(self):
        return (self.p_exam3[0] != None) and (self.p_exam3[2] != None)
    
    def act106(self):
        self.__test.append(('''check(self.p_exam3[1].__add__(self.p_exam3[0])) ''',self.guard106,self.act106))
        try:
            check(self.p_exam3[1].__add__(self.p_exam3[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[1]=True
        self.p_exam3_used[0]=True
    def guard106(self):
        return (self.p_exam3[1] != None) and (self.p_exam3[0] != None)
    
    def act107(self):
        self.__test.append(('''check(self.p_exam3[1].__add__(self.p_exam3[1])) ''',self.guard107,self.act107))
        try:
            check(self.p_exam3[1].__add__(self.p_exam3[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[1]=True
        self.p_exam3_used[1]=True
    def guard107(self):
        return (self.p_exam3[1] != None) and (self.p_exam3[1] != None)
    
    def act108(self):
        self.__test.append(('''check(self.p_exam3[1].__add__(self.p_exam3[2])) ''',self.guard108,self.act108))
        try:
            check(self.p_exam3[1].__add__(self.p_exam3[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[1]=True
        self.p_exam3_used[2]=True
    def guard108(self):
        return (self.p_exam3[1] != None) and (self.p_exam3[2] != None)
    
    def act109(self):
        self.__test.append(('''check(self.p_exam3[2].__add__(self.p_exam3[0])) ''',self.guard109,self.act109))
        try:
            check(self.p_exam3[2].__add__(self.p_exam3[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[2]=True
        self.p_exam3_used[0]=True
    def guard109(self):
        return (self.p_exam3[2] != None) and (self.p_exam3[0] != None)
    
    def act110(self):
        self.__test.append(('''check(self.p_exam3[2].__add__(self.p_exam3[1])) ''',self.guard110,self.act110))
        try:
            check(self.p_exam3[2].__add__(self.p_exam3[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[2]=True
        self.p_exam3_used[1]=True
    def guard110(self):
        return (self.p_exam3[2] != None) and (self.p_exam3[1] != None)
    
    def act111(self):
        self.__test.append(('''check(self.p_exam3[2].__add__(self.p_exam3[2])) ''',self.guard111,self.act111))
        try:
            check(self.p_exam3[2].__add__(self.p_exam3[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam3_used[2]=True
        self.p_exam3_used[2]=True
    def guard111(self):
        return (self.p_exam3[2] != None) and (self.p_exam3[2] != None)
    
    def act112(self):
        self.__test.append(('''check(self.p_exam1[0].__add__(self.p_exam3[0])) ''',self.guard112,self.act112))
        try:
            check(self.p_exam1[0].__add__(self.p_exam3[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[0]=True
        self.p_exam3_used[0]=True
    def guard112(self):
        return (self.p_exam1[0] != None) and (self.p_exam3[0] != None)
    
    def act113(self):
        self.__test.append(('''check(self.p_exam1[0].__add__(self.p_exam3[1])) ''',self.guard113,self.act113))
        try:
            check(self.p_exam1[0].__add__(self.p_exam3[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[0]=True
        self.p_exam3_used[1]=True
    def guard113(self):
        return (self.p_exam1[0] != None) and (self.p_exam3[1] != None)
    
    def act114(self):
        self.__test.append(('''check(self.p_exam1[0].__add__(self.p_exam3[2])) ''',self.guard114,self.act114))
        try:
            check(self.p_exam1[0].__add__(self.p_exam3[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[0]=True
        self.p_exam3_used[2]=True
    def guard114(self):
        return (self.p_exam1[0] != None) and (self.p_exam3[2] != None)
    
    def act115(self):
        self.__test.append(('''check(self.p_exam1[1].__add__(self.p_exam3[0])) ''',self.guard115,self.act115))
        try:
            check(self.p_exam1[1].__add__(self.p_exam3[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[1]=True
        self.p_exam3_used[0]=True
    def guard115(self):
        return (self.p_exam1[1] != None) and (self.p_exam3[0] != None)
    
    def act116(self):
        self.__test.append(('''check(self.p_exam1[1].__add__(self.p_exam3[1])) ''',self.guard116,self.act116))
        try:
            check(self.p_exam1[1].__add__(self.p_exam3[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[1]=True
        self.p_exam3_used[1]=True
    def guard116(self):
        return (self.p_exam1[1] != None) and (self.p_exam3[1] != None)
    
    def act117(self):
        self.__test.append(('''check(self.p_exam1[1].__add__(self.p_exam3[2])) ''',self.guard117,self.act117))
        try:
            check(self.p_exam1[1].__add__(self.p_exam3[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[1]=True
        self.p_exam3_used[2]=True
    def guard117(self):
        return (self.p_exam1[1] != None) and (self.p_exam3[2] != None)
    
    def act118(self):
        self.__test.append(('''check(self.p_exam1[2].__add__(self.p_exam3[0])) ''',self.guard118,self.act118))
        try:
            check(self.p_exam1[2].__add__(self.p_exam3[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[2]=True
        self.p_exam3_used[0]=True
    def guard118(self):
        return (self.p_exam1[2] != None) and (self.p_exam3[0] != None)
    
    def act119(self):
        self.__test.append(('''check(self.p_exam1[2].__add__(self.p_exam3[1])) ''',self.guard119,self.act119))
        try:
            check(self.p_exam1[2].__add__(self.p_exam3[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[2]=True
        self.p_exam3_used[1]=True
    def guard119(self):
        return (self.p_exam1[2] != None) and (self.p_exam3[1] != None)
    
    def act120(self):
        self.__test.append(('''check(self.p_exam1[2].__add__(self.p_exam3[2])) ''',self.guard120,self.act120))
        try:
            check(self.p_exam1[2].__add__(self.p_exam3[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_exam1_used[2]=True
        self.p_exam3_used[2]=True
    def guard120(self):
        return (self.p_exam1[2] != None) and (self.p_exam3[2] != None)
    
    def act121(self):
        self.__test.append(('''print (examine.Structure([])) ''',self.guard121,self.act121))
        try:
            print (examine.Structure([]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
    def guard121(self):
        return True
    
    def act122(self):
        self.__test.append(('''print (examine.Structure({})) ''',self.guard122,self.act122))
        try:
            print (examine.Structure({}))

        finally:
            try:
                test_after_each(self)
            except:
                pass
    def guard122(self):
        return True
    
    def act123(self):
        self.__test.append(('''self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard123,self.act123))
        try:
            self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alist_used[0]=False
    def guard123(self):
        return (((self.p_alist_used[0]) or (self.p_alist[0] == None) or (self.__relaxUsedRestriction)))
    
    def act124(self):
        self.__test.append(('''self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard124,self.act124))
        try:
            self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alist_used[1]=False
    def guard124(self):
        return (((self.p_alist_used[1]) or (self.p_alist[1] == None) or (self.__relaxUsedRestriction)))
    
    def act125(self):
        self.__test.append(('''self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard125,self.act125))
        try:
            self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alist_used[2]=False
    def guard125(self):
        return (((self.p_alist_used[2]) or (self.p_alist[2] == None) or (self.__relaxUsedRestriction)))
    
    def act126(self):
        self.__test.append(('''print (examine.Structure(self.p_alist[0])) ''',self.guard126,self.act126))
        try:
            print (examine.Structure(self.p_alist[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alist_used[0]=True
    def guard126(self):
        return (self.p_alist[0] != None)
    
    def act127(self):
        self.__test.append(('''print (examine.Structure(self.p_alist[1])) ''',self.guard127,self.act127))
        try:
            print (examine.Structure(self.p_alist[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alist_used[1]=True
    def guard127(self):
        return (self.p_alist[1] != None)
    
    def act128(self):
        self.__test.append(('''print (examine.Structure(self.p_alist[2])) ''',self.guard128,self.act128))
        try:
            print (examine.Structure(self.p_alist[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alist_used[2]=True
    def guard128(self):
        return (self.p_alist[2] != None)
    
    def act129(self):
        self.__test.append(('''self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}] ''',self.guard129,self.act129))
        try:
            self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alistmerge_used[0]=False
    def guard129(self):
        return (((self.p_alistmerge_used[0]) or (self.p_alistmerge[0] == None) or (self.__relaxUsedRestriction)))
    
    def act130(self):
        self.__test.append(('''self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}] ''',self.guard130,self.act130))
        try:
            self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alistmerge_used[1]=False
    def guard130(self):
        return (((self.p_alistmerge_used[1]) or (self.p_alistmerge[1] == None) or (self.__relaxUsedRestriction)))
    
    def act131(self):
        self.__test.append(('''self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}] ''',self.guard131,self.act131))
        try:
            self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alistmerge_used[2]=False
    def guard131(self):
        return (((self.p_alistmerge_used[2]) or (self.p_alistmerge[2] == None) or (self.__relaxUsedRestriction)))
    
    def act132(self):
        self.__test.append(('''print (examine.Structure(self.p_alistmerge[0])) ''',self.guard132,self.act132))
        try:
            print (examine.Structure(self.p_alistmerge[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alistmerge_used[0]=True
    def guard132(self):
        return (self.p_alistmerge[0] != None)
    
    def act133(self):
        self.__test.append(('''print (examine.Structure(self.p_alistmerge[1])) ''',self.guard133,self.act133))
        try:
            print (examine.Structure(self.p_alistmerge[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alistmerge_used[1]=True
    def guard133(self):
        return (self.p_alistmerge[1] != None)
    
    def act134(self):
        self.__test.append(('''print (examine.Structure(self.p_alistmerge[2])) ''',self.guard134,self.act134))
        try:
            print (examine.Structure(self.p_alistmerge[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_alistmerge_used[2]=True
    def guard134(self):
        return (self.p_alistmerge[2] != None)
    
    def act135(self):
        self.__test.append(('''self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard135,self.act135))
        try:
            self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nestedlist_used[0]=False
    def guard135(self):
        return (((self.p_nestedlist_used[0]) or (self.p_nestedlist[0] == None) or (self.__relaxUsedRestriction)))
    
    def act136(self):
        self.__test.append(('''self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard136,self.act136))
        try:
            self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nestedlist_used[1]=False
    def guard136(self):
        return (((self.p_nestedlist_used[1]) or (self.p_nestedlist[1] == None) or (self.__relaxUsedRestriction)))
    
    def act137(self):
        self.__test.append(('''self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard137,self.act137))
        try:
            self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nestedlist_used[2]=False
    def guard137(self):
        return (((self.p_nestedlist_used[2]) or (self.p_nestedlist[2] == None) or (self.__relaxUsedRestriction)))
    
    def act138(self):
        self.__test.append(('''print (examine.Structure(self.p_nestedlist[0])) ''',self.guard138,self.act138))
        try:
            print (examine.Structure(self.p_nestedlist[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nestedlist_used[0]=True
    def guard138(self):
        return (self.p_nestedlist[0] != None)
    
    def act139(self):
        self.__test.append(('''print (examine.Structure(self.p_nestedlist[1])) ''',self.guard139,self.act139))
        try:
            print (examine.Structure(self.p_nestedlist[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nestedlist_used[1]=True
    def guard139(self):
        return (self.p_nestedlist[1] != None)
    
    def act140(self):
        self.__test.append(('''print (examine.Structure(self.p_nestedlist[2])) ''',self.guard140,self.act140))
        try:
            print (examine.Structure(self.p_nestedlist[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nestedlist_used[2]=True
    def guard140(self):
        return (self.p_nestedlist[2] != None)
    
    def act141(self):
        self.__test.append(('''self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard141,self.act141))
        try:
            self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_incosistentdepth_used[0]=False
    def guard141(self):
        return (((self.p_incosistentdepth_used[0]) or (self.p_incosistentdepth[0] == None) or (self.__relaxUsedRestriction)))
    
    def act142(self):
        self.__test.append(('''self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard142,self.act142))
        try:
            self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_incosistentdepth_used[1]=False
    def guard142(self):
        return (((self.p_incosistentdepth_used[1]) or (self.p_incosistentdepth[1] == None) or (self.__relaxUsedRestriction)))
    
    def act143(self):
        self.__test.append(('''self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard143,self.act143))
        try:
            self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_incosistentdepth_used[2]=False
    def guard143(self):
        return (((self.p_incosistentdepth_used[2]) or (self.p_incosistentdepth[2] == None) or (self.__relaxUsedRestriction)))
    
    def act144(self):
        self.__test.append(('''print (examine.Structure(self.p_incosistentdepth[0])) ''',self.guard144,self.act144))
        try:
            print (examine.Structure(self.p_incosistentdepth[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_incosistentdepth_used[0]=True
    def guard144(self):
        return (self.p_incosistentdepth[0] != None)
    
    def act145(self):
        self.__test.append(('''print (examine.Structure(self.p_incosistentdepth[1])) ''',self.guard145,self.act145))
        try:
            print (examine.Structure(self.p_incosistentdepth[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_incosistentdepth_used[1]=True
    def guard145(self):
        return (self.p_incosistentdepth[1] != None)
    
    def act146(self):
        self.__test.append(('''print (examine.Structure(self.p_incosistentdepth[2])) ''',self.guard146,self.act146))
        try:
            print (examine.Structure(self.p_incosistentdepth[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_incosistentdepth_used[2]=True
    def guard146(self):
        return (self.p_incosistentdepth[2] != None)
    
    def act147(self):
        self.__test.append(('''self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard147,self.act147))
        try:
            self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}}

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nesteddict_used[0]=False
    def guard147(self):
        return (((self.p_nesteddict_used[0]) or (self.p_nesteddict[0] == None) or (self.__relaxUsedRestriction)))
    
    def act148(self):
        self.__test.append(('''self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard148,self.act148))
        try:
            self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}}

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nesteddict_used[1]=False
    def guard148(self):
        return (((self.p_nesteddict_used[1]) or (self.p_nesteddict[1] == None) or (self.__relaxUsedRestriction)))
    
    def act149(self):
        self.__test.append(('''self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard149,self.act149))
        try:
            self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}}

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nesteddict_used[2]=False
    def guard149(self):
        return (((self.p_nesteddict_used[2]) or (self.p_nesteddict[2] == None) or (self.__relaxUsedRestriction)))
    
    def act150(self):
        self.__test.append(('''print (examine.Structure(self.p_nesteddict[0])) ''',self.guard150,self.act150))
        try:
            print (examine.Structure(self.p_nesteddict[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nesteddict_used[0]=True
    def guard150(self):
        return (self.p_nesteddict[0] != None)
    
    def act151(self):
        self.__test.append(('''print (examine.Structure(self.p_nesteddict[1])) ''',self.guard151,self.act151))
        try:
            print (examine.Structure(self.p_nesteddict[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nesteddict_used[1]=True
    def guard151(self):
        return (self.p_nesteddict[1] != None)
    
    def act152(self):
        self.__test.append(('''print (examine.Structure(self.p_nesteddict[2])) ''',self.guard152,self.act152))
        try:
            print (examine.Structure(self.p_nesteddict[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nesteddict_used[2]=True
    def guard152(self):
        return (self.p_nesteddict[2] != None)
    
    def act153(self):
        self.__test.append(('''self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard153,self.act153))
        try:
            self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_addemptylistdicts_used[0]=False
    def guard153(self):
        return (((self.p_addemptylistdicts_used[0]) or (self.p_addemptylistdicts[0] == None) or (self.__relaxUsedRestriction)))
    
    def act154(self):
        self.__test.append(('''self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard154,self.act154))
        try:
            self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_addemptylistdicts_used[1]=False
    def guard154(self):
        return (((self.p_addemptylistdicts_used[1]) or (self.p_addemptylistdicts[1] == None) or (self.__relaxUsedRestriction)))
    
    def act155(self):
        self.__test.append(('''self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard155,self.act155))
        try:
            self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_addemptylistdicts_used[2]=False
    def guard155(self):
        return (((self.p_addemptylistdicts_used[2]) or (self.p_addemptylistdicts[2] == None) or (self.__relaxUsedRestriction)))
    
    def act156(self):
        self.__test.append(('''print (examine.Structure(self.p_addemptylistdicts[0])) ''',self.guard156,self.act156))
        try:
            print (examine.Structure(self.p_addemptylistdicts[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_addemptylistdicts_used[0]=True
    def guard156(self):
        return (self.p_addemptylistdicts[0] != None)
    
    def act157(self):
        self.__test.append(('''print (examine.Structure(self.p_addemptylistdicts[1])) ''',self.guard157,self.act157))
        try:
            print (examine.Structure(self.p_addemptylistdicts[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_addemptylistdicts_used[1]=True
    def guard157(self):
        return (self.p_addemptylistdicts[1] != None)
    
    def act158(self):
        self.__test.append(('''print (examine.Structure(self.p_addemptylistdicts[2])) ''',self.guard158,self.act158))
        try:
            print (examine.Structure(self.p_addemptylistdicts[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_addemptylistdicts_used[2]=True
    def guard158(self):
        return (self.p_addemptylistdicts[2] != None)
    
    def act159(self):
        self.__test.append(('''self.p_noneinlist[0]=[1, 2, 3, None] ''',self.guard159,self.act159))
        try:
            self.p_noneinlist[0]=[1, 2, 3, None]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_noneinlist_used[0]=False
    def guard159(self):
        return (((self.p_noneinlist_used[0]) or (self.p_noneinlist[0] == None) or (self.__relaxUsedRestriction)))
    
    def act160(self):
        self.__test.append(('''self.p_noneinlist[1]=[1, 2, 3, None] ''',self.guard160,self.act160))
        try:
            self.p_noneinlist[1]=[1, 2, 3, None]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_noneinlist_used[1]=False
    def guard160(self):
        return (((self.p_noneinlist_used[1]) or (self.p_noneinlist[1] == None) or (self.__relaxUsedRestriction)))
    
    def act161(self):
        self.__test.append(('''self.p_noneinlist[2]=[1, 2, 3, None] ''',self.guard161,self.act161))
        try:
            self.p_noneinlist[2]=[1, 2, 3, None]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_noneinlist_used[2]=False
    def guard161(self):
        return (((self.p_noneinlist_used[2]) or (self.p_noneinlist[2] == None) or (self.__relaxUsedRestriction)))
    
    def act162(self):
        self.__test.append(('''print (examine.Structure(self.p_noneinlist[0])) ''',self.guard162,self.act162))
        try:
            print (examine.Structure(self.p_noneinlist[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_noneinlist_used[0]=True
    def guard162(self):
        return (self.p_noneinlist[0] != None)
    
    def act163(self):
        self.__test.append(('''print (examine.Structure(self.p_noneinlist[1])) ''',self.guard163,self.act163))
        try:
            print (examine.Structure(self.p_noneinlist[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_noneinlist_used[1]=True
    def guard163(self):
        return (self.p_noneinlist[1] != None)
    
    def act164(self):
        self.__test.append(('''print (examine.Structure(self.p_noneinlist[2])) ''',self.guard164,self.act164))
        try:
            print (examine.Structure(self.p_noneinlist[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_noneinlist_used[2]=True
    def guard164(self):
        return (self.p_noneinlist[2] != None)
    
    def act165(self):
        self.__test.append(('''self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}] ''',self.guard165,self.act165))
        try:
            self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nonekeydicts_used[0]=False
    def guard165(self):
        return (((self.p_nonekeydicts_used[0]) or (self.p_nonekeydicts[0] == None) or (self.__relaxUsedRestriction)))
    
    def act166(self):
        self.__test.append(('''self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}] ''',self.guard166,self.act166))
        try:
            self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nonekeydicts_used[1]=False
    def guard166(self):
        return (((self.p_nonekeydicts_used[1]) or (self.p_nonekeydicts[1] == None) or (self.__relaxUsedRestriction)))
    
    def act167(self):
        self.__test.append(('''self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}] ''',self.guard167,self.act167))
        try:
            self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nonekeydicts_used[2]=False
    def guard167(self):
        return (((self.p_nonekeydicts_used[2]) or (self.p_nonekeydicts[2] == None) or (self.__relaxUsedRestriction)))
    
    def act168(self):
        self.__test.append(('''print (examine.Structure(self.p_nonekeydicts[0])) ''',self.guard168,self.act168))
        try:
            print (examine.Structure(self.p_nonekeydicts[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nonekeydicts_used[0]=True
    def guard168(self):
        return (self.p_nonekeydicts[0] != None)
    
    def act169(self):
        self.__test.append(('''print (examine.Structure(self.p_nonekeydicts[1])) ''',self.guard169,self.act169))
        try:
            print (examine.Structure(self.p_nonekeydicts[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nonekeydicts_used[1]=True
    def guard169(self):
        return (self.p_nonekeydicts[1] != None)
    
    def act170(self):
        self.__test.append(('''print (examine.Structure(self.p_nonekeydicts[2])) ''',self.guard170,self.act170))
        try:
            print (examine.Structure(self.p_nonekeydicts[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_nonekeydicts_used[2]=True
    def guard170(self):
        return (self.p_nonekeydicts[2] != None)
    
    def act171(self):
        self.__test.append(('''self.p_tuple[0]= ('string', 1) ''',self.guard171,self.act171))
        try:
            self.p_tuple[0]= ('string', 1)

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_tuple_used[0]=False
    def guard171(self):
        return (((self.p_tuple_used[0]) or (self.p_tuple[0] == None) or (self.__relaxUsedRestriction)))
    
    def act172(self):
        self.__test.append(('''self.p_tuple[1]= ('string', 1) ''',self.guard172,self.act172))
        try:
            self.p_tuple[1]= ('string', 1)

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_tuple_used[1]=False
    def guard172(self):
        return (((self.p_tuple_used[1]) or (self.p_tuple[1] == None) or (self.__relaxUsedRestriction)))
    
    def act173(self):
        self.__test.append(('''self.p_tuple[2]= ('string', 1) ''',self.guard173,self.act173))
        try:
            self.p_tuple[2]= ('string', 1)

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_tuple_used[2]=False
    def guard173(self):
        return (((self.p_tuple_used[2]) or (self.p_tuple[2] == None) or (self.__relaxUsedRestriction)))
    
    def act174(self):
        self.__test.append(('''print (examine.Structure(self.p_tuple[0])) ''',self.guard174,self.act174))
        try:
            print (examine.Structure(self.p_tuple[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_tuple_used[0]=True
    def guard174(self):
        return (self.p_tuple[0] != None)
    
    def act175(self):
        self.__test.append(('''print (examine.Structure(self.p_tuple[1])) ''',self.guard175,self.act175))
        try:
            print (examine.Structure(self.p_tuple[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_tuple_used[1]=True
    def guard175(self):
        return (self.p_tuple[1] != None)
    
    def act176(self):
        self.__test.append(('''print (examine.Structure(self.p_tuple[2])) ''',self.guard176,self.act176))
        try:
            print (examine.Structure(self.p_tuple[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_tuple_used[2]=True
    def guard176(self):
        return (self.p_tuple[2] != None)
    
    def act177(self):
        self.__test.append(('''self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []] ''',self.guard177,self.act177))
        try:
            self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_deeplistnest_used[0]=False
    def guard177(self):
        return (((self.p_deeplistnest_used[0]) or (self.p_deeplistnest[0] == None) or (self.__relaxUsedRestriction)))
    
    def act178(self):
        self.__test.append(('''self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []] ''',self.guard178,self.act178))
        try:
            self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_deeplistnest_used[1]=False
    def guard178(self):
        return (((self.p_deeplistnest_used[1]) or (self.p_deeplistnest[1] == None) or (self.__relaxUsedRestriction)))
    
    def act179(self):
        self.__test.append(('''self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []] ''',self.guard179,self.act179))
        try:
            self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_deeplistnest_used[2]=False
    def guard179(self):
        return (((self.p_deeplistnest_used[2]) or (self.p_deeplistnest[2] == None) or (self.__relaxUsedRestriction)))
    
    def act180(self):
        self.__test.append(('''print (examine.Structure(self.p_deeplistnest[0])) ''',self.guard180,self.act180))
        try:
            print (examine.Structure(self.p_deeplistnest[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_deeplistnest_used[0]=True
    def guard180(self):
        return (self.p_deeplistnest[0] != None)
    
    def act181(self):
        self.__test.append(('''print (examine.Structure(self.p_deeplistnest[1])) ''',self.guard181,self.act181))
        try:
            print (examine.Structure(self.p_deeplistnest[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_deeplistnest_used[1]=True
    def guard181(self):
        return (self.p_deeplistnest[1] != None)
    
    def act182(self):
        self.__test.append(('''print (examine.Structure(self.p_deeplistnest[2])) ''',self.guard182,self.act182))
        try:
            print (examine.Structure(self.p_deeplistnest[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_deeplistnest_used[2]=True
    def guard182(self):
        return (self.p_deeplistnest[2] != None)
    
    def act183(self):
        self.__test.append(('''self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard183,self.act183))
        try:
            self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_listuples_used[0]=False
    def guard183(self):
        return (((self.p_listuples_used[0]) or (self.p_listuples[0] == None) or (self.__relaxUsedRestriction)))
    
    def act184(self):
        self.__test.append(('''self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard184,self.act184))
        try:
            self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_listuples_used[1]=False
    def guard184(self):
        return (((self.p_listuples_used[1]) or (self.p_listuples[1] == None) or (self.__relaxUsedRestriction)))
    
    def act185(self):
        self.__test.append(('''self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard185,self.act185))
        try:
            self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_listuples_used[2]=False
    def guard185(self):
        return (((self.p_listuples_used[2]) or (self.p_listuples[2] == None) or (self.__relaxUsedRestriction)))
    
    def act186(self):
        self.__test.append(('''print (examine.Structure(self.p_listuples[0])) ''',self.guard186,self.act186))
        try:
            print (examine.Structure(self.p_listuples[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_listuples_used[0]=True
    def guard186(self):
        return (self.p_listuples[0] != None)
    
    def act187(self):
        self.__test.append(('''print (examine.Structure(self.p_listuples[1])) ''',self.guard187,self.act187))
        try:
            print (examine.Structure(self.p_listuples[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_listuples_used[1]=True
    def guard187(self):
        return (self.p_listuples[1] != None)
    
    def act188(self):
        self.__test.append(('''print (examine.Structure(self.p_listuples[2])) ''',self.guard188,self.act188))
        try:
            print (examine.Structure(self.p_listuples[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_listuples_used[2]=True
    def guard188(self):
        return (self.p_listuples[2] != None)
    
    def act189(self):
        self.__test.append(('''self.p_emptytuplemerging[0]= [tuple(), ('str', 1)] ''',self.guard189,self.act189))
        try:
            self.p_emptytuplemerging[0]= [tuple(), ('str', 1)]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_emptytuplemerging_used[0]=False
    def guard189(self):
        return (((self.p_emptytuplemerging_used[0]) or (self.p_emptytuplemerging[0] == None) or (self.__relaxUsedRestriction)))
    
    def act190(self):
        self.__test.append(('''self.p_emptytuplemerging[1]= [tuple(), ('str', 1)] ''',self.guard190,self.act190))
        try:
            self.p_emptytuplemerging[1]= [tuple(), ('str', 1)]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_emptytuplemerging_used[1]=False
    def guard190(self):
        return (((self.p_emptytuplemerging_used[1]) or (self.p_emptytuplemerging[1] == None) or (self.__relaxUsedRestriction)))
    
    def act191(self):
        self.__test.append(('''self.p_emptytuplemerging[2]= [tuple(), ('str', 1)] ''',self.guard191,self.act191))
        try:
            self.p_emptytuplemerging[2]= [tuple(), ('str', 1)]

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_emptytuplemerging_used[2]=False
    def guard191(self):
        return (((self.p_emptytuplemerging_used[2]) or (self.p_emptytuplemerging[2] == None) or (self.__relaxUsedRestriction)))
    
    def act192(self):
        self.__test.append(('''print (examine.Structure(self.p_emptytuplemerging[0])) ''',self.guard192,self.act192))
        try:
            print (examine.Structure(self.p_emptytuplemerging[0]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_emptytuplemerging_used[0]=True
    def guard192(self):
        return (self.p_emptytuplemerging[0] != None)
    
    def act193(self):
        self.__test.append(('''print (examine.Structure(self.p_emptytuplemerging[1])) ''',self.guard193,self.act193))
        try:
            print (examine.Structure(self.p_emptytuplemerging[1]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_emptytuplemerging_used[1]=True
    def guard193(self):
        return (self.p_emptytuplemerging[1] != None)
    
    def act194(self):
        self.__test.append(('''print (examine.Structure(self.p_emptytuplemerging[2])) ''',self.guard194,self.act194))
        try:
            print (examine.Structure(self.p_emptytuplemerging[2]))

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_emptytuplemerging_used[2]=True
    def guard194(self):
        return (self.p_emptytuplemerging[2] != None)
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__modules.append(r"examine.py")
        self.__features = []
        self.__replayBacktrack = False
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_list1 = {}
        self.p_list1_used = {}
        self.__pools.append("self.p_list1")
        self.p_list1[0] = None
        self.p_list1_used[0] = True
        self.p_list1[1] = None
        self.p_list1_used[1] = True
        self.p_list1[2] = None
        self.p_list1_used[2] = True
        self.p_list1[3] = None
        self.p_list1_used[3] = True
        self.p_datalist = {}
        self.p_datalist_used = {}
        self.__pools.append("self.p_datalist")
        self.p_datalist[0] = None
        self.p_datalist_used[0] = True
        self.p_datalist[1] = None
        self.p_datalist_used[1] = True
        self.p_datalist[2] = None
        self.p_datalist_used[2] = True
        self.p_datalist[3] = None
        self.p_datalist_used[3] = True
        self.p_strtest = {}
        self.p_strtest_used = {}
        self.__pools.append("self.p_strtest")
        self.p_strtest[0] = None
        self.p_strtest_used[0] = True
        self.p_strtest[1] = None
        self.p_strtest_used[1] = True
        self.p_strtest[2] = None
        self.p_strtest_used[2] = True
        self.p_strtest[3] = None
        self.p_strtest_used[3] = True
        self.p_emptytuplemerging = {}
        self.p_emptytuplemerging_used = {}
        self.__pools.append("self.p_emptytuplemerging")
        self.p_emptytuplemerging[0] = None
        self.p_emptytuplemerging_used[0] = True
        self.p_emptytuplemerging[1] = None
        self.p_emptytuplemerging_used[1] = True
        self.p_emptytuplemerging[2] = None
        self.p_emptytuplemerging_used[2] = True
        self.p_emptytuplemerging[3] = None
        self.p_emptytuplemerging_used[3] = True
        self.p_listuples = {}
        self.p_listuples_used = {}
        self.__pools.append("self.p_listuples")
        self.p_listuples[0] = None
        self.p_listuples_used[0] = True
        self.p_listuples[1] = None
        self.p_listuples_used[1] = True
        self.p_listuples[2] = None
        self.p_listuples_used[2] = True
        self.p_listuples[3] = None
        self.p_listuples_used[3] = True
        self.p_exam1 = {}
        self.p_exam1_used = {}
        self.__pools.append("self.p_exam1")
        self.p_exam1[0] = None
        self.p_exam1_used[0] = True
        self.p_exam1[1] = None
        self.p_exam1_used[1] = True
        self.p_exam1[2] = None
        self.p_exam1_used[2] = True
        self.p_exam1[3] = None
        self.p_exam1_used[3] = True
        self.p_exam2 = {}
        self.p_exam2_used = {}
        self.__pools.append("self.p_exam2")
        self.p_exam2[0] = None
        self.p_exam2_used[0] = True
        self.p_exam2[1] = None
        self.p_exam2_used[1] = True
        self.p_exam2[2] = None
        self.p_exam2_used[2] = True
        self.p_exam2[3] = None
        self.p_exam2_used[3] = True
        self.p_addemptylistdicts = {}
        self.p_addemptylistdicts_used = {}
        self.__pools.append("self.p_addemptylistdicts")
        self.p_addemptylistdicts[0] = None
        self.p_addemptylistdicts_used[0] = True
        self.p_addemptylistdicts[1] = None
        self.p_addemptylistdicts_used[1] = True
        self.p_addemptylistdicts[2] = None
        self.p_addemptylistdicts_used[2] = True
        self.p_addemptylistdicts[3] = None
        self.p_addemptylistdicts_used[3] = True
        self.p_tuple = {}
        self.p_tuple_used = {}
        self.__pools.append("self.p_tuple")
        self.p_tuple[0] = None
        self.p_tuple_used[0] = True
        self.p_tuple[1] = None
        self.p_tuple_used[1] = True
        self.p_tuple[2] = None
        self.p_tuple_used[2] = True
        self.p_tuple[3] = None
        self.p_tuple_used[3] = True
        self.p_nestedlist = {}
        self.p_nestedlist_used = {}
        self.__pools.append("self.p_nestedlist")
        self.p_nestedlist[0] = None
        self.p_nestedlist_used[0] = True
        self.p_nestedlist[1] = None
        self.p_nestedlist_used[1] = True
        self.p_nestedlist[2] = None
        self.p_nestedlist_used[2] = True
        self.p_nestedlist[3] = None
        self.p_nestedlist_used[3] = True
        self.p_exams = {}
        self.p_exams_used = {}
        self.__pools.append("self.p_exams")
        self.p_exams[0] = None
        self.p_exams_used[0] = True
        self.p_exams[1] = None
        self.p_exams_used[1] = True
        self.p_exams[2] = None
        self.p_exams_used[2] = True
        self.p_exams[3] = None
        self.p_exams_used[3] = True
        self.p_deeplistnest = {}
        self.p_deeplistnest_used = {}
        self.__pools.append("self.p_deeplistnest")
        self.p_deeplistnest[0] = None
        self.p_deeplistnest_used[0] = True
        self.p_deeplistnest[1] = None
        self.p_deeplistnest_used[1] = True
        self.p_deeplistnest[2] = None
        self.p_deeplistnest_used[2] = True
        self.p_deeplistnest[3] = None
        self.p_deeplistnest_used[3] = True
        self.p_alist = {}
        self.p_alist_used = {}
        self.__pools.append("self.p_alist")
        self.p_alist[0] = None
        self.p_alist_used[0] = True
        self.p_alist[1] = None
        self.p_alist_used[1] = True
        self.p_alist[2] = None
        self.p_alist_used[2] = True
        self.p_alist[3] = None
        self.p_alist_used[3] = True
        self.p_noneinlist = {}
        self.p_noneinlist_used = {}
        self.__pools.append("self.p_noneinlist")
        self.p_noneinlist[0] = None
        self.p_noneinlist_used[0] = True
        self.p_noneinlist[1] = None
        self.p_noneinlist_used[1] = True
        self.p_noneinlist[2] = None
        self.p_noneinlist_used[2] = True
        self.p_noneinlist[3] = None
        self.p_noneinlist_used[3] = True
        self.p_strname = {}
        self.p_strname_used = {}
        self.__pools.append("self.p_strname")
        self.p_strname[0] = None
        self.p_strname_used[0] = True
        self.p_strname[1] = None
        self.p_strname_used[1] = True
        self.p_strname[2] = None
        self.p_strname_used[2] = True
        self.p_strname[3] = None
        self.p_strname_used[3] = True
        self.p_nesteddict = {}
        self.p_nesteddict_used = {}
        self.__pools.append("self.p_nesteddict")
        self.p_nesteddict[0] = None
        self.p_nesteddict_used[0] = True
        self.p_nesteddict[1] = None
        self.p_nesteddict_used[1] = True
        self.p_nesteddict[2] = None
        self.p_nesteddict_used[2] = True
        self.p_nesteddict[3] = None
        self.p_nesteddict_used[3] = True
        self.p_exam3 = {}
        self.p_exam3_used = {}
        self.__pools.append("self.p_exam3")
        self.p_exam3[0] = None
        self.p_exam3_used[0] = True
        self.p_exam3[1] = None
        self.p_exam3_used[1] = True
        self.p_exam3[2] = None
        self.p_exam3_used[2] = True
        self.p_exam3[3] = None
        self.p_exam3_used[3] = True
        self.p_incosistentdepth = {}
        self.p_incosistentdepth_used = {}
        self.__pools.append("self.p_incosistentdepth")
        self.p_incosistentdepth[0] = None
        self.p_incosistentdepth_used[0] = True
        self.p_incosistentdepth[1] = None
        self.p_incosistentdepth_used[1] = True
        self.p_incosistentdepth[2] = None
        self.p_incosistentdepth_used[2] = True
        self.p_incosistentdepth[3] = None
        self.p_incosistentdepth_used[3] = True
        self.p_nonekeydicts = {}
        self.p_nonekeydicts_used = {}
        self.__pools.append("self.p_nonekeydicts")
        self.p_nonekeydicts[0] = None
        self.p_nonekeydicts_used[0] = True
        self.p_nonekeydicts[1] = None
        self.p_nonekeydicts_used[1] = True
        self.p_nonekeydicts[2] = None
        self.p_nonekeydicts_used[2] = True
        self.p_nonekeydicts[3] = None
        self.p_nonekeydicts_used[3] = True
        self.p_alistmerge = {}
        self.p_alistmerge_used = {}
        self.__pools.append("self.p_alistmerge")
        self.p_alistmerge[0] = None
        self.p_alistmerge_used[0] = True
        self.p_alistmerge[1] = None
        self.p_alistmerge_used[1] = True
        self.p_alistmerge[2] = None
        self.p_alistmerge_used[2] = True
        self.p_alistmerge[3] = None
        self.p_alistmerge_used[3] = True
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
        self.__actions.append(('''self.p_strtest[0] =[] ''',self.guard0,self.act0))

        self.__names['''self.p_strtest[0] =[] '''] = ('''self.p_strtest[0] =[] ''',self.guard0,self.act0)

        self.__orderings['''self.p_strtest[0] =[] '''] = 1

        self.__okExcepts['''self.p_strtest[0] =[] '''] = ''''''

        self.__actions.append(('''self.p_strtest[1] =[] ''',self.guard1,self.act1))

        self.__names['''self.p_strtest[1] =[] '''] = ('''self.p_strtest[1] =[] ''',self.guard1,self.act1)

        self.__orderings['''self.p_strtest[1] =[] '''] = 2

        self.__okExcepts['''self.p_strtest[1] =[] '''] = ''''''

        self.__actions.append(('''self.p_strtest[2] =[] ''',self.guard2,self.act2))

        self.__names['''self.p_strtest[2] =[] '''] = ('''self.p_strtest[2] =[] ''',self.guard2,self.act2)

        self.__orderings['''self.p_strtest[2] =[] '''] = 3

        self.__okExcepts['''self.p_strtest[2] =[] '''] = ''''''

        self.__actions.append(('''self.p_strtest[0] +=[{'key1': 'val1'}] ''',self.guard3,self.act3))

        self.__names['''self.p_strtest[0] +=[{'key1': 'val1'}] '''] = ('''self.p_strtest[0] +=[{'key1': 'val1'}] ''',self.guard3,self.act3)

        self.__orderings['''self.p_strtest[0] +=[{'key1': 'val1'}] '''] = 4

        self.__okExcepts['''self.p_strtest[0] +=[{'key1': 'val1'}] '''] = ''''''

        self.__actions.append(('''self.p_strtest[1] +=[{'key1': 'val1'}] ''',self.guard4,self.act4))

        self.__names['''self.p_strtest[1] +=[{'key1': 'val1'}] '''] = ('''self.p_strtest[1] +=[{'key1': 'val1'}] ''',self.guard4,self.act4)

        self.__orderings['''self.p_strtest[1] +=[{'key1': 'val1'}] '''] = 5

        self.__okExcepts['''self.p_strtest[1] +=[{'key1': 'val1'}] '''] = ''''''

        self.__actions.append(('''self.p_strtest[2] +=[{'key1': 'val1'}] ''',self.guard5,self.act5))

        self.__names['''self.p_strtest[2] +=[{'key1': 'val1'}] '''] = ('''self.p_strtest[2] +=[{'key1': 'val1'}] ''',self.guard5,self.act5)

        self.__orderings['''self.p_strtest[2] +=[{'key1': 'val1'}] '''] = 6

        self.__okExcepts['''self.p_strtest[2] +=[{'key1': 'val1'}] '''] = ''''''

        self.__actions.append(('''self.p_strtest[0] +=['coding', 'snowboarding'] ''',self.guard6,self.act6))

        self.__names['''self.p_strtest[0] +=['coding', 'snowboarding'] '''] = ('''self.p_strtest[0] +=['coding', 'snowboarding'] ''',self.guard6,self.act6)

        self.__orderings['''self.p_strtest[0] +=['coding', 'snowboarding'] '''] = 7

        self.__okExcepts['''self.p_strtest[0] +=['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_strtest[1] +=['coding', 'snowboarding'] ''',self.guard7,self.act7))

        self.__names['''self.p_strtest[1] +=['coding', 'snowboarding'] '''] = ('''self.p_strtest[1] +=['coding', 'snowboarding'] ''',self.guard7,self.act7)

        self.__orderings['''self.p_strtest[1] +=['coding', 'snowboarding'] '''] = 8

        self.__okExcepts['''self.p_strtest[1] +=['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_strtest[2] +=['coding', 'snowboarding'] ''',self.guard8,self.act8))

        self.__names['''self.p_strtest[2] +=['coding', 'snowboarding'] '''] = ('''self.p_strtest[2] +=['coding', 'snowboarding'] ''',self.guard8,self.act8)

        self.__orderings['''self.p_strtest[2] +=['coding', 'snowboarding'] '''] = 9

        self.__okExcepts['''self.p_strtest[2] +=['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0]) ''',self.guard9,self.act9))

        self.__names['''print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0]) '''] = ('''print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0]) ''',self.guard9,self.act9)

        self.__orderings['''print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0]) '''] = 10

        self.__okExcepts['''print(self.p_strtest[0],self.p_strtest[0],self.p_strtest[0],self.p_strtest[0]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1]) ''',self.guard10,self.act10))

        self.__names['''print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1]) '''] = ('''print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1]) ''',self.guard10,self.act10)

        self.__orderings['''print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1]) '''] = 11

        self.__okExcepts['''print(self.p_strtest[0],self.p_strtest[1],self.p_strtest[0],self.p_strtest[1]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2]) ''',self.guard11,self.act11))

        self.__names['''print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2]) '''] = ('''print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2]) ''',self.guard11,self.act11)

        self.__orderings['''print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2]) '''] = 12

        self.__okExcepts['''print(self.p_strtest[0],self.p_strtest[2],self.p_strtest[0],self.p_strtest[2]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0]) ''',self.guard12,self.act12))

        self.__names['''print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0]) '''] = ('''print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0]) ''',self.guard12,self.act12)

        self.__orderings['''print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0]) '''] = 13

        self.__okExcepts['''print(self.p_strtest[1],self.p_strtest[0],self.p_strtest[1],self.p_strtest[0]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1]) ''',self.guard13,self.act13))

        self.__names['''print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1]) '''] = ('''print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1]) ''',self.guard13,self.act13)

        self.__orderings['''print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1]) '''] = 14

        self.__okExcepts['''print(self.p_strtest[1],self.p_strtest[1],self.p_strtest[1],self.p_strtest[1]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2]) ''',self.guard14,self.act14))

        self.__names['''print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2]) '''] = ('''print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2]) ''',self.guard14,self.act14)

        self.__orderings['''print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2]) '''] = 15

        self.__okExcepts['''print(self.p_strtest[1],self.p_strtest[2],self.p_strtest[1],self.p_strtest[2]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0]) ''',self.guard15,self.act15))

        self.__names['''print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0]) '''] = ('''print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0]) ''',self.guard15,self.act15)

        self.__orderings['''print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0]) '''] = 16

        self.__okExcepts['''print(self.p_strtest[2],self.p_strtest[0],self.p_strtest[2],self.p_strtest[0]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1]) ''',self.guard16,self.act16))

        self.__names['''print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1]) '''] = ('''print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1]) ''',self.guard16,self.act16)

        self.__orderings['''print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1]) '''] = 17

        self.__okExcepts['''print(self.p_strtest[2],self.p_strtest[1],self.p_strtest[2],self.p_strtest[1]) '''] = ''''''

        self.__actions.append(('''print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2]) ''',self.guard17,self.act17))

        self.__names['''print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2]) '''] = ('''print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2]) ''',self.guard17,self.act17)

        self.__orderings['''print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2]) '''] = 18

        self.__okExcepts['''print(self.p_strtest[2],self.p_strtest[2],self.p_strtest[2],self.p_strtest[2]) '''] = ''''''

        self.__actions.append(('''self.p_strname[0] = ['coding', 'snowboarding'] ''',self.guard18,self.act18))

        self.__names['''self.p_strname[0] = ['coding', 'snowboarding'] '''] = ('''self.p_strname[0] = ['coding', 'snowboarding'] ''',self.guard18,self.act18)

        self.__orderings['''self.p_strname[0] = ['coding', 'snowboarding'] '''] = 19

        self.__okExcepts['''self.p_strname[0] = ['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_strname[1] = ['coding', 'snowboarding'] ''',self.guard19,self.act19))

        self.__names['''self.p_strname[1] = ['coding', 'snowboarding'] '''] = ('''self.p_strname[1] = ['coding', 'snowboarding'] ''',self.guard19,self.act19)

        self.__orderings['''self.p_strname[1] = ['coding', 'snowboarding'] '''] = 20

        self.__okExcepts['''self.p_strname[1] = ['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_strname[2] = ['coding', 'snowboarding'] ''',self.guard20,self.act20))

        self.__names['''self.p_strname[2] = ['coding', 'snowboarding'] '''] = ('''self.p_strname[2] = ['coding', 'snowboarding'] ''',self.guard20,self.act20)

        self.__orderings['''self.p_strname[2] = ['coding', 'snowboarding'] '''] = 21

        self.__okExcepts['''self.p_strname[2] = ['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard21,self.act21))

        self.__names['''self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = ('''self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard21,self.act21)

        self.__orderings['''self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = 22

        self.__okExcepts['''self.p_list1[0] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = ''''''

        self.__actions.append(('''self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard22,self.act22))

        self.__names['''self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = ('''self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard22,self.act22)

        self.__orderings['''self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = 23

        self.__okExcepts['''self.p_list1[1] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = ''''''

        self.__actions.append(('''self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard23,self.act23))

        self.__names['''self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = ('''self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}] ''',self.guard23,self.act23)

        self.__orderings['''self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = 24

        self.__okExcepts['''self.p_list1[2] =[{'key1': 'val1'}, {'key2': 'val2'}] '''] = ''''''

        self.__actions.append(('''print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0]) ''',self.guard24,self.act24))

        self.__names['''print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0]) '''] = ('''print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0]) ''',self.guard24,self.act24)

        self.__orderings['''print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0]) '''] = 25

        self.__okExcepts['''print examine.Structure(self.p_list1[0]);examine.Structure(self.p_list1[0]) '''] = ''''''

        self.__actions.append(('''print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1]) ''',self.guard25,self.act25))

        self.__names['''print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1]) '''] = ('''print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1]) ''',self.guard25,self.act25)

        self.__orderings['''print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1]) '''] = 26

        self.__okExcepts['''print examine.Structure(self.p_list1[1]);examine.Structure(self.p_list1[1]) '''] = ''''''

        self.__actions.append(('''print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2]) ''',self.guard26,self.act26))

        self.__names['''print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2]) '''] = ('''print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2]) ''',self.guard26,self.act26)

        self.__orderings['''print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2]) '''] = 27

        self.__okExcepts['''print examine.Structure(self.p_list1[2]);examine.Structure(self.p_list1[2]) '''] = ''''''

        self.__actions.append(('''print (examine.Structure([None])).__add__(examine.Structure([])) ''',self.guard27,self.act27))

        self.__names['''print (examine.Structure([None])).__add__(examine.Structure([])) '''] = ('''print (examine.Structure([None])).__add__(examine.Structure([])) ''',self.guard27,self.act27)

        self.__orderings['''print (examine.Structure([None])).__add__(examine.Structure([])) '''] = 28

        self.__okExcepts['''print (examine.Structure([None])).__add__(examine.Structure([])) '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard28,self.act28))

        self.__names['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard28,self.act28)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]'] '''] = 29

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard29,self.act29))

        self.__names['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard29,self.act29)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]'] '''] = 30

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard30,self.act30))

        self.__names['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard30,self.act30)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]'] '''] = 31

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[0]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard31,self.act31))

        self.__names['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard31,self.act31)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]'] '''] = 32

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard32,self.act32))

        self.__names['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard32,self.act32)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]'] '''] = 33

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard33,self.act33))

        self.__names['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard33,self.act33)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]'] '''] = 34

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[1]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard34,self.act34))

        self.__names['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard34,self.act34)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]'] '''] = 35

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard35,self.act35))

        self.__names['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard35,self.act35)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]'] '''] = 36

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard36,self.act36))

        self.__names['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]'] '''] = ('''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard36,self.act36)

        self.__orderings['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]'] '''] = 37

        self.__okExcepts['''self.p_datalist[0] = ['self.p_list1[2]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard37,self.act37))

        self.__names['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard37,self.act37)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]'] '''] = 38

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard38,self.act38))

        self.__names['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard38,self.act38)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]'] '''] = 39

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard39,self.act39))

        self.__names['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard39,self.act39)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]'] '''] = 40

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[0]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard40,self.act40))

        self.__names['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard40,self.act40)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]'] '''] = 41

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard41,self.act41))

        self.__names['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard41,self.act41)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]'] '''] = 42

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard42,self.act42))

        self.__names['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard42,self.act42)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]'] '''] = 43

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[1]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard43,self.act43))

        self.__names['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard43,self.act43)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]'] '''] = 44

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard44,self.act44))

        self.__names['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard44,self.act44)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]'] '''] = 45

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard45,self.act45))

        self.__names['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]'] '''] = ('''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard45,self.act45)

        self.__orderings['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]'] '''] = 46

        self.__okExcepts['''self.p_datalist[1] = ['self.p_list1[2]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard46,self.act46))

        self.__names['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]'] ''',self.guard46,self.act46)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]'] '''] = 47

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard47,self.act47))

        self.__names['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]'] ''',self.guard47,self.act47)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]'] '''] = 48

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard48,self.act48))

        self.__names['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]'] ''',self.guard48,self.act48)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]'] '''] = 49

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[0]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard49,self.act49))

        self.__names['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]'] ''',self.guard49,self.act49)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]'] '''] = 50

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard50,self.act50))

        self.__names['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]'] ''',self.guard50,self.act50)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]'] '''] = 51

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard51,self.act51))

        self.__names['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]'] ''',self.guard51,self.act51)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]'] '''] = 52

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[1]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard52,self.act52))

        self.__names['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]'] ''',self.guard52,self.act52)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]'] '''] = 53

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[0]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard53,self.act53))

        self.__names['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]'] ''',self.guard53,self.act53)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]'] '''] = 54

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[1]'] '''] = ''''''

        self.__actions.append(('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard54,self.act54))

        self.__names['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]'] '''] = ('''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]'] ''',self.guard54,self.act54)

        self.__orderings['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]'] '''] = 55

        self.__okExcepts['''self.p_datalist[2] = ['self.p_list1[2]','self.p_strname[2]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[0] = ['self.p_list1[0]'] ''',self.guard55,self.act55))

        self.__names['''self.p_exams[0] = ['self.p_list1[0]'] '''] = ('''self.p_exams[0] = ['self.p_list1[0]'] ''',self.guard55,self.act55)

        self.__orderings['''self.p_exams[0] = ['self.p_list1[0]'] '''] = 56

        self.__okExcepts['''self.p_exams[0] = ['self.p_list1[0]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[0] = ['self.p_list1[1]'] ''',self.guard56,self.act56))

        self.__names['''self.p_exams[0] = ['self.p_list1[1]'] '''] = ('''self.p_exams[0] = ['self.p_list1[1]'] ''',self.guard56,self.act56)

        self.__orderings['''self.p_exams[0] = ['self.p_list1[1]'] '''] = 57

        self.__okExcepts['''self.p_exams[0] = ['self.p_list1[1]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[0] = ['self.p_list1[2]'] ''',self.guard57,self.act57))

        self.__names['''self.p_exams[0] = ['self.p_list1[2]'] '''] = ('''self.p_exams[0] = ['self.p_list1[2]'] ''',self.guard57,self.act57)

        self.__orderings['''self.p_exams[0] = ['self.p_list1[2]'] '''] = 58

        self.__okExcepts['''self.p_exams[0] = ['self.p_list1[2]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[1] = ['self.p_list1[0]'] ''',self.guard58,self.act58))

        self.__names['''self.p_exams[1] = ['self.p_list1[0]'] '''] = ('''self.p_exams[1] = ['self.p_list1[0]'] ''',self.guard58,self.act58)

        self.__orderings['''self.p_exams[1] = ['self.p_list1[0]'] '''] = 59

        self.__okExcepts['''self.p_exams[1] = ['self.p_list1[0]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[1] = ['self.p_list1[1]'] ''',self.guard59,self.act59))

        self.__names['''self.p_exams[1] = ['self.p_list1[1]'] '''] = ('''self.p_exams[1] = ['self.p_list1[1]'] ''',self.guard59,self.act59)

        self.__orderings['''self.p_exams[1] = ['self.p_list1[1]'] '''] = 60

        self.__okExcepts['''self.p_exams[1] = ['self.p_list1[1]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[1] = ['self.p_list1[2]'] ''',self.guard60,self.act60))

        self.__names['''self.p_exams[1] = ['self.p_list1[2]'] '''] = ('''self.p_exams[1] = ['self.p_list1[2]'] ''',self.guard60,self.act60)

        self.__orderings['''self.p_exams[1] = ['self.p_list1[2]'] '''] = 61

        self.__okExcepts['''self.p_exams[1] = ['self.p_list1[2]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[2] = ['self.p_list1[0]'] ''',self.guard61,self.act61))

        self.__names['''self.p_exams[2] = ['self.p_list1[0]'] '''] = ('''self.p_exams[2] = ['self.p_list1[0]'] ''',self.guard61,self.act61)

        self.__orderings['''self.p_exams[2] = ['self.p_list1[0]'] '''] = 62

        self.__okExcepts['''self.p_exams[2] = ['self.p_list1[0]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[2] = ['self.p_list1[1]'] ''',self.guard62,self.act62))

        self.__names['''self.p_exams[2] = ['self.p_list1[1]'] '''] = ('''self.p_exams[2] = ['self.p_list1[1]'] ''',self.guard62,self.act62)

        self.__orderings['''self.p_exams[2] = ['self.p_list1[1]'] '''] = 63

        self.__okExcepts['''self.p_exams[2] = ['self.p_list1[1]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[2] = ['self.p_list1[2]'] ''',self.guard63,self.act63))

        self.__names['''self.p_exams[2] = ['self.p_list1[2]'] '''] = ('''self.p_exams[2] = ['self.p_list1[2]'] ''',self.guard63,self.act63)

        self.__orderings['''self.p_exams[2] = ['self.p_list1[2]'] '''] = 64

        self.__okExcepts['''self.p_exams[2] = ['self.p_list1[2]'] '''] = ''''''

        self.__actions.append(('''self.p_exams[0].append(self.p_datalist[0]) ''',self.guard64,self.act64))

        self.__names['''self.p_exams[0].append(self.p_datalist[0]) '''] = ('''self.p_exams[0].append(self.p_datalist[0]) ''',self.guard64,self.act64)

        self.__orderings['''self.p_exams[0].append(self.p_datalist[0]) '''] = 65

        self.__okExcepts['''self.p_exams[0].append(self.p_datalist[0]) '''] = ''''''

        self.__actions.append(('''self.p_exams[0].append(self.p_datalist[1]) ''',self.guard65,self.act65))

        self.__names['''self.p_exams[0].append(self.p_datalist[1]) '''] = ('''self.p_exams[0].append(self.p_datalist[1]) ''',self.guard65,self.act65)

        self.__orderings['''self.p_exams[0].append(self.p_datalist[1]) '''] = 66

        self.__okExcepts['''self.p_exams[0].append(self.p_datalist[1]) '''] = ''''''

        self.__actions.append(('''self.p_exams[0].append(self.p_datalist[2]) ''',self.guard66,self.act66))

        self.__names['''self.p_exams[0].append(self.p_datalist[2]) '''] = ('''self.p_exams[0].append(self.p_datalist[2]) ''',self.guard66,self.act66)

        self.__orderings['''self.p_exams[0].append(self.p_datalist[2]) '''] = 67

        self.__okExcepts['''self.p_exams[0].append(self.p_datalist[2]) '''] = ''''''

        self.__actions.append(('''self.p_exams[1].append(self.p_datalist[0]) ''',self.guard67,self.act67))

        self.__names['''self.p_exams[1].append(self.p_datalist[0]) '''] = ('''self.p_exams[1].append(self.p_datalist[0]) ''',self.guard67,self.act67)

        self.__orderings['''self.p_exams[1].append(self.p_datalist[0]) '''] = 68

        self.__okExcepts['''self.p_exams[1].append(self.p_datalist[0]) '''] = ''''''

        self.__actions.append(('''self.p_exams[1].append(self.p_datalist[1]) ''',self.guard68,self.act68))

        self.__names['''self.p_exams[1].append(self.p_datalist[1]) '''] = ('''self.p_exams[1].append(self.p_datalist[1]) ''',self.guard68,self.act68)

        self.__orderings['''self.p_exams[1].append(self.p_datalist[1]) '''] = 69

        self.__okExcepts['''self.p_exams[1].append(self.p_datalist[1]) '''] = ''''''

        self.__actions.append(('''self.p_exams[1].append(self.p_datalist[2]) ''',self.guard69,self.act69))

        self.__names['''self.p_exams[1].append(self.p_datalist[2]) '''] = ('''self.p_exams[1].append(self.p_datalist[2]) ''',self.guard69,self.act69)

        self.__orderings['''self.p_exams[1].append(self.p_datalist[2]) '''] = 70

        self.__okExcepts['''self.p_exams[1].append(self.p_datalist[2]) '''] = ''''''

        self.__actions.append(('''self.p_exams[2].append(self.p_datalist[0]) ''',self.guard70,self.act70))

        self.__names['''self.p_exams[2].append(self.p_datalist[0]) '''] = ('''self.p_exams[2].append(self.p_datalist[0]) ''',self.guard70,self.act70)

        self.__orderings['''self.p_exams[2].append(self.p_datalist[0]) '''] = 71

        self.__okExcepts['''self.p_exams[2].append(self.p_datalist[0]) '''] = ''''''

        self.__actions.append(('''self.p_exams[2].append(self.p_datalist[1]) ''',self.guard71,self.act71))

        self.__names['''self.p_exams[2].append(self.p_datalist[1]) '''] = ('''self.p_exams[2].append(self.p_datalist[1]) ''',self.guard71,self.act71)

        self.__orderings['''self.p_exams[2].append(self.p_datalist[1]) '''] = 72

        self.__okExcepts['''self.p_exams[2].append(self.p_datalist[1]) '''] = ''''''

        self.__actions.append(('''self.p_exams[2].append(self.p_datalist[2]) ''',self.guard72,self.act72))

        self.__names['''self.p_exams[2].append(self.p_datalist[2]) '''] = ('''self.p_exams[2].append(self.p_datalist[2]) ''',self.guard72,self.act72)

        self.__orderings['''self.p_exams[2].append(self.p_datalist[2]) '''] = 73

        self.__okExcepts['''self.p_exams[2].append(self.p_datalist[2]) '''] = ''''''

        self.__actions.append(('''self.p_strname[0] = ['coding', 'snowboarding'] ''',self.guard73,self.act73))

        self.__names['''self.p_strname[0] = ['coding', 'snowboarding'] '''] = ('''self.p_strname[0] = ['coding', 'snowboarding'] ''',self.guard73,self.act73)

        self.__orderings['''self.p_strname[0] = ['coding', 'snowboarding'] '''] = 74

        self.__okExcepts['''self.p_strname[0] = ['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_strname[1] = ['coding', 'snowboarding'] ''',self.guard74,self.act74))

        self.__names['''self.p_strname[1] = ['coding', 'snowboarding'] '''] = ('''self.p_strname[1] = ['coding', 'snowboarding'] ''',self.guard74,self.act74)

        self.__orderings['''self.p_strname[1] = ['coding', 'snowboarding'] '''] = 75

        self.__okExcepts['''self.p_strname[1] = ['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_strname[2] = ['coding', 'snowboarding'] ''',self.guard75,self.act75))

        self.__names['''self.p_strname[2] = ['coding', 'snowboarding'] '''] = ('''self.p_strname[2] = ['coding', 'snowboarding'] ''',self.guard75,self.act75)

        self.__orderings['''self.p_strname[2] = ['coding', 'snowboarding'] '''] = 76

        self.__okExcepts['''self.p_strname[2] = ['coding', 'snowboarding'] '''] = ''''''

        self.__actions.append(('''self.p_exam1[0]= examine.Structure(self.p_strname[0]) ''',self.guard76,self.act76))

        self.__names['''self.p_exam1[0]= examine.Structure(self.p_strname[0]) '''] = ('''self.p_exam1[0]= examine.Structure(self.p_strname[0]) ''',self.guard76,self.act76)

        self.__orderings['''self.p_exam1[0]= examine.Structure(self.p_strname[0]) '''] = 77

        self.__okExcepts['''self.p_exam1[0]= examine.Structure(self.p_strname[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[0]= examine.Structure(self.p_strname[1]) ''',self.guard77,self.act77))

        self.__names['''self.p_exam1[0]= examine.Structure(self.p_strname[1]) '''] = ('''self.p_exam1[0]= examine.Structure(self.p_strname[1]) ''',self.guard77,self.act77)

        self.__orderings['''self.p_exam1[0]= examine.Structure(self.p_strname[1]) '''] = 78

        self.__okExcepts['''self.p_exam1[0]= examine.Structure(self.p_strname[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[0]= examine.Structure(self.p_strname[2]) ''',self.guard78,self.act78))

        self.__names['''self.p_exam1[0]= examine.Structure(self.p_strname[2]) '''] = ('''self.p_exam1[0]= examine.Structure(self.p_strname[2]) ''',self.guard78,self.act78)

        self.__orderings['''self.p_exam1[0]= examine.Structure(self.p_strname[2]) '''] = 79

        self.__okExcepts['''self.p_exam1[0]= examine.Structure(self.p_strname[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[1]= examine.Structure(self.p_strname[0]) ''',self.guard79,self.act79))

        self.__names['''self.p_exam1[1]= examine.Structure(self.p_strname[0]) '''] = ('''self.p_exam1[1]= examine.Structure(self.p_strname[0]) ''',self.guard79,self.act79)

        self.__orderings['''self.p_exam1[1]= examine.Structure(self.p_strname[0]) '''] = 80

        self.__okExcepts['''self.p_exam1[1]= examine.Structure(self.p_strname[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[1]= examine.Structure(self.p_strname[1]) ''',self.guard80,self.act80))

        self.__names['''self.p_exam1[1]= examine.Structure(self.p_strname[1]) '''] = ('''self.p_exam1[1]= examine.Structure(self.p_strname[1]) ''',self.guard80,self.act80)

        self.__orderings['''self.p_exam1[1]= examine.Structure(self.p_strname[1]) '''] = 81

        self.__okExcepts['''self.p_exam1[1]= examine.Structure(self.p_strname[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[1]= examine.Structure(self.p_strname[2]) ''',self.guard81,self.act81))

        self.__names['''self.p_exam1[1]= examine.Structure(self.p_strname[2]) '''] = ('''self.p_exam1[1]= examine.Structure(self.p_strname[2]) ''',self.guard81,self.act81)

        self.__orderings['''self.p_exam1[1]= examine.Structure(self.p_strname[2]) '''] = 82

        self.__okExcepts['''self.p_exam1[1]= examine.Structure(self.p_strname[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[2]= examine.Structure(self.p_strname[0]) ''',self.guard82,self.act82))

        self.__names['''self.p_exam1[2]= examine.Structure(self.p_strname[0]) '''] = ('''self.p_exam1[2]= examine.Structure(self.p_strname[0]) ''',self.guard82,self.act82)

        self.__orderings['''self.p_exam1[2]= examine.Structure(self.p_strname[0]) '''] = 83

        self.__okExcepts['''self.p_exam1[2]= examine.Structure(self.p_strname[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[2]= examine.Structure(self.p_strname[1]) ''',self.guard83,self.act83))

        self.__names['''self.p_exam1[2]= examine.Structure(self.p_strname[1]) '''] = ('''self.p_exam1[2]= examine.Structure(self.p_strname[1]) ''',self.guard83,self.act83)

        self.__orderings['''self.p_exam1[2]= examine.Structure(self.p_strname[1]) '''] = 84

        self.__okExcepts['''self.p_exam1[2]= examine.Structure(self.p_strname[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam1[2]= examine.Structure(self.p_strname[2]) ''',self.guard84,self.act84))

        self.__names['''self.p_exam1[2]= examine.Structure(self.p_strname[2]) '''] = ('''self.p_exam1[2]= examine.Structure(self.p_strname[2]) ''',self.guard84,self.act84)

        self.__orderings['''self.p_exam1[2]= examine.Structure(self.p_strname[2]) '''] = 85

        self.__okExcepts['''self.p_exam1[2]= examine.Structure(self.p_strname[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[0]= examine.Structure(self.p_list1[0]) ''',self.guard85,self.act85))

        self.__names['''self.p_exam2[0]= examine.Structure(self.p_list1[0]) '''] = ('''self.p_exam2[0]= examine.Structure(self.p_list1[0]) ''',self.guard85,self.act85)

        self.__orderings['''self.p_exam2[0]= examine.Structure(self.p_list1[0]) '''] = 86

        self.__okExcepts['''self.p_exam2[0]= examine.Structure(self.p_list1[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[0]= examine.Structure(self.p_list1[1]) ''',self.guard86,self.act86))

        self.__names['''self.p_exam2[0]= examine.Structure(self.p_list1[1]) '''] = ('''self.p_exam2[0]= examine.Structure(self.p_list1[1]) ''',self.guard86,self.act86)

        self.__orderings['''self.p_exam2[0]= examine.Structure(self.p_list1[1]) '''] = 87

        self.__okExcepts['''self.p_exam2[0]= examine.Structure(self.p_list1[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[0]= examine.Structure(self.p_list1[2]) ''',self.guard87,self.act87))

        self.__names['''self.p_exam2[0]= examine.Structure(self.p_list1[2]) '''] = ('''self.p_exam2[0]= examine.Structure(self.p_list1[2]) ''',self.guard87,self.act87)

        self.__orderings['''self.p_exam2[0]= examine.Structure(self.p_list1[2]) '''] = 88

        self.__okExcepts['''self.p_exam2[0]= examine.Structure(self.p_list1[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[1]= examine.Structure(self.p_list1[0]) ''',self.guard88,self.act88))

        self.__names['''self.p_exam2[1]= examine.Structure(self.p_list1[0]) '''] = ('''self.p_exam2[1]= examine.Structure(self.p_list1[0]) ''',self.guard88,self.act88)

        self.__orderings['''self.p_exam2[1]= examine.Structure(self.p_list1[0]) '''] = 89

        self.__okExcepts['''self.p_exam2[1]= examine.Structure(self.p_list1[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[1]= examine.Structure(self.p_list1[1]) ''',self.guard89,self.act89))

        self.__names['''self.p_exam2[1]= examine.Structure(self.p_list1[1]) '''] = ('''self.p_exam2[1]= examine.Structure(self.p_list1[1]) ''',self.guard89,self.act89)

        self.__orderings['''self.p_exam2[1]= examine.Structure(self.p_list1[1]) '''] = 90

        self.__okExcepts['''self.p_exam2[1]= examine.Structure(self.p_list1[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[1]= examine.Structure(self.p_list1[2]) ''',self.guard90,self.act90))

        self.__names['''self.p_exam2[1]= examine.Structure(self.p_list1[2]) '''] = ('''self.p_exam2[1]= examine.Structure(self.p_list1[2]) ''',self.guard90,self.act90)

        self.__orderings['''self.p_exam2[1]= examine.Structure(self.p_list1[2]) '''] = 91

        self.__okExcepts['''self.p_exam2[1]= examine.Structure(self.p_list1[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[2]= examine.Structure(self.p_list1[0]) ''',self.guard91,self.act91))

        self.__names['''self.p_exam2[2]= examine.Structure(self.p_list1[0]) '''] = ('''self.p_exam2[2]= examine.Structure(self.p_list1[0]) ''',self.guard91,self.act91)

        self.__orderings['''self.p_exam2[2]= examine.Structure(self.p_list1[0]) '''] = 92

        self.__okExcepts['''self.p_exam2[2]= examine.Structure(self.p_list1[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[2]= examine.Structure(self.p_list1[1]) ''',self.guard92,self.act92))

        self.__names['''self.p_exam2[2]= examine.Structure(self.p_list1[1]) '''] = ('''self.p_exam2[2]= examine.Structure(self.p_list1[1]) ''',self.guard92,self.act92)

        self.__orderings['''self.p_exam2[2]= examine.Structure(self.p_list1[1]) '''] = 93

        self.__okExcepts['''self.p_exam2[2]= examine.Structure(self.p_list1[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam2[2]= examine.Structure(self.p_list1[2]) ''',self.guard93,self.act93))

        self.__names['''self.p_exam2[2]= examine.Structure(self.p_list1[2]) '''] = ('''self.p_exam2[2]= examine.Structure(self.p_list1[2]) ''',self.guard93,self.act93)

        self.__orderings['''self.p_exam2[2]= examine.Structure(self.p_list1[2]) '''] = 94

        self.__okExcepts['''self.p_exam2[2]= examine.Structure(self.p_list1[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[0]= examine.Structure(self.p_exams[0]) ''',self.guard94,self.act94))

        self.__names['''self.p_exam3[0]= examine.Structure(self.p_exams[0]) '''] = ('''self.p_exam3[0]= examine.Structure(self.p_exams[0]) ''',self.guard94,self.act94)

        self.__orderings['''self.p_exam3[0]= examine.Structure(self.p_exams[0]) '''] = 95

        self.__okExcepts['''self.p_exam3[0]= examine.Structure(self.p_exams[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[0]= examine.Structure(self.p_exams[1]) ''',self.guard95,self.act95))

        self.__names['''self.p_exam3[0]= examine.Structure(self.p_exams[1]) '''] = ('''self.p_exam3[0]= examine.Structure(self.p_exams[1]) ''',self.guard95,self.act95)

        self.__orderings['''self.p_exam3[0]= examine.Structure(self.p_exams[1]) '''] = 96

        self.__okExcepts['''self.p_exam3[0]= examine.Structure(self.p_exams[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[0]= examine.Structure(self.p_exams[2]) ''',self.guard96,self.act96))

        self.__names['''self.p_exam3[0]= examine.Structure(self.p_exams[2]) '''] = ('''self.p_exam3[0]= examine.Structure(self.p_exams[2]) ''',self.guard96,self.act96)

        self.__orderings['''self.p_exam3[0]= examine.Structure(self.p_exams[2]) '''] = 97

        self.__okExcepts['''self.p_exam3[0]= examine.Structure(self.p_exams[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[1]= examine.Structure(self.p_exams[0]) ''',self.guard97,self.act97))

        self.__names['''self.p_exam3[1]= examine.Structure(self.p_exams[0]) '''] = ('''self.p_exam3[1]= examine.Structure(self.p_exams[0]) ''',self.guard97,self.act97)

        self.__orderings['''self.p_exam3[1]= examine.Structure(self.p_exams[0]) '''] = 98

        self.__okExcepts['''self.p_exam3[1]= examine.Structure(self.p_exams[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[1]= examine.Structure(self.p_exams[1]) ''',self.guard98,self.act98))

        self.__names['''self.p_exam3[1]= examine.Structure(self.p_exams[1]) '''] = ('''self.p_exam3[1]= examine.Structure(self.p_exams[1]) ''',self.guard98,self.act98)

        self.__orderings['''self.p_exam3[1]= examine.Structure(self.p_exams[1]) '''] = 99

        self.__okExcepts['''self.p_exam3[1]= examine.Structure(self.p_exams[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[1]= examine.Structure(self.p_exams[2]) ''',self.guard99,self.act99))

        self.__names['''self.p_exam3[1]= examine.Structure(self.p_exams[2]) '''] = ('''self.p_exam3[1]= examine.Structure(self.p_exams[2]) ''',self.guard99,self.act99)

        self.__orderings['''self.p_exam3[1]= examine.Structure(self.p_exams[2]) '''] = 100

        self.__okExcepts['''self.p_exam3[1]= examine.Structure(self.p_exams[2]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[2]= examine.Structure(self.p_exams[0]) ''',self.guard100,self.act100))

        self.__names['''self.p_exam3[2]= examine.Structure(self.p_exams[0]) '''] = ('''self.p_exam3[2]= examine.Structure(self.p_exams[0]) ''',self.guard100,self.act100)

        self.__orderings['''self.p_exam3[2]= examine.Structure(self.p_exams[0]) '''] = 101

        self.__okExcepts['''self.p_exam3[2]= examine.Structure(self.p_exams[0]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[2]= examine.Structure(self.p_exams[1]) ''',self.guard101,self.act101))

        self.__names['''self.p_exam3[2]= examine.Structure(self.p_exams[1]) '''] = ('''self.p_exam3[2]= examine.Structure(self.p_exams[1]) ''',self.guard101,self.act101)

        self.__orderings['''self.p_exam3[2]= examine.Structure(self.p_exams[1]) '''] = 102

        self.__okExcepts['''self.p_exam3[2]= examine.Structure(self.p_exams[1]) '''] = ''''''

        self.__actions.append(('''self.p_exam3[2]= examine.Structure(self.p_exams[2]) ''',self.guard102,self.act102))

        self.__names['''self.p_exam3[2]= examine.Structure(self.p_exams[2]) '''] = ('''self.p_exam3[2]= examine.Structure(self.p_exams[2]) ''',self.guard102,self.act102)

        self.__orderings['''self.p_exam3[2]= examine.Structure(self.p_exams[2]) '''] = 103

        self.__okExcepts['''self.p_exam3[2]= examine.Structure(self.p_exams[2]) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[0].__add__(self.p_exam3[0])) ''',self.guard103,self.act103))

        self.__names['''check(self.p_exam3[0].__add__(self.p_exam3[0])) '''] = ('''check(self.p_exam3[0].__add__(self.p_exam3[0])) ''',self.guard103,self.act103)

        self.__orderings['''check(self.p_exam3[0].__add__(self.p_exam3[0])) '''] = 104

        self.__okExcepts['''check(self.p_exam3[0].__add__(self.p_exam3[0])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[0].__add__(self.p_exam3[1])) ''',self.guard104,self.act104))

        self.__names['''check(self.p_exam3[0].__add__(self.p_exam3[1])) '''] = ('''check(self.p_exam3[0].__add__(self.p_exam3[1])) ''',self.guard104,self.act104)

        self.__orderings['''check(self.p_exam3[0].__add__(self.p_exam3[1])) '''] = 105

        self.__okExcepts['''check(self.p_exam3[0].__add__(self.p_exam3[1])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[0].__add__(self.p_exam3[2])) ''',self.guard105,self.act105))

        self.__names['''check(self.p_exam3[0].__add__(self.p_exam3[2])) '''] = ('''check(self.p_exam3[0].__add__(self.p_exam3[2])) ''',self.guard105,self.act105)

        self.__orderings['''check(self.p_exam3[0].__add__(self.p_exam3[2])) '''] = 106

        self.__okExcepts['''check(self.p_exam3[0].__add__(self.p_exam3[2])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[1].__add__(self.p_exam3[0])) ''',self.guard106,self.act106))

        self.__names['''check(self.p_exam3[1].__add__(self.p_exam3[0])) '''] = ('''check(self.p_exam3[1].__add__(self.p_exam3[0])) ''',self.guard106,self.act106)

        self.__orderings['''check(self.p_exam3[1].__add__(self.p_exam3[0])) '''] = 107

        self.__okExcepts['''check(self.p_exam3[1].__add__(self.p_exam3[0])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[1].__add__(self.p_exam3[1])) ''',self.guard107,self.act107))

        self.__names['''check(self.p_exam3[1].__add__(self.p_exam3[1])) '''] = ('''check(self.p_exam3[1].__add__(self.p_exam3[1])) ''',self.guard107,self.act107)

        self.__orderings['''check(self.p_exam3[1].__add__(self.p_exam3[1])) '''] = 108

        self.__okExcepts['''check(self.p_exam3[1].__add__(self.p_exam3[1])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[1].__add__(self.p_exam3[2])) ''',self.guard108,self.act108))

        self.__names['''check(self.p_exam3[1].__add__(self.p_exam3[2])) '''] = ('''check(self.p_exam3[1].__add__(self.p_exam3[2])) ''',self.guard108,self.act108)

        self.__orderings['''check(self.p_exam3[1].__add__(self.p_exam3[2])) '''] = 109

        self.__okExcepts['''check(self.p_exam3[1].__add__(self.p_exam3[2])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[2].__add__(self.p_exam3[0])) ''',self.guard109,self.act109))

        self.__names['''check(self.p_exam3[2].__add__(self.p_exam3[0])) '''] = ('''check(self.p_exam3[2].__add__(self.p_exam3[0])) ''',self.guard109,self.act109)

        self.__orderings['''check(self.p_exam3[2].__add__(self.p_exam3[0])) '''] = 110

        self.__okExcepts['''check(self.p_exam3[2].__add__(self.p_exam3[0])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[2].__add__(self.p_exam3[1])) ''',self.guard110,self.act110))

        self.__names['''check(self.p_exam3[2].__add__(self.p_exam3[1])) '''] = ('''check(self.p_exam3[2].__add__(self.p_exam3[1])) ''',self.guard110,self.act110)

        self.__orderings['''check(self.p_exam3[2].__add__(self.p_exam3[1])) '''] = 111

        self.__okExcepts['''check(self.p_exam3[2].__add__(self.p_exam3[1])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam3[2].__add__(self.p_exam3[2])) ''',self.guard111,self.act111))

        self.__names['''check(self.p_exam3[2].__add__(self.p_exam3[2])) '''] = ('''check(self.p_exam3[2].__add__(self.p_exam3[2])) ''',self.guard111,self.act111)

        self.__orderings['''check(self.p_exam3[2].__add__(self.p_exam3[2])) '''] = 112

        self.__okExcepts['''check(self.p_exam3[2].__add__(self.p_exam3[2])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[0].__add__(self.p_exam3[0])) ''',self.guard112,self.act112))

        self.__names['''check(self.p_exam1[0].__add__(self.p_exam3[0])) '''] = ('''check(self.p_exam1[0].__add__(self.p_exam3[0])) ''',self.guard112,self.act112)

        self.__orderings['''check(self.p_exam1[0].__add__(self.p_exam3[0])) '''] = 113

        self.__okExcepts['''check(self.p_exam1[0].__add__(self.p_exam3[0])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[0].__add__(self.p_exam3[1])) ''',self.guard113,self.act113))

        self.__names['''check(self.p_exam1[0].__add__(self.p_exam3[1])) '''] = ('''check(self.p_exam1[0].__add__(self.p_exam3[1])) ''',self.guard113,self.act113)

        self.__orderings['''check(self.p_exam1[0].__add__(self.p_exam3[1])) '''] = 114

        self.__okExcepts['''check(self.p_exam1[0].__add__(self.p_exam3[1])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[0].__add__(self.p_exam3[2])) ''',self.guard114,self.act114))

        self.__names['''check(self.p_exam1[0].__add__(self.p_exam3[2])) '''] = ('''check(self.p_exam1[0].__add__(self.p_exam3[2])) ''',self.guard114,self.act114)

        self.__orderings['''check(self.p_exam1[0].__add__(self.p_exam3[2])) '''] = 115

        self.__okExcepts['''check(self.p_exam1[0].__add__(self.p_exam3[2])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[1].__add__(self.p_exam3[0])) ''',self.guard115,self.act115))

        self.__names['''check(self.p_exam1[1].__add__(self.p_exam3[0])) '''] = ('''check(self.p_exam1[1].__add__(self.p_exam3[0])) ''',self.guard115,self.act115)

        self.__orderings['''check(self.p_exam1[1].__add__(self.p_exam3[0])) '''] = 116

        self.__okExcepts['''check(self.p_exam1[1].__add__(self.p_exam3[0])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[1].__add__(self.p_exam3[1])) ''',self.guard116,self.act116))

        self.__names['''check(self.p_exam1[1].__add__(self.p_exam3[1])) '''] = ('''check(self.p_exam1[1].__add__(self.p_exam3[1])) ''',self.guard116,self.act116)

        self.__orderings['''check(self.p_exam1[1].__add__(self.p_exam3[1])) '''] = 117

        self.__okExcepts['''check(self.p_exam1[1].__add__(self.p_exam3[1])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[1].__add__(self.p_exam3[2])) ''',self.guard117,self.act117))

        self.__names['''check(self.p_exam1[1].__add__(self.p_exam3[2])) '''] = ('''check(self.p_exam1[1].__add__(self.p_exam3[2])) ''',self.guard117,self.act117)

        self.__orderings['''check(self.p_exam1[1].__add__(self.p_exam3[2])) '''] = 118

        self.__okExcepts['''check(self.p_exam1[1].__add__(self.p_exam3[2])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[2].__add__(self.p_exam3[0])) ''',self.guard118,self.act118))

        self.__names['''check(self.p_exam1[2].__add__(self.p_exam3[0])) '''] = ('''check(self.p_exam1[2].__add__(self.p_exam3[0])) ''',self.guard118,self.act118)

        self.__orderings['''check(self.p_exam1[2].__add__(self.p_exam3[0])) '''] = 119

        self.__okExcepts['''check(self.p_exam1[2].__add__(self.p_exam3[0])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[2].__add__(self.p_exam3[1])) ''',self.guard119,self.act119))

        self.__names['''check(self.p_exam1[2].__add__(self.p_exam3[1])) '''] = ('''check(self.p_exam1[2].__add__(self.p_exam3[1])) ''',self.guard119,self.act119)

        self.__orderings['''check(self.p_exam1[2].__add__(self.p_exam3[1])) '''] = 120

        self.__okExcepts['''check(self.p_exam1[2].__add__(self.p_exam3[1])) '''] = ''''''

        self.__actions.append(('''check(self.p_exam1[2].__add__(self.p_exam3[2])) ''',self.guard120,self.act120))

        self.__names['''check(self.p_exam1[2].__add__(self.p_exam3[2])) '''] = ('''check(self.p_exam1[2].__add__(self.p_exam3[2])) ''',self.guard120,self.act120)

        self.__orderings['''check(self.p_exam1[2].__add__(self.p_exam3[2])) '''] = 121

        self.__okExcepts['''check(self.p_exam1[2].__add__(self.p_exam3[2])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure([])) ''',self.guard121,self.act121))

        self.__names['''print (examine.Structure([])) '''] = ('''print (examine.Structure([])) ''',self.guard121,self.act121)

        self.__orderings['''print (examine.Structure([])) '''] = 122

        self.__okExcepts['''print (examine.Structure([])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure({})) ''',self.guard122,self.act122))

        self.__names['''print (examine.Structure({})) '''] = ('''print (examine.Structure({})) ''',self.guard122,self.act122)

        self.__orderings['''print (examine.Structure({})) '''] = 123

        self.__okExcepts['''print (examine.Structure({})) '''] = ''''''

        self.__actions.append(('''self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard123,self.act123))

        self.__names['''self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}] '''] = ('''self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard123,self.act123)

        self.__orderings['''self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}] '''] = 124

        self.__okExcepts['''self.p_alist[0]= [{'list': [1, 2, 3]}, {'list': []}] '''] = ''''''

        self.__actions.append(('''self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard124,self.act124))

        self.__names['''self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}] '''] = ('''self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard124,self.act124)

        self.__orderings['''self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}] '''] = 125

        self.__okExcepts['''self.p_alist[1]= [{'list': [1, 2, 3]}, {'list': []}] '''] = ''''''

        self.__actions.append(('''self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard125,self.act125))

        self.__names['''self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}] '''] = ('''self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}] ''',self.guard125,self.act125)

        self.__orderings['''self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}] '''] = 126

        self.__okExcepts['''self.p_alist[2]= [{'list': [1, 2, 3]}, {'list': []}] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_alist[0])) ''',self.guard126,self.act126))

        self.__names['''print (examine.Structure(self.p_alist[0])) '''] = ('''print (examine.Structure(self.p_alist[0])) ''',self.guard126,self.act126)

        self.__orderings['''print (examine.Structure(self.p_alist[0])) '''] = 127

        self.__okExcepts['''print (examine.Structure(self.p_alist[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_alist[1])) ''',self.guard127,self.act127))

        self.__names['''print (examine.Structure(self.p_alist[1])) '''] = ('''print (examine.Structure(self.p_alist[1])) ''',self.guard127,self.act127)

        self.__orderings['''print (examine.Structure(self.p_alist[1])) '''] = 128

        self.__okExcepts['''print (examine.Structure(self.p_alist[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_alist[2])) ''',self.guard128,self.act128))

        self.__names['''print (examine.Structure(self.p_alist[2])) '''] = ('''print (examine.Structure(self.p_alist[2])) ''',self.guard128,self.act128)

        self.__orderings['''print (examine.Structure(self.p_alist[2])) '''] = 129

        self.__okExcepts['''print (examine.Structure(self.p_alist[2])) '''] = ''''''

        self.__actions.append(('''self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}] ''',self.guard129,self.act129))

        self.__names['''self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}] '''] = ('''self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}] ''',self.guard129,self.act129)

        self.__orderings['''self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}] '''] = 130

        self.__okExcepts['''self.p_alistmerge[0]= [{'list': []}, {'list': 'str'}] '''] = ''''''

        self.__actions.append(('''self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}] ''',self.guard130,self.act130))

        self.__names['''self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}] '''] = ('''self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}] ''',self.guard130,self.act130)

        self.__orderings['''self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}] '''] = 131

        self.__okExcepts['''self.p_alistmerge[1]= [{'list': []}, {'list': 'str'}] '''] = ''''''

        self.__actions.append(('''self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}] ''',self.guard131,self.act131))

        self.__names['''self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}] '''] = ('''self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}] ''',self.guard131,self.act131)

        self.__orderings['''self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}] '''] = 132

        self.__okExcepts['''self.p_alistmerge[2]= [{'list': []}, {'list': 'str'}] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_alistmerge[0])) ''',self.guard132,self.act132))

        self.__names['''print (examine.Structure(self.p_alistmerge[0])) '''] = ('''print (examine.Structure(self.p_alistmerge[0])) ''',self.guard132,self.act132)

        self.__orderings['''print (examine.Structure(self.p_alistmerge[0])) '''] = 133

        self.__okExcepts['''print (examine.Structure(self.p_alistmerge[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_alistmerge[1])) ''',self.guard133,self.act133))

        self.__names['''print (examine.Structure(self.p_alistmerge[1])) '''] = ('''print (examine.Structure(self.p_alistmerge[1])) ''',self.guard133,self.act133)

        self.__orderings['''print (examine.Structure(self.p_alistmerge[1])) '''] = 134

        self.__okExcepts['''print (examine.Structure(self.p_alistmerge[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_alistmerge[2])) ''',self.guard134,self.act134))

        self.__names['''print (examine.Structure(self.p_alistmerge[2])) '''] = ('''print (examine.Structure(self.p_alistmerge[2])) ''',self.guard134,self.act134)

        self.__orderings['''print (examine.Structure(self.p_alistmerge[2])) '''] = 135

        self.__okExcepts['''print (examine.Structure(self.p_alistmerge[2])) '''] = ''''''

        self.__actions.append(('''self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard135,self.act135))

        self.__names['''self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = ('''self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard135,self.act135)

        self.__orderings['''self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = 136

        self.__okExcepts['''self.p_nestedlist[0]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = ''''''

        self.__actions.append(('''self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard136,self.act136))

        self.__names['''self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = ('''self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard136,self.act136)

        self.__orderings['''self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = 137

        self.__okExcepts['''self.p_nestedlist[1]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = ''''''

        self.__actions.append(('''self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard137,self.act137))

        self.__names['''self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = ('''self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] ''',self.guard137,self.act137)

        self.__orderings['''self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = 138

        self.__okExcepts['''self.p_nestedlist[2]= [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9]]] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nestedlist[0])) ''',self.guard138,self.act138))

        self.__names['''print (examine.Structure(self.p_nestedlist[0])) '''] = ('''print (examine.Structure(self.p_nestedlist[0])) ''',self.guard138,self.act138)

        self.__orderings['''print (examine.Structure(self.p_nestedlist[0])) '''] = 139

        self.__okExcepts['''print (examine.Structure(self.p_nestedlist[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nestedlist[1])) ''',self.guard139,self.act139))

        self.__names['''print (examine.Structure(self.p_nestedlist[1])) '''] = ('''print (examine.Structure(self.p_nestedlist[1])) ''',self.guard139,self.act139)

        self.__orderings['''print (examine.Structure(self.p_nestedlist[1])) '''] = 140

        self.__okExcepts['''print (examine.Structure(self.p_nestedlist[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nestedlist[2])) ''',self.guard140,self.act140))

        self.__names['''print (examine.Structure(self.p_nestedlist[2])) '''] = ('''print (examine.Structure(self.p_nestedlist[2])) ''',self.guard140,self.act140)

        self.__orderings['''print (examine.Structure(self.p_nestedlist[2])) '''] = 141

        self.__okExcepts['''print (examine.Structure(self.p_nestedlist[2])) '''] = ''''''

        self.__actions.append(('''self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard141,self.act141))

        self.__names['''self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = ('''self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard141,self.act141)

        self.__orderings['''self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = 142

        self.__okExcepts['''self.p_incosistentdepth[0]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = ''''''

        self.__actions.append(('''self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard142,self.act142))

        self.__names['''self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = ('''self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard142,self.act142)

        self.__orderings['''self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = 143

        self.__okExcepts['''self.p_incosistentdepth[1]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = ''''''

        self.__actions.append(('''self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard143,self.act143))

        self.__names['''self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = ('''self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] ''',self.guard143,self.act143)

        self.__orderings['''self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = 144

        self.__okExcepts['''self.p_incosistentdepth[2]= [[1, 2, 3], [[4, 5, 6], [7, 8, 9]]] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_incosistentdepth[0])) ''',self.guard144,self.act144))

        self.__names['''print (examine.Structure(self.p_incosistentdepth[0])) '''] = ('''print (examine.Structure(self.p_incosistentdepth[0])) ''',self.guard144,self.act144)

        self.__orderings['''print (examine.Structure(self.p_incosistentdepth[0])) '''] = 145

        self.__okExcepts['''print (examine.Structure(self.p_incosistentdepth[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_incosistentdepth[1])) ''',self.guard145,self.act145))

        self.__names['''print (examine.Structure(self.p_incosistentdepth[1])) '''] = ('''print (examine.Structure(self.p_incosistentdepth[1])) ''',self.guard145,self.act145)

        self.__orderings['''print (examine.Structure(self.p_incosistentdepth[1])) '''] = 146

        self.__okExcepts['''print (examine.Structure(self.p_incosistentdepth[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_incosistentdepth[2])) ''',self.guard146,self.act146))

        self.__names['''print (examine.Structure(self.p_incosistentdepth[2])) '''] = ('''print (examine.Structure(self.p_incosistentdepth[2])) ''',self.guard146,self.act146)

        self.__orderings['''print (examine.Structure(self.p_incosistentdepth[2])) '''] = 147

        self.__okExcepts['''print (examine.Structure(self.p_incosistentdepth[2])) '''] = ''''''

        self.__actions.append(('''self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard147,self.act147))

        self.__names['''self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}} '''] = ('''self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard147,self.act147)

        self.__orderings['''self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}} '''] = 148

        self.__okExcepts['''self.p_nesteddict[0]= {'l1': {'l2': {'l3': 'val'}}} '''] = ''''''

        self.__actions.append(('''self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard148,self.act148))

        self.__names['''self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}} '''] = ('''self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard148,self.act148)

        self.__orderings['''self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}} '''] = 149

        self.__okExcepts['''self.p_nesteddict[1]= {'l1': {'l2': {'l3': 'val'}}} '''] = ''''''

        self.__actions.append(('''self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard149,self.act149))

        self.__names['''self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}} '''] = ('''self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}} ''',self.guard149,self.act149)

        self.__orderings['''self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}} '''] = 150

        self.__okExcepts['''self.p_nesteddict[2]= {'l1': {'l2': {'l3': 'val'}}} '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nesteddict[0])) ''',self.guard150,self.act150))

        self.__names['''print (examine.Structure(self.p_nesteddict[0])) '''] = ('''print (examine.Structure(self.p_nesteddict[0])) ''',self.guard150,self.act150)

        self.__orderings['''print (examine.Structure(self.p_nesteddict[0])) '''] = 151

        self.__okExcepts['''print (examine.Structure(self.p_nesteddict[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nesteddict[1])) ''',self.guard151,self.act151))

        self.__names['''print (examine.Structure(self.p_nesteddict[1])) '''] = ('''print (examine.Structure(self.p_nesteddict[1])) ''',self.guard151,self.act151)

        self.__orderings['''print (examine.Structure(self.p_nesteddict[1])) '''] = 152

        self.__okExcepts['''print (examine.Structure(self.p_nesteddict[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nesteddict[2])) ''',self.guard152,self.act152))

        self.__names['''print (examine.Structure(self.p_nesteddict[2])) '''] = ('''print (examine.Structure(self.p_nesteddict[2])) ''',self.guard152,self.act152)

        self.__orderings['''print (examine.Structure(self.p_nesteddict[2])) '''] = 153

        self.__okExcepts['''print (examine.Structure(self.p_nesteddict[2])) '''] = ''''''

        self.__actions.append(('''self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard153,self.act153))

        self.__names['''self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = ('''self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard153,self.act153)

        self.__orderings['''self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = 154

        self.__okExcepts['''self.p_addemptylistdicts[0]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = ''''''

        self.__actions.append(('''self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard154,self.act154))

        self.__names['''self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = ('''self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard154,self.act154)

        self.__orderings['''self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = 155

        self.__okExcepts['''self.p_addemptylistdicts[1]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = ''''''

        self.__actions.append(('''self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard155,self.act155))

        self.__names['''self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = ('''self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] ''',self.guard155,self.act155)

        self.__orderings['''self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = 156

        self.__okExcepts['''self.p_addemptylistdicts[2]= [{'key1': [{'subkey1': 'subval1', 'subkey2': 'subval2'}]},{'key1': []},{'key1': [{'subkey1': 'subval1'}]}] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_addemptylistdicts[0])) ''',self.guard156,self.act156))

        self.__names['''print (examine.Structure(self.p_addemptylistdicts[0])) '''] = ('''print (examine.Structure(self.p_addemptylistdicts[0])) ''',self.guard156,self.act156)

        self.__orderings['''print (examine.Structure(self.p_addemptylistdicts[0])) '''] = 157

        self.__okExcepts['''print (examine.Structure(self.p_addemptylistdicts[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_addemptylistdicts[1])) ''',self.guard157,self.act157))

        self.__names['''print (examine.Structure(self.p_addemptylistdicts[1])) '''] = ('''print (examine.Structure(self.p_addemptylistdicts[1])) ''',self.guard157,self.act157)

        self.__orderings['''print (examine.Structure(self.p_addemptylistdicts[1])) '''] = 158

        self.__okExcepts['''print (examine.Structure(self.p_addemptylistdicts[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_addemptylistdicts[2])) ''',self.guard158,self.act158))

        self.__names['''print (examine.Structure(self.p_addemptylistdicts[2])) '''] = ('''print (examine.Structure(self.p_addemptylistdicts[2])) ''',self.guard158,self.act158)

        self.__orderings['''print (examine.Structure(self.p_addemptylistdicts[2])) '''] = 159

        self.__okExcepts['''print (examine.Structure(self.p_addemptylistdicts[2])) '''] = ''''''

        self.__actions.append(('''self.p_noneinlist[0]=[1, 2, 3, None] ''',self.guard159,self.act159))

        self.__names['''self.p_noneinlist[0]=[1, 2, 3, None] '''] = ('''self.p_noneinlist[0]=[1, 2, 3, None] ''',self.guard159,self.act159)

        self.__orderings['''self.p_noneinlist[0]=[1, 2, 3, None] '''] = 160

        self.__okExcepts['''self.p_noneinlist[0]=[1, 2, 3, None] '''] = ''''''

        self.__actions.append(('''self.p_noneinlist[1]=[1, 2, 3, None] ''',self.guard160,self.act160))

        self.__names['''self.p_noneinlist[1]=[1, 2, 3, None] '''] = ('''self.p_noneinlist[1]=[1, 2, 3, None] ''',self.guard160,self.act160)

        self.__orderings['''self.p_noneinlist[1]=[1, 2, 3, None] '''] = 161

        self.__okExcepts['''self.p_noneinlist[1]=[1, 2, 3, None] '''] = ''''''

        self.__actions.append(('''self.p_noneinlist[2]=[1, 2, 3, None] ''',self.guard161,self.act161))

        self.__names['''self.p_noneinlist[2]=[1, 2, 3, None] '''] = ('''self.p_noneinlist[2]=[1, 2, 3, None] ''',self.guard161,self.act161)

        self.__orderings['''self.p_noneinlist[2]=[1, 2, 3, None] '''] = 162

        self.__okExcepts['''self.p_noneinlist[2]=[1, 2, 3, None] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_noneinlist[0])) ''',self.guard162,self.act162))

        self.__names['''print (examine.Structure(self.p_noneinlist[0])) '''] = ('''print (examine.Structure(self.p_noneinlist[0])) ''',self.guard162,self.act162)

        self.__orderings['''print (examine.Structure(self.p_noneinlist[0])) '''] = 163

        self.__okExcepts['''print (examine.Structure(self.p_noneinlist[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_noneinlist[1])) ''',self.guard163,self.act163))

        self.__names['''print (examine.Structure(self.p_noneinlist[1])) '''] = ('''print (examine.Structure(self.p_noneinlist[1])) ''',self.guard163,self.act163)

        self.__orderings['''print (examine.Structure(self.p_noneinlist[1])) '''] = 164

        self.__okExcepts['''print (examine.Structure(self.p_noneinlist[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_noneinlist[2])) ''',self.guard164,self.act164))

        self.__names['''print (examine.Structure(self.p_noneinlist[2])) '''] = ('''print (examine.Structure(self.p_noneinlist[2])) ''',self.guard164,self.act164)

        self.__orderings['''print (examine.Structure(self.p_noneinlist[2])) '''] = 165

        self.__okExcepts['''print (examine.Structure(self.p_noneinlist[2])) '''] = ''''''

        self.__actions.append(('''self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}] ''',self.guard165,self.act165))

        self.__names['''self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}] '''] = ('''self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}] ''',self.guard165,self.act165)

        self.__orderings['''self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}] '''] = 166

        self.__okExcepts['''self.p_nonekeydicts[0]= [{'key': 'val'}, {'key': None}] '''] = ''''''

        self.__actions.append(('''self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}] ''',self.guard166,self.act166))

        self.__names['''self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}] '''] = ('''self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}] ''',self.guard166,self.act166)

        self.__orderings['''self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}] '''] = 167

        self.__okExcepts['''self.p_nonekeydicts[1]= [{'key': 'val'}, {'key': None}] '''] = ''''''

        self.__actions.append(('''self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}] ''',self.guard167,self.act167))

        self.__names['''self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}] '''] = ('''self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}] ''',self.guard167,self.act167)

        self.__orderings['''self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}] '''] = 168

        self.__okExcepts['''self.p_nonekeydicts[2]= [{'key': 'val'}, {'key': None}] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nonekeydicts[0])) ''',self.guard168,self.act168))

        self.__names['''print (examine.Structure(self.p_nonekeydicts[0])) '''] = ('''print (examine.Structure(self.p_nonekeydicts[0])) ''',self.guard168,self.act168)

        self.__orderings['''print (examine.Structure(self.p_nonekeydicts[0])) '''] = 169

        self.__okExcepts['''print (examine.Structure(self.p_nonekeydicts[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nonekeydicts[1])) ''',self.guard169,self.act169))

        self.__names['''print (examine.Structure(self.p_nonekeydicts[1])) '''] = ('''print (examine.Structure(self.p_nonekeydicts[1])) ''',self.guard169,self.act169)

        self.__orderings['''print (examine.Structure(self.p_nonekeydicts[1])) '''] = 170

        self.__okExcepts['''print (examine.Structure(self.p_nonekeydicts[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_nonekeydicts[2])) ''',self.guard170,self.act170))

        self.__names['''print (examine.Structure(self.p_nonekeydicts[2])) '''] = ('''print (examine.Structure(self.p_nonekeydicts[2])) ''',self.guard170,self.act170)

        self.__orderings['''print (examine.Structure(self.p_nonekeydicts[2])) '''] = 171

        self.__okExcepts['''print (examine.Structure(self.p_nonekeydicts[2])) '''] = ''''''

        self.__actions.append(('''self.p_tuple[0]= ('string', 1) ''',self.guard171,self.act171))

        self.__names['''self.p_tuple[0]= ('string', 1) '''] = ('''self.p_tuple[0]= ('string', 1) ''',self.guard171,self.act171)

        self.__orderings['''self.p_tuple[0]= ('string', 1) '''] = 172

        self.__okExcepts['''self.p_tuple[0]= ('string', 1) '''] = ''''''

        self.__actions.append(('''self.p_tuple[1]= ('string', 1) ''',self.guard172,self.act172))

        self.__names['''self.p_tuple[1]= ('string', 1) '''] = ('''self.p_tuple[1]= ('string', 1) ''',self.guard172,self.act172)

        self.__orderings['''self.p_tuple[1]= ('string', 1) '''] = 173

        self.__okExcepts['''self.p_tuple[1]= ('string', 1) '''] = ''''''

        self.__actions.append(('''self.p_tuple[2]= ('string', 1) ''',self.guard173,self.act173))

        self.__names['''self.p_tuple[2]= ('string', 1) '''] = ('''self.p_tuple[2]= ('string', 1) ''',self.guard173,self.act173)

        self.__orderings['''self.p_tuple[2]= ('string', 1) '''] = 174

        self.__okExcepts['''self.p_tuple[2]= ('string', 1) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_tuple[0])) ''',self.guard174,self.act174))

        self.__names['''print (examine.Structure(self.p_tuple[0])) '''] = ('''print (examine.Structure(self.p_tuple[0])) ''',self.guard174,self.act174)

        self.__orderings['''print (examine.Structure(self.p_tuple[0])) '''] = 175

        self.__okExcepts['''print (examine.Structure(self.p_tuple[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_tuple[1])) ''',self.guard175,self.act175))

        self.__names['''print (examine.Structure(self.p_tuple[1])) '''] = ('''print (examine.Structure(self.p_tuple[1])) ''',self.guard175,self.act175)

        self.__orderings['''print (examine.Structure(self.p_tuple[1])) '''] = 176

        self.__okExcepts['''print (examine.Structure(self.p_tuple[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_tuple[2])) ''',self.guard176,self.act176))

        self.__names['''print (examine.Structure(self.p_tuple[2])) '''] = ('''print (examine.Structure(self.p_tuple[2])) ''',self.guard176,self.act176)

        self.__orderings['''print (examine.Structure(self.p_tuple[2])) '''] = 177

        self.__okExcepts['''print (examine.Structure(self.p_tuple[2])) '''] = ''''''

        self.__actions.append(('''self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []] ''',self.guard177,self.act177))

        self.__names['''self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []] '''] = ('''self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []] ''',self.guard177,self.act177)

        self.__orderings['''self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []] '''] = 178

        self.__okExcepts['''self.p_deeplistnest[0]= [[[1], []], [[], [1]], None, []] '''] = ''''''

        self.__actions.append(('''self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []] ''',self.guard178,self.act178))

        self.__names['''self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []] '''] = ('''self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []] ''',self.guard178,self.act178)

        self.__orderings['''self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []] '''] = 179

        self.__okExcepts['''self.p_deeplistnest[1]= [[[1], []], [[], [1]], None, []] '''] = ''''''

        self.__actions.append(('''self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []] ''',self.guard179,self.act179))

        self.__names['''self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []] '''] = ('''self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []] ''',self.guard179,self.act179)

        self.__orderings['''self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []] '''] = 180

        self.__okExcepts['''self.p_deeplistnest[2]= [[[1], []], [[], [1]], None, []] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_deeplistnest[0])) ''',self.guard180,self.act180))

        self.__names['''print (examine.Structure(self.p_deeplistnest[0])) '''] = ('''print (examine.Structure(self.p_deeplistnest[0])) ''',self.guard180,self.act180)

        self.__orderings['''print (examine.Structure(self.p_deeplistnest[0])) '''] = 181

        self.__okExcepts['''print (examine.Structure(self.p_deeplistnest[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_deeplistnest[1])) ''',self.guard181,self.act181))

        self.__names['''print (examine.Structure(self.p_deeplistnest[1])) '''] = ('''print (examine.Structure(self.p_deeplistnest[1])) ''',self.guard181,self.act181)

        self.__orderings['''print (examine.Structure(self.p_deeplistnest[1])) '''] = 182

        self.__okExcepts['''print (examine.Structure(self.p_deeplistnest[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_deeplistnest[2])) ''',self.guard182,self.act182))

        self.__names['''print (examine.Structure(self.p_deeplistnest[2])) '''] = ('''print (examine.Structure(self.p_deeplistnest[2])) ''',self.guard182,self.act182)

        self.__orderings['''print (examine.Structure(self.p_deeplistnest[2])) '''] = 183

        self.__okExcepts['''print (examine.Structure(self.p_deeplistnest[2])) '''] = ''''''

        self.__actions.append(('''self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard183,self.act183))

        self.__names['''self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')] '''] = ('''self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard183,self.act183)

        self.__orderings['''self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')] '''] = 184

        self.__okExcepts['''self.p_listuples[0]= [('str', None, []), ('str', 1, 2, 'over')] '''] = ''''''

        self.__actions.append(('''self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard184,self.act184))

        self.__names['''self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')] '''] = ('''self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard184,self.act184)

        self.__orderings['''self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')] '''] = 185

        self.__okExcepts['''self.p_listuples[1]= [('str', None, []), ('str', 1, 2, 'over')] '''] = ''''''

        self.__actions.append(('''self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard185,self.act185))

        self.__names['''self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')] '''] = ('''self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')] ''',self.guard185,self.act185)

        self.__orderings['''self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')] '''] = 186

        self.__okExcepts['''self.p_listuples[2]= [('str', None, []), ('str', 1, 2, 'over')] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_listuples[0])) ''',self.guard186,self.act186))

        self.__names['''print (examine.Structure(self.p_listuples[0])) '''] = ('''print (examine.Structure(self.p_listuples[0])) ''',self.guard186,self.act186)

        self.__orderings['''print (examine.Structure(self.p_listuples[0])) '''] = 187

        self.__okExcepts['''print (examine.Structure(self.p_listuples[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_listuples[1])) ''',self.guard187,self.act187))

        self.__names['''print (examine.Structure(self.p_listuples[1])) '''] = ('''print (examine.Structure(self.p_listuples[1])) ''',self.guard187,self.act187)

        self.__orderings['''print (examine.Structure(self.p_listuples[1])) '''] = 188

        self.__okExcepts['''print (examine.Structure(self.p_listuples[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_listuples[2])) ''',self.guard188,self.act188))

        self.__names['''print (examine.Structure(self.p_listuples[2])) '''] = ('''print (examine.Structure(self.p_listuples[2])) ''',self.guard188,self.act188)

        self.__orderings['''print (examine.Structure(self.p_listuples[2])) '''] = 189

        self.__okExcepts['''print (examine.Structure(self.p_listuples[2])) '''] = ''''''

        self.__actions.append(('''self.p_emptytuplemerging[0]= [tuple(), ('str', 1)] ''',self.guard189,self.act189))

        self.__names['''self.p_emptytuplemerging[0]= [tuple(), ('str', 1)] '''] = ('''self.p_emptytuplemerging[0]= [tuple(), ('str', 1)] ''',self.guard189,self.act189)

        self.__orderings['''self.p_emptytuplemerging[0]= [tuple(), ('str', 1)] '''] = 190

        self.__okExcepts['''self.p_emptytuplemerging[0]= [tuple(), ('str', 1)] '''] = ''''''

        self.__actions.append(('''self.p_emptytuplemerging[1]= [tuple(), ('str', 1)] ''',self.guard190,self.act190))

        self.__names['''self.p_emptytuplemerging[1]= [tuple(), ('str', 1)] '''] = ('''self.p_emptytuplemerging[1]= [tuple(), ('str', 1)] ''',self.guard190,self.act190)

        self.__orderings['''self.p_emptytuplemerging[1]= [tuple(), ('str', 1)] '''] = 191

        self.__okExcepts['''self.p_emptytuplemerging[1]= [tuple(), ('str', 1)] '''] = ''''''

        self.__actions.append(('''self.p_emptytuplemerging[2]= [tuple(), ('str', 1)] ''',self.guard191,self.act191))

        self.__names['''self.p_emptytuplemerging[2]= [tuple(), ('str', 1)] '''] = ('''self.p_emptytuplemerging[2]= [tuple(), ('str', 1)] ''',self.guard191,self.act191)

        self.__orderings['''self.p_emptytuplemerging[2]= [tuple(), ('str', 1)] '''] = 192

        self.__okExcepts['''self.p_emptytuplemerging[2]= [tuple(), ('str', 1)] '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_emptytuplemerging[0])) ''',self.guard192,self.act192))

        self.__names['''print (examine.Structure(self.p_emptytuplemerging[0])) '''] = ('''print (examine.Structure(self.p_emptytuplemerging[0])) ''',self.guard192,self.act192)

        self.__orderings['''print (examine.Structure(self.p_emptytuplemerging[0])) '''] = 193

        self.__okExcepts['''print (examine.Structure(self.p_emptytuplemerging[0])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_emptytuplemerging[1])) ''',self.guard193,self.act193))

        self.__names['''print (examine.Structure(self.p_emptytuplemerging[1])) '''] = ('''print (examine.Structure(self.p_emptytuplemerging[1])) ''',self.guard193,self.act193)

        self.__orderings['''print (examine.Structure(self.p_emptytuplemerging[1])) '''] = 194

        self.__okExcepts['''print (examine.Structure(self.p_emptytuplemerging[1])) '''] = ''''''

        self.__actions.append(('''print (examine.Structure(self.p_emptytuplemerging[2])) ''',self.guard194,self.act194))

        self.__names['''print (examine.Structure(self.p_emptytuplemerging[2])) '''] = ('''print (examine.Structure(self.p_emptytuplemerging[2])) ''',self.guard194,self.act194)

        self.__orderings['''print (examine.Structure(self.p_emptytuplemerging[2])) '''] = 195

        self.__okExcepts['''print (examine.Structure(self.p_emptytuplemerging[2])) '''] = ''''''

        self.__actions_backup = list(self.__actions)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
    # BEGIN RELOAD CODE
        reload(examine)
    # END RELOAD CODE
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_list1 = {}
        self.p_list1_used = {}
        self.__pools.append("self.p_list1")
        self.p_list1[0] = None
        self.p_list1_used[0] = True
        self.p_list1[1] = None
        self.p_list1_used[1] = True
        self.p_list1[2] = None
        self.p_list1_used[2] = True
        self.p_list1[3] = None
        self.p_list1_used[3] = True
        self.p_datalist = {}
        self.p_datalist_used = {}
        self.__pools.append("self.p_datalist")
        self.p_datalist[0] = None
        self.p_datalist_used[0] = True
        self.p_datalist[1] = None
        self.p_datalist_used[1] = True
        self.p_datalist[2] = None
        self.p_datalist_used[2] = True
        self.p_datalist[3] = None
        self.p_datalist_used[3] = True
        self.p_strtest = {}
        self.p_strtest_used = {}
        self.__pools.append("self.p_strtest")
        self.p_strtest[0] = None
        self.p_strtest_used[0] = True
        self.p_strtest[1] = None
        self.p_strtest_used[1] = True
        self.p_strtest[2] = None
        self.p_strtest_used[2] = True
        self.p_strtest[3] = None
        self.p_strtest_used[3] = True
        self.p_emptytuplemerging = {}
        self.p_emptytuplemerging_used = {}
        self.__pools.append("self.p_emptytuplemerging")
        self.p_emptytuplemerging[0] = None
        self.p_emptytuplemerging_used[0] = True
        self.p_emptytuplemerging[1] = None
        self.p_emptytuplemerging_used[1] = True
        self.p_emptytuplemerging[2] = None
        self.p_emptytuplemerging_used[2] = True
        self.p_emptytuplemerging[3] = None
        self.p_emptytuplemerging_used[3] = True
        self.p_listuples = {}
        self.p_listuples_used = {}
        self.__pools.append("self.p_listuples")
        self.p_listuples[0] = None
        self.p_listuples_used[0] = True
        self.p_listuples[1] = None
        self.p_listuples_used[1] = True
        self.p_listuples[2] = None
        self.p_listuples_used[2] = True
        self.p_listuples[3] = None
        self.p_listuples_used[3] = True
        self.p_exam1 = {}
        self.p_exam1_used = {}
        self.__pools.append("self.p_exam1")
        self.p_exam1[0] = None
        self.p_exam1_used[0] = True
        self.p_exam1[1] = None
        self.p_exam1_used[1] = True
        self.p_exam1[2] = None
        self.p_exam1_used[2] = True
        self.p_exam1[3] = None
        self.p_exam1_used[3] = True
        self.p_exam2 = {}
        self.p_exam2_used = {}
        self.__pools.append("self.p_exam2")
        self.p_exam2[0] = None
        self.p_exam2_used[0] = True
        self.p_exam2[1] = None
        self.p_exam2_used[1] = True
        self.p_exam2[2] = None
        self.p_exam2_used[2] = True
        self.p_exam2[3] = None
        self.p_exam2_used[3] = True
        self.p_addemptylistdicts = {}
        self.p_addemptylistdicts_used = {}
        self.__pools.append("self.p_addemptylistdicts")
        self.p_addemptylistdicts[0] = None
        self.p_addemptylistdicts_used[0] = True
        self.p_addemptylistdicts[1] = None
        self.p_addemptylistdicts_used[1] = True
        self.p_addemptylistdicts[2] = None
        self.p_addemptylistdicts_used[2] = True
        self.p_addemptylistdicts[3] = None
        self.p_addemptylistdicts_used[3] = True
        self.p_tuple = {}
        self.p_tuple_used = {}
        self.__pools.append("self.p_tuple")
        self.p_tuple[0] = None
        self.p_tuple_used[0] = True
        self.p_tuple[1] = None
        self.p_tuple_used[1] = True
        self.p_tuple[2] = None
        self.p_tuple_used[2] = True
        self.p_tuple[3] = None
        self.p_tuple_used[3] = True
        self.p_nestedlist = {}
        self.p_nestedlist_used = {}
        self.__pools.append("self.p_nestedlist")
        self.p_nestedlist[0] = None
        self.p_nestedlist_used[0] = True
        self.p_nestedlist[1] = None
        self.p_nestedlist_used[1] = True
        self.p_nestedlist[2] = None
        self.p_nestedlist_used[2] = True
        self.p_nestedlist[3] = None
        self.p_nestedlist_used[3] = True
        self.p_exams = {}
        self.p_exams_used = {}
        self.__pools.append("self.p_exams")
        self.p_exams[0] = None
        self.p_exams_used[0] = True
        self.p_exams[1] = None
        self.p_exams_used[1] = True
        self.p_exams[2] = None
        self.p_exams_used[2] = True
        self.p_exams[3] = None
        self.p_exams_used[3] = True
        self.p_deeplistnest = {}
        self.p_deeplistnest_used = {}
        self.__pools.append("self.p_deeplistnest")
        self.p_deeplistnest[0] = None
        self.p_deeplistnest_used[0] = True
        self.p_deeplistnest[1] = None
        self.p_deeplistnest_used[1] = True
        self.p_deeplistnest[2] = None
        self.p_deeplistnest_used[2] = True
        self.p_deeplistnest[3] = None
        self.p_deeplistnest_used[3] = True
        self.p_alist = {}
        self.p_alist_used = {}
        self.__pools.append("self.p_alist")
        self.p_alist[0] = None
        self.p_alist_used[0] = True
        self.p_alist[1] = None
        self.p_alist_used[1] = True
        self.p_alist[2] = None
        self.p_alist_used[2] = True
        self.p_alist[3] = None
        self.p_alist_used[3] = True
        self.p_noneinlist = {}
        self.p_noneinlist_used = {}
        self.__pools.append("self.p_noneinlist")
        self.p_noneinlist[0] = None
        self.p_noneinlist_used[0] = True
        self.p_noneinlist[1] = None
        self.p_noneinlist_used[1] = True
        self.p_noneinlist[2] = None
        self.p_noneinlist_used[2] = True
        self.p_noneinlist[3] = None
        self.p_noneinlist_used[3] = True
        self.p_strname = {}
        self.p_strname_used = {}
        self.__pools.append("self.p_strname")
        self.p_strname[0] = None
        self.p_strname_used[0] = True
        self.p_strname[1] = None
        self.p_strname_used[1] = True
        self.p_strname[2] = None
        self.p_strname_used[2] = True
        self.p_strname[3] = None
        self.p_strname_used[3] = True
        self.p_nesteddict = {}
        self.p_nesteddict_used = {}
        self.__pools.append("self.p_nesteddict")
        self.p_nesteddict[0] = None
        self.p_nesteddict_used[0] = True
        self.p_nesteddict[1] = None
        self.p_nesteddict_used[1] = True
        self.p_nesteddict[2] = None
        self.p_nesteddict_used[2] = True
        self.p_nesteddict[3] = None
        self.p_nesteddict_used[3] = True
        self.p_exam3 = {}
        self.p_exam3_used = {}
        self.__pools.append("self.p_exam3")
        self.p_exam3[0] = None
        self.p_exam3_used[0] = True
        self.p_exam3[1] = None
        self.p_exam3_used[1] = True
        self.p_exam3[2] = None
        self.p_exam3_used[2] = True
        self.p_exam3[3] = None
        self.p_exam3_used[3] = True
        self.p_incosistentdepth = {}
        self.p_incosistentdepth_used = {}
        self.__pools.append("self.p_incosistentdepth")
        self.p_incosistentdepth[0] = None
        self.p_incosistentdepth_used[0] = True
        self.p_incosistentdepth[1] = None
        self.p_incosistentdepth_used[1] = True
        self.p_incosistentdepth[2] = None
        self.p_incosistentdepth_used[2] = True
        self.p_incosistentdepth[3] = None
        self.p_incosistentdepth_used[3] = True
        self.p_nonekeydicts = {}
        self.p_nonekeydicts_used = {}
        self.__pools.append("self.p_nonekeydicts")
        self.p_nonekeydicts[0] = None
        self.p_nonekeydicts_used[0] = True
        self.p_nonekeydicts[1] = None
        self.p_nonekeydicts_used[1] = True
        self.p_nonekeydicts[2] = None
        self.p_nonekeydicts_used[2] = True
        self.p_nonekeydicts[3] = None
        self.p_nonekeydicts_used[3] = True
        self.p_alistmerge = {}
        self.p_alistmerge_used = {}
        self.__pools.append("self.p_alistmerge")
        self.p_alistmerge[0] = None
        self.p_alistmerge_used[0] = True
        self.p_alistmerge[1] = None
        self.p_alistmerge_used[1] = True
        self.p_alistmerge[2] = None
        self.p_alistmerge_used[2] = True
        self.p_alistmerge[3] = None
        self.p_alistmerge_used[3] = True
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
        return [ copy.deepcopy(self.p_list1),copy.deepcopy(self.p_list1_used),copy.deepcopy(self.p_datalist),copy.deepcopy(self.p_datalist_used),copy.deepcopy(self.p_strtest),copy.deepcopy(self.p_strtest_used),copy.deepcopy(self.p_emptytuplemerging),copy.deepcopy(self.p_emptytuplemerging_used),copy.deepcopy(self.p_listuples),copy.deepcopy(self.p_listuples_used),copy.deepcopy(self.p_exam1),copy.deepcopy(self.p_exam1_used),copy.deepcopy(self.p_exam2),copy.deepcopy(self.p_exam2_used),copy.deepcopy(self.p_addemptylistdicts),copy.deepcopy(self.p_addemptylistdicts_used),copy.deepcopy(self.p_tuple),copy.deepcopy(self.p_tuple_used),copy.deepcopy(self.p_nestedlist),copy.deepcopy(self.p_nestedlist_used),copy.deepcopy(self.p_exams),copy.deepcopy(self.p_exams_used),copy.deepcopy(self.p_deeplistnest),copy.deepcopy(self.p_deeplistnest_used),copy.deepcopy(self.p_alist),copy.deepcopy(self.p_alist_used),copy.deepcopy(self.p_noneinlist),copy.deepcopy(self.p_noneinlist_used),copy.deepcopy(self.p_strname),copy.deepcopy(self.p_strname_used),copy.deepcopy(self.p_nesteddict),copy.deepcopy(self.p_nesteddict_used),copy.deepcopy(self.p_exam3),copy.deepcopy(self.p_exam3_used),copy.deepcopy(self.p_incosistentdepth),copy.deepcopy(self.p_incosistentdepth_used),copy.deepcopy(self.p_nonekeydicts),copy.deepcopy(self.p_nonekeydicts_used),copy.deepcopy(self.p_alistmerge),copy.deepcopy(self.p_alistmerge_used)]
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_list1 = copy.deepcopy(old[0])
        self.p_list1_used = copy.deepcopy(old[1])
        self.p_datalist = copy.deepcopy(old[2])
        self.p_datalist_used = copy.deepcopy(old[3])
        self.p_strtest = copy.deepcopy(old[4])
        self.p_strtest_used = copy.deepcopy(old[5])
        self.p_emptytuplemerging = copy.deepcopy(old[6])
        self.p_emptytuplemerging_used = copy.deepcopy(old[7])
        self.p_listuples = copy.deepcopy(old[8])
        self.p_listuples_used = copy.deepcopy(old[9])
        self.p_exam1 = copy.deepcopy(old[10])
        self.p_exam1_used = copy.deepcopy(old[11])
        self.p_exam2 = copy.deepcopy(old[12])
        self.p_exam2_used = copy.deepcopy(old[13])
        self.p_addemptylistdicts = copy.deepcopy(old[14])
        self.p_addemptylistdicts_used = copy.deepcopy(old[15])
        self.p_tuple = copy.deepcopy(old[16])
        self.p_tuple_used = copy.deepcopy(old[17])
        self.p_nestedlist = copy.deepcopy(old[18])
        self.p_nestedlist_used = copy.deepcopy(old[19])
        self.p_exams = copy.deepcopy(old[20])
        self.p_exams_used = copy.deepcopy(old[21])
        self.p_deeplistnest = copy.deepcopy(old[22])
        self.p_deeplistnest_used = copy.deepcopy(old[23])
        self.p_alist = copy.deepcopy(old[24])
        self.p_alist_used = copy.deepcopy(old[25])
        self.p_noneinlist = copy.deepcopy(old[26])
        self.p_noneinlist_used = copy.deepcopy(old[27])
        self.p_strname = copy.deepcopy(old[28])
        self.p_strname_used = copy.deepcopy(old[29])
        self.p_nesteddict = copy.deepcopy(old[30])
        self.p_nesteddict_used = copy.deepcopy(old[31])
        self.p_exam3 = copy.deepcopy(old[32])
        self.p_exam3_used = copy.deepcopy(old[33])
        self.p_incosistentdepth = copy.deepcopy(old[34])
        self.p_incosistentdepth_used = copy.deepcopy(old[35])
        self.p_nonekeydicts = copy.deepcopy(old[36])
        self.p_nonekeydicts_used = copy.deepcopy(old[37])
        self.p_alistmerge = copy.deepcopy(old[38])
        self.p_alistmerge_used = copy.deepcopy(old[39])
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
