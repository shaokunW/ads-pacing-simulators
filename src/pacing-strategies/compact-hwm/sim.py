import numpy as np
# offline

n = 3
m = 4
# Biparti Graph
# given n supplies and m demands


# define demand
demands= np.zeros(m)
# define supply
supplies = np.zeros(n)
# define edges
edges = np.zeros((n, m))

# objective
# solver
def solve(supplies, demands, edges, order_func):
    remaing_supplies = supplies.copy()
    demands = order_func(demands)
    d_s = {}
    for d_i in range(demands):
        targeted = []
        for s_j in range(supplies):
            if edges[s_j][d_i]:
                targeted.append(s_j)
        d_s[d_i] = targeted
    alphas = []
    for d_i in range(demands):
        targeted = d_s[d_i]
        targetd_supplies = [supplies[j] for j in targeted]
        # a) solve alphaj
        alpha = solve_alpha(targetd_supplies, remaing_supplies, demands[d_i])
        # b) update ri
        for s_j in targeted:
            r = remaing_supplies[s_j]
            remaing_supplies[s_j] = r - min(r, supplies[s_j] *alpha)
        alphas.append(alpha)
    return alphas


def solve_alpha(targetd_supplies, suplies, remaing_supplies, demand, max_iter = 20):
    l = 0
    # set right to 2 so we can start from 1 to see if there is a solution
    # if no solution, then the alpha will be larger than 1, so we can return 1 as per the paper
    r = 2
    while max_iter > 0:
        alpha = (l + r) / 2
        if alpha > 1:
            return 1
        total = sum([min(remaing_supplies[i], suplies[i] * alpha) for i in targetd_supplies])
        if abs(total - demand) < 1:
            return alpha
        elif total > demand:
            r = alpha
        else:
            l = alpha
        max_iter = max_iter - 1
    return alpha


# allocation order
def allocation_order(arr):
    return arr


# online serving
def online_serve(supplies, demands, edges, alphas, order_func, feedback_func):
    pass