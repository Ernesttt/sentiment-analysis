# -*- coding: utf-8 -*-
import codecs
from metrics_reduced import SpanishTools
from pattern.vector import Document
from constants import * # See constants.py to check variables used in this file
import time

#globals
spanish_tools = SpanishTools()


class VectorQuantization:
    """
    Creates vector of features 
    """
    def morphosyntactic_vector(self, comment):
        comment_tagged = spanish_tools.pos_tagging_infinitive(comment)
        custom_dict = {}
        document = None
        # Constructing vector
        for i in range(50):
            if len(comment_tagged) > i and len(comment_tagged) <= 50:
                word = spanish_tools.remove_accents(comment_tagged[i].split(':')[0])
                tag  = comment_tagged[i].split(':')[1]
                # Adjectives 
                if tag in adjectives:
                    if word in positive_words:
                        custom_dict[feature_list[3*i]]     = 0.99
                        custom_dict[feature_list[3*i + 1]] = 0.99
                        custom_dict[feature_list[3*i + 2]] = 0.99
                    elif word in negative_words:
                        custom_dict[feature_list[3*i]]     = 0.01
                        custom_dict[feature_list[3*i + 1]] = 0.01
                        custom_dict[feature_list[3*i + 2]] = 0.5
                    else:
                        custom_dict[feature_list[3*i]]     = 0.5
                        custom_dict[feature_list[3*i + 1]] = 0.5
                        custom_dict[feature_list[3*i + 2]] = 0.5
                # Adverbs        
                elif tag in (adverbs or determiners or conjunctions):
                    if word in positive_words:
                        custom_dict[feature_list[3*i]]     = 0.99
                        custom_dict[feature_list[3*i + 1]] = 0.99
                        custom_dict[feature_list[3*i + 2]] = 0.5
                    elif word in negative_words:
                        custom_dict[feature_list[3*i]]     = 0.01
                        custom_dict[feature_list[3*i + 1]] = 0.01
                        custom_dict[feature_list[3*i + 2]] = 0.01
                    else:
                        custom_dict[feature_list[3*i]]     = 0.5
                        custom_dict[feature_list[3*i + 1]] = 0.5
                        custom_dict[feature_list[3*i + 2]] = 0.5
                # Verbs        
                elif tag in verbs:
                    if word in positive_words:
                        custom_dict[feature_list[3*i]]     = 0.5
                        custom_dict[feature_list[3*i + 1]] = 0.99
                        custom_dict[feature_list[3*i + 2]] = 0.99
                    elif word in negative_words:
                        custom_dict[feature_list[3*i]]     = 0.5
                        custom_dict[feature_list[3*i + 1]] = 0.01
                        custom_dict[feature_list[3*i + 2]] = 0.01
                    else:
                        custom_dict[feature_list[3*i]]     = 0.5
                        custom_dict[feature_list[3*i + 1]] = 0.5
                        custom_dict[feature_list[3*i + 2]] = 0.5
                # Nouns        
                elif tag in nouns:
                    if word in positive_words:
                        custom_dict[feature_list[3*i]]     = 0.99
                        custom_dict[feature_list[3*i + 1]] = 0.5
                        custom_dict[feature_list[3*i + 2]] = 0.99
                    elif word in negative_words:
                        custom_dict[feature_list[3*i]]     = 0.01
                        custom_dict[feature_list[3*i + 1]] = 0.5
                        custom_dict[feature_list[3*i + 2]] = 0.01
                    else:
                        custom_dict[feature_list[3*i]]     = 0.5
                        custom_dict[feature_list[3*i + 1]] = 0.5
                        custom_dict[feature_list[3*i + 2]] = 0.5
                # Other categories
                else:
                    custom_dict[feature_list[3*i]]     = 0.5
                    custom_dict[feature_list[3*i + 1]] = 0.5
                    custom_dict[feature_list[3*i + 2]] = 0.5
            # Dummy
            elif len(comment_tagged) <= 50:
                    custom_dict[feature_list[3*i]]     = 0.5
                    custom_dict[feature_list[3*i + 1]] = 0.5
                    custom_dict[feature_list[3*i + 2]] = 0.5
        # -           
        if len(custom_dict) > 0:                    
            document = Document(custom_dict)
        return document



    def bigram_vector(self, comment):
        document = None
        dictionary_features = dict.fromkeys(bigram_feature_list, 0)
        list_elements = spanish_tools.n_grams(comment, 2)
        for e in list_elements:
            if dictionary_features.has_key(e):
                dictionary_features[e] = dictionary_features[e] + 1
        document = Document(dictionary_features)
        return document

