from utils import load, save, bounds_on_scores, problem_names

from state import Solver

for pid in problem_names:
    state = load(pid)
    solver = Solver(state)
    solution = solver.dumdumsolver()
    save(pid, solution, solver.state.street_names)
