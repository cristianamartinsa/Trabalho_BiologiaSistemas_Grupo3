import cobra
import pandas
from cobra.flux_analysis import single_gene_deletion

# Importação do modelo
model = cobra.io.read_sbml_model('iML1515.xml')

# Condições ambientais
model.reactions.get_by_id("EX_o2_e").upper_bound = 1000
model.reactions.get_by_id("EX_o2_e").lower_bound = 0
model.reactions.get_by_id("EX_glc__D_e").upper_bound = 1000
model.reactions.get_by_id("EX_glc__D_e").lower_bound = -15

# Otimização
print(model.optimize())


# Função objetivo: maximização da biomassa e malato
model.objective = 'BIOMASS_Ec_iML1515_core_75p37M' 
model.objective = 'EX_mal__L_e'

model.reactions.get_by_id('BIOMASS_Ec_iML1515_core_75p37M').lower_bound = 0.266 
model.reactions.get_by_id('BIOMASS_Ec_iML1515_core_75p37M').upper_bound = 1000

pandas.set_option('display.max_rows', 2000)


# Deleções
delecao = single_gene_deletion(model)
print(deletion_results.sort_values(by = ['growth'], ascending = False))