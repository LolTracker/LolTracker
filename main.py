import openai
import pyfiglet
from termcolor import colored

openai.api_key = "API-key-openai"

display_LolTracker()

def prompt(pergunta): # função que faz o prompt para perguntar ao GPT
    model_engine = "text-davinci-002"
    # modelo GPT-3 que será utilizado, davinci é o mais confiável    
    prompt = f"Por favor, faça o cálculo de probabilidade de qual time de lol irá ganhar a partida. Os times são {timex} e {timey}, o formato será {md} \nResposta: "
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1250,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text.strip()
    return message

# Tela inicial com as opções
# Função para exibir o texto RedMoon em ASCII art
def display_LolTracker():
    Lol_ascii_art = pyfiglet.figlet_format("Lol", font="epic")
    Tracker_ascii_art = pyfiglet.figlet_format("Tracker", font="epic")
    red_colored = colored(Lol_ascii_art, 'red')
    combined_art = ""
    for Lol_line, Tracker_line in zip(Lol_colored.split('\n'), Tracker_ascii_art.split('\n')):
        combined_art += Lol_line + Tracker_line + "\n"
    print(combined_art)

tipopartida = input("Bem vindo ao LolTracker!\nOnde ninguém aposta no escuro...\n Escolha uma opção:\n1. Melhor de 3\n 2. Melhor de 5\n3.  Partida unica ")
                                                    
if (tipopartida = 1){
  md = ("melhor de 3")
}
elif (tipopartida = 2){
  md = ("melhor de 5")
}
elif (tipopartida = 3){
  md = ("partida unica")
}

timex = input("Digite o primeiro time: ")
timey = input("Digite o segundo time: ")
resposta = prompt(pergunta)
print(resposta)

input() 
