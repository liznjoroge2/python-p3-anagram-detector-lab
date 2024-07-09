class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)
        
        # List to hold the anagrams
        matches = []
        
        # Iterate over the list of possible anagrams
        for candidate in possible_anagrams:
            # Check if the sorted letters of the candidate match the sorted letters of the word
            if sorted(candidate) == sorted_word:
                matches.append(candidate)
        
        return matches
