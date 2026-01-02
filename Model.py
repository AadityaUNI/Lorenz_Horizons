from scipy.integrate import solve_ivp
import numpy as np


class LorenzModel:
    T = 75
    N = 1000
    
    def __init__(self, constants, initial, behavior):
        self.constants = constants
        self.initial = initial
        self.behavior = behavior
        self.solveModel()

    def solveModel(self):
        t_eval = np.linspace(0, self.T, self.N)
        self.solution = solve_ivp(self.modelEquation, (0, self.T), self.initial, args=self.constants, t_eval=t_eval)    

    @staticmethod
    def modelEquation(t, vars, sigma, beta, rho):
        x = vars[0]
        y = vars[1]
        z = vars[2]

        dxdt = sigma*(y - x)
        dydt = x*(rho - z) - y
        dzdt = x*y - beta*z

        return [dxdt, dydt, dzdt]
