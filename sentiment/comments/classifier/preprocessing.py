from metrics_reduced import SpanishTools

# globals
spanish_tools = SpanishTools()

class Preprocessing:
    """
    for SVM it gets rid of repetitive vowels and special characters
    for MNB it gets rid of repetitive vowels, accents and special characters
    """
    def preprocessing(self, comment, lower_case=True, special_characters=True, 
                      repeated_vowels=True, accents=False, stopwords=False):
        '''
        Removes any characteristic of text if True. For example: 
            if repeated_vowels is set to True it will eliminate all repeated 
            vowels from the text: "Goooool" =====> "Gol"
        '''
        if lower_case:
            comment = comment.lower()
        if special_characters:
            comment = spanish_tools.remove_special_characters(comment)
        if repeated_vowels:
            comment = spanish_tools.remove_repeated_vowels(comment)
        if accents:
            comment = spanish_tools.remove_accents(comment)
        if stopwords:
            comment = spanish_tools.remove_stopwords(comment)
        return comment 


