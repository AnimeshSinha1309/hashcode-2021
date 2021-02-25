import numpy as np

from collections import namedtuple, defaultdict

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

        self.start_intersection_mapping = defaultdict(list)
        self.end_intersection_mapping = defaultdict(list)

        for idx, street in enumerate(self.streets):
            self.start_intersection_mapping[street.start].append(idx)
            self.end_intersection_mapping[street.end].append(idx)

        # list of lists where i-th list is indices of streets the i-th car goes for
        self.car_paths = car_paths

        self.F = f
        self.D = d

    def calculate_average_inflow(self):
        street_averages = np.zeros(self.street_count)

        for path in self.car_paths:
            for s_idx in path[1:]:
                street_averages[s_idx] += 1

        return street_averages


class Solver:
    def __init__(self, state: GameState):
        self.state = state

    def weighted_solver(self):
        avg_flow = self.state.calculate_average_inflow()
        schedules = {}

        for intersection, streets in self.state.end_intersection_mapping.items():
            weights = np.array([avg_flow[x] for x in streets])
            if np.sum(weights) == 0:
                continue

            weights = np.round(weights / np.sum(weights))

            if np.sum(weights) == 0:
                continue

            schedule = [[x, weights[s_i]] for s_i, x in enumerate(streets)]
            schedules[intersection] = schedule

        return schedules
