class GameState:
    def __init__(self, streets, street_names, street_name_to_idx, car_paths, ic, f, d):
        # list of tuples (inter_start, inter_end, length)
        self.streets = streets
        # list of street names
        self.street_names = street_names
        # dictionary mapping
        self.street_name_to_idx = street_name_to_idx

        self.intersection_count = ic

        # list of lists where i-th list is indices of streets the i-th car goes for
        self.car_paths = car_paths

        self.F = f
        self.D = d
