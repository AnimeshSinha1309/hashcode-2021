import numpy as np

from collections import namedtuple

Street = namedtuple("Street", "start end l")


class GameState:
    def __init__(self, streets, street_names, street_name_to_idx, car_paths, ic, f, d):
        # list of tuples (inter_start, inter_end, length)
        self.streets = [Street(x, y, z) for x, y, z in streets]
        # list of street names
        self.street_names = street_names
        # dictionary mapping
        self.street_name_to_idx = street_name_to_idx

        self.street_count = len(street_names)

        self.intersection_count = ic

        self.intersection_mapping = {}
        for i in range(self.intersection_count):
            self.intersection_mapping[i] = []

        for idx, street in enumerate(self.streets):
            self.intersection_count[street.start].append(idx)
            self.intersection_count[street.end].append(idx)

        # list of lists where i-th list is indices of streets the i-th car goes for
        self.car_paths = car_paths

        self.F = f
        self.D = d

    def calculate_average_inflow(self):
        street_averages = np.zeros(self.street_count)

        for path in self.car_paths:
            for s_idx in path:
                street_averages[s_idx] += 1

        return street_averages


class Solver:
    def __init__(self, state: GameState):
        self.state = state

    def weighted_solver(self):
        avg_flow = self.state.calculate_average_inflow()

        for intersection, streets in self.state.intersection_mapping.items():
            weights = np.array([avg_flow[x] for x in streets])
            weights = weights / np.sum(weights)
            schedule = np.round(weights)

        # TODO
