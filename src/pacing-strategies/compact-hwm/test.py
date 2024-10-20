import unittest
import numpy as np
from sim import solve, online_serve

K = 1_000
M = 1_000_000
B = 1_000_000_000

class TestSolver(unittest.TestCase):
    
    def testExampleInPaper(self):
        # define demand
        demands= np.array([200 * K, 200 * K, 1 * M])
        # define supply
        supplies = np.array([400 * K, 400 * K, 100 * K, 100 * K, 500 * K, 300 * K])
        # define edges
        edges = np.full((len(supplies), len(demands)), False)
        edges[0][0] = edges[0][2] = True
        edges[1][2] = True
        edges[2][1] = edges[2][2] = True
        edges[3][1] = edges[3][2] = True
        edges[4][2] = True
        edges[5][2] = True
        probs = solve(supplies, demands, edges)
        print(probs)
        
    
    def test2(self):
        pass


if __name__ == '__main__':
    unittest.main()