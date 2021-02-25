from utils import load, save

from state import Solver

pid = 4
state = load(pid)
solver = Solver(state)
solution = solver.weighted_solver()
save(pid, solution, solver.state.street_names)
