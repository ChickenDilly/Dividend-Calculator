from matplotlib.ticker import *
import matplotlib.pyplot as plt


def normalize_data(data):
    # normalize dataframe column for comparison to other dataframes
    return (data - data[0]) / (data[0]) * 100


def graphing(data1):
    # graphing MACD & signal line
    # setting up figure and legend
    fig, ax = plt.subplots()
    fig.autofmt_xdate(rotation=-65, ha='center', which='major')
    # setting up x/y axes and major/minor ticks
    ax.set_xlabel('Date'), ax.set_ylabel('Gain (%)')
    ax.xaxis.set_major_locator(MultipleLocator(30))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', width=2, length=8), ax.tick_params(which='minor', width=2, length=3)
    # data plotting
    total_gain1 = normalize_data(data1['assets'])
    ax.plot(data1['date'], total_gain1, label="Assets", color='b')
    ax.legend()
    plt.show()
