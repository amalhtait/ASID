# -*- coding: utf-8 -*-
"""
Created on Thu July 7 14:40:51 2018

@author: 
"""

import gensim.models as gm
import io, sys, re, string
from nltk.corpus import stopwords 
from operator import itemgetter

# load model
dom = sys.argv[2].upper()   #Domain of text: "tw" for tweets and "br" for book reviews.
lang = sys.argv[3].upper()  #Language: "en" for english, "fr" for french and "ar" for arabic.

model_file = 'models/model_'+dom+'_'+lang+'/model'+lang+'_newData_skip_gram' # Loading the model
model = gm.Word2Vec.load(model_file)
 


# load seed words
list_seeds_pos = 'seed-words/pos_'+dom+'_'+lang
list_seeds_neg = 'seed-words/neg_'+dom+'_'+lang

content_seed_pos = open(list_seeds_pos, 'r').readlines()
content_seed_neg = open(list_seeds_neg, 'r').readlines()

# load test data
file_name = sys.argv[1]  #get the test file's name
content_test = open(file_name, 'r').readlines()
 
#get the stop words according to language
if lang == 'EN':
	stop_words = set(stopwords.words('english')) 
elif lang == 'FR':
	stop_words = set(stopwords.words('french')) 
elif lang == 'AR':
	stop_words = set(stopwords.words('arabic')) 

#used to remove punctuation
exclude = set(string.punctuation)


string = "" 
j=0


for lines in content_test:
	my_array = []
	j=j+1
	lines = lines.replace('\n','')
	lines = ''.join(ch for ch in lines if ch not in exclude)
	lines2 = lines.lower()

	data = "sentence_" + str(j) + "\n"

	words = lines2.split(" ")

	for i in range(len(words)):

		if (len(words) > 0) and words[i] not in stop_words: 
			sim = 0
			count = 0
			val = 0

			val_pos = 0
			val_neg = 0

			for seed in content_seed_pos:
				try:
					seed = seed.replace('\n','')
					seed = seed.encode('utf-8')
					word = words[i]					

					sim = sim + model.similarity(seed,word)
					count = count + 1		
				except:
					pass
			if count <> 0: # avg of similarity with positive seed-words
				val_pos = float(sim)/float(count)



			sim = 0
			count = 0
			seed = ''

			for seed in content_seed_neg:
				try:
					seed = seed.replace('\n','')
					seed = seed.encode('utf-8')
					word = words[i]	

					sim = sim + model.similarity(seed,word)
					count = count + 1		
				except:
					pass
			if count <> 0:# avg of similarity with negative seed-words
				val_neg = float(sim)/float(count)



			val = float(val_pos) - float(val_neg) # the difference between the 2 avg

			my_array.append([words[i],val])

	# order the words in the sentence from most positive to least positive
	my_array_sorted = sorted(my_array, key=itemgetter(1), reverse=True)
	
	for a in range(len(my_array_sorted)):
		text = ''
		for b in range(len(my_array_sorted[a])):
			text = text + str(my_array_sorted[a][b]) + ' '
		data = data + text + '\n'


	string = string + data + "\n"		


file_res = open(file_name+'_ASID_'+dom+'_'+lang,"w") 
file_res.write(string)
file_res.close()
