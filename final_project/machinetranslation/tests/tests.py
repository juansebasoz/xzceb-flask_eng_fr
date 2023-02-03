import unittest

from translator import french_to_english, english_to_french

class TestFrench2English(unittest.TestCase):
    
    def test_null(self):
        self.assertIsNone(french_to_english(None))
    
    def test_text(self):
        testText = "Bonjour"                
        self.assertEqual(french_to_english(testText), 'Hello')


class TestEnglish2French(unittest.TestCase):
    
    def test_null(self):
        self.assertIsNone(english_to_french(None))

    def test_text(self):
        testText = "Hello"        
        self.assertEqual(english_to_french(testText), 'Bonjour')

if __name__ == '__main__':
    unittest.main()        