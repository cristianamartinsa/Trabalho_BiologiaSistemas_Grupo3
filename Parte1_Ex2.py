# Importação do modelo usando COBRApy
from cobra.io import read_sbml_model
model = read_sbml_model('iML1515.xml')

# Simulação
from mewpy.simulation import get_simulator
simul = get_simulator(model)

# Condições ambientais
envcond = {'EX_glc__D_e': (-15, 999999.0), 'EX_o2_e': (0, 999999.0)}
simul = get_simulator(model, envcond = envcond)

###### Capacidade de produção máxima de malato ######
simul.objective = 'EX_mal__L_e'
simul.objective

result_b = simul.simulate(method = 'FBA')
result_b

result_b.fluxes['EX_mal__L_e']

%matplotlib inline
from mewpy.visualization.envelope import plot_flux_envelope

plot_flux_envelope(simul,'EX_mal__L_e','BIOMASS_Ec_iML1515_core_75p37M')

# Com produção mínima de biomassa
min_biomassa = result_a2.fluxes['BIOMASS_Ec_iML1515_core_75p37M']*0.1
min_biomassa

envcond2 = {'EX_glc__D_e': (-15.0, 100000.0), 'EX_o2_e':(0,0), 'BIOMASS_Ec_iML1515_core_75p37M': (min_biomassa, 10000)}

simul_env2 = get_simulator(model,envcond=envcond2)

result_b_env2 = simul_env2.simulate(method = 'FBA')
result_b_env2

%matplotlib inline
from mewpy.visualization.envelope import plot_flux_envelope

plot_flux_envelope(simul_env2,'EX_mal__L_e','BIOMASS_Ec_iML1515_core_75p37M')