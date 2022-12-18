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
    plt.bar(english_df['Full name'], english_df['Points'], width=1.0, edgecolor='black')
    plt.bar(russian_df['Full name'], russian_df['Points'], width=1.0, edgecolor='black')
    plt.bar(mathematics_df['Full name'], mathematics_df['Points'], width=1.0, edgecolor='black')
    plt.grid()
    plt.legend(labels=['English', 'Russian', 'Mathematics'])
    plt.title('The Points of Teachers of 3 disciplines', fontsize=20, weight='bold')
    plt.xlabel('Teachers', fontsize=20)
    plt.ylabel('Points(%)', fontsize=20)
    plt.show()

    # Task 2.2: You need to deduce data on work experience, education, teaching methods of teachers
    # who teach disciplines
    df = pd.DataFrame([
        ['John John', 5, 'Phd', 'offline', 'English'],
        ['Joe Sam', 7, 'Magistrate', 'online', 'English'],
        ['Lars Jake', 12, 'Magistrate', 'offline', 'English'],
        ['Carl Carl', 11, 'Phd', 'offline', 'Mathematics'],
        ['Alexandr Lars', 13, 'Magistrate', 'offline', 'Mathematics'],
        ['Joe Jake', 14, 'Magistrate', 'offline', 'Mathematics'],
        ['Mary Mary', 17, 'Phd', 'online', 'Russian'],
        ['Mary Lars', 18, 'Magistrate', 'online', 'Russian'],
        ['Don Jey', 19, 'Magistrate', 'offline' 'Russian'],
    ], columns=['Full name', 'Working Experience', 'Education', 'Teaching Method', 'Discipline'])
    fig, axs = plt.subplots(2, 2, figsize=(16, 9))
    plt.suptitle('Statistics of teachers')
    # Working Experience
    ax1 = axs[0, 0]
    experience_less_than_10 = df[df['Working Experience'] < 10].count()[0]
    experience_less_than_15 = df[df['Working Experience'] < 15].count()[0]
    experience_more_than_15 = df[df['Working Experience'] >= 15].count()[0]
    all_experience = [experience_less_than_10, experience_less_than_15, experience_more_than_15]
    ax1.pie(all_experience, autopct='%1.1f%%')
    ax1.set_title('Working Experience')
    ax1.legend(['Experience less than 10',
                'Experience less than 15',
                'Experience equal or more than 15'],
               loc='lower left', bbox_to_anchor=(-0.5, 0, 0.5, 0.5))
    # Education
    ax2 = axs[0, 1]
    magistrate = df[df['Education'] == 'Magistrate'].count()[0]
    phd = df[df['Education'] == 'Phd'].count()[0]
    all_education = [magistrate, phd]
    ax2.pie(all_education, autopct='%1.1f%%')
    ax2.set_title('Education')
    ax2.legend(['Magistrate',
                'Phd'],
               loc='lower left', bbox_to_anchor=(-0.5, 0, 0.5, 0.5))
    # Teaching Method
    ax3 = axs[1, 0]
    offline = df[df['Teaching Method'] == 'offline'].count()[0]
    online = df[df['Teaching Method'] == 'online'].count()[0]
    all_teaching_methods = [offline, online]
    ax3.pie(all_teaching_methods, autopct='%1.1f%%')
    ax3.set_title('Teaching Method')
    ax3.legend(['offline',
                'online'],
               loc='lower left', bbox_to_anchor=(-0.5, 0, 0.5, 0.5))
    # Discipline
    ax4 = axs[1, 1]
    english = df[df['Discipline'] == 'English'].count()[0]
    mathematics = df[df['Discipline'] == 'Mathematics'].count()[0]
    russian = df[df['Discipline'] == 'Russian'].count()[0]
    all_disciplines = [english, mathematics, russian]
    ax4.pie(all_disciplines, autopct='%1.1f%%')
    ax4.set_title('Discipline')
    ax4.legend(['English',
                'Mathematics',
                'Russian'],
               loc='lower left', bbox_to_anchor=(-0.5, 0, 0.5, 0.5))
    plt.show()

    # Task 2.3: You need to make a data output using all the graph types presented
    car = ['Daewoo', 'Mercedes', 'Samsung', 'Toyota', 'Honda']
    explode = (0.05, 0.05, 0.05, 0.05, 0.05)
    number_of_cars = [255000, 300000, 70000, 450000, 130000]
    plt.pie(number_of_cars, labels=car, explode=explode, autopct='%1.1f%%', pctdistance=0.80)
    # Draw a Circle
    centre = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    # Add in Pie Chart
    fig.gca().add_artist(centre)
    plt.title('The popularity of car brands in Kazakhstan')
    plt.show()


def graph_pdf():
    # Reading of CSV
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    plt.suptitle('Difference between longitude and latitude values')
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
