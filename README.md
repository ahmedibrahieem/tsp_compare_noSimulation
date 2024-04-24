Visualisation of Simulated Annealing algorithm to solve the Travelling Salesman Problem in Python
=======
Using [simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) metaheuristic to solve the [travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), and animating the results.

A simple implementation which provides decent results.

Requires [python3](https://docs.python.org/3/), [matplotlib](https://matplotlib.org/) and [numpy](http://www.numpy.org/) to work

--------
The new update will not show the simulation of the anealing algorithn progress, but if you want to show them, you can go and uncomint ploting lines in the simulating_anealing file. The .dat files stores matrecies of the output of the comparison process. The ones with "1" at the end of the name (like "NN1.dat") are done by repeatin the iterations for 50 times and taking the average, while the ones without "1" at the end of the naem are done by 10 iterations only (like "NN.dat"). Those files are for referencing. 

A problem we have currently is that some times the simulated anealing algorithm does not work, and I do not know why.  
