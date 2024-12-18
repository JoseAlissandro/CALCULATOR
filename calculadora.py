import flet as ft
import os

# Pega o nome e o caminho da pasta
nome_da_pasta = 'pasta_calculadora'
arquivo = os.path.join(os.getcwd(), nome_da_pasta)
caminho = str(arquivo)

if not os.path.exists(arquivo): 
    try: # Criar a pasta 
        os.makedirs(arquivo, exist_ok=True) 
        print(f"Pasta '{nome_da_pasta}' criada com sucesso em {arquivo}") 
    except Exception as e: 
        print(f"Erro ao criar a pasta: {e}") 
else: 
    print(f"A pasta '{nome_da_pasta}' já existe em {arquivo}")

def TUDO(page: ft.Page):
    # Função para atualizar a tela de exibição
    def update_display(value):
        display.value = value
        page.update()


    # Função que trata os cliques nos botões
    def button_click(e):
        current_text = display.value
        button_text = e.control.text

        if button_text == "=":
            try:
                result = str(eval(current_text))
                update_display(result)
            except Exception as ex:
                update_display("Erro")
        elif button_text == "C":
            update_display("")
        elif button_text == "M":
            with open(caminho+"/ARQUIVO_M.txt", "w") as arquivo:
                arquivo.write(f"{current_text}\n")
                update_display("")
        elif button_text == "+M":
            with open(caminho+"/ARQUIVO_M.txt", "r") as arquivo:
                conteudo = arquivo.read()
                if conteudo != "":
                    update_display(current_text + f'+{conteudo}')
        elif button_text == "-M":
            with open(caminho+"/ARQUIVO_M.txt", "r") as arquivo:
                conteudo = arquivo.read()
                if conteudo != "":
                    update_display(current_text + f'-{conteudo}')
        else:
            update_display(current_text + button_text)

    # Criando a tela de exibição
    display = ft.TextField(value="", read_only=True, width=400, height=100, text_size=24)

    # Criando os botões da calculadora
    botoes = [
        ["7", "8", "9", "/", "C", "("],
        ["4", "5", "6", "*", "M", ")"],
        ["1", "2", "3", "-", "+M", ""],
        ["0", ".", "", "+", "-M", "="]
    ]

    linhas = []
    for linha in botoes:
        botoes_linha = []
        for texto in linha:
            if texto == "":
                botoes_linha.append(ft.Container(width=60, height=60))
            else:
                botoes_linha.append(
                    ft.ElevatedButton(texto, width=60, height=60, on_click=button_click)
                )
        linhas.append(ft.Row(controls=botoes_linha, spacing=5))

    # Adicionamos a tela de exibição e as linhas de botões na página
    page.add(display)
    for r in linhas:
        page.add(r)

# Executamos a aplicação Flet
ft.app(target=TUDO)
