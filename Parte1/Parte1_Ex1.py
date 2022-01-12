# Importação do modelo usando COBRApy
from cobra.io import read_sbml_model
model = read_sbml_model('iML1515.xml')

# Simulação
from mewpy.simulation import get_simulator
simul = get_simulator(model)

# Condições ambientais
envcond = {'EX_glc__D_e': (-15, 999999.0), 'EX_o2_e': (0, 999999.0)}
simul = get_simulator(model, envcond = envcond)


####### Produção wild type de malato ####### 

# Para biomass = 'BIOMASS_Ec_iML1515_WT_75p37M'
simul.objective = 'BIOMASS_Ec_iML1515_WT_75p37M'
simul.objective

result_a1 = simul.simulate(method = 'FBA')
result_a1

result_a1.fluxes['EX_mal__L_e']

%matplotlib inline
from mewpy.visualization.envelope import plot_flux_envelope

plot_flux_envelope(simul,'BIOMASS_Ec_iML1515_WT_75p37M','EX_mal__L_e')



# Para biomass = 'BIOMASS_Ec_iML1515_core_75p37M'

simul.objective = 'BIOMASS_Ec_iML1515_core_75p37M'
simul.objective

result_a2 = simul.simulate(method='FBA')
result_a2

result_a2.fluxes['EX_mal__L_e']
result_a2.fluxes['BIOMASS_Ec_iML1515_core_75p37M']

%matplotlib inline
from mewpy.visualization.envelope import plot_flux_envelope

plot_flux_envelope(simul,'BIOMASS_Ec_iML1515_core_75p37M','EX_mal__L_e')