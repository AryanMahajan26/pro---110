import pandas as pd
import csv
import statistics
import plotly.graph_objects as go
import random
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["temp"] .tolist()
mean = statistics.mean(data)
std = statistics.stdev(data)
print(mean, std)
fig = ff.create_distplot([data],["Temperature"],show_hist = False)
fig.show()
dataset = []
for i in range(0,100):
    random_index = random.randint(0, len(data))
    values = data[random_index]
    dataset.append(values)
mean1 = statistics.mean(dataset)
std1 = statistics.stdev(dataset)
print(mean1, std1)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
     random_index = random.randint(0, len(data)-1)
     values = data[random_index]
     dataset.append(values)
    mean2 = statistics.mean(dataset)
    std2 = statistics.stdev(dataset)
    return mean2
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["Temperature"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1], mode = "lines", name = "mean"))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean3 = statistics.mean(mean_list)
    std3 = statistics. stdev(mean_list)
    print(mean3 , std3)
setup()


















































