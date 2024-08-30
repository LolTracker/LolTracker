import openai
openai.api_key = "API-key-openai"

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
tipopartida = input("Bem vindo ao...\n
  _           _ _______             _             
 | |         | |__   __|           | |            
 | |     ___ | |  | |_ __ __ _  ___| | _____ _ __ 
 | |    / _ \| |  | | '__/ _` |/ __| |/ / _ \ '__|
 | |___| (_) | |  | | | | (_| | (__|   <  __/ |   
 |______\___/|_|  |_|_|  \__,_|\___|_|\_\___|_|   
                                                  
                                                    \nOnde ninguém aposta no escuro.\n Escolha uma opção:\n1. Melhor de 3\n 2. Melhor de 5\n3.  Partida unica ")
                                                    
if (tipopartida = 1){
  md = ("melhor de 3")
}
if (tipopartida = 2){
  md = ("melhor de 5")
}
if (tipopartida = 3){
  md = ("partida única")
}

timex = input("Digite o primeiro time: ")
timey = input("Digite o segundo time: ")
resposta = prompt(pergunta)
print(resposta)

input() 
