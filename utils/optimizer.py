from deap import base, creator, tools, algorithms
import numpy as np

def eval_portfolio(individual, returns, penalties):
    total = sum(individual)
    if abs(total - 1.0) > 0.05:
        return -1000.0,
    score = sum(i * r - i * p for i, r, p in zip(individual, returns, penalties))
    return score,

def optimize_portfolio(returns, penalties, asset_names):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", np.random.rand)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, len(asset_names))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", lambda ind: eval_portfolio(ind, returns, penalties))
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)

    pop = toolbox.population(n=100)
    algorithms.eaSimple(pop, toolbox, 0.5, 0.2, 50, verbose=False)
    best = tools.selBest(pop, 1)[0]
    best = np.maximum(best, 0)
    total = sum(best)
    weights = np.round(best / total, 2)
    return {name: f"{int(w * 100)}%" for name, w in zip(asset_names, weights)}
