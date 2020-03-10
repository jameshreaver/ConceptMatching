from source.dictionary import generate_dictionary
import unittest 

class TestDictionary(unittest.TestCase): 
    
    def test_no_concepts(self):
        dictionary = generate_dictionary([])
        self.assertEqual(dictionary.size(), 0) 
        self.assertFalse(dictionary.contains('Food')) 
            
    def test_one_word_concept(self):
        concepts = ['Food']
        dictionary = generate_dictionary(concepts)
        self.assertEqual(dictionary.size(), 1) 
        self.assertTrue(dictionary.contains('Food')) 

    def test_one_word_concepts(self):
        concepts = ['Pasta', 'Pizza', 'Gnocchi', 'Risotto']
        dictionary = generate_dictionary(concepts)
        self.assertEqual(dictionary.size(), len(concepts)) 
        for concept in concepts:
            self.assertTrue(dictionary.contains(concept))
            
    def test_parent_of_none_is_concept(self):
        first, second  = ['South East', 'South East Asian']
        dictionary = generate_dictionary([first, second])
        for word in second.split():
            word, dictionary = dictionary.get(word)
            if dictionary.contains(None):
                break
        self.assertEqual(word, 'East')

    def test_multi_word_concept(self):
        concept = 'Texan Chilli Con Carne'
        dictionary = generate_dictionary([concept])
        for word in concept.split():
            self.assertEqual(dictionary.size(), 1)
            self.assertTrue(dictionary.contains(word))
            word, dictionary = dictionary.get(word)

    def test_concepts_same_start(self):
        concepts = ['South', 'South East Asian']
        dictionary = generate_dictionary(concepts)
        self.assertEqual(dictionary.size(), 1)
        word, sub_dict = dictionary.get('South')
        self.assertTrue(sub_dict.contains(None))
        self.assertTrue(sub_dict.contains('East'))
    
    def test_concepts_share_dictionaries(self):
        first, second  = ['One Two Three', 'One Two Three Four Five']
        dictionary = generate_dictionary([first, second])
        for word in first.split():
            self.assertEqual(dictionary.size(), 1)
            word, dictionary = dictionary.get(word)
        self.assertEqual(dictionary.size(), 2)
        
    def test_duplicate_concepts(self):
        concepts = ['West', 'Indian', 'West']
        dictionary = generate_dictionary(concepts)
        self.assertEqual(dictionary.size(), 2)


if __name__ == '__main__': 
    unittest.main() 