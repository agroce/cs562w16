import copy
import traceback
import re
import sys
from itertools import chain, combinations
# BEGIN STANDALONE CODE
from skiplist import SortedDict as CSort
from sortedcontainers import SortedDict as PSort
import time
import random
import csv

def genString2(strSize):
	s = ''
	length = random.randint(0, strSize)			
	while (len(s) < length):
		s = s + chr(random.randint(0, 255))
	return s
	
def genString(strSize):
	s = ''	
	while (len(s) < strSize):
		s = s + chr(random.randint(0, 255))
	return s
	

def genMulDict(low, high, size, strSize):
	d = {}
	flag = random.randint(0,3)
	while (len(d) < size):
		if (flag == 0):
			d[genString(strSize)] = genString(strSize)
		elif (flag == 1):
			d[random.randint(low, high)] = genString(strSize)
		elif (flag == 2):
			d[genString(strSize)] = random.randint(low, high)
		else:
			d[random.randint(low, high)] = random.randint(low, high)
	return d

def genNumDict(low, high, size):
	d = {}
	while (len(d) < size):
		d[random.randint(low, high)] = random.randint(low, high)
	return d
	
def genStrDict(high, size, strSize):
	d = {}
	while (len(d) < size):
		d[genString(strSize)] = genString(strSize)
	return d
		
def testCSortDict(dict):
	dura = time.time()
	CSort(dict)
	dura = time.time() - dura
	return dura
	
def testPSortDict(dict):
	dura = time.time()
	PSort(dict)
	dura = time.time() - dura
	return dura

def EqualResult(dict):
	c = CSort(dict)
	p = PSort(dict)
	if (c == p):
		return True
	else:
		return False
		
def outputResult(cdura, pdura, dict, size, strsize, result):
	f = file('dura.csv', 'ab')
	writer = csv.writer(f)
	writer.writerow([cdura, pdura, size, strsize, dict, result])
	f.close()

# END STANDALONE CODE
class sut(object):
    def act0(self):
        self.__test.append(('''self.p_dict[0]		= {} ''',self.guard0,self.act0))
        try:
            self.p_dict[0]		= {}

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_dict_used[0]=False
    def guard0(self):
        return (((self.p_dict_used[0]) or (self.p_dict[0] == None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        self.__test.append(('''self.p_size[0]		= 10 ''',self.guard1,self.act1))
        try:
            self.p_size[0]		= 10

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard1(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        self.__test.append(('''self.p_size[0]		=  20 ''',self.guard2,self.act2))
        try:
            self.p_size[0]		=  20

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard2(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        self.__test.append(('''self.p_size[0]		=  30 ''',self.guard3,self.act3))
        try:
            self.p_size[0]		=  30

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard3(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act4(self):
        self.__test.append(('''self.p_size[0]		=  50 ''',self.guard4,self.act4))
        try:
            self.p_size[0]		=  50

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard4(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act5(self):
        self.__test.append(('''self.p_size[0]		=  100 ''',self.guard5,self.act5))
        try:
            self.p_size[0]		=  100

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard5(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act6(self):
        self.__test.append(('''self.p_size[0]		=  150 ''',self.guard6,self.act6))
        try:
            self.p_size[0]		=  150

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard6(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act7(self):
        self.__test.append(('''self.p_size[0]		=  200 ''',self.guard7,self.act7))
        try:
            self.p_size[0]		=  200

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=False
    def guard7(self):
        return (((self.p_size_used[0]) or (self.p_size[0] == None) or (self.__relaxUsedRestriction)))
    
    def act8(self):
        self.__test.append(('''self.p_strsize[0]	= 400 ''',self.guard8,self.act8))
        try:
            self.p_strsize[0]	= 400

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_strsize_used[0]=False
    def guard8(self):
        return (((self.p_strsize_used[0]) or (self.p_strsize[0] == None) or (self.__relaxUsedRestriction)))
    
    def act9(self):
        self.__test.append(('''self.p_high[0]		= 1000 ''',self.guard9,self.act9))
        try:
            self.p_high[0]		= 1000

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_high_used[0]=False
    def guard9(self):
        return (((self.p_high_used[0]) or (self.p_high[0] == None) or (self.__relaxUsedRestriction)))
    
    def act10(self):
        self.__test.append(('''self.p_low[0]		= -1000 ''',self.guard10,self.act10))
        try:
            self.p_low[0]		= -1000

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_low_used[0]=False
    def guard10(self):
        return (((self.p_low_used[0]) or (self.p_low[0] == None) or (self.__relaxUsedRestriction)))
    
    def act11(self):
        self.__test.append(('''self.p_cdura[0]		= 0.0 ''',self.guard11,self.act11))
        try:
            self.p_cdura[0]		= 0.0

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_cdura_used[0]=False
    def guard11(self):
        return (((self.p_cdura_used[0]) or (self.p_cdura[0] == None) or (self.__relaxUsedRestriction)))
    
    def act12(self):
        self.__test.append(('''self.p_pdura[0]		= 0.0 ''',self.guard12,self.act12))
        try:
            self.p_pdura[0]		= 0.0

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_pdura_used[0]=False
    def guard12(self):
        return (((self.p_pdura_used[0]) or (self.p_pdura[0] == None) or (self.__relaxUsedRestriction)))
    
    def act13(self):
        self.__test.append(('''self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	 ''',self.guard13,self.act13))
        try:
            self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_size_used[0]=True
        self.p_dict_used[0]=True
        self.p_low_used[0]=True
        self.p_high_used[0]=True
        self.p_strsize_used[0]=True
    def guard13(self):
        return (self.p_size[0] != None) and (self.p_dict[0] != None) and (self.p_low[0] != None) and (self.p_high[0] != None) and (self.p_strsize[0] != None)
    
    def act14(self):
        self.__test.append(('''flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag); ''',self.guard14,self.act14))
        try:
            flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag);

        finally:
            try:
                test_after_each(self)
            except:
                pass
        self.p_cdura_used[0]=True
        self.p_cdura_used[0]=True
        self.p_cdura_used[0]=True
        self.p_size_used[0]=True
        self.p_size_used[0]=True
        self.p_size_used[0]=True
        self.p_size_used[0]=True
        self.p_pdura_used[0]=True
        self.p_pdura_used[0]=True
        self.p_pdura_used[0]=True
        self.p_dict_used[0]=True
        self.p_dict_used[0]=True
        self.p_dict_used[0]=True
        self.p_dict_used[0]=True
        self.p_dict_used[0]=True
        self.p_dict_used[0]=True
        self.p_strsize_used[0]=True
    def guard14(self):
        return (self.p_cdura[0] != None) and (self.p_cdura[0] != None) and (self.p_cdura[0] != None) and (self.p_size[0] != None) and (self.p_size[0] != None) and (self.p_size[0] != None) and (self.p_size[0] != None) and (self.p_pdura[0] != None) and (self.p_pdura[0] != None) and (self.p_pdura[0] != None) and (self.p_dict[0] != None) and (self.p_dict[0] != None) and (self.p_dict[0] != None) and (self.p_dict[0] != None) and (self.p_dict[0] != None) and (self.p_dict[0] != None) and (self.p_strsize[0] != None) and (len(self.p_dict[0]) == self.p_size[0])
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__features = []
        self.__replayBacktrack = False
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_cdura = {}
        self.p_cdura_used = {}
        self.__pools.append("self.p_cdura")
        self.p_cdura[0] = None
        self.p_cdura_used[0] = True
        self.p_cdura[1] = None
        self.p_cdura_used[1] = True
        self.p_size = {}
        self.p_size_used = {}
        self.__pools.append("self.p_size")
        self.p_size[0] = None
        self.p_size_used[0] = True
        self.p_size[1] = None
        self.p_size_used[1] = True
        self.p_pdura = {}
        self.p_pdura_used = {}
        self.__pools.append("self.p_pdura")
        self.p_pdura[0] = None
        self.p_pdura_used[0] = True
        self.p_pdura[1] = None
        self.p_pdura_used[1] = True
        self.p_dict = {}
        self.p_dict_used = {}
        self.__pools.append("self.p_dict")
        self.p_dict[0] = None
        self.p_dict_used[0] = True
        self.p_dict[1] = None
        self.p_dict_used[1] = True
        self.p_low = {}
        self.p_low_used = {}
        self.__pools.append("self.p_low")
        self.p_low[0] = None
        self.p_low_used[0] = True
        self.p_low[1] = None
        self.p_low_used[1] = True
        self.p_high = {}
        self.p_high_used = {}
        self.__pools.append("self.p_high")
        self.p_high[0] = None
        self.p_high_used[0] = True
        self.p_high[1] = None
        self.p_high_used[1] = True
        self.p_strsize = {}
        self.p_strsize_used = {}
        self.__pools.append("self.p_strsize")
        self.p_strsize[0] = None
        self.p_strsize_used[0] = True
        self.p_strsize[1] = None
        self.p_strsize_used[1] = True
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
        self.__actions.append(('''self.p_dict[0]		= {} ''',self.guard0,self.act0))

        self.__names['''self.p_dict[0]		= {} '''] = ('''self.p_dict[0]		= {} ''',self.guard0,self.act0)

        self.__orderings['''self.p_dict[0]		= {} '''] = 1

        self.__okExcepts['''self.p_dict[0]		= {} '''] = ''''''

        self.__actions.append(('''self.p_size[0]		= 10 ''',self.guard1,self.act1))

        self.__names['''self.p_size[0]		= 10 '''] = ('''self.p_size[0]		= 10 ''',self.guard1,self.act1)

        self.__orderings['''self.p_size[0]		= 10 '''] = 2

        self.__okExcepts['''self.p_size[0]		= 10 '''] = ''''''

        self.__actions.append(('''self.p_size[0]		=  20 ''',self.guard2,self.act2))

        self.__names['''self.p_size[0]		=  20 '''] = ('''self.p_size[0]		=  20 ''',self.guard2,self.act2)

        self.__orderings['''self.p_size[0]		=  20 '''] = 3

        self.__okExcepts['''self.p_size[0]		=  20 '''] = ''''''

        self.__actions.append(('''self.p_size[0]		=  30 ''',self.guard3,self.act3))

        self.__names['''self.p_size[0]		=  30 '''] = ('''self.p_size[0]		=  30 ''',self.guard3,self.act3)

        self.__orderings['''self.p_size[0]		=  30 '''] = 4

        self.__okExcepts['''self.p_size[0]		=  30 '''] = ''''''

        self.__actions.append(('''self.p_size[0]		=  50 ''',self.guard4,self.act4))

        self.__names['''self.p_size[0]		=  50 '''] = ('''self.p_size[0]		=  50 ''',self.guard4,self.act4)

        self.__orderings['''self.p_size[0]		=  50 '''] = 5

        self.__okExcepts['''self.p_size[0]		=  50 '''] = ''''''

        self.__actions.append(('''self.p_size[0]		=  100 ''',self.guard5,self.act5))

        self.__names['''self.p_size[0]		=  100 '''] = ('''self.p_size[0]		=  100 ''',self.guard5,self.act5)

        self.__orderings['''self.p_size[0]		=  100 '''] = 6

        self.__okExcepts['''self.p_size[0]		=  100 '''] = ''''''

        self.__actions.append(('''self.p_size[0]		=  150 ''',self.guard6,self.act6))

        self.__names['''self.p_size[0]		=  150 '''] = ('''self.p_size[0]		=  150 ''',self.guard6,self.act6)

        self.__orderings['''self.p_size[0]		=  150 '''] = 7

        self.__okExcepts['''self.p_size[0]		=  150 '''] = ''''''

        self.__actions.append(('''self.p_size[0]		=  200 ''',self.guard7,self.act7))

        self.__names['''self.p_size[0]		=  200 '''] = ('''self.p_size[0]		=  200 ''',self.guard7,self.act7)

        self.__orderings['''self.p_size[0]		=  200 '''] = 8

        self.__okExcepts['''self.p_size[0]		=  200 '''] = ''''''

        self.__actions.append(('''self.p_strsize[0]	= 400 ''',self.guard8,self.act8))

        self.__names['''self.p_strsize[0]	= 400 '''] = ('''self.p_strsize[0]	= 400 ''',self.guard8,self.act8)

        self.__orderings['''self.p_strsize[0]	= 400 '''] = 9

        self.__okExcepts['''self.p_strsize[0]	= 400 '''] = ''''''

        self.__actions.append(('''self.p_high[0]		= 1000 ''',self.guard9,self.act9))

        self.__names['''self.p_high[0]		= 1000 '''] = ('''self.p_high[0]		= 1000 ''',self.guard9,self.act9)

        self.__orderings['''self.p_high[0]		= 1000 '''] = 10

        self.__okExcepts['''self.p_high[0]		= 1000 '''] = ''''''

        self.__actions.append(('''self.p_low[0]		= -1000 ''',self.guard10,self.act10))

        self.__names['''self.p_low[0]		= -1000 '''] = ('''self.p_low[0]		= -1000 ''',self.guard10,self.act10)

        self.__orderings['''self.p_low[0]		= -1000 '''] = 11

        self.__okExcepts['''self.p_low[0]		= -1000 '''] = ''''''

        self.__actions.append(('''self.p_cdura[0]		= 0.0 ''',self.guard11,self.act11))

        self.__names['''self.p_cdura[0]		= 0.0 '''] = ('''self.p_cdura[0]		= 0.0 ''',self.guard11,self.act11)

        self.__orderings['''self.p_cdura[0]		= 0.0 '''] = 12

        self.__okExcepts['''self.p_cdura[0]		= 0.0 '''] = ''''''

        self.__actions.append(('''self.p_pdura[0]		= 0.0 ''',self.guard12,self.act12))

        self.__names['''self.p_pdura[0]		= 0.0 '''] = ('''self.p_pdura[0]		= 0.0 ''',self.guard12,self.act12)

        self.__orderings['''self.p_pdura[0]		= 0.0 '''] = 13

        self.__okExcepts['''self.p_pdura[0]		= 0.0 '''] = ''''''

        self.__actions.append(('''self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	 ''',self.guard13,self.act13))

        self.__names['''self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	 '''] = ('''self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	 ''',self.guard13,self.act13)

        self.__orderings['''self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	 '''] = 14

        self.__okExcepts['''self.p_dict[0] = genMulDict(self.p_low[0], self.p_high[0], self.p_size[0], self.p_strsize[0]) 	 '''] = ''''''

        self.__actions.append(('''flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag); ''',self.guard14,self.act14))

        self.__names['''flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag); '''] = ('''flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag); ''',self.guard14,self.act14)

        self.__orderings['''flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag); '''] = 15

        self.__okExcepts['''flag = EqualResult(self.p_dict[0]); self.p_cdura[0] = testCSortDict(self.p_dict[0]); self.p_pdura[0] = testPSortDict(self.p_dict[0]); print '============New Test============'; print 'Dictrionary: ', self.p_dict[0]; print 'C Sort: size = ', self.p_size[0], ';Duration = ', self.p_cdura[0]; print 'P Sort: size = ', self.p_size[0], ';Duration = ', self.p_pdura[0]; print 'Result Corretness: ', flag; outputResult(self.p_cdura[0], self.p_pdura[0], self.p_size[0], self.p_strsize[0], self.p_dict[0], flag); '''] = ''''''

        self.__actions_backup = list(self.__actions)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
    # BEGIN RELOAD CODE
        reload(time)
        reload(random)
        reload(csv)
    # END RELOAD CODE
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_cdura = {}
        self.p_cdura_used = {}
        self.__pools.append("self.p_cdura")
        self.p_cdura[0] = None
        self.p_cdura_used[0] = True
        self.p_cdura[1] = None
        self.p_cdura_used[1] = True
        self.p_size = {}
        self.p_size_used = {}
        self.__pools.append("self.p_size")
        self.p_size[0] = None
        self.p_size_used[0] = True
        self.p_size[1] = None
        self.p_size_used[1] = True
        self.p_pdura = {}
        self.p_pdura_used = {}
        self.__pools.append("self.p_pdura")
        self.p_pdura[0] = None
        self.p_pdura_used[0] = True
        self.p_pdura[1] = None
        self.p_pdura_used[1] = True
        self.p_dict = {}
        self.p_dict_used = {}
        self.__pools.append("self.p_dict")
        self.p_dict[0] = None
        self.p_dict_used[0] = True
        self.p_dict[1] = None
        self.p_dict_used[1] = True
        self.p_low = {}
        self.p_low_used = {}
        self.__pools.append("self.p_low")
        self.p_low[0] = None
        self.p_low_used[0] = True
        self.p_low[1] = None
        self.p_low_used[1] = True
        self.p_high = {}
        self.p_high_used = {}
        self.__pools.append("self.p_high")
        self.p_high[0] = None
        self.p_high_used[0] = True
        self.p_high[1] = None
        self.p_high_used[1] = True
        self.p_strsize = {}
        self.p_strsize_used = {}
        self.__pools.append("self.p_strsize")
        self.p_strsize[0] = None
        self.p_strsize_used[0] = True
        self.p_strsize[1] = None
        self.p_strsize_used[1] = True
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
        return [ copy.deepcopy(self.p_cdura),copy.deepcopy(self.p_cdura_used),copy.deepcopy(self.p_size),copy.deepcopy(self.p_size_used),copy.deepcopy(self.p_pdura),copy.deepcopy(self.p_pdura_used),copy.deepcopy(self.p_dict),copy.deepcopy(self.p_dict_used),copy.deepcopy(self.p_low),copy.deepcopy(self.p_low_used),copy.deepcopy(self.p_high),copy.deepcopy(self.p_high_used),copy.deepcopy(self.p_strsize),copy.deepcopy(self.p_strsize_used)]
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_cdura = copy.deepcopy(old[0])
        self.p_cdura_used = copy.deepcopy(old[1])
        self.p_size = copy.deepcopy(old[2])
        self.p_size_used = copy.deepcopy(old[3])
        self.p_pdura = copy.deepcopy(old[4])
        self.p_pdura_used = copy.deepcopy(old[5])
        self.p_dict = copy.deepcopy(old[6])
        self.p_dict_used = copy.deepcopy(old[7])
        self.p_low = copy.deepcopy(old[8])
        self.p_low_used = copy.deepcopy(old[9])
        self.p_high = copy.deepcopy(old[10])
        self.p_high_used = copy.deepcopy(old[11])
        self.p_strsize = copy.deepcopy(old[12])
        self.p_strsize_used = copy.deepcopy(old[13])
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
