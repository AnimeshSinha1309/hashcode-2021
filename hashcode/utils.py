from hashcode.state import GameState

problem_names = ["a", "b", "c", "d", "e", "f"]


def load(pid):
    file_path = f"problem/{problem_names[pid]}.txt"

    with open(file_path) as f:
        content = f.read().split("\n")
        d, i, s, c, f = list(map(int, content[0].split(" ")))

        streets = []
        street_names = []
        street_name_to_idx = {}
        car_paths = []

        street_content = content[1 : s + 1]
        car_content = content[s + 1 : s + c + 1]

        for idx, line in enumerate(street_content):
            vals = line.split(" ")
            start, end, name, l = int(vals[0]), int(vals[1]), vals[2], int(vals[3])
            street_names.append(name)
            streets.append((start, end, l))
            street_name_to_idx[name] = idx

        for line in car_content:
            car_streets = line.split(" ")[1:]
            car_streets_idx = [street_name_to_idx[x] for x in car_streets]
            car_paths.append(car_streets_idx)

    return GameState(streets, street_names, street_name_to_idx, car_paths, i, f, d)


def save(pid, solution):
    pass


def score(pid, solution):
    pass
