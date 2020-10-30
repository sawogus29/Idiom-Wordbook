import unittest
from mydict import search_dict

class Test_mydict(unittest.TestCase):
    def test_search_dict(self):
        text = 'of course'
        correct_meaning = '물론이야'
        meaning = search_dict(text)
        self.assertEqual(correct_meaning, meaning)
    

if __name__ == '__main__':
   unittest.main() 

    
   