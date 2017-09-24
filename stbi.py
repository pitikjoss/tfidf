#import fungsi dari file tfidf
from tfidf import tf, idf

#variable
n_terms = 3
total_terms = 100

#memanggil fungsi tf untuk menghitung fungsi term frequency
#variable tf value akan menampung file dari hasil komputasi fungsi tf

tf_value = tf(n_terms, total_terms)

#print tf value
print("Term frequency: {0}". format(tf_value))



n_term = 1000
total_term = 10000000

idf_value = idf(n_term, total_term)

print ("Term : {0}" .format(idf_value))

tfidf_value = idf_value*tf_value

print("Term: {0}" .format(tfidf_value))