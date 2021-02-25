from typing import Dict

from hashcode.state import GameState

problem_names = ["a", "b", "c", "d", "e", "f"]


def bounds_on_scores(gs: GameState):
    upper_bound_score = 0

    for path in gs.car_paths:
        time = 0
        for street in path[1:]:
            time += gs.streets[street].l
        upper_bound_score += max(0, (gs.D - time) + gs.F)

    print("Upper bound on score", upper_bound_score)


def load(pid):
    if type(pid) == str:
        file_path = f"problem/{pid}.txt"
    else:
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
            streets.append([start, end, l])
            street_name_to_idx[name] = idx

        for line in car_content:
            car_streets = line.split(" ")[1:]
            car_streets_idx = [street_name_to_idx[x] for x in car_streets]
            car_paths.append(car_streets_idx)

    return GameState(streets, street_names, street_name_to_idx, car_paths, i, f, d)


# solution = dictionary of lists
# dictionary key is the intersection
# the list has size number of streets for the i-th intersection
# list[j] denotes time for which j-th street light remains on at i-th intersection
# solution must contain integers (or floats with integer values)
def save(pid, solution: Dict, street_names):
    open_count = 0
    write_solution = []

    # validates against all 0 streets
    for intersection, times in solution.items():
        write_list = []
        for s_i, time in times:
            if time > 0:
                write_list.append([s_i, time])
        if not write_list:
            continue
        open_count += 1
        write_solution.append([intersection, write_list])

    namesave = pid if type(pid) == str else chr(pid + 97)
    with open(f"solution/{namesave}", "w") as f:
        f.write(f"{open_count}\n")

        for idx, write_list in write_solution:
            f.write(f"{idx}\n")
            f.write(f"{len(write_list)}\n")
            for s_idx, time in write_list:
                f.write(f"{street_names[s_idx]} {int(time)}\n")


def score(pid, solution):
    pass
