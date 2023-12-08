"""
AoC Day 6
"""

from numpy import prod

# Part 1

def get_num_soln(Time, Distance):
    result = prod([sum([(i * (t-i)) > d for i in range(t)]) for t,d in zip(Time,Distance)])
    return result

Time = [52, 94, 75, 94]
Distance = [426, 1374, 1279, 1216]

[sum([(i * (t-i)) > d for i in floor(range(t/2))]) for t,d in zip(Time,Distance)]
get_num_soln(Time,Distance)

# Part 2
def kern(x):
    result = [int(''.join([str(i) for i in x]))]
    return result
kerned_Time = kern(Time)
kerned_Distance = kern(Distance)
get_num_soln(kerned_Time, kerned_Distance)


