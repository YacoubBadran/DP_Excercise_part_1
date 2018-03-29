import matplotlib.pyplot as plt
import pandas as pd

def main():
    GDP = pd.read_csv('data/GDP_CAT.csv')
    GDPNew = GDP.iloc[2:]
    #GDP2 = GDP[['Year', 'GDP']]
    GDP3 = GDPNew['Year']
    GDP4 = GDPNew['GDP']

    suicide = pd.read_csv('data/suicide.csv')
    suicideNew = suicide.iloc[6:20]
    suicide1 = suicideNew['TIME']
    suicide2 = suicideNew['Value']

    fig, ax1 = plt.subplots()
    ax1.plot(GDP3, GDP4, 'r-')
    ax1.set_xlabel('Time (annual)')
    ax1.set_ylabel('Catalonia GDP', color='r')
    ax1.tick_params('y', colors='r')

    ax2 = ax1.twinx()
    ax2.plot(suicide1, suicide2, 'b-')
    ax2.set_ylabel('Australia suicide average', color='b')
    ax2.tick_params('y', colors='b')

    print(suicide)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(GDP)

    fig.tight_layout()

    plt.savefig('plot.png')
    plt.show()


main()

