import PySimpleGUI as sg

sg.theme('reddit')

janela_inicial = [
    [sg.Text('E-mail'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher Pasta dos Anexos', target='input_anexos'), sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher Pasta da Planilha', target='input_planilha'), sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]
]

aplicativo =sg.Window('Principal', layout = janela_inicial)

while True:
    event, values = aplicativo.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values ['email']
        senha = values ['senha']
        caminho_pasta_anexos = values ['input_anexos']
        caminho_pasta_planilha = values ['input_planilha']

#Aplicação de interface grafica criada para fins de estudos utilizando a biblioteca PySimpleGUI em linguagem Python
