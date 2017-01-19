Langugage used: Python 2.7
Packages required: nltk, seaborn, matplotlib, numpy, pandas, sklearn
Steps for execution of the project:
- All the files should be in the same directory
- Open command Line to execute the following python files
- python word_freq.py // computes the unigrams and bigrams frequencies using tf-idf
- python interrupt.py // computes interrupts, applause and laughter for candidate's response
- python ner.py // computes the topics using NER. It generates freq.txt which contains the frequencies of the NEs.
- python ner_freq.py //visualizes the topics using NEs through bar plots
- python adjective.py //computes chunking of noun phrases with adjectives and sentiments of the phrases. It generates adj_phrase.txt which contains all the phrases with their polarity scores
- python adj_freq.py //output the positive and negative sentiments of the phrases and list the top phrases

Note:
Computing ner.py and adjective.py takes time for execution as it deals with POS tagging. As the corpus is huge it also takes time for executing POS tags of the entire corpus.