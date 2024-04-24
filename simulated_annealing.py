import math
import random
import matplotlib.pyplot as plt
import tsp_utils
import animated_visualizer
import time


class SimulatedAnnealing:
    
    def __init__(self, coords, temp, alpha, stopping_temp, stopping_iter):
        ''' animate the solution over time

            Parameters
            ----------
            coords: array_like
                list of coordinates
            temp: float
                initial temperature
            alpha: float
                rate at which temp decreases
            stopping_temp: float
                temerature at which annealing process terminates
            stopping_iter: int
                interation at which annealing process terminates

        '''
        global t1
        t1 =time.time()
        self.coords = coords
        self.sample_size = len(coords)
        self.temp = temp
        self.alpha = alpha
        self.stopping_temp = stopping_temp
        self.stopping_iter = stopping_iter
        self.iteration = 1
        global minw
        self.minw=[]
        self.dist_matrix = tsp_utils.vectorToDistMatrix(coords)
        #self.curr_solution = tsp_utils.nearestNeighbourSolution(self.dist_matrix)
        filename = 'christ.txt'
        ys=[]

        file = open(filename, 'r')
        read = file.readline()
        for line in file:
            ys.append(int((line.strip())))
        file.close()
        self.curr_solution = ys
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

        #print('Intial weight: ', self.curr_weight)

    def weight(self, sol):
        '''
        Calcuate weight
        '''
        return sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])

    def acceptance_probability(self, candidate_weight):
        '''
        Acceptance probability as described in:
        https://stackoverflow.com/questions/19757551/basics-of-simulated-annealing-in-python
        '''
        return math.exp(-abs(candidate_weight - self.curr_weight) / self.temp)

    def accept(self, candidate):
        '''
        Accept with probability 1 if candidate solution is better than
        current solution, else accept with probability equal to the
        acceptance_probability()
        '''
        #Difine Holder of the minimum wight coordinates:
        global minw
        candidate_weight = self.weight(candidate)
        if candidate_weight < self.curr_weight:
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
            if candidate_weight < self.min_weight:
                self.min_weight = candidate_weight
                self.best_solution = candidate
                self.minw = self.curr_solution
        

        else:
            if random.random() < self.acceptance_probability(candidate_weight):
                self.curr_weight = candidate_weight
                self.curr_solution = candidate
        return self.minw
    def anneal(self):
        '''
        Annealing process with 2-opt
        described here: https://en.wikipedia.org/wiki/2-opt
        '''
        while self.temp >= self.stopping_temp and self.iteration < self.stopping_iter:
            candidate = list(self.curr_solution)
            l = random.randint(2, self.sample_size - 1)
            i = random.randint(0, self.sample_size - l)

            candidate[i: (i + l)] = reversed(candidate[i: (i + l)])

            mtour = self.accept(candidate)

            self.temp *= self.alpha
            self.iteration += 1
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)
        global t2 
        t2 = time.time()
        global timecost
        timecost = t2-t1
        return mtour
        #print('Minimum weight: ', self.min_weight)
        #print('Improvement: ',
        #      round((self.initial_weight - self.min_weight) / (self.initial_weight), 4) * 100, '%')
        

        
    #def animateSolutions(self):
    #    animated_visualizer.animateTSP(self.solution_history, self.coords)
     

    #def plotLearning(self):
       # plt.plot([i for i in range(len(self.weight_list))], self.weight_list)
        #line_init = plt.axhline(y=self.initial_weight, color='r', linestyle='--')
        #line_min = plt.axhline(y=self.min_weight, color='g', linestyle='--')
        #plt.legend([line_init, line_min], ['Initial weight', 'Optimized weight'])
        #plt.ylabel('Weight')
        #plt.xlabel('Iteration')
        #plt.show()
    def savefiles(self):
        filename = ('aneal.txt')
        f = open(filename, 'w')
        with open('aneal.txt', 'w') as f:
            f.write('\n')
            f.write(str(self.min_weight))
            f.write('\n')
            f.write(str(timecost))
            f.write('\n')
        f.close()
        #print(minw)
       
            