from collections import defaultdict

import numpy as np

from hashcode.utils import load, save

val = 5
val2 = 0


def solve(pid):
    gs = load(pid)

    intersection_times = defaultdict(lambda: defaultdict(float))
    intersection_counts = defaultdict(int)

    l = len(gs.car_paths)
    for car_path in gs.car_paths[l//2:]:
        t = 0
        for c in car_path:
            street = gs.streets[c]
            intersection_times[street.end][c] += 1 - (min(t+val2, gs.D) / gs.D)
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
            v[_v] = min(gs.D, np.ceil(v[_v]).astype("int"))
        output[k] = list(v.items())

    return output, gs.street_names


for pid in range(6):
    save(pid, *solve(pid))
