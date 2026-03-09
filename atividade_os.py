import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando:",e)

def exibir_data():
    executar_comando("date /t")

def exibir_hora():
    executar_comando("time /t")

def exibir_arquivos():
    executar_comando("dir")

def endereço_mac_da_placa_de_rede():
    executar_comando("getmac")

def copiar_item():
    executar_comando("cp")

def limpar_tela_do_prompt():
    executar_comando("cls")

def remover_item():
    executar_comando("rmdir")

def criar_pasta():
    executar_comando("mkdir")

def processos_em_execução():
    executar_comando("tasklist")

def nome_do_computador():
    executar_comando("hostname")

def menu():
    while True:
        print("\n============Ferramenta de rede=============")
        print("1 - exibir data")
        print("2 - exibir_hora")
        print("3 - exibir arquivos")
        print("4 - endereço mac da placa de rede")
        print("5 - copiar item")
        print("6 - limpar tela do prompt")
        print("7 - remover item")
        print("8 - criar pasta")
        print("9 - processos em execução")
        print("10 - nome do computador")
        print("0 - SAIR")
        print("=============Criado por Thiago===============")
        opcao = str(input("Escolha: "))

        match opcao:
            case "1":
                exibir_data()
            case "2":
                exibir_hora()
            case "3":
                exibir_arquivos()
            case "4":
                endereço_mac_da_placa_de_rede()
            case "5":
                copiar_item()
            case "6":
                limpar_tela_do_prompt()
            case "7":
                remover_item()
            case "8":
                criar_pasta()
            case "9":
                processos_em_execução()
            case "10":
                nome_do_computador()
            case "0":
                print("Saindo")
                break
            case _:
                print("Eita caba sabido!!!")
if __name__ == "__main__":
    menu()