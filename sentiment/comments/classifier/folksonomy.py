from metrics_reduced import SpanishTools


# Part-of-Speech tags
nouns        = ['NN', 'NNS', 'NNP', 'NNPS']
verbs        = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
adjectives   = ['JJ','JJR','JJS']
determiners  = ['DT']
conjunctions = ['IN', 'CC']
adverbs      = ['RB','RBR', 'RBS']
modals       = ['MD']
utterances   = ['UH']

def folksonomy(list, n):
	'''
	Determines the top elements in a list of comments
	'''
	spanish_tools = SpanishTools()
	unigrams = []
	bigrams = []
	trigrams = []
	pos_filtered_unigrams = []
	pos_filtered_bigrams = []
	pos_filtered_trigrams = []
	for e in list:
		if e.split() > 0:
			unigrams+= spanish_tools.n_grams(e,1)
		if e.split() > 1:
			bigrams+= spanish_tools.n_grams(e,2)
		if e.split() > 2:
			trigrams+= spanish_tools.n_grams(e,3)

	for word in unigrams:
		if spanish_tools.pos_tagging(word)[0].split(':')[1] in nouns:
			pos_filtered_unigrams.append(word)
	for bigram in bigrams:
		if spanish_tools.pos_tagging(bigram)[0].split(':')[1] in (nouns) and \
		   spanish_tools.pos_tagging(bigram)[1].split(':')[1] in (nouns):
		   	pos_filtered_bigrams.append(bigram)
	for trigram in trigrams:
		if spanish_tools.pos_tagging(trigram)[0].split(':')[1] in (nouns) and \
		   spanish_tools.pos_tagging(trigram)[1].split(':')[1] in (conjunctions) and \
		   spanish_tools.pos_tagging(trigram)[2].split(':')[1] in (nouns):
		   	pos_filtered_trigrams.append(trigram)

	top_unigrams = spanish_tools.top_elements(pos_filtered_unigrams, 'uni', int(n/3))
	top_bigrams = spanish_tools.top_elements(pos_filtered_bigrams, 'bi', int(n/3))
	top_trigrams = spanish_tools.top_elements(pos_filtered_trigrams, 'tri', int(n/3))

	return dict(top_unigrams.items() + top_bigrams.items() + top_trigrams.items())
