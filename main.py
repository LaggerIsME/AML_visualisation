import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math


def graph_word():
    # Task 2.1: You need to output data on the schedule of teachers who teach disciplines and add a column "points
    # for subjects"
    df = pd.DataFrame([
        ['John John', 'English', 90],
        ['Joe Sam', 'English', 80],
        ['Lars Jake', 'English', 70],
        ['Carl Carl', 'Mathematics', 80],
        ['Alexandr Lars', 'Mathematics', 95],
        ['Joe Jake', 'Mathematics', 70],
        ['Mary Mary', 'Russian', 100],
        ['Mary Lars', 'Russian', 70],
        ['Don Jey', 'Russian', 90],
    ],
        columns=['Full name', 'Subject', 'Points'])
    plt.figure(figsize=(16, 9))
    english_df = df.loc[df['Subject'] == 'English']
    russian_df = df.loc[df['Subject'] == 'Russian']
    mathematics_df = df.loc[df['Subject'] == 'Mathematics']
    plt.bar(english_df['Full name'], english_df['Points'])
    plt.bar(russian_df['Full name'], russian_df['Points'])
    plt.bar(mathematics_df['Full name'], mathematics_df['Points'])
    plt.grid()
    plt.legend(labels=['English', 'Russian', 'Mathematics'])
    plt.title('The Points of Teachers of 3 disciplines', fontsize=20, weight='bold')
    plt.xlabel('Full names', fontsize=20)
    plt.ylabel('Points', fontsize=20)
    plt.show()

    # Task 2.2: You need to deduce data on work experience, education, teaching methods of teachers
    # who teach disciplines


    # Task 2.3: You need to make a data output using all the graph types presented


def graph_pdf():
    # Reading of CSV
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    plt.suptitle('Assignment 2')
    df = pd.read_csv('AML_DataVisualization.csv')
    longitude = df['longitude']
    latitude = df['latitude']

    # With the matplotlib defaults
    ax1 = axs[0, 0]
    ax1.set_title('1)With the matplotlib defaults')
    ax1.scatter(longitude, latitude)
    ax1.set_xlabel('longitude')
    ax1.set_ylabel('latitude')

    # With marker size 50% and alpha 50%
    ax2 = axs[0, 1]
    ax2.set_title('2)With marker size 50% and alpha 50%')
    # Default size is rcParams['lines.markersize'] ** 2
    ax2.scatter(longitude, latitude, s=(rcParams['lines.markersize'] ** 2) * 0.5, alpha=0.5)
    ax2.set_xlabel('longitude')
    ax2.set_ylabel('latitude')

    # With hexbin plot
    ax3 = axs[1, 0]
    ax3.set_title('3)With hexbin plot')
    hb = ax3.hexbin(x=longitude, y=latitude, bins='log', cmap='viridis')
    ax3.set_xlabel('longitude')
    ax3.set_ylabel('latitude')
    # Colorbar
    cb = fig.colorbar(hb, ax=ax3)
    cb.set_label('log10(N)')

    # With Subsampling
    ax4 = axs[1, 1]
    sub_longitude = longitude[0:50000]
    sub_latitude = latitude[0:50000]
    ax4.set_title('4)With Subsampling(first 50000 values)')
    ax4.scatter(sub_longitude, sub_latitude)
    ax4.set_xlabel('longitude')
    ax4.set_ylabel('latitude')
    plt.show()


def main():
    # graph_pdf()
    graph_word()


if __name__ == '__main__':
    main()
