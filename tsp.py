from numpy import append
from nodes_generator import NodeGenerator
from simulated_annealing import SimulatedAnnealing


global v

def main():
    '''set the simulated annealing algorithm params'''
    temp = 1
    stopping_temp = 0.0000001
    alpha = 0.9995
    stopping_iter = 100000000

    '''set the dimensions of the grid'''
    size_width = 200
    size_height = 200

    

    '''generate random list of nodes'''
    nodes, v = NodeGenerator(size_width, size_height).generate()
    '''set the number of nodes'''
    population_size = v+1

    '''run simulated annealing algorithm with 2-opt'''
    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    '''animate'''
    sa.animateSolutions()

    '''show the improvement over time'''
    sa.plotLearning()


if __name__ == "__main__":
    main()
    