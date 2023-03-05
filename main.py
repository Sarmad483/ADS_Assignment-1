import pdb
import os
import pandas as pd
import matplotlib.pyplot as plt

path = os.getcwd()
def My_func1(): #Linechart
    df = pd.read_csv(path + "\\Malaria\\Malaria.csv")
    # pdb.set_trace()
    #Too much data, So only doing for Europe
    Location = df[df['ParentLocation'].str.contains("Europe")]
    #On X axis will be the years
    x = Location['Period']
    #On Y axis will be the Actual figures
    y = Location['FactValueNumeric']
    z = Location['ParentLocation']
    #changing fonts/size
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
    #Adding Title
    plt.title("Malaria Cases reported in Europe", fontdict = font1)
    plt.xlabel("Years", fontdict = font2)
    plt.ylabel("Actual Figures", fontdict = font2)
    # pdb.set_trace()

    # plt.figure(figsize=(3, 4))
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()
    # plt.pie(y, labels=z)
    plt.show()

My_func1()

def My_func2(): #Piechart
    #Reading CSV
    df = pd.read_csv(path + "\\Malaria\\Malaria.csv")
    total = df['Location'].value_counts().values.sum()
    #Filtering only Europe
    Location = df[df['ParentLocation'].str.contains("Europe")]

    #Formating and percentage calculation
    def fmt(xyz):
        return '{:.1f}%\n{:.0f}'.format(xyz, total * xyz / 100)
    #making Piechart
    plt.pie(Location['Location'].value_counts().values, labels=Location['Location'].value_counts().index, autopct=fmt)
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    plt.title("Location wise count of Malayria", fontdict = font1)
    plt.show()
My_func2()

def My_func3(): #Barchart
    df = pd.read_csv(path + "\\Malaria\\Malaria.csv")
    total = df['Location'].value_counts().values.sum()
    # Filtering only Europe
    Location = df[df['ParentLocation'].str.contains("Europe")]
    x = Location['Period']
    # On Y axis will be the Actual figures
    y = Location['FactValueNumeric']
    z = Location['ParentLocation']
    # changing fonts/size
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
    # Adding Title
    plt.title("Malaria Cases reported in Europe", fontdict=font1)
    plt.xlabel("Years", fontdict=font2)
    plt.ylabel("Actual Figures", fontdict=font2)
    plt.bar(x, y)
    plt.show()


My_func3()
