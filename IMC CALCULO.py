import PySimpleGUI as sg

sg.theme('DarkRed')

layout = [ 
            [sg.Text('Índice de massa corpórea')],
            [sg.Push(), sg.Text('Massa:'), sg.Input(key='-MASS-', size=(5,1)), sg.Push()],
            [sg.Push(), sg.Text('Altura:'), sg.Input(key='-HIGH-', size=(5,1)), sg.Push()],
            [sg.Push(), sg.Button('Calcular'), sg.Push()]
         ]

window = sg.Window('IMC', layout, font='playfair 20')
while True:
    event, value = window.read() 
    print(event, value)
    Massa=float(value['-MASS-'])
    Altura=float(value['-HIGH-'])
    imc= Massa / (Altura**2)
    sg.Popup(f'Seu IMC: {imc:.2f}',font= 'fixed 24')
    if event == sg.WIN_CLOSED or event == 'Exit': 
      break
