import numpy as np

def test_day6():
    Time = [52, 94, 75, 94]
    Distance = [426, 1374, 1279, 1216]
    result = np.prod([sum([(i * (t-i)) > d for i in range(t)]) for t,d in zip(Time,Distance)])
    assert result > 0