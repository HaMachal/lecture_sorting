import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(number_array, direction='ascending'):
    """

    :param number_array: list with numeric array
    :param direction: string indicating direction: ascending/descending
    :return: sorted numeric array
    """
    for i in range(len(number_array)):
        extreme_idx = i
        for j in range(i + 1, len(number_array)):
            if (direction == "ascending") & (number_array[j] < number_array[extreme_idx]):
                extreme_idx = j
            elif (direction == "descending") & (number_array[j] > number_array[extreme_idx]):
                extreme_idx = j
        number_array[i], number_array[extreme_idx] = number_array[extreme_idx], number_array[i]
    return number_array

def bubble_sort(number_array):
    """

    :param number_array: list of numbers to be sorted
    :return: sorted numeric array
    """
    # Není moc efektivní, for cyklus by mohl být n - i dlouhý –> upravit vnější for cyklus na i
    bool = True
    while bool:
        bool = False
        for i in range(len(number_array) - 1):
            if number_array[i] > number_array[i + 1]:
                number_array[i], number_array[i + 1] = number_array[i + 1], number_array[i]
                bool = True
    return number_array

def bubble_sort2(number_array):
    n = len(number_array)
    for i in range(n - 1):
        for num_idx in range(n - i):
            if number_array[num_idx] > number_array[num_idx + 1]:
                number_array[num_idx], number_array[num_idx + 1] = number_array[num_idx + 1], number_array[num_idx]

def insertion_sort(number_arr):
    for i in range(1, len(number_arr)):
        idx = i
        while number_arr[idx] < number_arr[idx - 1]:
            number_arr[idx - 1], number_arr[idx] = number_arr[idx], number_arr[idx - 1]
            idx = idx - 1
    return number_arr


def main():
    data = read_data("numbers.csv")
    print(data)
    print(insertion_sort(data["series_2"]))


if __name__ == '__main__':
    main()
