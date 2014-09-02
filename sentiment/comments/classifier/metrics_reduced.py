# -*- coding: utf-8 -*-
import re
import codecs
import unicodedata
from pattern.es import parse, split
from collections import Counter
from pattern.en import ngrams
from pattern.es import singularize, conjugate, INFINITIVE, predicative


class SpanishTools:
    """
    A serie of tools for spanish text preprocessing
    """
    # Global variable
    stopwords = []

    #Constructor
    def __init__(self):   
            stopwords = self.read_file_to_list('comments/classifier/vocabularies/words/spanish-stopwords.txt')

        
    def __call__(self):
            self.__init__
            

    def remove_accents(self,s):
            '''
            Remove accents
            In:
                  (s:string) text string
            Out:
                  (string) text string without accents
            '''
            try:
                return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
            except TypeError:
                return ""     
            except UnicodeDecodeError:
                return ""
            except:
                return ""   




    def remove_stopwords(self, s, exception_list=[]):
            '''
              Removing stopwords
              
              In:
                    (s:string, exception_list:list) text string              
              Out:
                    (string) string without stopwords
            '''
            [stopwords.remove(x) for x in exception_list if x in stopwords]
            list = []
            if isinstance(s, str):
                text = unicode(s, "utf-8", "xmlcharrefreplace")
            list = text.split()
            for word in list:
                if word not in stopwords:
                    list.append(word)
            return u' '.join(list)
       
       
       

    def remove_special_characters(self, s):
            '''
              Removing specaial characters
              
              In:
                    (s:string) text string               
              Out:
                    (string) text string free of special characters in unicode
            '''
            PRINTABLE = set(('Lu', 'Ll', 'Zs'))
            if isinstance(s, str):
                s = unicode(s, "utf-8", "xmlcharrefreplace")
            result = []
            for word in s:
                word = unicodedata.category(word) in PRINTABLE and word or u'#'
                result.append(word)
            return u''.join(result).replace(u'#', u' ')  
            
            

        
    def remove_repeated_vowels(self, s):
            '''
              Repeated vowels filter
              
              In:
                    (s: string) text string               
              Out:
                    (string) text string with words without repeated vowels
            '''
            if isinstance(s, str):
                s = unicode(s, "utf-8", "xmlcharrefreplace")
            result = []
            list = s.split()
            for word in list:
                word_wo_rv = re.sub(r'([aeiou])\1+', r'\1', word)
                result.append(word_wo_rv)
            return u' '.join(result)



   
    def pos_tagging_infinitive(self, s):
            '''
              Grammatical category of each word a.k.a. Part-of-Speech (pos) tagging,
              but transformming adjectives to predicative form, singularizing nouns and
              verbs to infinitive form

              ej. ella:PRP maneja:VBD carros:NNS rojos:JJ
                    PRP: Possesive pronoun  ---> ella
                    VBD: Verb in past tense ----> manejar(infinitive)
                    NNS: Noun in plural --------> carro (singularized)
                    JJ: adjective --------------> rojo (predicative)
              In:
                    (s:string) string text               
              Out:
                    (list) list with grammatical categories in the form 'word:category'
            '''
            categories = parse(s)
            list = []
            if isinstance(s, str):
                s = unicode(s, "utf-8", "xmlcharrefreplace")
            for x in categories.split():
                for y in x:
                    if y[1] in ['NNS']:
                        word = singularize(y[0])  
                        list.append(word+":NN")
                    elif y[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
                        word = conjugate(y[0], INFINITIVE)  
                        list.append(word+":VB")
                    elif y[1] in ['JJ','JJR','JJS']:
                        word = predicative(y[0])  
                        list.append(word+":JJ")
                    else:
                        list.append(y[0]+':'+y[1])
            return list





    def pos_tagging(self, s):
            '''
              Grammatical category of each word

              ej. she:PRP drove:VBD a:DT silver:NN pt:NN cruiser:NN
                    PRP: Possesive pronoun
                    VBD: Verb in past tense
                    DT: Determiner
                    NN: Noun in singular
              In:
                    (s:string) string text               
              Out:
                    (list) list with grammatical categories associated to every word
            '''
            categories = parse(s)
            list = []
            if isinstance(s, str):
                s = unicode(s, "utf-8", "xmlcharrefreplace")
            for x in categories.split():
                for y in x:
                    list.append(y[0]+":"+y[1])
            return list





    def read_file_to_list(self, filename):
          '''
            Reads a file separated by '\n'

            In:
                (filename:string)
            Out:
                (list) python list with every word in the file
          '''
          with codecs.open(filename, 'r', 'utf-8') as f:
                word_list = f.read().splitlines()
          return word_list





    def n_grams(self, s, n=2):
          '''
            Obtain n-grams

            In:
                (s:string, n:int) text string and size of the n-gram
            Out:
                (list) list of n-grams
          '''
          list = []
          ngrams_list = ngrams(s, n=n)
          for ngram in ngrams_list:
              ngram_joined = ''
              for word in ngram:
                  ngram_joined += word + ' '
              list.append(ngram_joined.rstrip())
          if len(list)>=1:
              return list
          else:
              return []





    def top_elements(self, l, type, n=10):
          '''
            Top n elements in a list

            In:
                (l:list, n:int) list of words, bigrams or trigrams
            Out:
                (dictionary: dict) dictionary of the top n elements 
          '''
          dictionary = {}
          for e in Counter(l).most_common(n):
              dictionary[e[0]]=e[1]
          return dictionary


      

  