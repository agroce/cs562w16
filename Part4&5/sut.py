# _*_ coding: utf-8 _*_
import copy
import traceback
import re
import sys
from itertools import chain, combinations
import coverage
# BEGIN STANDALONE CODE
from xpinyin import Pinyin
# END STANDALONE CODE
class sut(object):
    def act0(self):
        self.__test.append(('''self.p_w[0] = Pinyin()
 ''',self.guard0,self.act0))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_w[0] = Pinyin()

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=False
    def guard0(self):
        return (((self.p_w_used[0]) or (self.p_w[0] == None) or (self.__relaxUsedRestriction)))
    
    def act1(self):
        self.__test.append(('''self.p_word1[0] = u"骉: biao1"
 ''',self.guard1,self.act1))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[0] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=False
    def guard1(self):
        return (((self.p_word1_used[0]) or (self.p_word1[0] == None) or (self.__relaxUsedRestriction)))
    
    def act2(self):
        self.__test.append(('''self.p_word1[0] = u"麤: cu1"
 ''',self.guard2,self.act2))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[0] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=False
    def guard2(self):
        return (((self.p_word1_used[0]) or (self.p_word1[0] == None) or (self.__relaxUsedRestriction)))
    
    def act3(self):
        self.__test.append(('''self.p_word1[0] =  u"奡: ao4"
 ''',self.guard3,self.act3))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[0] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=False
    def guard3(self):
        return (((self.p_word1_used[0]) or (self.p_word1[0] == None) or (self.__relaxUsedRestriction)))
    
    def act4(self):
        self.__test.append(('''self.p_word1[0] = u"砳: le4"
 ''',self.guard4,self.act4))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[0] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=False
    def guard4(self):
        return (((self.p_word1_used[0]) or (self.p_word1[0] == None) or (self.__relaxUsedRestriction)))
    
    def act5(self):
        self.__test.append(('''self.p_word1[0] = u"嘂: jiao"
 ''',self.guard5,self.act5))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[0] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=False
    def guard5(self):
        return (((self.p_word1_used[0]) or (self.p_word1[0] == None) or (self.__relaxUsedRestriction)))
    
    def act6(self):
        self.__test.append(('''self.p_word1[1] = u"骉: biao1"
 ''',self.guard6,self.act6))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[1] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=False
    def guard6(self):
        return (((self.p_word1_used[1]) or (self.p_word1[1] == None) or (self.__relaxUsedRestriction)))
    
    def act7(self):
        self.__test.append(('''self.p_word1[1] = u"麤: cu1"
 ''',self.guard7,self.act7))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[1] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=False
    def guard7(self):
        return (((self.p_word1_used[1]) or (self.p_word1[1] == None) or (self.__relaxUsedRestriction)))
    
    def act8(self):
        self.__test.append(('''self.p_word1[1] =  u"奡: ao4"
 ''',self.guard8,self.act8))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[1] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=False
    def guard8(self):
        return (((self.p_word1_used[1]) or (self.p_word1[1] == None) or (self.__relaxUsedRestriction)))
    
    def act9(self):
        self.__test.append(('''self.p_word1[1] = u"砳: le4"
 ''',self.guard9,self.act9))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[1] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=False
    def guard9(self):
        return (((self.p_word1_used[1]) or (self.p_word1[1] == None) or (self.__relaxUsedRestriction)))
    
    def act10(self):
        self.__test.append(('''self.p_word1[1] = u"嘂: jiao"
 ''',self.guard10,self.act10))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[1] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=False
    def guard10(self):
        return (((self.p_word1_used[1]) or (self.p_word1[1] == None) or (self.__relaxUsedRestriction)))
    
    def act11(self):
        self.__test.append(('''self.p_word1[2] = u"骉: biao1"
 ''',self.guard11,self.act11))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[2] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=False
    def guard11(self):
        return (((self.p_word1_used[2]) or (self.p_word1[2] == None) or (self.__relaxUsedRestriction)))
    
    def act12(self):
        self.__test.append(('''self.p_word1[2] = u"麤: cu1"
 ''',self.guard12,self.act12))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[2] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=False
    def guard12(self):
        return (((self.p_word1_used[2]) or (self.p_word1[2] == None) or (self.__relaxUsedRestriction)))
    
    def act13(self):
        self.__test.append(('''self.p_word1[2] =  u"奡: ao4"
 ''',self.guard13,self.act13))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[2] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=False
    def guard13(self):
        return (((self.p_word1_used[2]) or (self.p_word1[2] == None) or (self.__relaxUsedRestriction)))
    
    def act14(self):
        self.__test.append(('''self.p_word1[2] = u"砳: le4"
 ''',self.guard14,self.act14))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[2] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=False
    def guard14(self):
        return (((self.p_word1_used[2]) or (self.p_word1[2] == None) or (self.__relaxUsedRestriction)))
    
    def act15(self):
        self.__test.append(('''self.p_word1[2] = u"嘂: jiao"
 ''',self.guard15,self.act15))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[2] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=False
    def guard15(self):
        return (((self.p_word1_used[2]) or (self.p_word1[2] == None) or (self.__relaxUsedRestriction)))
    
    def act16(self):
        self.__test.append(('''self.p_word1[3] = u"骉: biao1"
 ''',self.guard16,self.act16))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[3] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=False
    def guard16(self):
        return (((self.p_word1_used[3]) or (self.p_word1[3] == None) or (self.__relaxUsedRestriction)))
    
    def act17(self):
        self.__test.append(('''self.p_word1[3] = u"麤: cu1"
 ''',self.guard17,self.act17))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[3] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=False
    def guard17(self):
        return (((self.p_word1_used[3]) or (self.p_word1[3] == None) or (self.__relaxUsedRestriction)))
    
    def act18(self):
        self.__test.append(('''self.p_word1[3] =  u"奡: ao4"
 ''',self.guard18,self.act18))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[3] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=False
    def guard18(self):
        return (((self.p_word1_used[3]) or (self.p_word1[3] == None) or (self.__relaxUsedRestriction)))
    
    def act19(self):
        self.__test.append(('''self.p_word1[3] = u"砳: le4"
 ''',self.guard19,self.act19))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[3] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=False
    def guard19(self):
        return (((self.p_word1_used[3]) or (self.p_word1[3] == None) or (self.__relaxUsedRestriction)))
    
    def act20(self):
        self.__test.append(('''self.p_word1[3] = u"嘂: jiao"
 ''',self.guard20,self.act20))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[3] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=False
    def guard20(self):
        return (((self.p_word1_used[3]) or (self.p_word1[3] == None) or (self.__relaxUsedRestriction)))
    
    def act21(self):
        self.__test.append(('''self.p_word1[4] = u"骉: biao1"
 ''',self.guard21,self.act21))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[4] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=False
    def guard21(self):
        return (((self.p_word1_used[4]) or (self.p_word1[4] == None) or (self.__relaxUsedRestriction)))
    
    def act22(self):
        self.__test.append(('''self.p_word1[4] = u"麤: cu1"
 ''',self.guard22,self.act22))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[4] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=False
    def guard22(self):
        return (((self.p_word1_used[4]) or (self.p_word1[4] == None) or (self.__relaxUsedRestriction)))
    
    def act23(self):
        self.__test.append(('''self.p_word1[4] =  u"奡: ao4"
 ''',self.guard23,self.act23))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[4] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=False
    def guard23(self):
        return (((self.p_word1_used[4]) or (self.p_word1[4] == None) or (self.__relaxUsedRestriction)))
    
    def act24(self):
        self.__test.append(('''self.p_word1[4] = u"砳: le4"
 ''',self.guard24,self.act24))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[4] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=False
    def guard24(self):
        return (((self.p_word1_used[4]) or (self.p_word1[4] == None) or (self.__relaxUsedRestriction)))
    
    def act25(self):
        self.__test.append(('''self.p_word1[4] = u"嘂: jiao"
 ''',self.guard25,self.act25))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[4] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=False
    def guard25(self):
        return (((self.p_word1_used[4]) or (self.p_word1[4] == None) or (self.__relaxUsedRestriction)))
    
    def act26(self):
        self.__test.append(('''self.p_word1[5] = u"骉: biao1"
 ''',self.guard26,self.act26))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[5] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=False
    def guard26(self):
        return (((self.p_word1_used[5]) or (self.p_word1[5] == None) or (self.__relaxUsedRestriction)))
    
    def act27(self):
        self.__test.append(('''self.p_word1[5] = u"麤: cu1"
 ''',self.guard27,self.act27))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[5] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=False
    def guard27(self):
        return (((self.p_word1_used[5]) or (self.p_word1[5] == None) or (self.__relaxUsedRestriction)))
    
    def act28(self):
        self.__test.append(('''self.p_word1[5] =  u"奡: ao4"
 ''',self.guard28,self.act28))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[5] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=False
    def guard28(self):
        return (((self.p_word1_used[5]) or (self.p_word1[5] == None) or (self.__relaxUsedRestriction)))
    
    def act29(self):
        self.__test.append(('''self.p_word1[5] = u"砳: le4"
 ''',self.guard29,self.act29))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[5] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=False
    def guard29(self):
        return (((self.p_word1_used[5]) or (self.p_word1[5] == None) or (self.__relaxUsedRestriction)))
    
    def act30(self):
        self.__test.append(('''self.p_word1[5] = u"嘂: jiao"
 ''',self.guard30,self.act30))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[5] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=False
    def guard30(self):
        return (((self.p_word1_used[5]) or (self.p_word1[5] == None) or (self.__relaxUsedRestriction)))
    
    def act31(self):
        self.__test.append(('''self.p_word1[6] = u"骉: biao1"
 ''',self.guard31,self.act31))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[6] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=False
    def guard31(self):
        return (((self.p_word1_used[6]) or (self.p_word1[6] == None) or (self.__relaxUsedRestriction)))
    
    def act32(self):
        self.__test.append(('''self.p_word1[6] = u"麤: cu1"
 ''',self.guard32,self.act32))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[6] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=False
    def guard32(self):
        return (((self.p_word1_used[6]) or (self.p_word1[6] == None) or (self.__relaxUsedRestriction)))
    
    def act33(self):
        self.__test.append(('''self.p_word1[6] =  u"奡: ao4"
 ''',self.guard33,self.act33))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[6] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=False
    def guard33(self):
        return (((self.p_word1_used[6]) or (self.p_word1[6] == None) or (self.__relaxUsedRestriction)))
    
    def act34(self):
        self.__test.append(('''self.p_word1[6] = u"砳: le4"
 ''',self.guard34,self.act34))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[6] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=False
    def guard34(self):
        return (((self.p_word1_used[6]) or (self.p_word1[6] == None) or (self.__relaxUsedRestriction)))
    
    def act35(self):
        self.__test.append(('''self.p_word1[6] = u"嘂: jiao"
 ''',self.guard35,self.act35))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[6] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=False
    def guard35(self):
        return (((self.p_word1_used[6]) or (self.p_word1[6] == None) or (self.__relaxUsedRestriction)))
    
    def act36(self):
        self.__test.append(('''self.p_word1[7] = u"骉: biao1"
 ''',self.guard36,self.act36))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[7] = u"骉: biao1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=False
    def guard36(self):
        return (((self.p_word1_used[7]) or (self.p_word1[7] == None) or (self.__relaxUsedRestriction)))
    
    def act37(self):
        self.__test.append(('''self.p_word1[7] = u"麤: cu1"
 ''',self.guard37,self.act37))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[7] = u"麤: cu1"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=False
    def guard37(self):
        return (((self.p_word1_used[7]) or (self.p_word1[7] == None) or (self.__relaxUsedRestriction)))
    
    def act38(self):
        self.__test.append(('''self.p_word1[7] =  u"奡: ao4"
 ''',self.guard38,self.act38))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[7] =  u"奡: ao4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=False
    def guard38(self):
        return (((self.p_word1_used[7]) or (self.p_word1[7] == None) or (self.__relaxUsedRestriction)))
    
    def act39(self):
        self.__test.append(('''self.p_word1[7] = u"砳: le4"
 ''',self.guard39,self.act39))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[7] = u"砳: le4"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=False
    def guard39(self):
        return (((self.p_word1_used[7]) or (self.p_word1[7] == None) or (self.__relaxUsedRestriction)))
    
    def act40(self):
        self.__test.append(('''self.p_word1[7] = u"嘂: jiao"
 ''',self.guard40,self.act40))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word1[7] = u"嘂: jiao"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=False
    def guard40(self):
        return (((self.p_word1_used[7]) or (self.p_word1[7] == None) or (self.__relaxUsedRestriction)))
    
    def act41(self):
        self.__test.append(('''self.p_word2[0] = u"蛤蚌"
 ''',self.guard41,self.act41))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard41(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act42(self):
        self.__test.append(('''self.p_word2[0] = u"蚌埠"
 ''',self.guard42,self.act42))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard42(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act43(self):
        self.__test.append(('''self.p_word2[0] =  u"纸薄"
 ''',self.guard43,self.act43))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard43(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act44(self):
        self.__test.append(('''self.p_word2[0] = u"稀薄"
 ''',self.guard44,self.act44))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard44(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act45(self):
        self.__test.append(('''self.p_word2[0] = u"碉堡"
 ''',self.guard45,self.act45))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard45(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act46(self):
        self.__test.append(('''self.p_word2[0] = u"瓦窑堡"
 ''',self.guard46,self.act46))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard46(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act47(self):
        self.__test.append(('''self.p_word2[0] = u"十里堡"
 ''',self.guard47,self.act47))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[0] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=False
    def guard47(self):
        return (((self.p_word2_used[0]) or (self.p_word2[0] == None) or (self.__relaxUsedRestriction)))
    
    def act48(self):
        self.__test.append(('''self.p_word2[1] = u"蛤蚌"
 ''',self.guard48,self.act48))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard48(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act49(self):
        self.__test.append(('''self.p_word2[1] = u"蚌埠"
 ''',self.guard49,self.act49))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard49(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act50(self):
        self.__test.append(('''self.p_word2[1] =  u"纸薄"
 ''',self.guard50,self.act50))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard50(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act51(self):
        self.__test.append(('''self.p_word2[1] = u"稀薄"
 ''',self.guard51,self.act51))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard51(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act52(self):
        self.__test.append(('''self.p_word2[1] = u"碉堡"
 ''',self.guard52,self.act52))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard52(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act53(self):
        self.__test.append(('''self.p_word2[1] = u"瓦窑堡"
 ''',self.guard53,self.act53))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard53(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act54(self):
        self.__test.append(('''self.p_word2[1] = u"十里堡"
 ''',self.guard54,self.act54))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[1] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=False
    def guard54(self):
        return (((self.p_word2_used[1]) or (self.p_word2[1] == None) or (self.__relaxUsedRestriction)))
    
    def act55(self):
        self.__test.append(('''self.p_word2[2] = u"蛤蚌"
 ''',self.guard55,self.act55))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard55(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act56(self):
        self.__test.append(('''self.p_word2[2] = u"蚌埠"
 ''',self.guard56,self.act56))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard56(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act57(self):
        self.__test.append(('''self.p_word2[2] =  u"纸薄"
 ''',self.guard57,self.act57))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard57(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act58(self):
        self.__test.append(('''self.p_word2[2] = u"稀薄"
 ''',self.guard58,self.act58))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard58(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act59(self):
        self.__test.append(('''self.p_word2[2] = u"碉堡"
 ''',self.guard59,self.act59))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard59(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act60(self):
        self.__test.append(('''self.p_word2[2] = u"瓦窑堡"
 ''',self.guard60,self.act60))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard60(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act61(self):
        self.__test.append(('''self.p_word2[2] = u"十里堡"
 ''',self.guard61,self.act61))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[2] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=False
    def guard61(self):
        return (((self.p_word2_used[2]) or (self.p_word2[2] == None) or (self.__relaxUsedRestriction)))
    
    def act62(self):
        self.__test.append(('''self.p_word2[3] = u"蛤蚌"
 ''',self.guard62,self.act62))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard62(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act63(self):
        self.__test.append(('''self.p_word2[3] = u"蚌埠"
 ''',self.guard63,self.act63))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard63(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act64(self):
        self.__test.append(('''self.p_word2[3] =  u"纸薄"
 ''',self.guard64,self.act64))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard64(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act65(self):
        self.__test.append(('''self.p_word2[3] = u"稀薄"
 ''',self.guard65,self.act65))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard65(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act66(self):
        self.__test.append(('''self.p_word2[3] = u"碉堡"
 ''',self.guard66,self.act66))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard66(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act67(self):
        self.__test.append(('''self.p_word2[3] = u"瓦窑堡"
 ''',self.guard67,self.act67))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard67(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act68(self):
        self.__test.append(('''self.p_word2[3] = u"十里堡"
 ''',self.guard68,self.act68))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[3] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=False
    def guard68(self):
        return (((self.p_word2_used[3]) or (self.p_word2[3] == None) or (self.__relaxUsedRestriction)))
    
    def act69(self):
        self.__test.append(('''self.p_word2[4] = u"蛤蚌"
 ''',self.guard69,self.act69))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard69(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act70(self):
        self.__test.append(('''self.p_word2[4] = u"蚌埠"
 ''',self.guard70,self.act70))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard70(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act71(self):
        self.__test.append(('''self.p_word2[4] =  u"纸薄"
 ''',self.guard71,self.act71))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard71(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act72(self):
        self.__test.append(('''self.p_word2[4] = u"稀薄"
 ''',self.guard72,self.act72))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard72(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act73(self):
        self.__test.append(('''self.p_word2[4] = u"碉堡"
 ''',self.guard73,self.act73))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard73(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act74(self):
        self.__test.append(('''self.p_word2[4] = u"瓦窑堡"
 ''',self.guard74,self.act74))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard74(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act75(self):
        self.__test.append(('''self.p_word2[4] = u"十里堡"
 ''',self.guard75,self.act75))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[4] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=False
    def guard75(self):
        return (((self.p_word2_used[4]) or (self.p_word2[4] == None) or (self.__relaxUsedRestriction)))
    
    def act76(self):
        self.__test.append(('''self.p_word2[5] = u"蛤蚌"
 ''',self.guard76,self.act76))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard76(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act77(self):
        self.__test.append(('''self.p_word2[5] = u"蚌埠"
 ''',self.guard77,self.act77))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard77(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act78(self):
        self.__test.append(('''self.p_word2[5] =  u"纸薄"
 ''',self.guard78,self.act78))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard78(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act79(self):
        self.__test.append(('''self.p_word2[5] = u"稀薄"
 ''',self.guard79,self.act79))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard79(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act80(self):
        self.__test.append(('''self.p_word2[5] = u"碉堡"
 ''',self.guard80,self.act80))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard80(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act81(self):
        self.__test.append(('''self.p_word2[5] = u"瓦窑堡"
 ''',self.guard81,self.act81))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard81(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act82(self):
        self.__test.append(('''self.p_word2[5] = u"十里堡"
 ''',self.guard82,self.act82))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[5] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=False
    def guard82(self):
        return (((self.p_word2_used[5]) or (self.p_word2[5] == None) or (self.__relaxUsedRestriction)))
    
    def act83(self):
        self.__test.append(('''self.p_word2[6] = u"蛤蚌"
 ''',self.guard83,self.act83))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard83(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act84(self):
        self.__test.append(('''self.p_word2[6] = u"蚌埠"
 ''',self.guard84,self.act84))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard84(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act85(self):
        self.__test.append(('''self.p_word2[6] =  u"纸薄"
 ''',self.guard85,self.act85))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard85(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act86(self):
        self.__test.append(('''self.p_word2[6] = u"稀薄"
 ''',self.guard86,self.act86))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard86(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act87(self):
        self.__test.append(('''self.p_word2[6] = u"碉堡"
 ''',self.guard87,self.act87))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard87(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act88(self):
        self.__test.append(('''self.p_word2[6] = u"瓦窑堡"
 ''',self.guard88,self.act88))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard88(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act89(self):
        self.__test.append(('''self.p_word2[6] = u"十里堡"
 ''',self.guard89,self.act89))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[6] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=False
    def guard89(self):
        return (((self.p_word2_used[6]) or (self.p_word2[6] == None) or (self.__relaxUsedRestriction)))
    
    def act90(self):
        self.__test.append(('''self.p_word2[7] = u"蛤蚌"
 ''',self.guard90,self.act90))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] = u"蛤蚌"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard90(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act91(self):
        self.__test.append(('''self.p_word2[7] = u"蚌埠"
 ''',self.guard91,self.act91))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] = u"蚌埠"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard91(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act92(self):
        self.__test.append(('''self.p_word2[7] =  u"纸薄"
 ''',self.guard92,self.act92))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] =  u"纸薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard92(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act93(self):
        self.__test.append(('''self.p_word2[7] = u"稀薄"
 ''',self.guard93,self.act93))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] = u"稀薄"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard93(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act94(self):
        self.__test.append(('''self.p_word2[7] = u"碉堡"
 ''',self.guard94,self.act94))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] = u"碉堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard94(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act95(self):
        self.__test.append(('''self.p_word2[7] = u"瓦窑堡"
 ''',self.guard95,self.act95))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] = u"瓦窑堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard95(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act96(self):
        self.__test.append(('''self.p_word2[7] = u"十里堡"
 ''',self.guard96,self.act96))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word2[7] = u"十里堡"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=False
    def guard96(self):
        return (((self.p_word2_used[7]) or (self.p_word2[7] == None) or (self.__relaxUsedRestriction)))
    
    def act97(self):
        self.__test.append(('''self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard97,self.act97))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=False
    def guard97(self):
        return (((self.p_word3_used[0]) or (self.p_word3[0] == None) or (self.__relaxUsedRestriction)))
    
    def act98(self):
        self.__test.append(('''self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard98,self.act98))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=False
    def guard98(self):
        return (((self.p_word3_used[0]) or (self.p_word3[0] == None) or (self.__relaxUsedRestriction)))
    
    def act99(self):
        self.__test.append(('''self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard99,self.act99))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=False
    def guard99(self):
        return (((self.p_word3_used[0]) or (self.p_word3[0] == None) or (self.__relaxUsedRestriction)))
    
    def act100(self):
        self.__test.append(('''self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard100,self.act100))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=False
    def guard100(self):
        return (((self.p_word3_used[1]) or (self.p_word3[1] == None) or (self.__relaxUsedRestriction)))
    
    def act101(self):
        self.__test.append(('''self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard101,self.act101))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=False
    def guard101(self):
        return (((self.p_word3_used[1]) or (self.p_word3[1] == None) or (self.__relaxUsedRestriction)))
    
    def act102(self):
        self.__test.append(('''self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard102,self.act102))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=False
    def guard102(self):
        return (((self.p_word3_used[1]) or (self.p_word3[1] == None) or (self.__relaxUsedRestriction)))
    
    def act103(self):
        self.__test.append(('''self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard103,self.act103))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=False
    def guard103(self):
        return (((self.p_word3_used[2]) or (self.p_word3[2] == None) or (self.__relaxUsedRestriction)))
    
    def act104(self):
        self.__test.append(('''self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard104,self.act104))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=False
    def guard104(self):
        return (((self.p_word3_used[2]) or (self.p_word3[2] == None) or (self.__relaxUsedRestriction)))
    
    def act105(self):
        self.__test.append(('''self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard105,self.act105))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=False
    def guard105(self):
        return (((self.p_word3_used[2]) or (self.p_word3[2] == None) or (self.__relaxUsedRestriction)))
    
    def act106(self):
        self.__test.append(('''self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard106,self.act106))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[0]=False
    def guard106(self):
        return (((self.p_word4_used[0]) or (self.p_word4[0] == None) or (self.__relaxUsedRestriction)))
    
    def act107(self):
        self.__test.append(('''self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard107,self.act107))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[0]=False
    def guard107(self):
        return (((self.p_word4_used[0]) or (self.p_word4[0] == None) or (self.__relaxUsedRestriction)))
    
    def act108(self):
        self.__test.append(('''self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard108,self.act108))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[0]=False
    def guard108(self):
        return (((self.p_word4_used[0]) or (self.p_word4[0] == None) or (self.__relaxUsedRestriction)))
    
    def act109(self):
        self.__test.append(('''self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard109,self.act109))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[1]=False
    def guard109(self):
        return (((self.p_word4_used[1]) or (self.p_word4[1] == None) or (self.__relaxUsedRestriction)))
    
    def act110(self):
        self.__test.append(('''self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard110,self.act110))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[1]=False
    def guard110(self):
        return (((self.p_word4_used[1]) or (self.p_word4[1] == None) or (self.__relaxUsedRestriction)))
    
    def act111(self):
        self.__test.append(('''self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard111,self.act111))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[1]=False
    def guard111(self):
        return (((self.p_word4_used[1]) or (self.p_word4[1] == None) or (self.__relaxUsedRestriction)))
    
    def act112(self):
        self.__test.append(('''self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard112,self.act112))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[2]=False
    def guard112(self):
        return (((self.p_word4_used[2]) or (self.p_word4[2] == None) or (self.__relaxUsedRestriction)))
    
    def act113(self):
        self.__test.append(('''self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard113,self.act113))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[2]=False
    def guard113(self):
        return (((self.p_word4_used[2]) or (self.p_word4[2] == None) or (self.__relaxUsedRestriction)))
    
    def act114(self):
        self.__test.append(('''self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard114,self.act114))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word4_used[2]=False
    def guard114(self):
        return (((self.p_word4_used[2]) or (self.p_word4[2] == None) or (self.__relaxUsedRestriction)))
    
    def act115(self):
        self.__test.append(('''self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard115,self.act115))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[0]=False
    def guard115(self):
        return (((self.p_word5_used[0]) or (self.p_word5[0] == None) or (self.__relaxUsedRestriction)))
    
    def act116(self):
        self.__test.append(('''self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard116,self.act116))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[0]=False
    def guard116(self):
        return (((self.p_word5_used[0]) or (self.p_word5[0] == None) or (self.__relaxUsedRestriction)))
    
    def act117(self):
        self.__test.append(('''self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard117,self.act117))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[0]=False
    def guard117(self):
        return (((self.p_word5_used[0]) or (self.p_word5[0] == None) or (self.__relaxUsedRestriction)))
    
    def act118(self):
        self.__test.append(('''self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard118,self.act118))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[1]=False
    def guard118(self):
        return (((self.p_word5_used[1]) or (self.p_word5[1] == None) or (self.__relaxUsedRestriction)))
    
    def act119(self):
        self.__test.append(('''self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard119,self.act119))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[1]=False
    def guard119(self):
        return (((self.p_word5_used[1]) or (self.p_word5[1] == None) or (self.__relaxUsedRestriction)))
    
    def act120(self):
        self.__test.append(('''self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard120,self.act120))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[1]=False
    def guard120(self):
        return (((self.p_word5_used[1]) or (self.p_word5[1] == None) or (self.__relaxUsedRestriction)))
    
    def act121(self):
        self.__test.append(('''self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard121,self.act121))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[2]=False
    def guard121(self):
        return (((self.p_word5_used[2]) or (self.p_word5[2] == None) or (self.__relaxUsedRestriction)))
    
    def act122(self):
        self.__test.append(('''self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard122,self.act122))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[2]=False
    def guard122(self):
        return (((self.p_word5_used[2]) or (self.p_word5[2] == None) or (self.__relaxUsedRestriction)))
    
    def act123(self):
        self.__test.append(('''self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard123,self.act123))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word5_used[2]=False
    def guard123(self):
        return (((self.p_word5_used[2]) or (self.p_word5[2] == None) or (self.__relaxUsedRestriction)))
    
    def act124(self):
        self.__test.append(('''self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard124,self.act124))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=False
    def guard124(self):
        return (((self.p_word6_used[0]) or (self.p_word6[0] == None) or (self.__relaxUsedRestriction)))
    
    def act125(self):
        self.__test.append(('''self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard125,self.act125))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=False
    def guard125(self):
        return (((self.p_word6_used[0]) or (self.p_word6[0] == None) or (self.__relaxUsedRestriction)))
    
    def act126(self):
        self.__test.append(('''self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard126,self.act126))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=False
    def guard126(self):
        return (((self.p_word6_used[0]) or (self.p_word6[0] == None) or (self.__relaxUsedRestriction)))
    
    def act127(self):
        self.__test.append(('''self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard127,self.act127))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=False
    def guard127(self):
        return (((self.p_word6_used[1]) or (self.p_word6[1] == None) or (self.__relaxUsedRestriction)))
    
    def act128(self):
        self.__test.append(('''self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard128,self.act128))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=False
    def guard128(self):
        return (((self.p_word6_used[1]) or (self.p_word6[1] == None) or (self.__relaxUsedRestriction)))
    
    def act129(self):
        self.__test.append(('''self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard129,self.act129))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=False
    def guard129(self):
        return (((self.p_word6_used[1]) or (self.p_word6[1] == None) or (self.__relaxUsedRestriction)))
    
    def act130(self):
        self.__test.append(('''self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard130,self.act130))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=False
    def guard130(self):
        return (((self.p_word6_used[2]) or (self.p_word6[2] == None) or (self.__relaxUsedRestriction)))
    
    def act131(self):
        self.__test.append(('''self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard131,self.act131))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=False
    def guard131(self):
        return (((self.p_word6_used[2]) or (self.p_word6[2] == None) or (self.__relaxUsedRestriction)))
    
    def act132(self):
        self.__test.append(('''self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard132,self.act132))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=False
    def guard132(self):
        return (((self.p_word6_used[2]) or (self.p_word6[2] == None) or (self.__relaxUsedRestriction)))
    
    def act133(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[0])
 ''',self.guard133,self.act133))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=True
        self.p_w_used[0]=True
    def guard133(self):
        return (self.p_word1[0] != None) and (self.p_w[0] != None)
    
    def act134(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[1])
 ''',self.guard134,self.act134))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=True
        self.p_w_used[0]=True
    def guard134(self):
        return (self.p_word1[1] != None) and (self.p_w[0] != None)
    
    def act135(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[2])
 ''',self.guard135,self.act135))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=True
        self.p_w_used[0]=True
    def guard135(self):
        return (self.p_word1[2] != None) and (self.p_w[0] != None)
    
    def act136(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[3])
 ''',self.guard136,self.act136))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[3])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=True
        self.p_w_used[0]=True
    def guard136(self):
        return (self.p_word1[3] != None) and (self.p_w[0] != None)
    
    def act137(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[4])
 ''',self.guard137,self.act137))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[4])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=True
        self.p_w_used[0]=True
    def guard137(self):
        return (self.p_word1[4] != None) and (self.p_w[0] != None)
    
    def act138(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[5])
 ''',self.guard138,self.act138))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[5])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=True
        self.p_w_used[0]=True
    def guard138(self):
        return (self.p_word1[5] != None) and (self.p_w[0] != None)
    
    def act139(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[6])
 ''',self.guard139,self.act139))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[6])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=True
        self.p_w_used[0]=True
    def guard139(self):
        return (self.p_word1[6] != None) and (self.p_w[0] != None)
    
    def act140(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[7])
 ''',self.guard140,self.act140))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[7])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=True
        self.p_w_used[0]=True
    def guard140(self):
        return (self.p_word1[7] != None) and (self.p_w[0] != None)
    
    def act141(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[0])
 ''',self.guard141,self.act141))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=True
        self.p_w_used[0]=True
    def guard141(self):
        return (self.p_word2[0] != None) and (self.p_w[0] != None)
    
    def act142(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[1])
 ''',self.guard142,self.act142))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=True
        self.p_w_used[0]=True
    def guard142(self):
        return (self.p_word2[1] != None) and (self.p_w[0] != None)
    
    def act143(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[2])
 ''',self.guard143,self.act143))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=True
        self.p_w_used[0]=True
    def guard143(self):
        return (self.p_word2[2] != None) and (self.p_w[0] != None)
    
    def act144(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[3])
 ''',self.guard144,self.act144))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[3])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=True
        self.p_w_used[0]=True
    def guard144(self):
        return (self.p_word2[3] != None) and (self.p_w[0] != None)
    
    def act145(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[4])
 ''',self.guard145,self.act145))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[4])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=True
        self.p_w_used[0]=True
    def guard145(self):
        return (self.p_word2[4] != None) and (self.p_w[0] != None)
    
    def act146(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[5])
 ''',self.guard146,self.act146))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[5])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=True
        self.p_w_used[0]=True
    def guard146(self):
        return (self.p_word2[5] != None) and (self.p_w[0] != None)
    
    def act147(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[6])
 ''',self.guard147,self.act147))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[6])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=True
        self.p_w_used[0]=True
    def guard147(self):
        return (self.p_word2[6] != None) and (self.p_w[0] != None)
    
    def act148(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[7])
 ''',self.guard148,self.act148))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[7])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=True
        self.p_w_used[0]=True
    def guard148(self):
        return (self.p_word2[7] != None) and (self.p_w[0] != None)
    
    def act149(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[0])
 ''',self.guard149,self.act149))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=True
        self.p_w_used[0]=True
    def guard149(self):
        return (self.p_word3[0] != None) and (self.p_w[0] != None)
    
    def act150(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[1])
 ''',self.guard150,self.act150))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=True
        self.p_w_used[0]=True
    def guard150(self):
        return (self.p_word3[1] != None) and (self.p_w[0] != None)
    
    def act151(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[2])
 ''',self.guard151,self.act151))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=True
        self.p_w_used[0]=True
    def guard151(self):
        return (self.p_word3[2] != None) and (self.p_w[0] != None)
    
    def act152(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[0])
 ''',self.guard152,self.act152))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[0]=True
    def guard152(self):
        return (self.p_w[0] != None) and (self.p_word4[0] != None)
    
    def act153(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[1])
 ''',self.guard153,self.act153))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[1]=True
    def guard153(self):
        return (self.p_w[0] != None) and (self.p_word4[1] != None)
    
    def act154(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[2])
 ''',self.guard154,self.act154))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[2]=True
    def guard154(self):
        return (self.p_w[0] != None) and (self.p_word4[2] != None)
    
    def act155(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[0])
 ''',self.guard155,self.act155))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[0]=True
    def guard155(self):
        return (self.p_w[0] != None) and (self.p_word5[0] != None)
    
    def act156(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[1])
 ''',self.guard156,self.act156))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[1]=True
    def guard156(self):
        return (self.p_w[0] != None) and (self.p_word5[1] != None)
    
    def act157(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[2])
 ''',self.guard157,self.act157))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[2]=True
    def guard157(self):
        return (self.p_w[0] != None) and (self.p_word5[2] != None)
    
    def act158(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[0])
 ''',self.guard158,self.act158))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=True
        self.p_w_used[0]=True
    def guard158(self):
        return (self.p_word6[0] != None) and (self.p_w[0] != None)
    
    def act159(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[1])
 ''',self.guard159,self.act159))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=True
        self.p_w_used[0]=True
    def guard159(self):
        return (self.p_word6[1] != None) and (self.p_w[0] != None)
    
    def act160(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[2])
 ''',self.guard160,self.act160))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=True
        self.p_w_used[0]=True
    def guard160(self):
        return (self.p_word6[2] != None) and (self.p_w[0] != None)
    
    def act161(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[0])
 ''',self.guard161,self.act161))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=True
        self.p_w_used[0]=True
    def guard161(self):
        return (self.p_word1[0] != None) and (self.p_w[0] != None)
    
    def act162(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[1])
 ''',self.guard162,self.act162))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=True
        self.p_w_used[0]=True
    def guard162(self):
        return (self.p_word1[1] != None) and (self.p_w[0] != None)
    
    def act163(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[2])
 ''',self.guard163,self.act163))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=True
        self.p_w_used[0]=True
    def guard163(self):
        return (self.p_word1[2] != None) and (self.p_w[0] != None)
    
    def act164(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[3])
 ''',self.guard164,self.act164))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[3])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=True
        self.p_w_used[0]=True
    def guard164(self):
        return (self.p_word1[3] != None) and (self.p_w[0] != None)
    
    def act165(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[4])
 ''',self.guard165,self.act165))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[4])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=True
        self.p_w_used[0]=True
    def guard165(self):
        return (self.p_word1[4] != None) and (self.p_w[0] != None)
    
    def act166(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[5])
 ''',self.guard166,self.act166))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[5])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=True
        self.p_w_used[0]=True
    def guard166(self):
        return (self.p_word1[5] != None) and (self.p_w[0] != None)
    
    def act167(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[6])
 ''',self.guard167,self.act167))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[6])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=True
        self.p_w_used[0]=True
    def guard167(self):
        return (self.p_word1[6] != None) and (self.p_w[0] != None)
    
    def act168(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word1[7])
 ''',self.guard168,self.act168))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word1[7])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=True
        self.p_w_used[0]=True
    def guard168(self):
        return (self.p_word1[7] != None) and (self.p_w[0] != None)
    
    def act169(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[0])
 ''',self.guard169,self.act169))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=True
        self.p_w_used[0]=True
    def guard169(self):
        return (self.p_word2[0] != None) and (self.p_w[0] != None)
    
    def act170(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[1])
 ''',self.guard170,self.act170))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=True
        self.p_w_used[0]=True
    def guard170(self):
        return (self.p_word2[1] != None) and (self.p_w[0] != None)
    
    def act171(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[2])
 ''',self.guard171,self.act171))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=True
        self.p_w_used[0]=True
    def guard171(self):
        return (self.p_word2[2] != None) and (self.p_w[0] != None)
    
    def act172(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[3])
 ''',self.guard172,self.act172))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[3])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=True
        self.p_w_used[0]=True
    def guard172(self):
        return (self.p_word2[3] != None) and (self.p_w[0] != None)
    
    def act173(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[4])
 ''',self.guard173,self.act173))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[4])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=True
        self.p_w_used[0]=True
    def guard173(self):
        return (self.p_word2[4] != None) and (self.p_w[0] != None)
    
    def act174(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[5])
 ''',self.guard174,self.act174))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[5])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=True
        self.p_w_used[0]=True
    def guard174(self):
        return (self.p_word2[5] != None) and (self.p_w[0] != None)
    
    def act175(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[6])
 ''',self.guard175,self.act175))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[6])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=True
        self.p_w_used[0]=True
    def guard175(self):
        return (self.p_word2[6] != None) and (self.p_w[0] != None)
    
    def act176(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word2[7])
 ''',self.guard176,self.act176))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word2[7])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=True
        self.p_w_used[0]=True
    def guard176(self):
        return (self.p_word2[7] != None) and (self.p_w[0] != None)
    
    def act177(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word3[0])
 ''',self.guard177,self.act177))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word3[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=True
        self.p_w_used[0]=True
    def guard177(self):
        return (self.p_word3[0] != None) and (self.p_w[0] != None)
    
    def act178(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word3[1])
 ''',self.guard178,self.act178))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word3[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=True
        self.p_w_used[0]=True
    def guard178(self):
        return (self.p_word3[1] != None) and (self.p_w[0] != None)
    
    def act179(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word3[2])
 ''',self.guard179,self.act179))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word3[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=True
        self.p_w_used[0]=True
    def guard179(self):
        return (self.p_word3[2] != None) and (self.p_w[0] != None)
    
    def act180(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word4[0])
 ''',self.guard180,self.act180))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word4[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[0]=True
    def guard180(self):
        return (self.p_w[0] != None) and (self.p_word4[0] != None)
    
    def act181(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word4[1])
 ''',self.guard181,self.act181))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word4[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[1]=True
    def guard181(self):
        return (self.p_w[0] != None) and (self.p_word4[1] != None)
    
    def act182(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word4[2])
 ''',self.guard182,self.act182))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word4[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[2]=True
    def guard182(self):
        return (self.p_w[0] != None) and (self.p_word4[2] != None)
    
    def act183(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word5[0])
 ''',self.guard183,self.act183))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word5[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[0]=True
    def guard183(self):
        return (self.p_w[0] != None) and (self.p_word5[0] != None)
    
    def act184(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word5[1])
 ''',self.guard184,self.act184))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word5[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[1]=True
    def guard184(self):
        return (self.p_w[0] != None) and (self.p_word5[1] != None)
    
    def act185(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word5[2])
 ''',self.guard185,self.act185))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word5[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[2]=True
    def guard185(self):
        return (self.p_w[0] != None) and (self.p_word5[2] != None)
    
    def act186(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word6[0])
 ''',self.guard186,self.act186))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word6[0])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=True
        self.p_w_used[0]=True
    def guard186(self):
        return (self.p_word6[0] != None) and (self.p_w[0] != None)
    
    def act187(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word6[1])
 ''',self.guard187,self.act187))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word6[1])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=True
        self.p_w_used[0]=True
    def guard187(self):
        return (self.p_word6[1] != None) and (self.p_w[0] != None)
    
    def act188(self):
        self.__test.append(('''print self.p_w[0].get_initials(self.p_word6[2])
 ''',self.guard188,self.act188))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_initials(self.p_word6[2])

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=True
        self.p_w_used[0]=True
    def guard188(self):
        return (self.p_word6[2] != None) and (self.p_w[0] != None)
    
    def act189(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)
 ''',self.guard189,self.act189))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=True
        self.p_w_used[0]=True
    def guard189(self):
        return (self.p_word1[0] != None) and (self.p_w[0] != None)
    
    def act190(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)
 ''',self.guard190,self.act190))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=True
        self.p_w_used[0]=True
    def guard190(self):
        return (self.p_word1[1] != None) and (self.p_w[0] != None)
    
    def act191(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)
 ''',self.guard191,self.act191))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=True
        self.p_w_used[0]=True
    def guard191(self):
        return (self.p_word1[2] != None) and (self.p_w[0] != None)
    
    def act192(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)
 ''',self.guard192,self.act192))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=True
        self.p_w_used[0]=True
    def guard192(self):
        return (self.p_word1[3] != None) and (self.p_w[0] != None)
    
    def act193(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)
 ''',self.guard193,self.act193))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=True
        self.p_w_used[0]=True
    def guard193(self):
        return (self.p_word1[4] != None) and (self.p_w[0] != None)
    
    def act194(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)
 ''',self.guard194,self.act194))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=True
        self.p_w_used[0]=True
    def guard194(self):
        return (self.p_word1[5] != None) and (self.p_w[0] != None)
    
    def act195(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)
 ''',self.guard195,self.act195))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=True
        self.p_w_used[0]=True
    def guard195(self):
        return (self.p_word1[6] != None) and (self.p_w[0] != None)
    
    def act196(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)
 ''',self.guard196,self.act196))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=True
        self.p_w_used[0]=True
    def guard196(self):
        return (self.p_word1[7] != None) and (self.p_w[0] != None)
    
    def act197(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)
 ''',self.guard197,self.act197))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=True
        self.p_w_used[0]=True
    def guard197(self):
        return (self.p_word2[0] != None) and (self.p_w[0] != None)
    
    def act198(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)
 ''',self.guard198,self.act198))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=True
        self.p_w_used[0]=True
    def guard198(self):
        return (self.p_word2[1] != None) and (self.p_w[0] != None)
    
    def act199(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)
 ''',self.guard199,self.act199))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=True
        self.p_w_used[0]=True
    def guard199(self):
        return (self.p_word2[2] != None) and (self.p_w[0] != None)
    
    def act200(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)
 ''',self.guard200,self.act200))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=True
        self.p_w_used[0]=True
    def guard200(self):
        return (self.p_word2[3] != None) and (self.p_w[0] != None)
    
    def act201(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)
 ''',self.guard201,self.act201))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=True
        self.p_w_used[0]=True
    def guard201(self):
        return (self.p_word2[4] != None) and (self.p_w[0] != None)
    
    def act202(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)
 ''',self.guard202,self.act202))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=True
        self.p_w_used[0]=True
    def guard202(self):
        return (self.p_word2[5] != None) and (self.p_w[0] != None)
    
    def act203(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)
 ''',self.guard203,self.act203))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=True
        self.p_w_used[0]=True
    def guard203(self):
        return (self.p_word2[6] != None) and (self.p_w[0] != None)
    
    def act204(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)
 ''',self.guard204,self.act204))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=True
        self.p_w_used[0]=True
    def guard204(self):
        return (self.p_word2[7] != None) and (self.p_w[0] != None)
    
    def act205(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)
 ''',self.guard205,self.act205))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=True
        self.p_w_used[0]=True
    def guard205(self):
        return (self.p_word3[0] != None) and (self.p_w[0] != None)
    
    def act206(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)
 ''',self.guard206,self.act206))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=True
        self.p_w_used[0]=True
    def guard206(self):
        return (self.p_word3[1] != None) and (self.p_w[0] != None)
    
    def act207(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)
 ''',self.guard207,self.act207))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=True
        self.p_w_used[0]=True
    def guard207(self):
        return (self.p_word3[2] != None) and (self.p_w[0] != None)
    
    def act208(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)
 ''',self.guard208,self.act208))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[0]=True
    def guard208(self):
        return (self.p_w[0] != None) and (self.p_word4[0] != None)
    
    def act209(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)
 ''',self.guard209,self.act209))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[1]=True
    def guard209(self):
        return (self.p_w[0] != None) and (self.p_word4[1] != None)
    
    def act210(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)
 ''',self.guard210,self.act210))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[2]=True
    def guard210(self):
        return (self.p_w[0] != None) and (self.p_word4[2] != None)
    
    def act211(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)
 ''',self.guard211,self.act211))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[0]=True
    def guard211(self):
        return (self.p_w[0] != None) and (self.p_word5[0] != None)
    
    def act212(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)
 ''',self.guard212,self.act212))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[1]=True
    def guard212(self):
        return (self.p_w[0] != None) and (self.p_word5[1] != None)
    
    def act213(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)
 ''',self.guard213,self.act213))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[2]=True
    def guard213(self):
        return (self.p_w[0] != None) and (self.p_word5[2] != None)
    
    def act214(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)
 ''',self.guard214,self.act214))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=True
        self.p_w_used[0]=True
    def guard214(self):
        return (self.p_word6[0] != None) and (self.p_w[0] != None)
    
    def act215(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)
 ''',self.guard215,self.act215))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=True
        self.p_w_used[0]=True
    def guard215(self):
        return (self.p_word6[1] != None) and (self.p_w[0] != None)
    
    def act216(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)
 ''',self.guard216,self.act216))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=True
        self.p_w_used[0]=True
    def guard216(self):
        return (self.p_word6[2] != None) and (self.p_w[0] != None)
    
    def act217(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[0], ' ')
 ''',self.guard217,self.act217))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[0], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[0]=True
        self.p_w_used[0]=True
    def guard217(self):
        return (self.p_word1[0] != None) and (self.p_w[0] != None)
    
    def act218(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[1], ' ')
 ''',self.guard218,self.act218))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[1], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[1]=True
        self.p_w_used[0]=True
    def guard218(self):
        return (self.p_word1[1] != None) and (self.p_w[0] != None)
    
    def act219(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[2], ' ')
 ''',self.guard219,self.act219))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[2], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[2]=True
        self.p_w_used[0]=True
    def guard219(self):
        return (self.p_word1[2] != None) and (self.p_w[0] != None)
    
    def act220(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[3], ' ')
 ''',self.guard220,self.act220))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[3], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[3]=True
        self.p_w_used[0]=True
    def guard220(self):
        return (self.p_word1[3] != None) and (self.p_w[0] != None)
    
    def act221(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[4], ' ')
 ''',self.guard221,self.act221))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[4], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[4]=True
        self.p_w_used[0]=True
    def guard221(self):
        return (self.p_word1[4] != None) and (self.p_w[0] != None)
    
    def act222(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[5], ' ')
 ''',self.guard222,self.act222))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[5], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[5]=True
        self.p_w_used[0]=True
    def guard222(self):
        return (self.p_word1[5] != None) and (self.p_w[0] != None)
    
    def act223(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[6], ' ')
 ''',self.guard223,self.act223))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[6], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[6]=True
        self.p_w_used[0]=True
    def guard223(self):
        return (self.p_word1[6] != None) and (self.p_w[0] != None)
    
    def act224(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word1[7], ' ')
 ''',self.guard224,self.act224))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word1[7], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word1_used[7]=True
        self.p_w_used[0]=True
    def guard224(self):
        return (self.p_word1[7] != None) and (self.p_w[0] != None)
    
    def act225(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[0], ' ')
 ''',self.guard225,self.act225))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[0], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[0]=True
        self.p_w_used[0]=True
    def guard225(self):
        return (self.p_word2[0] != None) and (self.p_w[0] != None)
    
    def act226(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[1], ' ')
 ''',self.guard226,self.act226))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[1], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[1]=True
        self.p_w_used[0]=True
    def guard226(self):
        return (self.p_word2[1] != None) and (self.p_w[0] != None)
    
    def act227(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[2], ' ')
 ''',self.guard227,self.act227))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[2], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[2]=True
        self.p_w_used[0]=True
    def guard227(self):
        return (self.p_word2[2] != None) and (self.p_w[0] != None)
    
    def act228(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[3], ' ')
 ''',self.guard228,self.act228))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[3], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[3]=True
        self.p_w_used[0]=True
    def guard228(self):
        return (self.p_word2[3] != None) and (self.p_w[0] != None)
    
    def act229(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[4], ' ')
 ''',self.guard229,self.act229))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[4], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[4]=True
        self.p_w_used[0]=True
    def guard229(self):
        return (self.p_word2[4] != None) and (self.p_w[0] != None)
    
    def act230(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[5], ' ')
 ''',self.guard230,self.act230))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[5], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[5]=True
        self.p_w_used[0]=True
    def guard230(self):
        return (self.p_word2[5] != None) and (self.p_w[0] != None)
    
    def act231(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[6], ' ')
 ''',self.guard231,self.act231))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[6], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[6]=True
        self.p_w_used[0]=True
    def guard231(self):
        return (self.p_word2[6] != None) and (self.p_w[0] != None)
    
    def act232(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word2[7], ' ')
 ''',self.guard232,self.act232))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word2[7], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word2_used[7]=True
        self.p_w_used[0]=True
    def guard232(self):
        return (self.p_word2[7] != None) and (self.p_w[0] != None)
    
    def act233(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[0], ' ')
 ''',self.guard233,self.act233))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[0], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[0]=True
        self.p_w_used[0]=True
    def guard233(self):
        return (self.p_word3[0] != None) and (self.p_w[0] != None)
    
    def act234(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[1], ' ')
 ''',self.guard234,self.act234))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[1], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[1]=True
        self.p_w_used[0]=True
    def guard234(self):
        return (self.p_word3[1] != None) and (self.p_w[0] != None)
    
    def act235(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word3[2], ' ')
 ''',self.guard235,self.act235))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word3[2], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word3_used[2]=True
        self.p_w_used[0]=True
    def guard235(self):
        return (self.p_word3[2] != None) and (self.p_w[0] != None)
    
    def act236(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[0], ' ')
 ''',self.guard236,self.act236))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[0], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[0]=True
    def guard236(self):
        return (self.p_w[0] != None) and (self.p_word4[0] != None)
    
    def act237(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[1], ' ')
 ''',self.guard237,self.act237))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[1], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[1]=True
    def guard237(self):
        return (self.p_w[0] != None) and (self.p_word4[1] != None)
    
    def act238(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word4[2], ' ')
 ''',self.guard238,self.act238))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word4[2], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word4_used[2]=True
    def guard238(self):
        return (self.p_w[0] != None) and (self.p_word4[2] != None)
    
    def act239(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[0], ' ')
 ''',self.guard239,self.act239))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[0], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[0]=True
    def guard239(self):
        return (self.p_w[0] != None) and (self.p_word5[0] != None)
    
    def act240(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[1], ' ')
 ''',self.guard240,self.act240))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[1], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[1]=True
    def guard240(self):
        return (self.p_w[0] != None) and (self.p_word5[1] != None)
    
    def act241(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word5[2], ' ')
 ''',self.guard241,self.act241))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word5[2], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_w_used[0]=True
        self.p_word5_used[2]=True
    def guard241(self):
        return (self.p_w[0] != None) and (self.p_word5[2] != None)
    
    def act242(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[0], ' ')
 ''',self.guard242,self.act242))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[0], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[0]=True
        self.p_w_used[0]=True
    def guard242(self):
        return (self.p_word6[0] != None) and (self.p_w[0] != None)
    
    def act243(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[1], ' ')
 ''',self.guard243,self.act243))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[1], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[1]=True
        self.p_w_used[0]=True
    def guard243(self):
        return (self.p_word6[1] != None) and (self.p_w[0] != None)
    
    def act244(self):
        self.__test.append(('''print self.p_w[0].get_pinyin(self.p_word6[2], ' ')
 ''',self.guard244,self.act244))
        if self.__collectCov:
            self.__cov.start()
        try:
            test_before_each(self)
        except:
            pass
        try:
            print self.p_w[0].get_pinyin(self.p_word6[2], ' ')

        finally:
            try:
                test_after_each(self)
            except:
                pass
            if self.__collectCov:
                self.__cov.stop()
                self.__updateCov()
        self.p_word6_used[2]=True
        self.p_w_used[0]=True
    def guard244(self):
        return (self.p_word6[2] != None) and (self.p_w[0] != None)
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__features = []
        self.__replayBacktrack = False
        self.__cov = coverage.coverage(branch=True, source=[])
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
        self.p_word2 = {}
        self.p_word2_used = {}
        self.__pools.append("self.p_word2")
        self.p_word2[0] = None
        self.p_word2_used[0] = True
        self.p_word2[1] = None
        self.p_word2_used[1] = True
        self.p_word2[2] = None
        self.p_word2_used[2] = True
        self.p_word2[3] = None
        self.p_word2_used[3] = True
        self.p_word2[4] = None
        self.p_word2_used[4] = True
        self.p_word2[5] = None
        self.p_word2_used[5] = True
        self.p_word2[6] = None
        self.p_word2_used[6] = True
        self.p_word2[7] = None
        self.p_word2_used[7] = True
        self.p_word2[8] = None
        self.p_word2_used[8] = True
        self.p_word3 = {}
        self.p_word3_used = {}
        self.__pools.append("self.p_word3")
        self.p_word3[0] = None
        self.p_word3_used[0] = True
        self.p_word3[1] = None
        self.p_word3_used[1] = True
        self.p_word3[2] = None
        self.p_word3_used[2] = True
        self.p_word3[3] = None
        self.p_word3_used[3] = True
        self.p_word1 = {}
        self.p_word1_used = {}
        self.__pools.append("self.p_word1")
        self.p_word1[0] = None
        self.p_word1_used[0] = True
        self.p_word1[1] = None
        self.p_word1_used[1] = True
        self.p_word1[2] = None
        self.p_word1_used[2] = True
        self.p_word1[3] = None
        self.p_word1_used[3] = True
        self.p_word1[4] = None
        self.p_word1_used[4] = True
        self.p_word1[5] = None
        self.p_word1_used[5] = True
        self.p_word1[6] = None
        self.p_word1_used[6] = True
        self.p_word1[7] = None
        self.p_word1_used[7] = True
        self.p_word1[8] = None
        self.p_word1_used[8] = True
        self.p_word6 = {}
        self.p_word6_used = {}
        self.__pools.append("self.p_word6")
        self.p_word6[0] = None
        self.p_word6_used[0] = True
        self.p_word6[1] = None
        self.p_word6_used[1] = True
        self.p_word6[2] = None
        self.p_word6_used[2] = True
        self.p_word6[3] = None
        self.p_word6_used[3] = True
        self.p_w = {}
        self.p_w_used = {}
        self.__pools.append("self.p_w")
        self.p_w[0] = None
        self.p_w_used[0] = True
        self.p_w[1] = None
        self.p_w_used[1] = True
        self.p_word5 = {}
        self.p_word5_used = {}
        self.__pools.append("self.p_word5")
        self.p_word5[0] = None
        self.p_word5_used[0] = True
        self.p_word5[1] = None
        self.p_word5_used[1] = True
        self.p_word5[2] = None
        self.p_word5_used[2] = True
        self.p_word5[3] = None
        self.p_word5_used[3] = True
        self.p_word4 = {}
        self.p_word4_used = {}
        self.__pools.append("self.p_word4")
        self.p_word4[0] = None
        self.p_word4_used[0] = True
        self.p_word4[1] = None
        self.p_word4_used[1] = True
        self.p_word4[2] = None
        self.p_word4_used[2] = True
        self.p_word4[3] = None
        self.p_word4_used[3] = True
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
        self.__actions.append(('''self.p_w[0] = Pinyin()
 ''',self.guard0,self.act0))

        self.__names['''self.p_w[0] = Pinyin()
 '''] = ('''self.p_w[0] = Pinyin()
 ''',self.guard0,self.act0)

        self.__orderings['''self.p_w[0] = Pinyin()
 '''] = 1

        self.__okExcepts['''self.p_w[0] = Pinyin()
 '''] = ''''''

        self.__actions.append(('''self.p_word1[0] = u"骉: biao1"
 ''',self.guard1,self.act1))

        self.__names['''self.p_word1[0] = u"骉: biao1"
 '''] = ('''self.p_word1[0] = u"骉: biao1"
 ''',self.guard1,self.act1)

        self.__orderings['''self.p_word1[0] = u"骉: biao1"
 '''] = 2

        self.__okExcepts['''self.p_word1[0] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[0] = u"麤: cu1"
 ''',self.guard2,self.act2))

        self.__names['''self.p_word1[0] = u"麤: cu1"
 '''] = ('''self.p_word1[0] = u"麤: cu1"
 ''',self.guard2,self.act2)

        self.__orderings['''self.p_word1[0] = u"麤: cu1"
 '''] = 3

        self.__okExcepts['''self.p_word1[0] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[0] =  u"奡: ao4"
 ''',self.guard3,self.act3))

        self.__names['''self.p_word1[0] =  u"奡: ao4"
 '''] = ('''self.p_word1[0] =  u"奡: ao4"
 ''',self.guard3,self.act3)

        self.__orderings['''self.p_word1[0] =  u"奡: ao4"
 '''] = 4

        self.__okExcepts['''self.p_word1[0] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[0] = u"砳: le4"
 ''',self.guard4,self.act4))

        self.__names['''self.p_word1[0] = u"砳: le4"
 '''] = ('''self.p_word1[0] = u"砳: le4"
 ''',self.guard4,self.act4)

        self.__orderings['''self.p_word1[0] = u"砳: le4"
 '''] = 5

        self.__okExcepts['''self.p_word1[0] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[0] = u"嘂: jiao"
 ''',self.guard5,self.act5))

        self.__names['''self.p_word1[0] = u"嘂: jiao"
 '''] = ('''self.p_word1[0] = u"嘂: jiao"
 ''',self.guard5,self.act5)

        self.__orderings['''self.p_word1[0] = u"嘂: jiao"
 '''] = 6

        self.__okExcepts['''self.p_word1[0] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[1] = u"骉: biao1"
 ''',self.guard6,self.act6))

        self.__names['''self.p_word1[1] = u"骉: biao1"
 '''] = ('''self.p_word1[1] = u"骉: biao1"
 ''',self.guard6,self.act6)

        self.__orderings['''self.p_word1[1] = u"骉: biao1"
 '''] = 7

        self.__okExcepts['''self.p_word1[1] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[1] = u"麤: cu1"
 ''',self.guard7,self.act7))

        self.__names['''self.p_word1[1] = u"麤: cu1"
 '''] = ('''self.p_word1[1] = u"麤: cu1"
 ''',self.guard7,self.act7)

        self.__orderings['''self.p_word1[1] = u"麤: cu1"
 '''] = 8

        self.__okExcepts['''self.p_word1[1] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[1] =  u"奡: ao4"
 ''',self.guard8,self.act8))

        self.__names['''self.p_word1[1] =  u"奡: ao4"
 '''] = ('''self.p_word1[1] =  u"奡: ao4"
 ''',self.guard8,self.act8)

        self.__orderings['''self.p_word1[1] =  u"奡: ao4"
 '''] = 9

        self.__okExcepts['''self.p_word1[1] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[1] = u"砳: le4"
 ''',self.guard9,self.act9))

        self.__names['''self.p_word1[1] = u"砳: le4"
 '''] = ('''self.p_word1[1] = u"砳: le4"
 ''',self.guard9,self.act9)

        self.__orderings['''self.p_word1[1] = u"砳: le4"
 '''] = 10

        self.__okExcepts['''self.p_word1[1] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[1] = u"嘂: jiao"
 ''',self.guard10,self.act10))

        self.__names['''self.p_word1[1] = u"嘂: jiao"
 '''] = ('''self.p_word1[1] = u"嘂: jiao"
 ''',self.guard10,self.act10)

        self.__orderings['''self.p_word1[1] = u"嘂: jiao"
 '''] = 11

        self.__okExcepts['''self.p_word1[1] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[2] = u"骉: biao1"
 ''',self.guard11,self.act11))

        self.__names['''self.p_word1[2] = u"骉: biao1"
 '''] = ('''self.p_word1[2] = u"骉: biao1"
 ''',self.guard11,self.act11)

        self.__orderings['''self.p_word1[2] = u"骉: biao1"
 '''] = 12

        self.__okExcepts['''self.p_word1[2] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[2] = u"麤: cu1"
 ''',self.guard12,self.act12))

        self.__names['''self.p_word1[2] = u"麤: cu1"
 '''] = ('''self.p_word1[2] = u"麤: cu1"
 ''',self.guard12,self.act12)

        self.__orderings['''self.p_word1[2] = u"麤: cu1"
 '''] = 13

        self.__okExcepts['''self.p_word1[2] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[2] =  u"奡: ao4"
 ''',self.guard13,self.act13))

        self.__names['''self.p_word1[2] =  u"奡: ao4"
 '''] = ('''self.p_word1[2] =  u"奡: ao4"
 ''',self.guard13,self.act13)

        self.__orderings['''self.p_word1[2] =  u"奡: ao4"
 '''] = 14

        self.__okExcepts['''self.p_word1[2] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[2] = u"砳: le4"
 ''',self.guard14,self.act14))

        self.__names['''self.p_word1[2] = u"砳: le4"
 '''] = ('''self.p_word1[2] = u"砳: le4"
 ''',self.guard14,self.act14)

        self.__orderings['''self.p_word1[2] = u"砳: le4"
 '''] = 15

        self.__okExcepts['''self.p_word1[2] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[2] = u"嘂: jiao"
 ''',self.guard15,self.act15))

        self.__names['''self.p_word1[2] = u"嘂: jiao"
 '''] = ('''self.p_word1[2] = u"嘂: jiao"
 ''',self.guard15,self.act15)

        self.__orderings['''self.p_word1[2] = u"嘂: jiao"
 '''] = 16

        self.__okExcepts['''self.p_word1[2] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[3] = u"骉: biao1"
 ''',self.guard16,self.act16))

        self.__names['''self.p_word1[3] = u"骉: biao1"
 '''] = ('''self.p_word1[3] = u"骉: biao1"
 ''',self.guard16,self.act16)

        self.__orderings['''self.p_word1[3] = u"骉: biao1"
 '''] = 17

        self.__okExcepts['''self.p_word1[3] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[3] = u"麤: cu1"
 ''',self.guard17,self.act17))

        self.__names['''self.p_word1[3] = u"麤: cu1"
 '''] = ('''self.p_word1[3] = u"麤: cu1"
 ''',self.guard17,self.act17)

        self.__orderings['''self.p_word1[3] = u"麤: cu1"
 '''] = 18

        self.__okExcepts['''self.p_word1[3] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[3] =  u"奡: ao4"
 ''',self.guard18,self.act18))

        self.__names['''self.p_word1[3] =  u"奡: ao4"
 '''] = ('''self.p_word1[3] =  u"奡: ao4"
 ''',self.guard18,self.act18)

        self.__orderings['''self.p_word1[3] =  u"奡: ao4"
 '''] = 19

        self.__okExcepts['''self.p_word1[3] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[3] = u"砳: le4"
 ''',self.guard19,self.act19))

        self.__names['''self.p_word1[3] = u"砳: le4"
 '''] = ('''self.p_word1[3] = u"砳: le4"
 ''',self.guard19,self.act19)

        self.__orderings['''self.p_word1[3] = u"砳: le4"
 '''] = 20

        self.__okExcepts['''self.p_word1[3] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[3] = u"嘂: jiao"
 ''',self.guard20,self.act20))

        self.__names['''self.p_word1[3] = u"嘂: jiao"
 '''] = ('''self.p_word1[3] = u"嘂: jiao"
 ''',self.guard20,self.act20)

        self.__orderings['''self.p_word1[3] = u"嘂: jiao"
 '''] = 21

        self.__okExcepts['''self.p_word1[3] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[4] = u"骉: biao1"
 ''',self.guard21,self.act21))

        self.__names['''self.p_word1[4] = u"骉: biao1"
 '''] = ('''self.p_word1[4] = u"骉: biao1"
 ''',self.guard21,self.act21)

        self.__orderings['''self.p_word1[4] = u"骉: biao1"
 '''] = 22

        self.__okExcepts['''self.p_word1[4] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[4] = u"麤: cu1"
 ''',self.guard22,self.act22))

        self.__names['''self.p_word1[4] = u"麤: cu1"
 '''] = ('''self.p_word1[4] = u"麤: cu1"
 ''',self.guard22,self.act22)

        self.__orderings['''self.p_word1[4] = u"麤: cu1"
 '''] = 23

        self.__okExcepts['''self.p_word1[4] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[4] =  u"奡: ao4"
 ''',self.guard23,self.act23))

        self.__names['''self.p_word1[4] =  u"奡: ao4"
 '''] = ('''self.p_word1[4] =  u"奡: ao4"
 ''',self.guard23,self.act23)

        self.__orderings['''self.p_word1[4] =  u"奡: ao4"
 '''] = 24

        self.__okExcepts['''self.p_word1[4] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[4] = u"砳: le4"
 ''',self.guard24,self.act24))

        self.__names['''self.p_word1[4] = u"砳: le4"
 '''] = ('''self.p_word1[4] = u"砳: le4"
 ''',self.guard24,self.act24)

        self.__orderings['''self.p_word1[4] = u"砳: le4"
 '''] = 25

        self.__okExcepts['''self.p_word1[4] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[4] = u"嘂: jiao"
 ''',self.guard25,self.act25))

        self.__names['''self.p_word1[4] = u"嘂: jiao"
 '''] = ('''self.p_word1[4] = u"嘂: jiao"
 ''',self.guard25,self.act25)

        self.__orderings['''self.p_word1[4] = u"嘂: jiao"
 '''] = 26

        self.__okExcepts['''self.p_word1[4] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[5] = u"骉: biao1"
 ''',self.guard26,self.act26))

        self.__names['''self.p_word1[5] = u"骉: biao1"
 '''] = ('''self.p_word1[5] = u"骉: biao1"
 ''',self.guard26,self.act26)

        self.__orderings['''self.p_word1[5] = u"骉: biao1"
 '''] = 27

        self.__okExcepts['''self.p_word1[5] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[5] = u"麤: cu1"
 ''',self.guard27,self.act27))

        self.__names['''self.p_word1[5] = u"麤: cu1"
 '''] = ('''self.p_word1[5] = u"麤: cu1"
 ''',self.guard27,self.act27)

        self.__orderings['''self.p_word1[5] = u"麤: cu1"
 '''] = 28

        self.__okExcepts['''self.p_word1[5] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[5] =  u"奡: ao4"
 ''',self.guard28,self.act28))

        self.__names['''self.p_word1[5] =  u"奡: ao4"
 '''] = ('''self.p_word1[5] =  u"奡: ao4"
 ''',self.guard28,self.act28)

        self.__orderings['''self.p_word1[5] =  u"奡: ao4"
 '''] = 29

        self.__okExcepts['''self.p_word1[5] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[5] = u"砳: le4"
 ''',self.guard29,self.act29))

        self.__names['''self.p_word1[5] = u"砳: le4"
 '''] = ('''self.p_word1[5] = u"砳: le4"
 ''',self.guard29,self.act29)

        self.__orderings['''self.p_word1[5] = u"砳: le4"
 '''] = 30

        self.__okExcepts['''self.p_word1[5] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[5] = u"嘂: jiao"
 ''',self.guard30,self.act30))

        self.__names['''self.p_word1[5] = u"嘂: jiao"
 '''] = ('''self.p_word1[5] = u"嘂: jiao"
 ''',self.guard30,self.act30)

        self.__orderings['''self.p_word1[5] = u"嘂: jiao"
 '''] = 31

        self.__okExcepts['''self.p_word1[5] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[6] = u"骉: biao1"
 ''',self.guard31,self.act31))

        self.__names['''self.p_word1[6] = u"骉: biao1"
 '''] = ('''self.p_word1[6] = u"骉: biao1"
 ''',self.guard31,self.act31)

        self.__orderings['''self.p_word1[6] = u"骉: biao1"
 '''] = 32

        self.__okExcepts['''self.p_word1[6] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[6] = u"麤: cu1"
 ''',self.guard32,self.act32))

        self.__names['''self.p_word1[6] = u"麤: cu1"
 '''] = ('''self.p_word1[6] = u"麤: cu1"
 ''',self.guard32,self.act32)

        self.__orderings['''self.p_word1[6] = u"麤: cu1"
 '''] = 33

        self.__okExcepts['''self.p_word1[6] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[6] =  u"奡: ao4"
 ''',self.guard33,self.act33))

        self.__names['''self.p_word1[6] =  u"奡: ao4"
 '''] = ('''self.p_word1[6] =  u"奡: ao4"
 ''',self.guard33,self.act33)

        self.__orderings['''self.p_word1[6] =  u"奡: ao4"
 '''] = 34

        self.__okExcepts['''self.p_word1[6] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[6] = u"砳: le4"
 ''',self.guard34,self.act34))

        self.__names['''self.p_word1[6] = u"砳: le4"
 '''] = ('''self.p_word1[6] = u"砳: le4"
 ''',self.guard34,self.act34)

        self.__orderings['''self.p_word1[6] = u"砳: le4"
 '''] = 35

        self.__okExcepts['''self.p_word1[6] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[6] = u"嘂: jiao"
 ''',self.guard35,self.act35))

        self.__names['''self.p_word1[6] = u"嘂: jiao"
 '''] = ('''self.p_word1[6] = u"嘂: jiao"
 ''',self.guard35,self.act35)

        self.__orderings['''self.p_word1[6] = u"嘂: jiao"
 '''] = 36

        self.__okExcepts['''self.p_word1[6] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[7] = u"骉: biao1"
 ''',self.guard36,self.act36))

        self.__names['''self.p_word1[7] = u"骉: biao1"
 '''] = ('''self.p_word1[7] = u"骉: biao1"
 ''',self.guard36,self.act36)

        self.__orderings['''self.p_word1[7] = u"骉: biao1"
 '''] = 37

        self.__okExcepts['''self.p_word1[7] = u"骉: biao1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[7] = u"麤: cu1"
 ''',self.guard37,self.act37))

        self.__names['''self.p_word1[7] = u"麤: cu1"
 '''] = ('''self.p_word1[7] = u"麤: cu1"
 ''',self.guard37,self.act37)

        self.__orderings['''self.p_word1[7] = u"麤: cu1"
 '''] = 38

        self.__okExcepts['''self.p_word1[7] = u"麤: cu1"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[7] =  u"奡: ao4"
 ''',self.guard38,self.act38))

        self.__names['''self.p_word1[7] =  u"奡: ao4"
 '''] = ('''self.p_word1[7] =  u"奡: ao4"
 ''',self.guard38,self.act38)

        self.__orderings['''self.p_word1[7] =  u"奡: ao4"
 '''] = 39

        self.__okExcepts['''self.p_word1[7] =  u"奡: ao4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[7] = u"砳: le4"
 ''',self.guard39,self.act39))

        self.__names['''self.p_word1[7] = u"砳: le4"
 '''] = ('''self.p_word1[7] = u"砳: le4"
 ''',self.guard39,self.act39)

        self.__orderings['''self.p_word1[7] = u"砳: le4"
 '''] = 40

        self.__okExcepts['''self.p_word1[7] = u"砳: le4"
 '''] = ''''''

        self.__actions.append(('''self.p_word1[7] = u"嘂: jiao"
 ''',self.guard40,self.act40))

        self.__names['''self.p_word1[7] = u"嘂: jiao"
 '''] = ('''self.p_word1[7] = u"嘂: jiao"
 ''',self.guard40,self.act40)

        self.__orderings['''self.p_word1[7] = u"嘂: jiao"
 '''] = 41

        self.__okExcepts['''self.p_word1[7] = u"嘂: jiao"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] = u"蛤蚌"
 ''',self.guard41,self.act41))

        self.__names['''self.p_word2[0] = u"蛤蚌"
 '''] = ('''self.p_word2[0] = u"蛤蚌"
 ''',self.guard41,self.act41)

        self.__orderings['''self.p_word2[0] = u"蛤蚌"
 '''] = 42

        self.__okExcepts['''self.p_word2[0] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] = u"蚌埠"
 ''',self.guard42,self.act42))

        self.__names['''self.p_word2[0] = u"蚌埠"
 '''] = ('''self.p_word2[0] = u"蚌埠"
 ''',self.guard42,self.act42)

        self.__orderings['''self.p_word2[0] = u"蚌埠"
 '''] = 43

        self.__okExcepts['''self.p_word2[0] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] =  u"纸薄"
 ''',self.guard43,self.act43))

        self.__names['''self.p_word2[0] =  u"纸薄"
 '''] = ('''self.p_word2[0] =  u"纸薄"
 ''',self.guard43,self.act43)

        self.__orderings['''self.p_word2[0] =  u"纸薄"
 '''] = 44

        self.__okExcepts['''self.p_word2[0] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] = u"稀薄"
 ''',self.guard44,self.act44))

        self.__names['''self.p_word2[0] = u"稀薄"
 '''] = ('''self.p_word2[0] = u"稀薄"
 ''',self.guard44,self.act44)

        self.__orderings['''self.p_word2[0] = u"稀薄"
 '''] = 45

        self.__okExcepts['''self.p_word2[0] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] = u"碉堡"
 ''',self.guard45,self.act45))

        self.__names['''self.p_word2[0] = u"碉堡"
 '''] = ('''self.p_word2[0] = u"碉堡"
 ''',self.guard45,self.act45)

        self.__orderings['''self.p_word2[0] = u"碉堡"
 '''] = 46

        self.__okExcepts['''self.p_word2[0] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] = u"瓦窑堡"
 ''',self.guard46,self.act46))

        self.__names['''self.p_word2[0] = u"瓦窑堡"
 '''] = ('''self.p_word2[0] = u"瓦窑堡"
 ''',self.guard46,self.act46)

        self.__orderings['''self.p_word2[0] = u"瓦窑堡"
 '''] = 47

        self.__okExcepts['''self.p_word2[0] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[0] = u"十里堡"
 ''',self.guard47,self.act47))

        self.__names['''self.p_word2[0] = u"十里堡"
 '''] = ('''self.p_word2[0] = u"十里堡"
 ''',self.guard47,self.act47)

        self.__orderings['''self.p_word2[0] = u"十里堡"
 '''] = 48

        self.__okExcepts['''self.p_word2[0] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] = u"蛤蚌"
 ''',self.guard48,self.act48))

        self.__names['''self.p_word2[1] = u"蛤蚌"
 '''] = ('''self.p_word2[1] = u"蛤蚌"
 ''',self.guard48,self.act48)

        self.__orderings['''self.p_word2[1] = u"蛤蚌"
 '''] = 49

        self.__okExcepts['''self.p_word2[1] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] = u"蚌埠"
 ''',self.guard49,self.act49))

        self.__names['''self.p_word2[1] = u"蚌埠"
 '''] = ('''self.p_word2[1] = u"蚌埠"
 ''',self.guard49,self.act49)

        self.__orderings['''self.p_word2[1] = u"蚌埠"
 '''] = 50

        self.__okExcepts['''self.p_word2[1] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] =  u"纸薄"
 ''',self.guard50,self.act50))

        self.__names['''self.p_word2[1] =  u"纸薄"
 '''] = ('''self.p_word2[1] =  u"纸薄"
 ''',self.guard50,self.act50)

        self.__orderings['''self.p_word2[1] =  u"纸薄"
 '''] = 51

        self.__okExcepts['''self.p_word2[1] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] = u"稀薄"
 ''',self.guard51,self.act51))

        self.__names['''self.p_word2[1] = u"稀薄"
 '''] = ('''self.p_word2[1] = u"稀薄"
 ''',self.guard51,self.act51)

        self.__orderings['''self.p_word2[1] = u"稀薄"
 '''] = 52

        self.__okExcepts['''self.p_word2[1] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] = u"碉堡"
 ''',self.guard52,self.act52))

        self.__names['''self.p_word2[1] = u"碉堡"
 '''] = ('''self.p_word2[1] = u"碉堡"
 ''',self.guard52,self.act52)

        self.__orderings['''self.p_word2[1] = u"碉堡"
 '''] = 53

        self.__okExcepts['''self.p_word2[1] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] = u"瓦窑堡"
 ''',self.guard53,self.act53))

        self.__names['''self.p_word2[1] = u"瓦窑堡"
 '''] = ('''self.p_word2[1] = u"瓦窑堡"
 ''',self.guard53,self.act53)

        self.__orderings['''self.p_word2[1] = u"瓦窑堡"
 '''] = 54

        self.__okExcepts['''self.p_word2[1] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[1] = u"十里堡"
 ''',self.guard54,self.act54))

        self.__names['''self.p_word2[1] = u"十里堡"
 '''] = ('''self.p_word2[1] = u"十里堡"
 ''',self.guard54,self.act54)

        self.__orderings['''self.p_word2[1] = u"十里堡"
 '''] = 55

        self.__okExcepts['''self.p_word2[1] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] = u"蛤蚌"
 ''',self.guard55,self.act55))

        self.__names['''self.p_word2[2] = u"蛤蚌"
 '''] = ('''self.p_word2[2] = u"蛤蚌"
 ''',self.guard55,self.act55)

        self.__orderings['''self.p_word2[2] = u"蛤蚌"
 '''] = 56

        self.__okExcepts['''self.p_word2[2] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] = u"蚌埠"
 ''',self.guard56,self.act56))

        self.__names['''self.p_word2[2] = u"蚌埠"
 '''] = ('''self.p_word2[2] = u"蚌埠"
 ''',self.guard56,self.act56)

        self.__orderings['''self.p_word2[2] = u"蚌埠"
 '''] = 57

        self.__okExcepts['''self.p_word2[2] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] =  u"纸薄"
 ''',self.guard57,self.act57))

        self.__names['''self.p_word2[2] =  u"纸薄"
 '''] = ('''self.p_word2[2] =  u"纸薄"
 ''',self.guard57,self.act57)

        self.__orderings['''self.p_word2[2] =  u"纸薄"
 '''] = 58

        self.__okExcepts['''self.p_word2[2] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] = u"稀薄"
 ''',self.guard58,self.act58))

        self.__names['''self.p_word2[2] = u"稀薄"
 '''] = ('''self.p_word2[2] = u"稀薄"
 ''',self.guard58,self.act58)

        self.__orderings['''self.p_word2[2] = u"稀薄"
 '''] = 59

        self.__okExcepts['''self.p_word2[2] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] = u"碉堡"
 ''',self.guard59,self.act59))

        self.__names['''self.p_word2[2] = u"碉堡"
 '''] = ('''self.p_word2[2] = u"碉堡"
 ''',self.guard59,self.act59)

        self.__orderings['''self.p_word2[2] = u"碉堡"
 '''] = 60

        self.__okExcepts['''self.p_word2[2] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] = u"瓦窑堡"
 ''',self.guard60,self.act60))

        self.__names['''self.p_word2[2] = u"瓦窑堡"
 '''] = ('''self.p_word2[2] = u"瓦窑堡"
 ''',self.guard60,self.act60)

        self.__orderings['''self.p_word2[2] = u"瓦窑堡"
 '''] = 61

        self.__okExcepts['''self.p_word2[2] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[2] = u"十里堡"
 ''',self.guard61,self.act61))

        self.__names['''self.p_word2[2] = u"十里堡"
 '''] = ('''self.p_word2[2] = u"十里堡"
 ''',self.guard61,self.act61)

        self.__orderings['''self.p_word2[2] = u"十里堡"
 '''] = 62

        self.__okExcepts['''self.p_word2[2] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] = u"蛤蚌"
 ''',self.guard62,self.act62))

        self.__names['''self.p_word2[3] = u"蛤蚌"
 '''] = ('''self.p_word2[3] = u"蛤蚌"
 ''',self.guard62,self.act62)

        self.__orderings['''self.p_word2[3] = u"蛤蚌"
 '''] = 63

        self.__okExcepts['''self.p_word2[3] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] = u"蚌埠"
 ''',self.guard63,self.act63))

        self.__names['''self.p_word2[3] = u"蚌埠"
 '''] = ('''self.p_word2[3] = u"蚌埠"
 ''',self.guard63,self.act63)

        self.__orderings['''self.p_word2[3] = u"蚌埠"
 '''] = 64

        self.__okExcepts['''self.p_word2[3] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] =  u"纸薄"
 ''',self.guard64,self.act64))

        self.__names['''self.p_word2[3] =  u"纸薄"
 '''] = ('''self.p_word2[3] =  u"纸薄"
 ''',self.guard64,self.act64)

        self.__orderings['''self.p_word2[3] =  u"纸薄"
 '''] = 65

        self.__okExcepts['''self.p_word2[3] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] = u"稀薄"
 ''',self.guard65,self.act65))

        self.__names['''self.p_word2[3] = u"稀薄"
 '''] = ('''self.p_word2[3] = u"稀薄"
 ''',self.guard65,self.act65)

        self.__orderings['''self.p_word2[3] = u"稀薄"
 '''] = 66

        self.__okExcepts['''self.p_word2[3] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] = u"碉堡"
 ''',self.guard66,self.act66))

        self.__names['''self.p_word2[3] = u"碉堡"
 '''] = ('''self.p_word2[3] = u"碉堡"
 ''',self.guard66,self.act66)

        self.__orderings['''self.p_word2[3] = u"碉堡"
 '''] = 67

        self.__okExcepts['''self.p_word2[3] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] = u"瓦窑堡"
 ''',self.guard67,self.act67))

        self.__names['''self.p_word2[3] = u"瓦窑堡"
 '''] = ('''self.p_word2[3] = u"瓦窑堡"
 ''',self.guard67,self.act67)

        self.__orderings['''self.p_word2[3] = u"瓦窑堡"
 '''] = 68

        self.__okExcepts['''self.p_word2[3] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[3] = u"十里堡"
 ''',self.guard68,self.act68))

        self.__names['''self.p_word2[3] = u"十里堡"
 '''] = ('''self.p_word2[3] = u"十里堡"
 ''',self.guard68,self.act68)

        self.__orderings['''self.p_word2[3] = u"十里堡"
 '''] = 69

        self.__okExcepts['''self.p_word2[3] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] = u"蛤蚌"
 ''',self.guard69,self.act69))

        self.__names['''self.p_word2[4] = u"蛤蚌"
 '''] = ('''self.p_word2[4] = u"蛤蚌"
 ''',self.guard69,self.act69)

        self.__orderings['''self.p_word2[4] = u"蛤蚌"
 '''] = 70

        self.__okExcepts['''self.p_word2[4] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] = u"蚌埠"
 ''',self.guard70,self.act70))

        self.__names['''self.p_word2[4] = u"蚌埠"
 '''] = ('''self.p_word2[4] = u"蚌埠"
 ''',self.guard70,self.act70)

        self.__orderings['''self.p_word2[4] = u"蚌埠"
 '''] = 71

        self.__okExcepts['''self.p_word2[4] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] =  u"纸薄"
 ''',self.guard71,self.act71))

        self.__names['''self.p_word2[4] =  u"纸薄"
 '''] = ('''self.p_word2[4] =  u"纸薄"
 ''',self.guard71,self.act71)

        self.__orderings['''self.p_word2[4] =  u"纸薄"
 '''] = 72

        self.__okExcepts['''self.p_word2[4] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] = u"稀薄"
 ''',self.guard72,self.act72))

        self.__names['''self.p_word2[4] = u"稀薄"
 '''] = ('''self.p_word2[4] = u"稀薄"
 ''',self.guard72,self.act72)

        self.__orderings['''self.p_word2[4] = u"稀薄"
 '''] = 73

        self.__okExcepts['''self.p_word2[4] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] = u"碉堡"
 ''',self.guard73,self.act73))

        self.__names['''self.p_word2[4] = u"碉堡"
 '''] = ('''self.p_word2[4] = u"碉堡"
 ''',self.guard73,self.act73)

        self.__orderings['''self.p_word2[4] = u"碉堡"
 '''] = 74

        self.__okExcepts['''self.p_word2[4] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] = u"瓦窑堡"
 ''',self.guard74,self.act74))

        self.__names['''self.p_word2[4] = u"瓦窑堡"
 '''] = ('''self.p_word2[4] = u"瓦窑堡"
 ''',self.guard74,self.act74)

        self.__orderings['''self.p_word2[4] = u"瓦窑堡"
 '''] = 75

        self.__okExcepts['''self.p_word2[4] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[4] = u"十里堡"
 ''',self.guard75,self.act75))

        self.__names['''self.p_word2[4] = u"十里堡"
 '''] = ('''self.p_word2[4] = u"十里堡"
 ''',self.guard75,self.act75)

        self.__orderings['''self.p_word2[4] = u"十里堡"
 '''] = 76

        self.__okExcepts['''self.p_word2[4] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] = u"蛤蚌"
 ''',self.guard76,self.act76))

        self.__names['''self.p_word2[5] = u"蛤蚌"
 '''] = ('''self.p_word2[5] = u"蛤蚌"
 ''',self.guard76,self.act76)

        self.__orderings['''self.p_word2[5] = u"蛤蚌"
 '''] = 77

        self.__okExcepts['''self.p_word2[5] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] = u"蚌埠"
 ''',self.guard77,self.act77))

        self.__names['''self.p_word2[5] = u"蚌埠"
 '''] = ('''self.p_word2[5] = u"蚌埠"
 ''',self.guard77,self.act77)

        self.__orderings['''self.p_word2[5] = u"蚌埠"
 '''] = 78

        self.__okExcepts['''self.p_word2[5] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] =  u"纸薄"
 ''',self.guard78,self.act78))

        self.__names['''self.p_word2[5] =  u"纸薄"
 '''] = ('''self.p_word2[5] =  u"纸薄"
 ''',self.guard78,self.act78)

        self.__orderings['''self.p_word2[5] =  u"纸薄"
 '''] = 79

        self.__okExcepts['''self.p_word2[5] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] = u"稀薄"
 ''',self.guard79,self.act79))

        self.__names['''self.p_word2[5] = u"稀薄"
 '''] = ('''self.p_word2[5] = u"稀薄"
 ''',self.guard79,self.act79)

        self.__orderings['''self.p_word2[5] = u"稀薄"
 '''] = 80

        self.__okExcepts['''self.p_word2[5] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] = u"碉堡"
 ''',self.guard80,self.act80))

        self.__names['''self.p_word2[5] = u"碉堡"
 '''] = ('''self.p_word2[5] = u"碉堡"
 ''',self.guard80,self.act80)

        self.__orderings['''self.p_word2[5] = u"碉堡"
 '''] = 81

        self.__okExcepts['''self.p_word2[5] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] = u"瓦窑堡"
 ''',self.guard81,self.act81))

        self.__names['''self.p_word2[5] = u"瓦窑堡"
 '''] = ('''self.p_word2[5] = u"瓦窑堡"
 ''',self.guard81,self.act81)

        self.__orderings['''self.p_word2[5] = u"瓦窑堡"
 '''] = 82

        self.__okExcepts['''self.p_word2[5] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[5] = u"十里堡"
 ''',self.guard82,self.act82))

        self.__names['''self.p_word2[5] = u"十里堡"
 '''] = ('''self.p_word2[5] = u"十里堡"
 ''',self.guard82,self.act82)

        self.__orderings['''self.p_word2[5] = u"十里堡"
 '''] = 83

        self.__okExcepts['''self.p_word2[5] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] = u"蛤蚌"
 ''',self.guard83,self.act83))

        self.__names['''self.p_word2[6] = u"蛤蚌"
 '''] = ('''self.p_word2[6] = u"蛤蚌"
 ''',self.guard83,self.act83)

        self.__orderings['''self.p_word2[6] = u"蛤蚌"
 '''] = 84

        self.__okExcepts['''self.p_word2[6] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] = u"蚌埠"
 ''',self.guard84,self.act84))

        self.__names['''self.p_word2[6] = u"蚌埠"
 '''] = ('''self.p_word2[6] = u"蚌埠"
 ''',self.guard84,self.act84)

        self.__orderings['''self.p_word2[6] = u"蚌埠"
 '''] = 85

        self.__okExcepts['''self.p_word2[6] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] =  u"纸薄"
 ''',self.guard85,self.act85))

        self.__names['''self.p_word2[6] =  u"纸薄"
 '''] = ('''self.p_word2[6] =  u"纸薄"
 ''',self.guard85,self.act85)

        self.__orderings['''self.p_word2[6] =  u"纸薄"
 '''] = 86

        self.__okExcepts['''self.p_word2[6] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] = u"稀薄"
 ''',self.guard86,self.act86))

        self.__names['''self.p_word2[6] = u"稀薄"
 '''] = ('''self.p_word2[6] = u"稀薄"
 ''',self.guard86,self.act86)

        self.__orderings['''self.p_word2[6] = u"稀薄"
 '''] = 87

        self.__okExcepts['''self.p_word2[6] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] = u"碉堡"
 ''',self.guard87,self.act87))

        self.__names['''self.p_word2[6] = u"碉堡"
 '''] = ('''self.p_word2[6] = u"碉堡"
 ''',self.guard87,self.act87)

        self.__orderings['''self.p_word2[6] = u"碉堡"
 '''] = 88

        self.__okExcepts['''self.p_word2[6] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] = u"瓦窑堡"
 ''',self.guard88,self.act88))

        self.__names['''self.p_word2[6] = u"瓦窑堡"
 '''] = ('''self.p_word2[6] = u"瓦窑堡"
 ''',self.guard88,self.act88)

        self.__orderings['''self.p_word2[6] = u"瓦窑堡"
 '''] = 89

        self.__okExcepts['''self.p_word2[6] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[6] = u"十里堡"
 ''',self.guard89,self.act89))

        self.__names['''self.p_word2[6] = u"十里堡"
 '''] = ('''self.p_word2[6] = u"十里堡"
 ''',self.guard89,self.act89)

        self.__orderings['''self.p_word2[6] = u"十里堡"
 '''] = 90

        self.__okExcepts['''self.p_word2[6] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] = u"蛤蚌"
 ''',self.guard90,self.act90))

        self.__names['''self.p_word2[7] = u"蛤蚌"
 '''] = ('''self.p_word2[7] = u"蛤蚌"
 ''',self.guard90,self.act90)

        self.__orderings['''self.p_word2[7] = u"蛤蚌"
 '''] = 91

        self.__okExcepts['''self.p_word2[7] = u"蛤蚌"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] = u"蚌埠"
 ''',self.guard91,self.act91))

        self.__names['''self.p_word2[7] = u"蚌埠"
 '''] = ('''self.p_word2[7] = u"蚌埠"
 ''',self.guard91,self.act91)

        self.__orderings['''self.p_word2[7] = u"蚌埠"
 '''] = 92

        self.__okExcepts['''self.p_word2[7] = u"蚌埠"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] =  u"纸薄"
 ''',self.guard92,self.act92))

        self.__names['''self.p_word2[7] =  u"纸薄"
 '''] = ('''self.p_word2[7] =  u"纸薄"
 ''',self.guard92,self.act92)

        self.__orderings['''self.p_word2[7] =  u"纸薄"
 '''] = 93

        self.__okExcepts['''self.p_word2[7] =  u"纸薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] = u"稀薄"
 ''',self.guard93,self.act93))

        self.__names['''self.p_word2[7] = u"稀薄"
 '''] = ('''self.p_word2[7] = u"稀薄"
 ''',self.guard93,self.act93)

        self.__orderings['''self.p_word2[7] = u"稀薄"
 '''] = 94

        self.__okExcepts['''self.p_word2[7] = u"稀薄"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] = u"碉堡"
 ''',self.guard94,self.act94))

        self.__names['''self.p_word2[7] = u"碉堡"
 '''] = ('''self.p_word2[7] = u"碉堡"
 ''',self.guard94,self.act94)

        self.__orderings['''self.p_word2[7] = u"碉堡"
 '''] = 95

        self.__okExcepts['''self.p_word2[7] = u"碉堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] = u"瓦窑堡"
 ''',self.guard95,self.act95))

        self.__names['''self.p_word2[7] = u"瓦窑堡"
 '''] = ('''self.p_word2[7] = u"瓦窑堡"
 ''',self.guard95,self.act95)

        self.__orderings['''self.p_word2[7] = u"瓦窑堡"
 '''] = 96

        self.__okExcepts['''self.p_word2[7] = u"瓦窑堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word2[7] = u"十里堡"
 ''',self.guard96,self.act96))

        self.__names['''self.p_word2[7] = u"十里堡"
 '''] = ('''self.p_word2[7] = u"十里堡"
 ''',self.guard96,self.act96)

        self.__orderings['''self.p_word2[7] = u"十里堡"
 '''] = 97

        self.__okExcepts['''self.p_word2[7] = u"十里堡"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard97,self.act97))

        self.__names['''self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = ('''self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard97,self.act97)

        self.__orderings['''self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = 98

        self.__okExcepts['''self.p_word3[0] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard98,self.act98))

        self.__names['''self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = ('''self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard98,self.act98)

        self.__orderings['''self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = 99

        self.__okExcepts['''self.p_word3[0] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard99,self.act99))

        self.__names['''self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = ('''self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard99,self.act99)

        self.__orderings['''self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = 100

        self.__okExcepts['''self.p_word3[0] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard100,self.act100))

        self.__names['''self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = ('''self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard100,self.act100)

        self.__orderings['''self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = 101

        self.__okExcepts['''self.p_word3[1] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard101,self.act101))

        self.__names['''self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = ('''self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard101,self.act101)

        self.__orderings['''self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = 102

        self.__okExcepts['''self.p_word3[1] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard102,self.act102))

        self.__names['''self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = ('''self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard102,self.act102)

        self.__orderings['''self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = 103

        self.__okExcepts['''self.p_word3[1] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard103,self.act103))

        self.__names['''self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = ('''self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 ''',self.guard103,self.act103)

        self.__orderings['''self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = 104

        self.__okExcepts['''self.p_word3[2] = u"一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提广场上喂食的是秃鹰我用漂亮的押韵形容被掠夺一空的爱情啊乌云开始遮蔽 夜色不干净公园里葬礼的回音在漫天飞行送你的白色玫瑰在纯黑的环境凋乌鸦在树枝上诡异的很安静静静听我黑色的大衣想温暖你日渐冰冷的回忆"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard104,self.act104))

        self.__names['''self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = ('''self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 ''',self.guard104,self.act104)

        self.__orderings['''self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = 105

        self.__okExcepts['''self.p_word3[2] = u"走过的走过的生命啊四周弥漫雾气我在空旷的墓地老去后还爱你为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印那些断翅的蜻蜓散落在这森林而我的眼睛没有丝毫同情失去你泪水混浊不清失去你我连笑容都有阴影风在长满青苔的屋顶嘲笑我的伤心像一口没有水的枯井我用凄美的字型描绘后悔莫及的那爱情"
 '''] = ''''''

        self.__actions.append(('''self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard105,self.act105))

        self.__names['''self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = ('''self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 ''',self.guard105,self.act105)

        self.__orderings['''self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = 106

        self.__okExcepts['''self.p_word3[2] = u"为你弹奏肖邦的夜曲纪念我死去的爱情跟夜风一样的声音心碎的很好听手在键盘敲很轻我给的思念很小心你埋葬的地方叫幽冥为你弹奏肖邦的夜曲纪念我死去的爱情而我为你隐姓埋名在月光下弹琴对你心跳的感应还是如此温热亲近怀念你那鲜红的唇印一群嗜血的蚂蚁被腐肉所吸引我面无表情看孤独的风景失去你爱恨开始分明失去你还有什么事好关心当鸽子不再象征和平我终于被提醒广场上喂食的是秃鹰我用漂亮的押韵 形容被掠夺一空的爱情"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard106,self.act106))

        self.__names['''self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = ('''self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard106,self.act106)

        self.__orderings['''self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = 107

        self.__okExcepts['''self.p_word4[0] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard107,self.act107))

        self.__names['''self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = ('''self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard107,self.act107)

        self.__orderings['''self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = 108

        self.__okExcepts['''self.p_word4[0] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard108,self.act108))

        self.__names['''self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = ('''self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard108,self.act108)

        self.__orderings['''self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = 109

        self.__okExcepts['''self.p_word4[0] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard109,self.act109))

        self.__names['''self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = ('''self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard109,self.act109)

        self.__orderings['''self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = 110

        self.__okExcepts['''self.p_word4[1] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard110,self.act110))

        self.__names['''self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = ('''self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard110,self.act110)

        self.__orderings['''self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = 111

        self.__okExcepts['''self.p_word4[1] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard111,self.act111))

        self.__names['''self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = ('''self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard111,self.act111)

        self.__orderings['''self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = 112

        self.__okExcepts['''self.p_word4[1] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard112,self.act112))

        self.__names['''self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = ('''self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 ''',self.guard112,self.act112)

        self.__orderings['''self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = 113

        self.__okExcepts['''self.p_word4[2] = u"东海之外大壑少昊之国少吴孺帝颛顼于此弃其琴瑟有甘山者甘水出焉生甘渊知大荒大荒东南隅有名皮母地丘古东海东海之外大荒之中有山名曰大言日月所出有波谷山者有大人之国斋有大有大人之市名曰大人之堂有"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard113,self.act113))

        self.__names['''self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = ('''self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 ''',self.guard113,self.act113)

        self.__orderings['''self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = 114

        self.__okExcepts['''self.p_word4[2] = u"一大人踆其上张其两耳主有小有小人国名靖人知有神有神人面身名曰霝鬼之尸古有有潏山杨水出斋有蔿有蔿国黍食使鸟虎豹熊罴主大荒大荒之中有山名曰合虚日月所出知"
 '''] = ''''''

        self.__actions.append(('''self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard114,self.act114))

        self.__names['''self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = ('''self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 ''',self.guard114,self.act114)

        self.__orderings['''self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = 115

        self.__okExcepts['''self.p_word4[2] = u"有中有中容之国帝俊生中容中容人食木实使四鸟豹虎熊罴古有东有东口之山有君子之国其人衣冠带剑斋有司有司幽之国帝俊生晏龙晏龙生司幽司幽生思土不妻思女不夫食黍食兽"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard115,self.act115))

        self.__names['''self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = ('''self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard115,self.act115)

        self.__orderings['''self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = 116

        self.__okExcepts['''self.p_word5[0] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard116,self.act116))

        self.__names['''self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = ('''self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard116,self.act116)

        self.__orderings['''self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = 117

        self.__okExcepts['''self.p_word5[0] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard117,self.act117))

        self.__names['''self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = ('''self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard117,self.act117)

        self.__orderings['''self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = 118

        self.__okExcepts['''self.p_word5[0] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard118,self.act118))

        self.__names['''self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = ('''self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard118,self.act118)

        self.__orderings['''self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = 119

        self.__okExcepts['''self.p_word5[1] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard119,self.act119))

        self.__names['''self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = ('''self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard119,self.act119)

        self.__orderings['''self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = 120

        self.__okExcepts['''self.p_word5[1] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard120,self.act120))

        self.__names['''self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = ('''self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard120,self.act120)

        self.__orderings['''self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = 121

        self.__okExcepts['''self.p_word5[1] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard121,self.act121))

        self.__names['''self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = ('''self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 ''',self.guard121,self.act121)

        self.__orderings['''self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = 122

        self.__okExcepts['''self.p_word5[2] = u"君不見黃河之水天上來奔流到海不複回君不見高堂明鏡悲白發朝如青絲暮成雪"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard122,self.act122))

        self.__names['''self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = ('''self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 ''',self.guard122,self.act122)

        self.__orderings['''self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = 123

        self.__okExcepts['''self.p_word5[2] = u"人生得意須盡歡莫使金樽空對月天生我材必有用千金散盡還複來烹羊宰牛且為樂會須一飲三百杯岑夫子丹丘生將進酒杯莫停與君歌一曲請君為我傾耳聽"
 '''] = ''''''

        self.__actions.append(('''self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard123,self.act123))

        self.__names['''self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = ('''self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 ''',self.guard123,self.act123)

        self.__orderings['''self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = 124

        self.__okExcepts['''self.p_word5[2] = u"鍾鼓馔玉不足貴但願長醉不複醒古來聖賢皆寞惟有飲者留其名陳王昔時宴平樂鬥酒十千恣歡谑主人何為言少錢徑須沽取對君酌五花馬千金裘呼兒將出換美酒與爾同銷萬古愁"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard124,self.act124))

        self.__names['''self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = ('''self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard124,self.act124)

        self.__orderings['''self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = 125

        self.__okExcepts['''self.p_word6[0] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard125,self.act125))

        self.__names['''self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = ('''self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard125,self.act125)

        self.__orderings['''self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = 126

        self.__okExcepts['''self.p_word6[0] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard126,self.act126))

        self.__names['''self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = ('''self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard126,self.act126)

        self.__orderings['''self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = 127

        self.__okExcepts['''self.p_word6[0] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard127,self.act127))

        self.__names['''self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = ('''self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard127,self.act127)

        self.__orderings['''self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = 128

        self.__okExcepts['''self.p_word6[1] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard128,self.act128))

        self.__names['''self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = ('''self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard128,self.act128)

        self.__orderings['''self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = 129

        self.__okExcepts['''self.p_word6[1] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard129,self.act129))

        self.__names['''self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = ('''self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard129,self.act129)

        self.__orderings['''self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = 130

        self.__okExcepts['''self.p_word6[1] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard130,self.act130))

        self.__names['''self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = ('''self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 ''',self.guard130,self.act130)

        self.__orderings['''self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = 131

        self.__okExcepts['''self.p_word6[2] = u"当前已经有一些流行的也比较成熟的软件产品能够很好地支持关系型数据模型"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard131,self.act131))

        self.__names['''self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = ('''self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 ''',self.guard131,self.act131)

        self.__orderings['''self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = 132

        self.__okExcepts['''self.p_word6[2] = u"这些产品也因此称为关系型数据库管理系统RelationaDataBasManagemeSystemRDBM例如微软公司Microsoft Access和MSSQLServerSybase公司的Sybase甲骨文公司"
 '''] = ''''''

        self.__actions.append(('''self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard132,self.act132))

        self.__names['''self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = ('''self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 ''',self.guard132,self.act132)

        self.__orderings['''self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = 133

        self.__okExcepts['''self.p_word6[2] = u"的Oracle以及IBM公司的DB2其MicrosoftAccess是一个中小型数据库管理系统适用于一般的中小企MSSQLServerSybase和Oracle基本属于大中型的数据库管理而DB2则属于大型的数库管理系统并且对计算机硬件有很高和专门的要求"
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[0])
 ''',self.guard133,self.act133))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[0])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[0])
 ''',self.guard133,self.act133)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[0])
 '''] = 134

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[1])
 ''',self.guard134,self.act134))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[1])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[1])
 ''',self.guard134,self.act134)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[1])
 '''] = 135

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[2])
 ''',self.guard135,self.act135))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[2])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[2])
 ''',self.guard135,self.act135)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[2])
 '''] = 136

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[3])
 ''',self.guard136,self.act136))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[3])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[3])
 ''',self.guard136,self.act136)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[3])
 '''] = 137

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[3])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[4])
 ''',self.guard137,self.act137))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[4])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[4])
 ''',self.guard137,self.act137)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[4])
 '''] = 138

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[4])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[5])
 ''',self.guard138,self.act138))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[5])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[5])
 ''',self.guard138,self.act138)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[5])
 '''] = 139

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[5])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[6])
 ''',self.guard139,self.act139))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[6])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[6])
 ''',self.guard139,self.act139)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[6])
 '''] = 140

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[6])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[7])
 ''',self.guard140,self.act140))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[7])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[7])
 ''',self.guard140,self.act140)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[7])
 '''] = 141

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[7])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[0])
 ''',self.guard141,self.act141))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[0])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[0])
 ''',self.guard141,self.act141)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[0])
 '''] = 142

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[1])
 ''',self.guard142,self.act142))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[1])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[1])
 ''',self.guard142,self.act142)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[1])
 '''] = 143

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[2])
 ''',self.guard143,self.act143))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[2])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[2])
 ''',self.guard143,self.act143)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[2])
 '''] = 144

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[3])
 ''',self.guard144,self.act144))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[3])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[3])
 ''',self.guard144,self.act144)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[3])
 '''] = 145

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[3])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[4])
 ''',self.guard145,self.act145))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[4])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[4])
 ''',self.guard145,self.act145)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[4])
 '''] = 146

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[4])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[5])
 ''',self.guard146,self.act146))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[5])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[5])
 ''',self.guard146,self.act146)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[5])
 '''] = 147

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[5])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[6])
 ''',self.guard147,self.act147))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[6])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[6])
 ''',self.guard147,self.act147)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[6])
 '''] = 148

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[6])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[7])
 ''',self.guard148,self.act148))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[7])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[7])
 ''',self.guard148,self.act148)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[7])
 '''] = 149

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[7])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[0])
 ''',self.guard149,self.act149))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[0])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[0])
 ''',self.guard149,self.act149)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[0])
 '''] = 150

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[1])
 ''',self.guard150,self.act150))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[1])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[1])
 ''',self.guard150,self.act150)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[1])
 '''] = 151

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[2])
 ''',self.guard151,self.act151))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[2])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[2])
 ''',self.guard151,self.act151)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[2])
 '''] = 152

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[0])
 ''',self.guard152,self.act152))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[0])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[0])
 ''',self.guard152,self.act152)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[0])
 '''] = 153

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[1])
 ''',self.guard153,self.act153))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[1])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[1])
 ''',self.guard153,self.act153)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[1])
 '''] = 154

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[2])
 ''',self.guard154,self.act154))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[2])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[2])
 ''',self.guard154,self.act154)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[2])
 '''] = 155

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[0])
 ''',self.guard155,self.act155))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[0])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[0])
 ''',self.guard155,self.act155)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[0])
 '''] = 156

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[1])
 ''',self.guard156,self.act156))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[1])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[1])
 ''',self.guard156,self.act156)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[1])
 '''] = 157

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[2])
 ''',self.guard157,self.act157))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[2])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[2])
 ''',self.guard157,self.act157)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[2])
 '''] = 158

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[0])
 ''',self.guard158,self.act158))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[0])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[0])
 ''',self.guard158,self.act158)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[0])
 '''] = 159

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[1])
 ''',self.guard159,self.act159))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[1])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[1])
 ''',self.guard159,self.act159)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[1])
 '''] = 160

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[2])
 ''',self.guard160,self.act160))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[2])
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[2])
 ''',self.guard160,self.act160)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[2])
 '''] = 161

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[0])
 ''',self.guard161,self.act161))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[0])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[0])
 ''',self.guard161,self.act161)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[0])
 '''] = 162

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[1])
 ''',self.guard162,self.act162))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[1])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[1])
 ''',self.guard162,self.act162)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[1])
 '''] = 163

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[2])
 ''',self.guard163,self.act163))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[2])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[2])
 ''',self.guard163,self.act163)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[2])
 '''] = 164

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[3])
 ''',self.guard164,self.act164))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[3])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[3])
 ''',self.guard164,self.act164)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[3])
 '''] = 165

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[3])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[4])
 ''',self.guard165,self.act165))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[4])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[4])
 ''',self.guard165,self.act165)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[4])
 '''] = 166

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[4])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[5])
 ''',self.guard166,self.act166))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[5])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[5])
 ''',self.guard166,self.act166)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[5])
 '''] = 167

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[5])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[6])
 ''',self.guard167,self.act167))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[6])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[6])
 ''',self.guard167,self.act167)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[6])
 '''] = 168

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[6])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word1[7])
 ''',self.guard168,self.act168))

        self.__names['''print self.p_w[0].get_initials(self.p_word1[7])
 '''] = ('''print self.p_w[0].get_initials(self.p_word1[7])
 ''',self.guard168,self.act168)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word1[7])
 '''] = 169

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word1[7])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[0])
 ''',self.guard169,self.act169))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[0])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[0])
 ''',self.guard169,self.act169)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[0])
 '''] = 170

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[1])
 ''',self.guard170,self.act170))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[1])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[1])
 ''',self.guard170,self.act170)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[1])
 '''] = 171

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[2])
 ''',self.guard171,self.act171))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[2])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[2])
 ''',self.guard171,self.act171)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[2])
 '''] = 172

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[3])
 ''',self.guard172,self.act172))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[3])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[3])
 ''',self.guard172,self.act172)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[3])
 '''] = 173

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[3])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[4])
 ''',self.guard173,self.act173))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[4])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[4])
 ''',self.guard173,self.act173)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[4])
 '''] = 174

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[4])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[5])
 ''',self.guard174,self.act174))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[5])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[5])
 ''',self.guard174,self.act174)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[5])
 '''] = 175

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[5])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[6])
 ''',self.guard175,self.act175))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[6])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[6])
 ''',self.guard175,self.act175)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[6])
 '''] = 176

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[6])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word2[7])
 ''',self.guard176,self.act176))

        self.__names['''print self.p_w[0].get_initials(self.p_word2[7])
 '''] = ('''print self.p_w[0].get_initials(self.p_word2[7])
 ''',self.guard176,self.act176)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word2[7])
 '''] = 177

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word2[7])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word3[0])
 ''',self.guard177,self.act177))

        self.__names['''print self.p_w[0].get_initials(self.p_word3[0])
 '''] = ('''print self.p_w[0].get_initials(self.p_word3[0])
 ''',self.guard177,self.act177)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word3[0])
 '''] = 178

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word3[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word3[1])
 ''',self.guard178,self.act178))

        self.__names['''print self.p_w[0].get_initials(self.p_word3[1])
 '''] = ('''print self.p_w[0].get_initials(self.p_word3[1])
 ''',self.guard178,self.act178)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word3[1])
 '''] = 179

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word3[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word3[2])
 ''',self.guard179,self.act179))

        self.__names['''print self.p_w[0].get_initials(self.p_word3[2])
 '''] = ('''print self.p_w[0].get_initials(self.p_word3[2])
 ''',self.guard179,self.act179)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word3[2])
 '''] = 180

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word3[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word4[0])
 ''',self.guard180,self.act180))

        self.__names['''print self.p_w[0].get_initials(self.p_word4[0])
 '''] = ('''print self.p_w[0].get_initials(self.p_word4[0])
 ''',self.guard180,self.act180)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word4[0])
 '''] = 181

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word4[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word4[1])
 ''',self.guard181,self.act181))

        self.__names['''print self.p_w[0].get_initials(self.p_word4[1])
 '''] = ('''print self.p_w[0].get_initials(self.p_word4[1])
 ''',self.guard181,self.act181)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word4[1])
 '''] = 182

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word4[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word4[2])
 ''',self.guard182,self.act182))

        self.__names['''print self.p_w[0].get_initials(self.p_word4[2])
 '''] = ('''print self.p_w[0].get_initials(self.p_word4[2])
 ''',self.guard182,self.act182)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word4[2])
 '''] = 183

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word4[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word5[0])
 ''',self.guard183,self.act183))

        self.__names['''print self.p_w[0].get_initials(self.p_word5[0])
 '''] = ('''print self.p_w[0].get_initials(self.p_word5[0])
 ''',self.guard183,self.act183)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word5[0])
 '''] = 184

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word5[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word5[1])
 ''',self.guard184,self.act184))

        self.__names['''print self.p_w[0].get_initials(self.p_word5[1])
 '''] = ('''print self.p_w[0].get_initials(self.p_word5[1])
 ''',self.guard184,self.act184)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word5[1])
 '''] = 185

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word5[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word5[2])
 ''',self.guard185,self.act185))

        self.__names['''print self.p_w[0].get_initials(self.p_word5[2])
 '''] = ('''print self.p_w[0].get_initials(self.p_word5[2])
 ''',self.guard185,self.act185)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word5[2])
 '''] = 186

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word5[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word6[0])
 ''',self.guard186,self.act186))

        self.__names['''print self.p_w[0].get_initials(self.p_word6[0])
 '''] = ('''print self.p_w[0].get_initials(self.p_word6[0])
 ''',self.guard186,self.act186)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word6[0])
 '''] = 187

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word6[0])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word6[1])
 ''',self.guard187,self.act187))

        self.__names['''print self.p_w[0].get_initials(self.p_word6[1])
 '''] = ('''print self.p_w[0].get_initials(self.p_word6[1])
 ''',self.guard187,self.act187)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word6[1])
 '''] = 188

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word6[1])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_initials(self.p_word6[2])
 ''',self.guard188,self.act188))

        self.__names['''print self.p_w[0].get_initials(self.p_word6[2])
 '''] = ('''print self.p_w[0].get_initials(self.p_word6[2])
 ''',self.guard188,self.act188)

        self.__orderings['''print self.p_w[0].get_initials(self.p_word6[2])
 '''] = 189

        self.__okExcepts['''print self.p_w[0].get_initials(self.p_word6[2])
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)
 ''',self.guard189,self.act189))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)
 ''',self.guard189,self.act189)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)
 '''] = 190

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[0], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)
 ''',self.guard190,self.act190))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)
 ''',self.guard190,self.act190)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)
 '''] = 191

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[1], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)
 ''',self.guard191,self.act191))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)
 ''',self.guard191,self.act191)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)
 '''] = 192

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[2], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)
 ''',self.guard192,self.act192))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)
 ''',self.guard192,self.act192)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)
 '''] = 193

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[3], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)
 ''',self.guard193,self.act193))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)
 ''',self.guard193,self.act193)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)
 '''] = 194

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[4], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)
 ''',self.guard194,self.act194))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)
 ''',self.guard194,self.act194)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)
 '''] = 195

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[5], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)
 ''',self.guard195,self.act195))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)
 ''',self.guard195,self.act195)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)
 '''] = 196

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[6], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)
 ''',self.guard196,self.act196))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)
 ''',self.guard196,self.act196)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)
 '''] = 197

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[7], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)
 ''',self.guard197,self.act197))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)
 ''',self.guard197,self.act197)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)
 '''] = 198

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[0], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)
 ''',self.guard198,self.act198))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)
 ''',self.guard198,self.act198)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)
 '''] = 199

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[1], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)
 ''',self.guard199,self.act199))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)
 ''',self.guard199,self.act199)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)
 '''] = 200

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[2], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)
 ''',self.guard200,self.act200))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)
 ''',self.guard200,self.act200)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)
 '''] = 201

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[3], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)
 ''',self.guard201,self.act201))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)
 ''',self.guard201,self.act201)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)
 '''] = 202

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[4], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)
 ''',self.guard202,self.act202))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)
 ''',self.guard202,self.act202)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)
 '''] = 203

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[5], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)
 ''',self.guard203,self.act203))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)
 ''',self.guard203,self.act203)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)
 '''] = 204

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[6], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)
 ''',self.guard204,self.act204))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)
 ''',self.guard204,self.act204)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)
 '''] = 205

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[7], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)
 ''',self.guard205,self.act205))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)
 ''',self.guard205,self.act205)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)
 '''] = 206

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[0], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)
 ''',self.guard206,self.act206))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)
 ''',self.guard206,self.act206)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)
 '''] = 207

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[1], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)
 ''',self.guard207,self.act207))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)
 ''',self.guard207,self.act207)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)
 '''] = 208

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[2], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)
 ''',self.guard208,self.act208))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)
 ''',self.guard208,self.act208)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)
 '''] = 209

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[0], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)
 ''',self.guard209,self.act209))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)
 ''',self.guard209,self.act209)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)
 '''] = 210

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[1], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)
 ''',self.guard210,self.act210))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)
 ''',self.guard210,self.act210)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)
 '''] = 211

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[2], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)
 ''',self.guard211,self.act211))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)
 ''',self.guard211,self.act211)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)
 '''] = 212

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[0], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)
 ''',self.guard212,self.act212))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)
 ''',self.guard212,self.act212)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)
 '''] = 213

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[1], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)
 ''',self.guard213,self.act213))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)
 ''',self.guard213,self.act213)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)
 '''] = 214

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[2], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)
 ''',self.guard214,self.act214))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)
 ''',self.guard214,self.act214)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)
 '''] = 215

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[0], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)
 ''',self.guard215,self.act215))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)
 ''',self.guard215,self.act215)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)
 '''] = 216

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[1], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)
 ''',self.guard216,self.act216))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)
 ''',self.guard216,self.act216)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)
 '''] = 217

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[2], show_tone_marks=True)
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[0], ' ')
 ''',self.guard217,self.act217))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[0], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[0], ' ')
 ''',self.guard217,self.act217)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[0], ' ')
 '''] = 218

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[0], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[1], ' ')
 ''',self.guard218,self.act218))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[1], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[1], ' ')
 ''',self.guard218,self.act218)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[1], ' ')
 '''] = 219

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[1], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[2], ' ')
 ''',self.guard219,self.act219))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[2], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[2], ' ')
 ''',self.guard219,self.act219)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[2], ' ')
 '''] = 220

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[2], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[3], ' ')
 ''',self.guard220,self.act220))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[3], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[3], ' ')
 ''',self.guard220,self.act220)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[3], ' ')
 '''] = 221

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[3], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[4], ' ')
 ''',self.guard221,self.act221))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[4], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[4], ' ')
 ''',self.guard221,self.act221)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[4], ' ')
 '''] = 222

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[4], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[5], ' ')
 ''',self.guard222,self.act222))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[5], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[5], ' ')
 ''',self.guard222,self.act222)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[5], ' ')
 '''] = 223

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[5], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[6], ' ')
 ''',self.guard223,self.act223))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[6], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[6], ' ')
 ''',self.guard223,self.act223)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[6], ' ')
 '''] = 224

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[6], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word1[7], ' ')
 ''',self.guard224,self.act224))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word1[7], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word1[7], ' ')
 ''',self.guard224,self.act224)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word1[7], ' ')
 '''] = 225

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word1[7], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[0], ' ')
 ''',self.guard225,self.act225))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[0], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[0], ' ')
 ''',self.guard225,self.act225)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[0], ' ')
 '''] = 226

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[0], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[1], ' ')
 ''',self.guard226,self.act226))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[1], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[1], ' ')
 ''',self.guard226,self.act226)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[1], ' ')
 '''] = 227

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[1], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[2], ' ')
 ''',self.guard227,self.act227))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[2], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[2], ' ')
 ''',self.guard227,self.act227)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[2], ' ')
 '''] = 228

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[2], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[3], ' ')
 ''',self.guard228,self.act228))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[3], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[3], ' ')
 ''',self.guard228,self.act228)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[3], ' ')
 '''] = 229

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[3], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[4], ' ')
 ''',self.guard229,self.act229))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[4], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[4], ' ')
 ''',self.guard229,self.act229)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[4], ' ')
 '''] = 230

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[4], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[5], ' ')
 ''',self.guard230,self.act230))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[5], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[5], ' ')
 ''',self.guard230,self.act230)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[5], ' ')
 '''] = 231

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[5], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[6], ' ')
 ''',self.guard231,self.act231))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[6], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[6], ' ')
 ''',self.guard231,self.act231)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[6], ' ')
 '''] = 232

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[6], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word2[7], ' ')
 ''',self.guard232,self.act232))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word2[7], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word2[7], ' ')
 ''',self.guard232,self.act232)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word2[7], ' ')
 '''] = 233

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word2[7], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[0], ' ')
 ''',self.guard233,self.act233))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[0], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[0], ' ')
 ''',self.guard233,self.act233)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[0], ' ')
 '''] = 234

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[0], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[1], ' ')
 ''',self.guard234,self.act234))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[1], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[1], ' ')
 ''',self.guard234,self.act234)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[1], ' ')
 '''] = 235

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[1], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word3[2], ' ')
 ''',self.guard235,self.act235))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word3[2], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word3[2], ' ')
 ''',self.guard235,self.act235)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word3[2], ' ')
 '''] = 236

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word3[2], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[0], ' ')
 ''',self.guard236,self.act236))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[0], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[0], ' ')
 ''',self.guard236,self.act236)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[0], ' ')
 '''] = 237

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[0], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[1], ' ')
 ''',self.guard237,self.act237))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[1], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[1], ' ')
 ''',self.guard237,self.act237)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[1], ' ')
 '''] = 238

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[1], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word4[2], ' ')
 ''',self.guard238,self.act238))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word4[2], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word4[2], ' ')
 ''',self.guard238,self.act238)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word4[2], ' ')
 '''] = 239

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word4[2], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[0], ' ')
 ''',self.guard239,self.act239))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[0], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[0], ' ')
 ''',self.guard239,self.act239)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[0], ' ')
 '''] = 240

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[0], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[1], ' ')
 ''',self.guard240,self.act240))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[1], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[1], ' ')
 ''',self.guard240,self.act240)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[1], ' ')
 '''] = 241

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[1], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word5[2], ' ')
 ''',self.guard241,self.act241))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word5[2], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word5[2], ' ')
 ''',self.guard241,self.act241)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word5[2], ' ')
 '''] = 242

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word5[2], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[0], ' ')
 ''',self.guard242,self.act242))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[0], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[0], ' ')
 ''',self.guard242,self.act242)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[0], ' ')
 '''] = 243

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[0], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[1], ' ')
 ''',self.guard243,self.act243))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[1], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[1], ' ')
 ''',self.guard243,self.act243)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[1], ' ')
 '''] = 244

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[1], ' ')
 '''] = ''''''

        self.__actions.append(('''print self.p_w[0].get_pinyin(self.p_word6[2], ' ')
 ''',self.guard244,self.act244))

        self.__names['''print self.p_w[0].get_pinyin(self.p_word6[2], ' ')
 '''] = ('''print self.p_w[0].get_pinyin(self.p_word6[2], ' ')
 ''',self.guard244,self.act244)

        self.__orderings['''print self.p_w[0].get_pinyin(self.p_word6[2], ' ')
 '''] = 245

        self.__okExcepts['''print self.p_w[0].get_pinyin(self.p_word6[2], ' ')
 '''] = ''''''

        self.__actions_backup = list(self.__actions)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
        self.cleanCov()
    # BEGIN RELOAD CODE
    # END RELOAD CODE
        self.__test = []
        self.__pools = []
        self.__consts = []
        self.p_word2 = {}
        self.p_word2_used = {}
        self.__pools.append("self.p_word2")
        self.p_word2[0] = None
        self.p_word2_used[0] = True
        self.p_word2[1] = None
        self.p_word2_used[1] = True
        self.p_word2[2] = None
        self.p_word2_used[2] = True
        self.p_word2[3] = None
        self.p_word2_used[3] = True
        self.p_word2[4] = None
        self.p_word2_used[4] = True
        self.p_word2[5] = None
        self.p_word2_used[5] = True
        self.p_word2[6] = None
        self.p_word2_used[6] = True
        self.p_word2[7] = None
        self.p_word2_used[7] = True
        self.p_word2[8] = None
        self.p_word2_used[8] = True
        self.p_word3 = {}
        self.p_word3_used = {}
        self.__pools.append("self.p_word3")
        self.p_word3[0] = None
        self.p_word3_used[0] = True
        self.p_word3[1] = None
        self.p_word3_used[1] = True
        self.p_word3[2] = None
        self.p_word3_used[2] = True
        self.p_word3[3] = None
        self.p_word3_used[3] = True
        self.p_word1 = {}
        self.p_word1_used = {}
        self.__pools.append("self.p_word1")
        self.p_word1[0] = None
        self.p_word1_used[0] = True
        self.p_word1[1] = None
        self.p_word1_used[1] = True
        self.p_word1[2] = None
        self.p_word1_used[2] = True
        self.p_word1[3] = None
        self.p_word1_used[3] = True
        self.p_word1[4] = None
        self.p_word1_used[4] = True
        self.p_word1[5] = None
        self.p_word1_used[5] = True
        self.p_word1[6] = None
        self.p_word1_used[6] = True
        self.p_word1[7] = None
        self.p_word1_used[7] = True
        self.p_word1[8] = None
        self.p_word1_used[8] = True
        self.p_word6 = {}
        self.p_word6_used = {}
        self.__pools.append("self.p_word6")
        self.p_word6[0] = None
        self.p_word6_used[0] = True
        self.p_word6[1] = None
        self.p_word6_used[1] = True
        self.p_word6[2] = None
        self.p_word6_used[2] = True
        self.p_word6[3] = None
        self.p_word6_used[3] = True
        self.p_w = {}
        self.p_w_used = {}
        self.__pools.append("self.p_w")
        self.p_w[0] = None
        self.p_w_used[0] = True
        self.p_w[1] = None
        self.p_w_used[1] = True
        self.p_word5 = {}
        self.p_word5_used = {}
        self.__pools.append("self.p_word5")
        self.p_word5[0] = None
        self.p_word5_used[0] = True
        self.p_word5[1] = None
        self.p_word5_used[1] = True
        self.p_word5[2] = None
        self.p_word5_used[2] = True
        self.p_word5[3] = None
        self.p_word5_used[3] = True
        self.p_word4 = {}
        self.p_word4_used = {}
        self.__pools.append("self.p_word4")
        self.p_word4[0] = None
        self.p_word4_used[0] = True
        self.p_word4[1] = None
        self.p_word4_used[1] = True
        self.p_word4[2] = None
        self.p_word4_used[2] = True
        self.p_word4[3] = None
        self.p_word4_used[3] = True
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
        return [ copy.deepcopy(self.p_word2),copy.deepcopy(self.p_word2_used),copy.deepcopy(self.p_word3),copy.deepcopy(self.p_word3_used),copy.deepcopy(self.p_word1),copy.deepcopy(self.p_word1_used),copy.deepcopy(self.p_word6),copy.deepcopy(self.p_word6_used),copy.deepcopy(self.p_w),copy.deepcopy(self.p_w_used),copy.deepcopy(self.p_word5),copy.deepcopy(self.p_word5_used),copy.deepcopy(self.p_word4),copy.deepcopy(self.p_word4_used)]
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.p_word2 = copy.deepcopy(old[0])
        self.p_word2_used = copy.deepcopy(old[1])
        self.p_word3 = copy.deepcopy(old[2])
        self.p_word3_used = copy.deepcopy(old[3])
        self.p_word1 = copy.deepcopy(old[4])
        self.p_word1_used = copy.deepcopy(old[5])
        self.p_word6 = copy.deepcopy(old[6])
        self.p_word6_used = copy.deepcopy(old[7])
        self.p_w = copy.deepcopy(old[8])
        self.p_w_used = copy.deepcopy(old[9])
        self.p_word5 = copy.deepcopy(old[10])
        self.p_word5_used = copy.deepcopy(old[11])
        self.p_word4 = copy.deepcopy(old[12])
        self.p_word4_used = copy.deepcopy(old[13])
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
