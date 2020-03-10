
def find_matches(line, dictionary):        
    found = set()
    words = line.split()
    while words:
        matches = find_word_matches(words, dictionary)
        found.update(matches)
        start, *words = words
    return list(found)
    

# Return all matches that start
# with the first word in words

def find_word_matches(words, dictionary):
    found = []
    start, *rest = words
    if dictionary.contains(start):
        word, sub_dict = dictionary.get(start)
        if sub_dict.contains(None):
            found.append(word)
        if rest:
            matches = find_word_matches(rest, sub_dict)
            found += [word + " " + m for m in matches]
    return found