import math
from collections import Counter
import pandas as pd
import numpy as np
from maps import foot_length, foot_the_ball, sizes
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def knn_calc(ds_data, user_data):
    x1, y1 = ds_data
    x2, y2 = user_data

    delta_x = x1-x2
    delta_y = y1-y2

    return math.sqrt((delta_x**2) + (delta_y**2))

def knn(k, X_train, y, user_data):
    distances = []

    for i, ds_data in enumerate(X_train):
        dist = knn_calc(ds_data, user_data)
        distances.append({'dist': dist, 'size': y[i]})

    distances.sort(key=lambda data: data['dist'])
    distances = distances[:k]

    counter = Counter([d['size'] for d in distances])
    return counter.most_common(1)[0][0]

def main():



    gender = input('Your gender? M/F')
    if gender == 'M':
        df = pd.read_csv('male_clean.csv')
    else:
        df = pd.read_csv('female_cleaned.csv')
    while True:
        foot_length = input('How long is your feet in mm? ')
        if foot_length.isdigit():
            foot_length = int(foot_length)
            for foot in foot_length:
                foot_size = [f_l for f_l, f_l_range in foot_length.items() if int(foot) in f_l_range]
                if len(foot_size) > 0:
                    foot_size = foot_size[0]
                    shoe_size = sizes[foot_size]
                else:
                    print('no value')
            break
        print('Numbers pls')
    foot_lengths = df.footlength.tolist()
    while True:
        foot_circ = input('Measurement ball of foot in mm? ')
        if foot_circ.isdigit():
            foot_circ = int(foot_circ)
            break
        print('Numbers pls')



if __name__ == '__main__':
    main()