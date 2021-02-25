from utils import load, save, bounds_on_scores

from state import Solver

pid = 2
state = load(pid)
solver = Solver(state)
bounds_on_scores(state)
solution = solver.weighted_solver()
save(pid, solution, solver.state.street_names)
