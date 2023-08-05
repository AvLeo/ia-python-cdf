from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

redes_bayes = BayesianNetwork([('Lluvia','Mantenimiento'),('Lluvia','Tren'),('Mantenimiento','Tren'),('Tren','Reunion')])

dominio_lluvia = ['nula', 'ligera', 'fuerte']

lluvia = TabularCPD(variable='Lluvia',
                    variable_card=len(dominio_lluvia),
                    values=[[0.7],[0.2],[0.1]],
                    state_names={'Lluvia': dominio_lluvia})

print(lluvia)

dominio_mantenimiento = ['no', 'si']

mantenimiento = TabularCPD(variable='Mantenimiento',
                           variable_card=len(dominio_mantenimiento),
                           values=[[0.6,0.8,0.9],[0.4,0.2,0.1]],
                           evidence=['Lluvia'],
                           evidence_card=[3],
                           state_names={'Mantenimiento': dominio_mantenimiento,
                                        'Lluvia': dominio_lluvia}
                           )

print(mantenimiento)