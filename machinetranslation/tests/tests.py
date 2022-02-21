import unittest
from translator import englishToFrench
from translator import frenchToEnglish


class TestSquare(unittest.TestCase): 
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Null'),'Null')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('null'),' ')


class TestSquare1(unittest.TestCase): 
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Null'),'Null')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Null'),' ')


unittest.main()