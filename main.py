# Code by LolTracker devCrew

import openai
import pyfiglet
from termcolor import colored

openai.api_key = "chave-api-aqui"

def calcular_probabilidade(timex, timey, md):
    # função que faz o prompt para perguntar ao GPT
    pergunta = f"Por favor, faça o cálculo de probabilidade de qual time de lol irá ganhar a partida. Os times são {timex} e {timey}, o formato será {md}."
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista em cálculos de probabilidade de jogos."},
            {"role": "user", "content": pergunta}
        ],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].message['content'].strip()
    return message

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
