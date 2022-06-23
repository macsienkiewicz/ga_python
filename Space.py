from random import randint
import numpy


class Space:
    def __init__(self, rows, columns, number, data):
        self.rows = rows
        self.columns = columns
        self.number = number
        self.matrix = numpy.empty((rows, columns))
        self.matrix[:] = -1
        self.coordinates = []
        self.data = data

    def fitness_function(self): #funkcja przystosowania
        sum = 0
        for i in range(0, len(self.data.data_flow)):
            for j in range(i + 1, len(self.data.data_flow)):
                s = (abs(int(self.coordinates[i][0]) - int(self.coordinates[j][0])) + abs(
                    int(self.coordinates[i][1]) - int(self.coordinates[j][1]))) * int(self.data.data_flow[i][j]) * int(
                    self.data.data_cost[i][j])
                sum = sum + s
        return sum

    def get_random_matrix(self):  # metoda losowa
        matrix = numpy.empty((self.rows, self.columns))
        matrix[:] = -1
        coordinates = []
        for i in range(0, self.number):
            (x_fin, y_fin) = get_random_numbers(self.rows, self.columns, matrix)
            matrix[x_fin][y_fin] = int(i)
            coordinates.append((x_fin, y_fin))
        return matrix, coordinates



def get_random_numbers(rows, columns, matrix):
    rand_x = randint(0, rows - 1)
    rand_y = randint(0, columns - 1)
    if matrix[rand_x][rand_y] == -1:
        return int(rand_x), int(rand_y)
    else:
        return get_random_numbers(rows, columns, matrix)








