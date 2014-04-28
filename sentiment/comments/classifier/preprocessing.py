from metrics_reduced import SpanishTools

# globals
spanish_tools = SpanishTools()

class Preprocessing:
    """
    for SVM it gets rid of repetitive vowels and special characters
    for MNB it gets rid of repetitive vowels, accents and special characters
    """
    def svm_preprocessing(self, comment):
        comment_wo_sc = spanish_tools.remove_special_characters(comment.lower())
        comment_wo_rv = spanish_tools.remove_repeated_vowels(comment_wo_sc)
        # -- optional remove stopwords 'sw'
        #comment_wo_sw = spanish_tools.remove_stopwords(comment_wo_rv)
        return comment_wo_rv


    def mnb_preprocessing(self, comment):
        comment_wo_sc = spanish_tools.remove_special_characters(comment.lower())
        comment_wo_rv = spanish_tools.remove_repeated_vowels(comment_wo_sc)
        comment_wo_ac = spanish_tools.remove_accents(comment_wo_rv)
        # -- optional remove stopwords 'sw'
        #comment_wo_sw = spanish_tools.remove_stopwords(comment_wo_ac)
        return comment_wo_ac

