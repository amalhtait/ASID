# ASID
The "Adapted Sentiment Intensity Detector" is a tool to detect or predict sentiment intensity in text, at words level. It is adapted to certain domains, specified as parameters in command line. This tool is adapted to the following domains and languages:
```
- General Tweets in English Language
- General Tweets in Arabic Language
- Tweets about public transport in French Language
- Book Reviews in English Language
```

**Developer** <br />	
Amal Htait <br />
Ph.D. Candidate, Marseilles, France. <br />
LIS UMR 7020 CNRS <br />
CLEO - OpenEdition Lab <br />



**Citation** <br />
```	
If using this tool or its word embedding models, please cite our work using : 
		@inproceedings{htait19, 
  		title={Sentiment Analysis and Sentence Classification in Long Book-Search Queries}, 
  		author={Htait, Amal  and Fournier, Sebastien and Bellot, Patrice}, 
  		booktitle={20th International Conference on Computational Linguistics and Intelligent Text Processing (CICLing)}, 
  		year={2019} 
		} 
```

**Acknowledgments** <br />
This work has been supported by the French State, managed by the National Research Agency under the "Investissements d'avenir" program under the EquipEx DILOH projects (ANR-11-EQPX-0013). <br />

**License** <br />
ASID is released under the terms of the GPL version 2.

**Project Information** <br />
The sentiment in text can be measured by two scales: the sentiment from negative to positive, and the intensity from low to high. Therefore, predicting the Sentiment Intensity gives the possiblity of distinguishing words of same polarity, like: "Good" and "Exceptional", where both are positive but the world "Exceptional" is way stronger (high intensity) than "Good". The tool "ASID" is based on a semi-supervised method with sentiment lexicons as seed-words, and word embeddings models.<br />

**This script include** <br />
```
1 - Four word embedding models of size :
	Arabic Tweets : 9 million words  (models/model_TW_AR/modelAR_newData_skip_gram)
	English Tweets : 5 million words  (models/model_TW_EN/modelEN_newData_skip_gram)
        English Book Reviews : 2.5 million words  (models/model_BR_EN/modelEN_newData_skip_gram)
	French Tweets : 415 thousand words  (models/model_TW_FR/modelFR_newData_skip_gram)
  
```
```
2 - Four sets of seed-words lists :
	Arabic Tweets : pos_TW_AR and neg_TW_AR
	English Tweets : pos_TW_EN and neg_TW_EN
        English Book Reviews : pos_BR_EN and neg_BR_EN
	French Tweets : pos_TW_FR and neg_TW_FR
  
```

**Prerequisites** <br />
```
- Python 2.7.13
- gensim
- nltk 3.2.2
- operator
```

**Usage by command line** <br />
python ASID.py file_name domain language <br />
The output will be found in the same folder, and has the name : fileName_ASID. <br />
And will contain the list of words from the test file, grouped by sentences, with their predicted sentiment intensity, ordered from most to least positive. <br />
 
**Examples** <br />
An example of use with a file named test_sentences, in English language for book reviews domain: <br />
```
python ASID.py test_sentences BR EN
```
An example of use with a file named test_sentences_2, in Arabic language for Tweets domain: <br />
```
python ASID.py test_sentences_2 TW AR
```
An example of use with a file named test_sentences_3, in French language for Tweets domain: <br />
```
python ASID.py test_sentences_2 TW FR
```

