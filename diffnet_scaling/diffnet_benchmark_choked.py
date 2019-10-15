import matplotlib
from matplotlib import pyplot as plt 
import networkx as nx
import numpy as np
from scipy import linalg
from cvxopt import matrix
import examples as eg
import graph as gph
import sys
import diffnet as dn
import time

# ram limiting:
import sys
import resource
# credits to https://stackoverflow.com/questions/41105733/limit-ram-usage-to-python-program

## these are the matrices we have to imitate:
# nheavy = dict(A1=7, A2=6, B1=9, B2=6, C1=10, C2=10)
# sCOX2 = np.diag( [nheavy['A1'] + nheavy['B1'] + nheavy['C1'],
#                   nheavy['A1'] + nheavy['B1'] + nheavy['C2'],
#                   nheavy['A1'] + nheavy['B2'] + nheavy['C1'],
#                   nheavy['A1'] + nheavy['B2'] + nheavy['C2'],
#                   nheavy['A2'] + nheavy['B1'] + nheavy['C1'],
#                   nheavy['A2'] + nheavy['B1'] + nheavy['C2'],
#                   nheavy['A2'] + nheavy['B2'] + nheavy['C1'],
#                   nheavy['A2'] + nheavy['B2'] + nheavy['C2']]) + \
#        np.array( [[ 0,  1, 16, 17,  1,  2, 16, 17],
#                   [ 1,  0, 17, 16,  2,  1, 17, 16],
#                   [16, 17,  0,  1, 16, 17,  1,  2],
#                   [17, 16,  1,  0, 17, 16,  2,  1],
#                   [ 1,  2, 16, 17,  0,  1, 16, 17],
#                   [ 2,  1, 17, 16,  1,  0, 17, 16],
#                   [16, 17,  1,  2, 16, 17,  0,  1],
#                   [17, 16,  2,  1, 17, 16,  1,  0]], dtype=float)



def random_sym_matrix(n):
    """
    - generates a constants matrix modeled after the matrix normally inserted in the diffnet example

    args:
    - n: integer [>=2]
    
    returns:
    - the intended symmetrical matrix
    """
    a = 2
    A = np.matrix([np.random.randn(n) + np.random.randn(1)*a for i in range(n)])
    A = A*np.transpose(A)
    D_half = np.diag(np.diag(A)**(-0.5))
    prematrix = abs((D_half*A*D_half)-1)*10
    return prematrix.astype(int)



def main():
	# with increasing sizes of n, generate fictive variance matrices and record diffnet runtimes.
    for n in np.arange(8, 5000, 1):
        start = time.time()
        # these are the ways we imitate the matrices:
        lig_weights = np.diag(np.random.randint(22, 26, n))
        lig_constants = random_sym_matrix(n)
        pre_sij = lig_weights + lig_constants

        ## sometimes we get zeroes in the matrix; prevent this:
        pre_sij += 1

        # then the examplatory transformations are applied:
        pre_sij = pre_sij.astype(float)
        pre_sij = np.sqrt(pre_sij)
        sij = matrix(pre_sij)

        # now run the optimiser:
        results = dn.optimize( sij, optimalities=[ 'D', 'A', 'Etree'] )

        print "#############################"
        print "Finished computing for", n, "nodes."

        # record elapsed time and append to file:
        end = time.time()
        elapsed = (end - start)
        row = str(n)+","+str(elapsed)+"\n"
        with open("output/diffnet_5.csv", "a") as myfile:
            myfile.write(row)





def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (get_memory() * 1024 * 0.7, hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) == 'MemAvailable:':
                free_memory += int(sline[1])
                print(free_memory)
    return free_memory










if __name__ == '__main__':
    memory_limit() # Limits maximum memory usage to 70%
    try:
        main()
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)


	