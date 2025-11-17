print("importing seaborn takes a bit be patient!")
from seaborn import boxplot
from seaborn import scatterplot
from seaborn import lineplot
import matplotlib.pyplot as plt
from utils_package.utils import CWD
import datetime
print("done with imports\n")


'''
structure of make_figure from the assignment in canvas

after attempts of running debugging, data param is required for driver to run the given figures

see driver for this implementation
'''
def make_figure(data):
    data = data.sort_values(by=['education'])
    boxplot(x="education", y="wage", data=data)
    fig = plt.gcf() # store our figure in a variable we can manipulate

    fig.set_size_inches(10, 10) # set a scale for viewing
    plt.xticks(rotation=45) # adjust how our x_axis labels will look
    
    plt.show() # pauses the running of the code to display our code
    
    now = datetime.datetime.now()
    filepath = f"{CWD}/figures/boxplot_{now}.png"
    plt.savefig(filepath)

'''
make_scatter_plot considers education as x axis, and age as y axis. 

data is the df for this graph
'''  

def make_scatter_plot(data):
    data = data.sort_values(by=['age'])
    scatterplot(x="education", y="age", data=data)
    fig = plt.gcf()
    fig.set_size_inches(10,15)
    plt.xticks()
    plt.show()
    now = datetime.datetime.now()
    filepath = f"{CWD}/figures/scatterplot_{now}.png"
    plt.savefig(filepath)


'''
line graph (plot) consider x axis for wage, and y axis for age

sort data by wage - data is used in lineplot() and is the df for this function

.png is saved with plt.savefig()
'''
def make_line_plot(data):
    data = data.sort_values(by=['wage'])
    lineplot(x="wage", y="age", data=data)
    fig = plt.gcf()
    fig.set_size_inches(10, 15)
    plt.xticks()
    plt.show()
    now = datetime.datetime.now()
    filepath = f"{CWD}/figures/lineplot_{now}.png"
    plt.savefig(filepath)
    plt.close()