from source import dictionary
from source import matcher


dictionary = dictionary.generate_dictionary()

while True:
    line = input("Enter phrase: ")
    matches = matcher.find_matches(line, dictionary)
    print(matches)
    print()