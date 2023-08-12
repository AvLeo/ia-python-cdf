from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination

red_bayes = BayesianNetwork([('Lluvia','Mantenimiento'),('Lluvia','Tren'),('Mantenimiento','Tren'),('Tren','Reunion')])

dominio_lluvia = ['nula', 'ligera', 'fuerte']

lluvia_cpd = TabularCPD(variable='Lluvia',
                    variable_card=len(dominio_lluvia),
                    values=[[0.7],[0.2],[0.1]],
                    state_names={'Lluvia': dominio_lluvia})


dominio_mantenimiento = ['no', 'si']

mantenimiento_cpd = TabularCPD(variable='Mantenimiento',
                           variable_card=len(dominio_mantenimiento),
                           values=[[0.6,0.8,0.9],[0.4,0.2,0.1]],
                           evidence=['Lluvia'],
                           evidence_card=[3],
                           state_names={'Mantenimiento': dominio_mantenimiento,
                                        'Lluvia': dominio_lluvia}
                           )


dominio_tren = ['a tiempo', 'demorado']
distribucion_tren = {
    'a tiempo' : [0.9,0.8,0.7,0.6,0.5,0.4],
    'demorado' : [0.1,0.2,0.3,0.4,0.5,0.6]
}

tren_cpd = TabularCPD(variable='Tren',
                      variable_card=len(dominio_tren),
                      values=[distribucion_tren[key] for key in distribucion_tren],
                      evidence=['Lluvia', 'Mantenimiento'],
                      evidence_card= [3,2],
                      state_names={
                          'Tren': dominio_tren,
                          'Mantenimiento': dominio_mantenimiento,
                          'Lluvia': dominio_lluvia
                      }
                      )

# print(tren_cpd)

# dominio_reunion = ['asistir', 'no asistir']
distribucion_reunion = {
    'asistir': [0.9,0.6],
    'no asistir': [0.1,0.4]   
}

reunion_cpd = TabularCPD(
    variable='Reunion',
    variable_card=len(distribucion_reunion.keys()),
    values=[distribucion_reunion[key] for key in distribucion_reunion],
    evidence=['Tren'],
    evidence_card=[len(distribucion_tren.keys())],
    state_names={
        'Reunion': list(distribucion_reunion.keys()),
        'Tren': list(distribucion_tren.keys())
    }
)

# print(reunion_cpd)

red_bayes.add_cpds(lluvia_cpd, mantenimiento_cpd, tren_cpd, reunion_cpd)

inferencia = VariableElimination(red_bayes)

consulta_1 = inferencia.query(
    variables=['Reunion'],
    evidence={
        'Lluvia': 'ligera',
        'Mantenimiento': 'no'
    }
)
consulta_2 = inferencia.query(
    variables=['Lluvia'],
    evidence={
        'Reunion': 'asistir',
        'Mantenimiento': 'si'
    }
)
consulta_3 = inferencia.query(
    variables=['Lluvia', 'Mantenimiento'],
    evidence={
        'Reunion': 'no asistir'
    }
)
consulta_4 = inferencia.query(
    variables=['Lluvia', 'Mantenimiento', 'Tren'],
    evidence={
        'Reunion': 'asistir'
    }
)

print('Consulta 1 \n' , consulta_1)
print('Consulta 2 \n' , consulta_2)
print('Consulta 3 \n' , consulta_3)
print('Consulta 4 \n' , consulta_4)