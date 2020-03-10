from source.hashtable import HashTable
import unittest

class TestHashTable(unittest.TestCase): 
    
    def setUp(self):
        self.dictionary = HashTable()
  
    def test_empty_upon_creation(self):
        self.assertEqual(self.dictionary.size(), 0) 
        
    def test_contains_element(self):
        self.dictionary.put("key", 450)
        self.assertTrue(self.dictionary.contains("key")) 
        
    def test_contains_ignores_capitalisation(self):
        self.dictionary.put("key", 450)
        self.assertTrue(self.dictionary.contains("kEy")) 
                
    def test_get_element(self):
        self.dictionary.put("key", 450)
        self.assertTrue(self.dictionary.contains("key")) 
        self.assertEqual(self.dictionary.get("key"), ("key", 450)) 
        
    def test_get_ignores_capitalisation(self):
        self.dictionary.put("key", 450)
        self.assertEqual(self.dictionary.get("kEy"), ("key", 450)) 
            
    def test_get_non_element(self):
        self.dictionary.put("key", 450)
        self.assertEqual(self.dictionary.get("other"), (None, None)) 
        
    def test_put_element(self):
        self.dictionary.put("key", 450)
        self.assertEqual(self.dictionary.size(), 1) 
        self.assertTrue(self.dictionary.contains("key")) 
        
    def test_put_ignores_capitalisation(self):
        self.dictionary.put("key", 450).put("kEy", 500)
        self.assertEqual(self.dictionary.size(), 1) 
        self.assertEqual(self.dictionary.get("key"), ("kEy", 500)) 
                    
    def test_put_duplicate_element(self):
        self.dictionary.put("key", 450).put("key", 500)
        self.assertEqual(self.dictionary.size(), 1) 
        self.assertEqual(self.dictionary.get("key"), ("key", 500))
    
    def test_resize_if_crowded(self):
        self.assertEqual(self.dictionary.max_size, 1)
        self.dictionary.put("a", 450).put("b", 500).put("c",600)
        self.assertEqual(self.dictionary.max_size, 4)


if __name__ == '__main__': 
    unittest.main() 