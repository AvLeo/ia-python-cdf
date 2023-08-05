from logic import *

## TRIBUS 
# Hay tres tribus, VERDES, ROJOS y AZULES:

# VERDES siempre dicen la verdad
# ROJOS siempre mienten
# AZUL dicen la verdad y después mienten o viceversa

# El explorador se encuentra a 3 indios de diferentes tribus, y ellos le dicen:

# Primera persona: Yo soy verde
# Segunda persona: El primero es azul
# Tercera persona: Yo soy rojo

persona_uno_verde = Symbol('Primero Es Verde')
persona_uno_rojo = Symbol('Primero Es Rojo')
persona_uno_azul = Symbol('Primero Es Azul')
persona_dos_verde = Symbol('Primero Es Verde')
persona_dos_rojo = Symbol('Primero Es Rojo')
persona_dos_azul = Symbol('Primero Es Azul')
persona_tres_verde = Symbol('Primero Es Verde')
persona_tres_rojo = Symbol('Primero Es Rojo')
persona_tres_azul = Symbol('Primero Es Azul');

simbols = [persona_uno_verde,persona_uno_rojo,persona_uno_azul,persona_dos_verde,persona_dos_rojo,persona_dos_azul,persona_tres_verde,persona_tres_rojo,persona_tres_azul]

def solution(_escenario, _personajes):
    for personajes in _personajes:
        if model_check(_escenario, personajes):
            print(personajes)

escenario = And(
    Or(persona_uno_verde, persona_uno_azul, persona_uno_rojo),
    Not(And(persona_uno_azul, persona_uno_rojo, persona_uno_verde)),
    Or(persona_dos_verde, persona_dos_azul, persona_dos_rojo),
    Not(And(persona_dos_azul, persona_dos_rojo, persona_dos_verde)),
    Or(persona_tres_verde, persona_tres_azul, persona_tres_rojo),
    Not(And(persona_tres_azul, persona_tres_rojo, persona_tres_verde)),
    
    Implication(persona_uno_verde,)
)