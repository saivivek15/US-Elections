import pandas
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string,re
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.feature_extraction.text import TfidfTransformer as TFIDF
from wordcloud import WordCloud
from matplotlib import pyplot

df=pandas.DataFrame()
debate_data = pandas.read_csv("debate.csv",encoding='ISO-8859-1')
df=debate_data[debate_data['Speaker']=='Clinton']
df= df.append(debate_data[debate_data['Speaker']=='Trump'])
df = df.groupby(['Speaker','Date'])
df=df['Text'].apply(lambda x: ' '.join(x))
#print df
stop_set = stopwords.words('english')
len(stop_set)
pct = [p for p in string.punctuation]
pct= pct + ['',"''","``"]
not_included = ['well','think','going','said','would','want','get','know','said','make','take','way','much','one','say','look','like','tell','thing','let','things','let','come','also','see','lot','got']
debates=[]
for ind in df.index.values:
    debates.append(ind[0]+'-'+ind[1])
#print debates

def cleaning_data(data_set):
    clean_df=[]
    wn_lmt= WordNetLemmatizer()
    for text in data_set:
        tokens = word_tokenize(text)
        tokens = [k.lower() for k in tokens]
        tokens = [i for i in tokens if i not in stop_set]
        tokens = [i for i in tokens if i not in pct]
        tokens = [i for i in tokens if i not in not_included]
        tokens = [wn_lmt.lemmatize(i) for i in tokens]
        reg_tokens=[]
        for i in tokens:
            i = re.findall('^[a-z][a-z]+', i)
            if len(i) != 0:
                reg_tokens.append(i[0])
        reg_tokens=[i for i in reg_tokens if len(i)>2]
        clean_df.append(' '.join(reg_tokens))
    return clean_df

clean_df=cleaning_data(df)
#print clean_df

def compute_tfidf(text,count_vec):
    count = count_vec.fit_transform(text).toarray()
    print count
    tfidf = TFIDF().fit_transform(count).toarray()
    features_lst = count_vec.get_feature_names()
    return features_lst,count, tfidf


def compute_grams(features,count,tfidf):
    debate_frame = { 'Features': features }
    for i in range(len(debates)):
        debate_frame['tfidf-' + debates[i]] = tfidf[i]
        debate_frame['count-' + debates[i]] = count[i]
    debate_frame = pandas.DataFrame(debate_frame)
    for each in range(len(debates)):
        feat= debate_frame.sort_values('count-'+debates[each], ascending=False)[['Features', 'count-'+debates[each]]].head(20)
        print feat
        #filename=str(each)+'.csv'
        #feat.to_csv(filename)
        feat_str = ' '.join(feat['Features'])
        wordcloud = WordCloud(background_color='white', width=600, height=600).generate(feat_str)
        pyplot.imshow(wordcloud)
        pyplot.show()


unigram = cv(ngram_range=(1,1))
bigram = cv(ngram_range=(2,2))
clean_df=cleaning_data(df)
#print clean_df
features_uni,count_uni, tfidf_uni = compute_tfidf(clean_df,unigram)
features_bi,count_bi, tfidf_bi = compute_tfidf(clean_df,bigram)
compute_grams(features_uni,count_uni, tfidf_uni)
compute_grams(features_bi,count_bi, tfidf_bi)
