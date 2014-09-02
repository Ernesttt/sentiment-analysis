from metrics_reduced import SpanishTools

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
joins        = conjunctions + determiners

def folksonomy(list, n):
	'''
	Determines the topics (folksonomy) in a list of comments
	'''
	unigrams = []
	bigrams = []
	trigrams = []
	pos_filtered_unigrams = {}
	pos_filtered_bigrams = {}
	pos_filtered_trigrams = {}

	for e in list:
		if e.split() > 0:
			unigrams+= spanish_tools.n_grams(e,1)
		if e.split() > 1:
			bigrams+= spanish_tools.n_grams(e,2)
		if e.split() > 2:
			trigrams+= spanish_tools.n_grams(e,3)


	top_unigrams = spanish_tools.top_elements(unigrams, 'uni', 30)
	top_bigrams = spanish_tools.top_elements(bigrams, 'bi', 30)
	top_trigrams = spanish_tools.top_elements(trigrams, 'tri', 30)


	for word in top_unigrams:
		if spanish_tools.pos_tagging(word)[0].split(':')[1] in nouns:
			pos_filtered_unigrams[word]=top_unigrams[word]
	for bigram in top_bigrams:
		if spanish_tools.pos_tagging(bigram)[0].split(':')[1] in (nouns) and \
		   spanish_tools.pos_tagging(bigram)[1].split(':')[1] in (nouns):
		   	pos_filtered_bigrams[bigram]=top_bigrams[bigram]
	for trigram in top_trigrams:
		if spanish_tools.pos_tagging(trigram)[0].split(':')[1] in (nouns) and \
		   spanish_tools.pos_tagging(trigram)[1].split(':')[1] in (joins) and \
		   spanish_tools.pos_tagging(trigram)[2].split(':')[1] in (nouns):
		   	pos_filtered_trigrams[trigram]=top_trigrams[trigram]


	return dict(pos_filtered_unigrams.items() + pos_filtered_bigrams.items() + pos_filtered_trigrams.items())
