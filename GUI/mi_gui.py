import PySimpleGUI as sg
sg.theme('DarkGreen4')
home = [
    [sg.Text('Menu principal', font='Symbol 55')],
    [sg.Button('Click me',key='BOTON_1'),sg.Button('Click me 2',key='BOTON_2')],
    [sg.Combo(['nula', 'ligera', 'fuerte'], default_value ='nula', key = 'lluvia')],
    [sg.Output(size=(60,5))],
    [sg.Radio('Selector 1','1',default=False),sg.Radio('Selector 3','1',default=False),sg.Radio('Selector 2','1',default=False)]
]

ventana = sg.Window(title='Mi programa', layout=home)

while True:
    events, values = ventana.read();
    if events == sg.WIN_CLOSED:
        break
    if events == 'BOTON_1':
        sg.popup('me hiciste un click y soy el boton 1',title='Error')
    if events == 'BOTON_2':
        print('hola')