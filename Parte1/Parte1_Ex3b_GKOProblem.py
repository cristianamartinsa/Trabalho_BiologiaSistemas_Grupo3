# Importação do modelo usando COBRApy
from cobra.io import read_sbml_model
model = read_sbml_model('iML1515.xml')

# Condições ambientais
envcond = {'EX_glc__D_e': (-15, 999999.0), 'EX_o2_e': (0, 999999.0)}

# GKO Problem
from mewpy.optimization.evaluation import BPCY, WYIELD
from mewpy.problems import GKOProblem
from mewpy.optimization import EA
from mewpy.simulation import SimulationMethod

PRODUCT_ID = 'EX_mal__L_e_'
BIOMASS_ID = 'BIOMASS_Ec_iML1515_core_75p37M'
GLUC_ID = 'EX_glc_e_'

model.objective = 'BIOMASS_Ec_iML1515_core_75p37M'

evaluator_1 = BPCY(BIOMASS_ID, PRODUCT_ID, method = SimulationMethod.lMOMA)
evaluator_2 = WYIELD(BIOMASS_ID, PRODUCT_ID)

problem = GKOProblem(model, fevaluation=[evaluator_1, evaluator_2], envcond = envcond, candidate_max_size = 1)

ea = EA(problem, max_generations = 5, visualizer = True, mp = True)

final_pop = ea.run()
print(final_pop)