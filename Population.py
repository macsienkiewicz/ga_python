"""
Zmiana wzgledem etapu 2:  W pliku Population.py czesc selekcji ruletkowej wykonywana jest w
metodzie genetic_algorithm zamiast w roulette_selection, zeby pewne operacje mogly zostac
wykonane jedynie raz w ramach jednego pokolenia a nie za kazdym razem, kiedy wybierany
jest rodzic.
"""

import random
from Space import Space, get_random_numbers


class Population:
    def __init__(self, rows, columns, number, data, population_size):
        self.spaces = []
        self.size = population_size
        self.rows = rows
        self.columns = columns
        self.number = number
        self.data = data

    def create_population(self):
        spaces = []
        for i in range(0, self.size):
            sp = Space(self.rows, self.columns, self.number, self.data)
            sp.matrix, sp.coordinates = sp.get_random_matrix()
            spaces.append(sp)
        return spaces



    def tournament_selection(self, n):
        tournament = []
        chosen_spaces = []
        for i in range(0, n):
            x = random.randint(0, len(self.spaces) - 1)
            while x in chosen_spaces:
                x = random.randint(0, len(self.spaces) - 1)
            tournament.append(self.spaces[x])
            chosen_spaces.append(x)
        best_fitness = None
        best_x = 0
        for i in range(0, n):
            if best_fitness is None:
                best_fitness = tournament[i].fitness_function()
                best_x = i
            if tournament[i].fitness_function() < best_fitness:
                best_x = i
        return tournament[best_x]


    def roulette_selection(self, section):
        """
        total = 0
        for i in range(0, len(self.spaces)):
            total = total + (1 / self.spaces[i].fitness_function())
        last = 0.0
        section = []
        for i in range(0, len(self.spaces)):
            y = (1 / self.spaces[i].fitness_function())/total
            section.append((last, last + y))
            last = last + y
        """
        rand = random.uniform(0.0, 1.0)
        chosen = 0
        for i in range(0, len(section)):
            if section[i][0] < rand <= section[i][1]:
                chosen = i
        return self.spaces[chosen]






    def crossover(self, p1, p2):
        o1 = Space(self.rows, self.columns, self.number, self.data)
        for i in range(0, self.number):
            #krok 1
            if o1.matrix[p1.coordinates[i][0]][p1.coordinates[i][1]] == -1 and o1.matrix[p2.coordinates[i][0]][p2.coordinates[i][1]] == -1:
                rand = random.randint(1, 2)
                if rand == 1:
                    o1.matrix[p1.coordinates[i][0]][p1.coordinates[i][1]] = i
                    o1.coordinates.append((p1.coordinates[i][0], p1.coordinates[i][1]))
                else:
                    o1.matrix[p2.coordinates[i][0]][p2.coordinates[i][1]] = i
                    o1.coordinates.append((p2.coordinates[i][0], p2.coordinates[i][1]))
            #krok 2
            elif o1.matrix[p1.coordinates[i][0]][p1.coordinates[i][1]] == -1 and o1.matrix[p2.coordinates[i][0]][p2.coordinates[i][1]] != -1:
                o1.matrix[p1.coordinates[i][0]][p1.coordinates[i][1]] = i
                o1.coordinates.append((p1.coordinates[i][0], p1.coordinates[i][1]))
            #krok 3
            elif o1.matrix[p1.coordinates[i][0]][p1.coordinates[i][1]] != -1 and o1.matrix[p2.coordinates[i][0]][p2.coordinates[i][1]] == -1:
                o1.matrix[p2.coordinates[i][0]][p2.coordinates[i][1]] = i
                o1.coordinates.append((p2.coordinates[i][0], p2.coordinates[i][1]))
            #krok 4
            else:
                (x_fin, y_fin) = get_random_numbers(self.rows, self.columns, o1.matrix)
                o1.matrix[x_fin][y_fin] = int(i)
                o1.coordinates.append((x_fin, y_fin))
        return o1
    """
    Jak wyglada procedura krzyzowania:
    Dla obojga rodzicow p1 i p2 sprawdzam polozenie n-tej maszyny.
    Sprawdzam teraz czy te polozenia u dziecka jest juz zajete przez inna maszyne 
    1. Jezeli polozenie zarowno od rodzica p1 jak i p2 u dziecka o1 nie jest zajete przez inna maszyne
    to losuje na zasadzie 50:50 i dla n-tej maszyny dla dziecka wybieram jedno z tych dwoch polozen.
    2. Jezeli polozenie od rodzica p1 jest wolne ale polozenie od rodzica p2 jest zajete przez inna maszyne
    to n-ta maszyna u dziecka laduje w tym samym polozeniu co u rodzica p1
    3. Jezeli polozenie od rodzica p1 jest zajete przez inna maszyne ale polozenie od rodzica p2 jest wolne
    to n-ta maszyna u dziecka laduje w tym samym polozeniu co u rodzica p2
    4. Jezeli polozenie od rodzicow p1 i p2 sa zajete przez inne maszyny to losuje dla n-tej maszyny dowolne miejsce.
    
    Przyklad:
    Sprawdzam polozenie 6-tej maszyny u p1 i p2. U p1 jest ona w polu (2, 1) a u p2 (1, 2).
    Przypadek 1. U dziecka pola (2, 1) i (1, 2) jest puste, wiec losuje jedno z tych dwoch miejsc i wstawiam tam
    6-ta maszyne
    Przypadek 2: U dziecka pole (2, 1) jest puste ale (1, 2) zajete przez maszyne 4-ta, wiec maszyna 6-ta laduje 
    w polu (2, 1)
    Przypadek 3: U dziecka pole (2, 1) jest zajete przez 3-cia maszyne ale (1, 2) jest puste, wiec maszyna 6-ta laduje 
    w polu (1, 2)
    Przypadek 4: U dziecka pole (2, 1) jest zajete przez 2-ga maszyne a (1, 2) zajete przez 5-ta maszyne, wiec losuje
    dowolne puste miejsce dla 6-tej maszyny u dziecka, np. (1, 1). 
    """




    def mutation(self, o1):
        m1 = random.randint(0, int(self.number) - 1)
        m2 = random.randint(0, int(self.number) - 2)
        if m2 >= m1:
            m2 = m2 + 1
        m2_x = o1.coordinates[m2][0]
        m2_y = o1.coordinates[m2][1]
        o1.coordinates[m2] = (o1.coordinates[m1][0], o1.coordinates[m1][1])
        o1.matrix[o1.coordinates[m1][0]][o1.coordinates[m1][1]] = m2
        o1.coordinates[m1] = (m2_x, m2_y)
        o1.matrix[m2_x][m2_y] = m1
        return o1





def genetic_algorithm(population, final_t, p_crossover, p_mutation):
    population.spaces = population.create_population()
    t = 0
    best_zero = None
    for i in range(0, population.size):
        if best_zero is None or population.spaces[i].fitness_function() < best_zero:
            best_zero = population.spaces[i].fitness_function()
    best_all = None
    while t < final_t:
        """
        Przygotowanie do selekcji ruletkowej:
        """
        total = 0
        for i in range(0, len(population.spaces)):
            total = total + (1 / population.spaces[i].fitness_function())
        last = 0.0
        section = []
        for i in range(0, len(population.spaces)):
            y = (1 / population.spaces[i].fitness_function()) / total
            section.append((last, last + y))
            last = last + y
        """
        """
        new_pop = Population(population.rows, population.columns, population.number, population.data, population.size)
        best = None
        worst = None
        sum = 0
        while len(new_pop.spaces) <= new_pop.size:
            rand = random.randint(1, 2)
            p1 = population.roulette_selection(section)
            p2 = population.roulette_selection(section)
            if rand == 1:
                p1 = population.tournament_selection(20)
            else:
                p1 = population.roulette_selection(section)
            rand = random.randint(1, 2)
            if rand == 1:
                p2 = population.tournament_selection(20)
            else:
                p2 = population.roulette_selection(section)
            if random.uniform(0.0, 1.0) < p_crossover:
                o1 = population.crossover(p1, p2)
                new_pop.spaces.append(o1)
            else:
                o1 = p1
                new_pop.spaces.append(o1)
            if random.uniform(0.0, 1.0) < p_mutation:
                o1 = population.mutation(o1)
            if best is None or o1.fitness_function() < best:
                best = o1.fitness_function()
            if worst is None or o1.fitness_function() > worst:
                worst = o1.fitness_function()
            sum = sum + o1.fitness_function()
        if best_all is None or best < best_all:
            best_all = best
        avg = sum/new_pop.size
        print(str(t+1) + "\t" + str(worst) + "\t" + str(best)+ "\t" + str(int(avg)))
        population = new_pop
        t = t + 1
    #print(str(best_zero) + "\t" + str(best_all))








