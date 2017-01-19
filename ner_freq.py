import re
import seaborn
from matplotlib import pyplot
import numpy

def plot_bar(x,y):
    seaborn.set_context(rc={"figure.figsize": (7, 5)})
    width = 0.4
    pyplot.xticks(numpy.arange(len(x)) + width / 2., x,rotation=30)
    fig = pyplot.bar(numpy.arange(len(x)), y, color=seaborn.color_palette("Blues", len(x)), width=0.5)
    pyplot.legend(fig)
    pyplot.show()

speech=[]
with open('freq.txt') as f:
	freqs=f.read()
	freqs=re.split(r'#############################',freqs)
	#print freqs[1:]
	for i in freqs[1:]:
		a = i.split("\n")
		a = [each.split(" ") for each in a]
		a = a[1:-1]
		speech.append(a)

for each in speech:
	x=[]
	y=[]
	for word in each:
		if len(word) ==3:
			x.append(word[0]+" "+word[1])
			y.append(int(word[-1]))
		else:
			x.append(word[0])
			y.append(int(word[1]))
	#print x,y
	plot_bar(x,y)
