from __future__ import division
from classification import Classification
from metrics_reduced import SpanishTools
from folksonomy import folksonomy

classifier = Classification()
spanish_tools = SpanishTools()


class JSONClassificationResponse:
	"""
	Classifies all comments in a JSON file:		
	---------------------------------------
	control parameters:
		* classifier : 'automatic', 'SVM' , 'MNB'
		* no_classes : 'default', 'quick'
		* response : 'full' 'partial' 'minimal'

	see JSON format for sentiment REST Service txt file for details
	"""
	def classification_response(self, parsed_json):
		muy_negativos = []
		negativos = []
		neutros = []
		positivos = []
		muy_positivos = []
		try:
			# retrieving control options
			if parsed_json['control']['classifier'] != 'automatic':
				classifier_type = parsed_json['control']['classifier']
			else:
				classifier_type = 'SVM'
			if parsed_json['control']['no_classes'] == 'default':
				no_classes = 5
			elif parsed_json['control']['no_classes'] == 'quick':
				no_classes = 2
			else:
				return 'number of classes not defined'
			response_type = parsed_json['control']['response']
			# classifying comments
			for comment in parsed_json['data']:
				if len(comment['comment'].split()) > 50:
					classifier_type = 'MNB'
				else:
					classifier_type = 'SVM'
				sentiment = classifier.classify_comment(comment['comment'],
					                                    classifier_type,
					                                    no_classes)
				if sentiment == 'muy_negativo':
					comment[u'polarity'] = sentiment
					comment[u'ranking'] = 1
					muy_negativos.append(comment['comment'])
				if sentiment == 'negativo':
					comment[u'polarity'] = sentiment
					comment[u'ranking'] = 2
					negativos.append(comment['comment'])
				if sentiment == 'neutro':
					comment[u'polarity'] = sentiment
					comment[u'ranking'] = 3
					neutros.append(comment['comment'])
				if sentiment == 'positivo':
					comment[u'polarity'] = sentiment
					comment[u'ranking'] = 4
					positivos.append(comment['comment'])
				if sentiment == 'muy_positivo':
					comment[u'polarity'] = sentiment
					comment[u'ranking'] = 5
					muy_positivos.append(comment['comment'])
			# calculating statistics
			total_comments = len(muy_negativos) + len(negativos) + len(neutros) + \
			                 len(positivos) + len(muy_positivos)
			overall_sentiment = float((-2 * len(muy_negativos) - 1 * len(negativos) + \
				                1 * len(positivos) + 2 * len(muy_positivos)) / \
				                (total_comments))
			statistics = {
						u'muy_negativos':len(muy_negativos),
						u'negativos':len(negativos),
						u'neutros':len(neutros),
						u'positivos':len(positivos),
						u'muy_positivos':len(muy_positivos)}
			# returning response
			rf = response_type['folksonomies']
			rc = response_type['comments'] 
			if not isinstance(rf, bool) or rc not in ['nothing', 'ids_only', 'full']:
				return 'No response defined or wrong format'
			# statistics are always returned
			if rf:
				# retrieving folksonomies
				folksonomy_muy_negativos = {'muy_negativos':folksonomy(muy_negativos,10)}
				folksonomy_negativos = {'negativos':folksonomy(negativos,10)}
				folksonomy_neutros = {'neutros':folksonomy(neutros,10)}
				folksonomy_positivos = {'positivos':folksonomy(positivos,10)}
				folksonomy_muy_positivos = {'muy_positivos':folksonomy(muy_positivos,10)}
				folksonomy_list = [folksonomy_muy_negativos, folksonomy_negativos,
				                   folksonomy_neutros, folksonomy_positivos, 
								   folksonomy_muy_positivos]
				if rc == 'nothing':
					return {'Statistics':statistics, 'Overall Sentiment': overall_sentiment,
							'folksonomies': folksonomy_list}
				if rc == 'ids_only':
					for comment in parsed_json['data']:
						del comment['comment']
					return {'Statistics':statistics, 'Overall Sentiment': overall_sentiment,
					        'Comments':parsed_json['data'], 'folksonomies': folksonomy_list}
				if rc == 'full':
					return {'Statistics':statistics, 'Overall Sentiment': overall_sentiment, 
					        'Comments':parsed_json['data'], 'folksonomies': folksonomy_list}
			else:
				if rc == 'nothing':
					return {'Statistics':statistics, 'Overall Sentiment': overall_sentiment}
				if rc == 'ids_only':
					for comment in parsed_json['data']:
						del comment['comment']
					return {'Statistics':statistics, 'Overall Sentiment': overall_sentiment,
					        'Comments':parsed_json['data']}
				if rc == 'full':
					return {'Statistics':statistics, 'Overall Sentiment': overall_sentiment, 
					        'Comments':parsed_json['data']}

		except Exception as e:
			print e
			return {'wrong JSON format, valid is the form of:': {"control": { "classifier":
			        "automatic", "no_classes": "default", "response": { 
			        "folksonomies":True, "comments":"full"}}, "data":
			        [{"comment": "primer comentario", "id": 1}, {"comment":
			        "segundo comentario", "id": 2}, {"comment": "n-esimo comentario", "id": 
			        99}]}}

