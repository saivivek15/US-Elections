import pandas
import numpy
import nltk
from matplotlib import pyplot
import seaborn

trump_int=0
clinton_int=0
clinton_app=0
clinton_laugh=0
trump_app=0
trump_laugh=0
debate_data = pandas.read_csv("debate.csv",encoding='ISO-8859-1')
dates = debate_data['Date'].unique().tolist()
dates.remove('10/4/16')
intr=[]
appl=[]
laugh=[]
for date in dates:
    debate_num = debate_data[debate_data['Date']==date].reset_index()
    host = debate_num['Speaker'].unique()
    host=[i for i in host if i not in ['Trump','Clinton','CANDIDATES','Audience']]
    #print debate_num
    #print host
    for i in range(len(debate_num)-1):
        #print debate_num['Speaker'][i]
        if debate_num['Speaker'][i] == 'Clinton':
            if debate_num['Speaker'][i+1] in host:
                clinton_int+=1
            if debate_num['Text'][i + 1]=='(APPLAUSE)':
                clinton_app+=1
            if debate_num['Text'][i + 1] == '(LAUGHTER)':
                clinton_laugh += 1
        if debate_num['Speaker'][i] == 'Trump':
            if debate_num['Speaker'][i + 1] in host:
                trump_int += 1
            if debate_num['Text'][i + 1]=='(APPLAUSE)':
                trump_app+=1
            if debate_num['Text'][i + 1] == '(LAUGHTER)':
                trump_laugh += 1
    print "Date:", date
    print "Interruptions:", trump_int,clinton_int
    print "Applause:", trump_app,clinton_app
    print "Laughter", trump_laugh,clinton_laugh
    intr.append([clinton_int,trump_int])
    appl.append([clinton_app,trump_app])
    laugh.append([clinton_laugh, trump_laugh])

def plot_bar(y):
    seaborn.set_context(rc={"figure.figsize": (7, 5)})
    width = 0.4
    pyplot.xticks(numpy.arange(2) + width / 2., ('Clinton', 'Trump'))
    fig = pyplot.bar(numpy.arange(2), y, color=seaborn.color_palette("Blues", 2), width=0.3)
    pyplot.legend(fig)
    pyplot.show()
for i in intr:
    plot_bar(i)

for i in appl:
    plot_bar(i)

for i in laugh:
    plot_bar(i)