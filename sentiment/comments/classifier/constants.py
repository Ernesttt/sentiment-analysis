from metrics_reduced import SpanishTools
from pattern.vector import Classifier


spanish_tools = SpanishTools()

# Part-of-Speech tags
nouns        = ['NN', 'NNS', 'NNP', 'NNPS']
verbs        = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
adjectives   = ['JJ','JJR','JJS']
determiners  = ['DT']
conjunctions = ['IN', 'CC']
adverbs      = ['RB','RBR', 'RBS']
modals       = ['MD']
utterances   = ['UH']

# List of sentiment words
positive_adjectives = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/positive_adjectives.txt')
negative_adjectives = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/negative_adjectives.txt')
positive_adverbs    = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/positive_adverbs.txt')
negative_adverbs    = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/negative_adverbs.txt')
positive_verbs      = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/positive_verbs.txt')
negative_verbs      = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/negative_verbs.txt')
positive_nouns      = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/positive_nouns.txt')
negative_nouns      = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/negative_nouns.txt')
positive_others     = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/positive_others.txt')
negative_others     = spanish_tools.read_file_to_list('comments/classifier/vocabularies/words/negative_others.txt')
adversative_conj    = [u'pero', u'sin embargo', u'a pesar de', u'aparte de', u'al contrario', u'sino', u'sino que', 'pese a que']

# Comparison is made without accents to increase precision
positive_words = positive_adjectives + positive_adverbs + positive_verbs + positive_nouns + positive_others
for i, s in enumerate(positive_words):
    positive_words[i] = spanish_tools.remove_accents(s)
negative_words = negative_adjectives + negative_adverbs + negative_verbs + negative_nouns + negative_others
for i, s in enumerate(negative_words):
    negative_words[i] = spanish_tools.remove_accents(s)


# Feature list vector for SVM
feature_list = [u'w0',u'w1',u'w2',u'w3',u'w4',u'w5',u'w6',u'w7',u'w8',u'w9',u'w10',u'w11',u'w12',u'w13',u'w14',u'w15',u'w16',u'w17',u'w18',u'w19',u'w20',u'w21',u'w22',u'w23',u'w24',u'w25',u'w26',u'w27',u'w28',u'w29',u'w30',u'w31',u'w32',u'w33',u'w34',u'w35',u'w36',u'w37',u'w38',u'w39',u'w40',u'w41',u'w42',u'w43',u'w44',u'w45',u'w46',u'w47',u'w48',u'w49',u'w50',u'w51',u'w52',u'w53',u'w54',u'w55',u'w56',u'w57',u'w58',u'w59',u'w60',u'w61',u'w62',u'w63',u'w64',u'w65',u'w66',u'w67',u'w68',u'w69',u'w70',u'w71',u'w72u',u'w73u',u'w74',u'w75',u'w76',u'w77',u'w78',u'w79',u'w80',u'w81',u'w82',u'w83',u'w84',u'w85',u'w86',u'w87',u'w88',u'w89',u'w90',u'w91',u'w92',u'w93',u'w94',u'w95',u'w96',u'w97',u'w98',u'w99',u'w100',u'w101',u'w102',u'w103',u'w104',u'w105',u'w106',u'w107',u'w108',u'w109',u'w110',u'w111',u'w112',u'w113',u'w114',u'w115',u'w116',u'w117',u'w118',u'w119',u'w120',u'w121',u'w122',u'w123',u'w124',u'w125',u'w126',u'w127',u'w128',u'w129',u'w130',u'w131',u'w132',u'w133',u'w134',u'w135',u'w136',u'w137',u'w138',u'w139',u'w140',u'w141',u'w142',u'w143',u'w144',u'w145',u'w146',u'w147',u'w148',u'w149']

# Feature list vector for MNB
mnb_feature_list = spanish_tools.read_file_to_list('comments/classifier/vocabularies/features/bigram-features-500.txt')

# SVM Classifiers
classifier_svm = Classifier.load('comments/classifier/objects/classifiers/SVM/Classifier_SVM_2_classes')
classifier_svm_1_2 = Classifier.load('comments/classifier/objects/classifiers/SVM/Classifier_SVM_segmented_1_2')
classifier_svm_4_5 = Classifier.load('comments/classifier/objects/classifiers/SVM/Classifier_SVM_segmented_4_5')
classifier_svm_2_3 = Classifier.load('comments/classifier/objects/classifiers/SVM/Classifier_SVM_segmented_2_3')
classifier_svm_3_4 = Classifier.load('comments/classifier/objects/classifiers/SVM/Classifier_SVM_segmented_3_4')

# MNB Classifiers
classifier_mnb_2 = Classifier.load('comments/classifier/objects/classifiers/MNB/Classifier_MNB_2_classes')
classifier_mnb_5 = Classifier.load('comments/classifier/objects/classifiers/MNB/Classifier_MNB_5_classes')