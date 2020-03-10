from source import dictionary
from source import matcher
import unittest 

class TestMatcher(unittest.TestCase): 
    
    def setUp(self):
        self.dictionary = dictionary.generate_dictionary()

    def test_empty_input(self):
        output = matcher.find_matches("", self.dictionary)       
        self.assertCountEqual(output, [])
  
    def test_single_match(self):
        input = "I would like some Thai food"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['Thai']) 
        
    def test_multiple_match(self):
        input = "I want to eat Pub food or Italian"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['Pub', 'Italian']) 

    def test_non_capital_concept(self):
        input = "Where can I find good sushi"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['Sushi']) 
        
    def test_no_match(self):
        input = "Find me a place that does tapas"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, [])
    
    def test_duplicated_match(self):
        input = "Show me a pub that does pub food"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['Pub'])
        
    def test_two_word_matches(self):
        input = "I fancy some east European or East asian takeaway"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['East European', 'East Asian'])
        
    def test_two_word_match(self):
        input = "Which restaurants do East Asian food"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['East Asian'])
        
    def test_two_word_multiple_match(self):
        input = "Which restaurants do West Indian food"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['West Indian', 'West', 'Indian']) 
        
    def test_three_word_multiple_match(self):
        input = "Where can I get South East Asian or South American food"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, ['South East Asian', 'East Asian', 'South American']) 
                
    def test_no_match_again(self):
        input = "What is the weather like today"
        output = matcher.find_matches(input, self.dictionary)       
        self.assertCountEqual(output, [])

 
if __name__ == '__main__': 
    unittest.main() 