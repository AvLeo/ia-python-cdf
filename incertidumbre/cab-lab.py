from logic import *

#En una isla remota, hay dos tipos de habitantes: caballeros (knights) y ladrones (knaves). Los caballeros siempre dicen la verdad, mientras que los ladrones siempre mienten.

#Un día, te encuentras con tres habitantes de la isla, A y B (y C), pero no sabes quién es quién. Quieres averiguar qué tipo de habitante es cada uno de ellos:

ACaballero=Symbol("A es Caballero")
ALadron=Symbol("A es Ladrón")
BCaballero=Symbol("B es Caballero")
BLadron=Symbol("B es Ladrón")
CCaballero=Symbol("C es Caballero")
CLadron=Symbol("C es Ladrón")


ListaPersonajes=[ACaballero,ALadron,BCaballero,BLadron,CCaballero,CLadron]


def solution(_escenario, _personajes):
    for personajes in _personajes:
        if model_check(_escenario, personajes):
            print(personajes)    
# Primer escenario:

# **A dice: “Soy un caballero y un ladrón”**


escenario_1 = And(
    Or(ACaballero, ALadron),
    Not(And(ACaballero, ALadron)),
    
    Implication(ACaballero, And(ACaballero, ALadron)),
    Implication(ALadron, Not(And(ACaballero,ALadron)))
)

print('-----------------\nEscenario 1')
solution(escenario_1, ListaPersonajes)
# ---------------------------------------------------------------------------------------------------------

# Segundo escenario:

# **A dice: “Ambos somos ladrones”**

# **B no dice nada**







# ------------------------------------------------------------------------------------------------------------

# Tercer escenario:

# **A dice: “Somos del mismo tipo”**

# **B dice: “Somos de distintos tipos”**

# escenario_3 = And(
#     Or(ACaballero,ALadron),
#     Not(And(ACaballero,ALadron)),
#     Or(BCaballero, BLadron),
#     Not(And(BCaballero, BLadron))
   
#     Implication(ACaballero, )
# )

# ------------------------------------------------------------------------------------------------------------

# Cuarto escenario:

# **A dice: “Soy un caballero” o “Soy un ladrón” (pero no sabemos cuál frase dijo)**

# **B dice: “A dijo ‘Soy un ladrón’”**

# **B luego dice: “C es un ladrón”**

# **C dice “A es un caballero”**

escenario_4 = And(
      Or (ACaballero ,ALadron),
      Not (And (ACaballero,ALadron)),
      Or(BCaballero,BLadron),
      Not(And(BCaballero, BLadron)),
      Or(CCaballero, CLadron),
      Not(And (CCaballero,CLadron)),
      
      Implication(ALadron,And(BCaballero,CLadron)),
      Implication(BCaballero,And(ALadron,CCaballero)),
      Implication(CCaballero,Not(And(ALadron,BCaballero))),
      Implication(CLadron,Not(And(ACaballero,BLadron)))
)

print('-------------------\nEscenario 4:')
solution(escenario_4, ListaPersonajes)
