from is_inisde_circle import is_inside_circle
import numpy as np
def single_experiment():
    num_points=10000
    rng = np.random.default_rng()
    points = ((rng.random((num_points, 2)))-0.5)*2
    
    num_points_inside=0

    for p in points:
        if is_inside_circle(p,1):
            num_points_inside+=1

    pi=4*(num_points_inside/num_points)
    #print(f'pi is aprox:{pi}')
    return pi
