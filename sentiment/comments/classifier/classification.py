from preprocessing import Preprocessing
from vectorization import VectorQuantization
from constants import classifier_svm
from constants import classifier_svm_3
from constants import classifier_svm_1_2
from constants import classifier_svm_2_3
from constants import classifier_svm_3_4
from constants import classifier_svm_4_5
from constants import classifier_mnb


class Classification:
	"""
	Classifies comment according to parameters given:
	Classifier type: SVM or MNB
	No. of classes: 3(positivo-neutro-negativo) or 
					5(muy_positivo-positivo-neutro-negativo-muy_negativo) 
	"""
	# POLYNOMIAL CLASSIFFIER
	def classify_comment(self, comment, classifier_type='SVM', no_classes=5):
		sentiment = None
		preprocessor = Preprocessing()
		vectorizer = VectorQuantization()
		if classifier_type == 'SVM':
			preprocessed_comment = preprocessor.preprocessing(comment)
			comment_vector = vectorizer.morphosyntactic_vector(preprocessed_comment)
			sentiment = classifier_svm.classify(comment_vector)
			if no_classes == 5:
				return sentiment
			elif no_classes == 3:
				if sentiment == u'positivo' or sentiment == u'muy_positivo':
					return u'positivo'
				elif sentiment == u'negativo' or sentiment == u'muy_negativo':
					return u'negativo'
				else:
					return sentiment
		elif classifier_type == 'MNB':
			preprocessed_comment = preprocessor.preprocessing(comment)
			comment_vector = vectorizer.bigram_vector(preprocessed_comment)
			sentiment = classifier_mnb.classify(comment_vector)
			if no_classes == 5:
				return sentiment
			elif no_classes == 3:
				if sentiment == u'positivo' or sentiment == u'muy_positivo':
					return u'positivo'
				elif sentiment == u'negativo' or sentiment == u'muy_negativo':
					return u'negativo'
				else:
					return sentiment

	'''
	==================
	LINEAR CLASIFFIERS
	==================
	def classify_comment(self, comment, classifier_type='SVM', no_classes=5):
		sentiment = None
		preprocessor = Preprocessing()
		vectorizer = VectorQuantization()
		if classifier_type == 'SVM':
			preprocessed_comment = preprocessor.preprocessing(comment)
			comment_vector = vectorizer.morphosyntactic_vector(preprocessed_comment)
			if no_classes == 2:
				sentiment = classifier_svm_3.classify(comment_vector)
			elif no_classes == 5:
				pre_sentiment = classifier_svm_3.classify(comment_vector)
				if pre_sentiment == 'positivo':
					sentiment = classifier_svm_3_4.classify(comment_vector)
					if sentiment == 'positivo':
						sentiment = classifier_svm_4_5.classify(comment_vector)
				else:
					sentiment = classifier_svm_2_3.classify(comment_vector)
					if sentiment == 'negativo':
						sentiment = classifier_svm_1_2.classify(comment_vector)
			return sentiment
		elif classifier_type == 'MNB':
			preprocessed_comment = preprocessor.preprocessing(comment)
			comment_vector = vectorizer.bigram_vector(preprocessed_comment)
			sentiment = classifier_mnb.classify(comment_vector)
			if no_classes == 5:
				return sentiment
			elif no_classes == 3:
				if sentiment == u'positivo' or sentiment == u'muy_positivo':
					return u'positivo'
				elif sentiment == u'negativo' or sentiment == u'muy_negativo':
					return u'negativo'
				else:
					return sentiment
	'''

