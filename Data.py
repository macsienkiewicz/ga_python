import json
import numpy


class Data:
    def __init__(self, file_flow, file_cost, number):
        self.data_flow = load_data(file_flow, True, number)
        self.data_cost = load_data(file_cost, False, number)
        self.number = number


def load_data(file, flow, number): #ladowanie danych
    f = open(file)
    data = json.load(f)
    f.close()
    data_matrix = numpy.zeros((number, number))
    for i in range(0, len(data)):
        if flow:
            data_matrix[data[i]['source']][data[i]['dest']] = int(data[i]['amount'])
            data_matrix[data[i]['dest']][data[i]['source']] = int(data[i]['amount'])
        else:
            data_matrix[data[i]['source']][data[i]['dest']] = int(data[i]['cost'])
            data_matrix[data[i]['dest']][data[i]['source']] = int(data[i]['cost'])
    return data_matrix
