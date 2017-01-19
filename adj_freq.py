import re
sentiments = []
positive_phrase=[]
negative_phrase=[]
with open('adj_phrase.txt') as f:
    adj_p=f.read()
    adj_p=re.split(r'#############################',adj_p)
    #print adj_p[1]
    for i in adj_p[1:]:
        a=i.split("\n")
        a = [each.split(" ") for each in a]
        a=a[1:-1]
        pos=[]
        neg=[]
        phr=[]
        max_pos=[]
        max_neg=[]
        for each in a:
            pos.append(each[-2])
            neg.append(each[-1])
            phr.append(' '.join(each[:-3]))
        #print phr,pos,neg
        pos_count=0
        neg_count=0
        for ct in pos:
            if float(ct)>float(0.0):
                pos_count+=1
        for ct in neg:
            if float(ct)>float(0.0):
                neg_count+=1
        #print pos_count,neg_count
        sentiments.append([pos_count,neg_count])
        iter=0
        while(True):
            pos_m=pos.index(max(pos))
            pos_n = neg.index(max(neg))
            max_pos.append(phr[pos_m])
            max_neg.append(phr[pos_n])
            pos[pos_m]=0.0
            neg[pos_n]=0.0
            iter+=1
            if iter==10:
                break
        #print set(max_pos)
        #print set(max_neg)

        positive_phrase.append(max_pos)
        negative_phrase.append(max_neg)

date=['9/26/16-Clinton','10/9/16-Clinton','10/19/2016-Clinton','9/26/16-Trump','10/9/16-Trump','10/19/2016-Trump']
for i in range(6):
    print date[i]
    print "Number of positive sentiments: ",sentiments[i][0]
    print "Number of negative sentiments: ", sentiments[i][1]
    print "Adjective Phrases with positive sentiment:"
    for phrase in positive_phrase[i]:
        print phrase
    print "Adjective Phrases with negative sentiment:"
    for phrase in negative_phrase[i]:
        print phrase

