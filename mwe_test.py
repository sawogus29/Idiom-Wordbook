import unittest
from mwe import identify_MWE, is_MWE, gather_MWEs, pick_MWE_at_offset, get_MWE_at_offset, get_word_by_token_index, get_MWE_at_offset

class Test_MWE(unittest.TestCase):

    def test_identify_mwe(self):
        sent = 'Of course, I pull this up'
        correct_label = ['B', 'I', 'O', 'O', 'B', 'o', 'I']
        
        result = identify_MWE(sent)
        result_label = [label for label, _, _ in result]

        self.assertEqual(correct_label, result_label)

    def test_is_MWE(self):
        model_output = [('O', 'i', (0, 1)), ('O', 'love', (2, 6)), ('O', 'you', (7, 10))]   
        _is_MWE, token_index = is_MWE(3, model_output)
        self.assertEqual(_is_MWE, False)
        self.assertEqual(token_index, 1)

    def test_gather_MWEs(self):
        correct_MWEs = [[('B', 'of', (0, 2)), ('I', 'course', (3, 9))],
                        [('B', 'pull', (14, 18)), ('I', 'up', (24, 26))]
                    ]
        model_outputs = [('B', 'of', (0, 2)), ('I', 'course', (3, 9)), ('O', ',', (9,10)),
                ('O', 'I', (11,12)), ('B', 'pull', (14, 18)), ('o', 'this', (19, 23)), ('I', 'up', (24, 26))
                ]
        MWEs = gather_MWEs(model_outputs)
        self.assertEqual(MWEs, correct_MWEs)
    
    def test_pick_MWE_at_offset(self):
        correct_MWE = [('of', (0, 2)), ('course', (3, 9))]

        MWEs = [[('B', 'of', (0, 2)), ('I', 'cour', (3, 7)), ('I', '##se', (7, 9))],
                [('B', 'pull', (14, 18)), ('I', 'up', (24, 26))]
               ]
        
        MWE = pick_MWE_at_offset(4, MWEs)
        self.assertEqual(MWE, correct_MWE)
    
    def test_get_word_by_token_index(self):
        correct_word = [('this', (19, 23))]
        
        model_outputs = [('B', 'of', (0, 2)), ('I', 'course', (3, 9)), ('O', ',', (9,10)),
                ('O', 'I', (11,12)), ('B', 'pull', (14, 18)), ('o', 't', (19, 20)), ('o', '##hi', (20, 22)), ('o', '##s', (22, 23)), ('I', 'up', (24, 26))
                ]

        word = get_word_by_token_index(6, model_outputs)
        self.assertEqual(correct_word, word)
    
    def test_get_MWE_at_offset(self):
        sent = 'I pulled this up!!!'
        for i in range(len(sent)-1):
            result = get_MWE_at_offset(sent, i)
            print(f'offset[{i}] : {result}')
            

if __name__ == '__main__':
    unittest.main()
