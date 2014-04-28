from preprocessing import Preprocessing
from vectorization import VectorQuantization
from constants import classifier_svm, classifier_svm_1_2, classifier_svm_4_5
from constants import classifier_svm_2_3, classifier_svm_3_4
from constants import classifier_mnb_2, classifier_mnb_5


class Classification:
	"""
	Classifies comment according to parameters given:
	Classifier type: SVM or MNB
	No. of classes: 2,5 for MNB and 2,5 for SVM
	"""
	def classify_comment(self, comment, classifier_type='SVM', no_classes=5):
		sentiment = None
		preprocessor = Preprocessing()
		vectorizer = VectorQuantization()
		if classifier_type == 'SVM':
			preprocessed_comment = preprocessor.svm_preprocessing(comment)
			comment_vector = vectorizer.svm_vector(preprocessed_comment)
			if no_classes == 2:
				sentiment = classifier_svm.classify(comment_vector)
			elif no_classes == 5:
				pre_sentiment = classifier_svm.classify(comment_vector)
				if pre_sentiment == 'positivo':
					sentiment = classifier_svm_4_5.classify(comment_vector)
					if sentiment == 'positivo':
						sentiment = classifier_svm_3_4.classify(comment_vector)
				else:
					sentiment = classifier_svm_1_2.classify(comment_vector)
					if sentiment == 'negativo':
						sentiment = classifier_svm_2_3.classify(comment_vector)
		elif classifier_type == 'MNB':
			preprocessed_comment = preprocessor.mnb_preprocessing(comment)
			comment_vector = vectorizer.mnb_vector(preprocessed_comment)
			if no_classes == 2:
				sentiment = classifier_mnb_2.classify(comment_vector)
			elif no_classes == 5:
				sentiment = classifier_mnb_5.classify(comment_vector)
				if sentiment == '1':
					sentiment = 'muy_negativo'
				if sentiment == '2':
					sentiment = 'negativo'
				if sentiment == '3':
					sentiment = 'neutro'
				if sentiment == '4':
					sentiment = 'positivo'
				if sentiment == '5':
					sentiment = 'muy_positivo'
		return sentiment

