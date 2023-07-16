import unittest as t
import translator as trans

class Test(t.TestCase):
    def testcases(self):
        self.assertEquals(trans.englishToFrench("hello").lower(), "bonjour".lower())
        self.assertEquals(trans.frenchToEnglish("bonjour").lower(), "hello".lower())


    if __name__ == "__main__":
        unittest.main()