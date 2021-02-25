from utils import load, save, bounds_on_scores

from state import Solver

for pid in range(6):
    state = load(pid)
    print("State", pid)
    bounds_on_scores(state)
