import pandas
from collections import Counter
import nltk
import os,sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
grammar = r"""
  NP: {<DT|PP\$>?<JJ>+<NN>}
         """
cp = nltk.RegexpParser(grammar)
phrase_dict={}
def adjective_count():
    debate_data = pandas.read_csv("debate.csv", encoding='ISO-8859-1')
    df = debate_data[debate_data['Speaker'] == 'Clinton']
    df = df.append(debate_data[debate_data['Speaker'] == 'Trump'])
    df = df.groupby(['Speaker', 'Date'])
    df = df['Text'].apply(lambda x: ' '.join(x))
    for frame in range(len(df)):
        adj_phrase=[]
        print frame
        sent = nltk.sent_tokenize(df[frame])
        sent = [nltk.word_tokenize(s) for s in sent]
        print "tokenized"
        sent = [nltk.pos_tag(s) for s in sent]
        print "tagged"
        for i in sent:
            tree = cp.parse(i)
            for j in tree:
                try:
                    if j.label() == "NP":
                        #print j
                        str=''
                        for each in range(len(j)):
                            str += j[each][0]
                            str += " "
                        adj_phrase.append(str)
                except:
                    pass
        phrase_dict[frame]=adj_phrase
adjective_count()
pos_dict={}
neg_dict={}
sid = SentimentIntensityAnalyzer()
for entry in phrase_dict:
    print "entry ", entry
    pos = []
    neg = []
    for each in phrase_dict[entry]:
        pol = sid.polarity_scores(each)
        pos.append(pol['pos'])
        neg.append(pol['neg'])
    pos_dict[entry]=pos
    neg_dict[entry]=neg
print phrase_dict
print pos_dict
print neg_dict

with open('adj_phrase.txt','a') as f:
    for each in range(len(phrase_dict)):
        f.write("#############################\n")
        for phr in range(len(phrase_dict[each])):
            f.write(phrase_dict[each][phr].encode('latin-1'))
            f.write(" ")
            f.write(str(pos_dict[each][phr]))
            f.write(" ")
            f.write(str(neg_dict[each][phr]))
            f.write("\n")