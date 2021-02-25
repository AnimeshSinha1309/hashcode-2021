from utils import load, save

from state import GameState, Solver

pid = 0
state = load(pid)
solver = Solver(state)
solution = solver.weighted_solver()
save(pid, solution, solver.state.street_names)
