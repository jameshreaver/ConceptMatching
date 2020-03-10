from source.hashtable import HashTable
from source.concepts  import data 


def generate_dictionary(concepts = data):

    dictionary = HashTable()

    for concept in concepts:
        start, *rest = concept.split()
        
        # Find existing dictionary
        dict = dictionary
        while start and dict.contains(start):
            word, dict = dict.get(start)
            start, rest = split(rest)

        # Insert into dictionary
        if start or not dict.contains(start):
            dict.put(start, sub_dictionary(rest))
            
    return dictionary


# Create nested dictionaries when the
# concept is an unseen series of words

def sub_dictionary(words):
    if words:
        start, *rest = words
        sub_dict = sub_dictionary(rest)
        return HashTable().put(start, sub_dict)
    return HashTable().put(None)
    
# Split a list of words into start
# and rest catering for empty list

def split(words):
    if words:
        start, *rest = words
        return start, rest
    return None, words
               
    