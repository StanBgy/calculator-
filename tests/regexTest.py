import re, unittest 


from calculator.model import calcRegex
#import .calculator.calculator.model
calcR = calcRegex()

class TestRegexes(unittest.TestCase):

    def test_regex(self):
        t1 = calcR.search('10 + 10')
        self.assertTrue(t1.group())
        self.assertEqual(t1.group(), '10 + 10')
        self.assertEqual(t1.group(1), '')
        self.assertEqual(t1.group(2), '10')
        self.assertEqual(t1.group(3), '+')
        self.assertEqual(t1.group(4), '10')

    def test_regex2(self):
        t2 = calcR.search('9/8')
        self.assertTrue(t2.group())
        self.assertRegex(t2.group(), '9/8')
        self.assertRegex('9/3', calcR)
        self.assertEqual('', t2.group(1))
        self.assertEqual('9', t2.group(2))
        self.assertEqual('/', t2.group(3))
        self.assertEqual('8', t2.group(4))

    def test_regexF(self):
        self.assertFalse(calcR.match('Random String'))
        self.assertNotRegex('Random String', calcR)

    def test_regex3(self):
        string = '45 / 65 + 21 * 34'
        self.assertRegex(string, calcR)

    def test_regex4(self):
        string = 'random string 45 + 43 / 21 random string'
        self.assertNotRegex(string, calcR)

    def test_regex5(self):
        string = '45 // 21'
        self.assertNotRegex(string, calcR)
        

if __name__ == '__main__':
    unittest.main()
