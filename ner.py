import pandas
import nltk
from collections import Counter


def ner():
    debate_data = pandas.read_csv("debate.csv", encoding='ISO-8859-1')
    df = debate_data[debate_data['Speaker'] == 'Clinton']
    df = df.append(debate_data[debate_data['Speaker'] == 'Trump'])
    df = df.groupby(['Speaker', 'Date'])
    df = df['Text'].apply(lambda x: ' '.join(x))
    for frame in range(len(df)):
        print frame
        sent = nltk.sent_tokenize(df[frame])
        sent = [nltk.word_tokenize(s) for s in sent]
        print "tokenized"
        sent = [nltk.pos_tag(s) for s in sent]
        print "tagged"
        ner=[]
        for i in sent:
            ne = nltk.ne_chunk(i, binary=True)
            print "chunked"
            for j in ne:
                try:
                    l = j.label()
                    print l
                    ner.append(tuple([each[0] for each in j]))
                    print ner
                except:
                    pass
        ner_count=Counter(ner).most_common(20)
        print ner_count
        with open('freq.txt', 'a') as f:
            f.write("############################# \n")
            for b in ner_count:
                print b[0][0]
                f.write(b[0][0])
                f.write(" ")
                if len(b[0]) == 2:
                    f.write(b[0][1])
                    f.write(" ")
                    print b[0][1]
                print b[1]
                f.write(str(b[1]))
                f.write("\n")
        print "written!"
ner()