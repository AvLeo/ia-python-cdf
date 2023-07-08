from logic import *

rojo = Symbol('rojo')
azul = Symbol('azul')
verde = Symbol('verde')
tribus = [rojo, azul, verde]

persona_uno = Symbol('Persona1')
persona_dos = Symbol('Persona2')
persona_tres = Symbol('Persona3')
personas = [persona_uno,persona_dos,persona_tres]

symbols = []
knowledge = And()

for persona in personas:
    for tribu in tribus:
        symbols.append(f'{persona}{tribu}')

for persona in personas:
    knowledge.add(Or(
        Symbol(f'{persona}rojo'),
        Symbol(f'{persona}azul'),
        Symbol(f'{persona}verde')
    ))
    
# solo una tribu por persona
for persona in personas:
    for h1 in tribus:
        for h2 in tribus:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{persona}{h1}"), Not(Symbol(f"{persona}{h2}")))
                )

# solo una persona por tribu
for tribu in tribus:
    for p1 in personas:
        for p2 in personas:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{tribu}"), Not(Symbol(f"{p2}{tribu}")))
                )

    

knowledge.add(Not(Symbol('Persona3rojo')))
knowledge.add(Or(
    Symbol('Per')
))
print(knowledge)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)