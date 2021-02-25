from collections import defaultdict
from random import randint

import numpy as np

from hashcode.utils import load, save


def solve(pid):
    gs = load(pid)

    intersection_times = defaultdict(lambda: defaultdict(float))
    intersection_counts = defaultdict(int)

    for car_path in gs.car_paths:
        t = 0
        steps_left = len(car_path)
        total_steps = steps_left

        for c in car_path:
            steps_left -= 1
            street = gs.streets[c]
            intersection_times[street.end][c] += 1 - (t / gs.D)
            intersection_counts[street.end] += 1
            t += street.l

    for k, v in intersection_times.items():
        norm = np.array(list(v.values())).sum()
        for _v in v.keys():
            v[_v] /= norm

    output = {}

    for k in intersection_counts.keys():
        v = intersection_times[k]
        for _v in v.keys():
            v[_v] *= intersection_counts[k]
            v[_v] = min(np.ceil(v[_v]).astype("int"), gs.D)
            v[_v] = 1

        output[k] = list(v.items())

    return output, gs.street_names


for pid in range(6):
    save(pid, *solve(pid))
