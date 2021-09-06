import math


from math import sqrt
from single_experiment import single_experiment
import numpy as np


def do_experiments(num_experiments):
    results=[]
    print('Num of experimets:',num_experiments)
    for i in range(num_experiments):
        results.append(single_experiment())
        print(f' runing experiment:{i}', end='\r')

    result_arr=np.array(results)
    results_obj={}
    results_obj['mean']=np.mean(result_arr)
    results_obj['var']=np.var(result_arr)
    return results_obj

print(''.center(100,'-'))
print('Finding PI by the Monte Carlo method'.center(100,' '))
print(''.center(100,'-'))

num_experiments=500
print("Setting base values")
base=do_experiments(num_experiments)

result=None
for i in range(100):
    print(f" Iter num#{i+1} ".center(75,'-'))
    num_experiments+=100
    result=do_experiments(num_experiments)
    percentage_var=abs(result['var']-base['var'])/base['var']
    percentage_mean=abs(result['mean']-base['mean'])/(base['mean']-3)

    print(f'variation, mean={percentage_mean*100:.2f}% variance={percentage_var*100:.2f}%')
    print(result)
    if percentage_var<0.03 and percentage_mean<0.03:
        break
    else:
         base=result
    
sd=sqrt(result['var'])
print(f"Approximate value of pi {result['mean']} SD={sd} #experiments={num_experiments}")
print(f" interval [{result['mean']-sd},{result['mean']+sd}]")