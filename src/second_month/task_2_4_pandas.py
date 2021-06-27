import pandas as pd
import numpy as np

# task 1
# Write a Pandas program to add, subtract, multiple and divide two Pandas Series
a = pd.Series([1, 2, 1, np.nan], index=['a', 'b', 'c', 'd'])
b = pd.Series([3, 1, 2, np.nan], index=['a', 'b', 'c', 'd'])


def pandas_alg(a, b):
    print("Summ is\n", a.add(b), "\nSubtraction is\n", a.subtract(b), "\nMultiplication is\n", a.multiply(b),
          "Division is\n", a.divide(b))


# task2
# Write a Pandas program to convert a dictionary to a Pandas series
dict = {"a": 5, "b": 7, "c": 6, "d": 9}


def dict_convert(dict):
    return pd.Series(dict)


# task3
# Write a Pandas program to convert a NumPy array to a Pandas series
array = np.array([2, 6, 8, 9, 6])


def array_convert(array):
    return pd.Series(array)


# task4
# Write a Pandas program to convert the first column of a DataFrame as a Series

data = pd.DataFrame({"x": [1, 2], "y": [3, 4]})


def df_series(data,a):
    return pd.Series(data[a])


# task5
# Write a Pandas program to sort a given Series

def sort(a):
    return a.sort_values()


# task6
# Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def select_score(exam_data,column):
    df = pd.DataFrame(exam_data)
    return df.loc[(df[column].between(15,20))]



# task7
# Write a Pandas program to calculate the sum of the examination attempts by the students.

exam_data_1 = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def sum_of_examination_attempts(exam_data_1, a):
    df = pd.DataFrame(exam_data_1)
    if df[a].dtypes == int:
        return "Sum of the examination attempts by the students : {}".format(sum(df[a]))


def main():
    pandas_alg(a, b)
    print(dict_convert(dict))
    print(array_convert(array))
    print(df_series(data,"x"))
    print(sort(a))
    print(select_score(exam_data,"score"))
    print(sum_of_examination_attempts(exam_data_1,'attempts'))


main()
