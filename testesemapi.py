# Code by LolTracker devCrew

import openai
import pyfiglet
from termcolor import colored

openai.api_key = "asdasdasd"

def calcular_probabilidade(timex, timey, md):
    # Simulação de resposta sem chamar a API
    return f"Simulação: A probabilidade do time {timex} vencer contra {timey} em um formato {md} é de 50%."

# Tela inicial com as opções
def display_LolTracker():
    Lol_ascii_art = pyfiglet.figlet_format("Lol", font="bell")
    Tracker_ascii_art = pyfiglet.figlet_format("Tracker", font="bell")
    red_colored = colored(Lol_ascii_art, 'red')
    combined_art = ""
    for Lol_line, Tracker_line in zip(red_colored.split('\n'), Tracker_ascii_art.split('\n')):
        combined_art += Lol_line + " " + Tracker_line + "\n"
    print(combined_art)

display_LolTracker()

tipopartida = input("Bem-vindo ao LolTracker!\nOnde ninguém aposta no escuro...\nEscolha uma opção:\n1. Melhor de 3\n2. Melhor de 5\n3. Partida única\n ")

# Converter o input para inteiro
if tipopartida == "1":
    md = "melhor de 3"
elif tipopartida == "2":
    md = "melhor de 5"
elif tipopartida == "3":
    md = "partida única"
else:
    print("Opção inválida.")
    exit()

timex = input("Digite o nome do primeiro time: ")
timey = input("Digite o nome do segundo time: ")

# Chamar a função para calcular a probabilidade
resposta = calcular_probabilidade(timex, timey, md)
print("Resultado: ", resposta)

input("Pressione Enter para sair...")
