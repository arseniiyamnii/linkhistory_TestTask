#!/usr/bin/env python3
import unittest
from server import *
import time
class TestDBMS(unittest.TestCase):
    def setUp(self):
        self.db=DBMS()
    def test_gettingKeysListType(self):
        self.assertEqual(isinstance(self.db.getAllKeys(),list),True)
    def test_gettingKeysType(self):
        self.assertEqual(isinstance(self.db.getAllKeys()[0],int),True)
    def test_findNededKeys(self):
        self.assertEqual(self.db.findNeededKeys([1,9,3,4,5,6,7,8,9],3,7),[3,4,5,6,7])
    def test_domainParser(self):
        self.assertEqual(self.db.domainParser(["http://google.com","ya.ru/someurl","https://funbox.ru?somevalue=qwerty","https://ya.ru/someurl"]),["google.com","ya.ru","funbox.ru"])
    def test_sendAndSearchinDB(self):
        timeStampFrom=int(time.time())
        self.db.sendToDB(["http://google.com","http://yandex.ru"])
        timeStampTo=int(time.time())
        self.assertEqual(isinstance(self.db.searchAndReturnFromDB(timeStampFrom,timeStampTo),dict),True)
        for i in range(timeStampFrom-2,timeStampTo+2):
            self.db.db.delete(str(i))
if __name__ == "__main__":
    unittest.main()
