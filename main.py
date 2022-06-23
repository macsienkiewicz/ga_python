"""
Zmiana wzgledem etapu 2:  W pliku Population.py czesc selekcji ruletkowej wykonywana jest w
metodzie genetic_algorithm zamiast w roulette_selection, zeby pewne operacje mogly zostac
wykonane jedynie raz w ramach jednego pokolenia a nie za kazdym razem, kiedy wybierany
jest rodzic.
"""

from Data import Data
from Population import Population, genetic_algorithm
from Space import Space

if __name__ == '__main__':
    easy_data = Data('data\\easy_flow.json',
                'data\\easy_cost.json', 9)
    flat_data = Data('data\\flat_flow.json',
                'data\\flat_cost.json', 12)
    hard_data = Data('data\\hard_flow.json',
                'data\\hard_cost.json', 24)

    easy_space = Space(3, 3, 9, easy_data)
    flat_space = Space(1, 12, 12, flat_data)
    hard_space = Space(5, 6, 24, hard_data)

    (easy_space.matrix, easy_space.coordinates) = easy_space.get_random_matrix()
    (flat_space.matrix, flat_space.coordinates) = flat_space.get_random_matrix()
    (hard_space.matrix, hard_space.coordinates) = hard_space.get_random_matrix()

    print("easy: " + str(easy_space.fitness_function()))
    print("flat: " + str(flat_space.fitness_function()))
    print("hard: " + str(hard_space.fitness_function()))

    print("................................................\nEasy:")
    population_easy = Population(3, 3, 9, easy_data, 100)
    genetic_algorithm(population_easy, 50, 0.7, 0.2)

    print("................................................\nFlat:")
    population_flat = Population(1, 12, 12, flat_data, 100)
    genetic_algorithm(population_flat, 50, 0.7, 0.2)

    print("................................................\nHard:")
    population_hard = Population(5, 6, 24, hard_data, 100)
    genetic_algorithm(population_hard, 50, 0.7, 0.2)






