import math

def tf(n_terms, total_terms):
	tf = n_terms / total_terms
	return tf

def idf(n_term, total_term):
	idf = math.log10(total_term/n_term)
	return idf