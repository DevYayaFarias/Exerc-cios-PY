import random

def gerar_problema():
    tipos_problema = ['movimento_uniforme', 'movimento_variado', 'lancamento_projeteis']
    tipo = random.choice(tipos_problema)
    
    if tipo == 'movimento_uniforme':
        velocidade = random.uniform(5, 20)
        tempo = random.uniform(1, 10)
        distancia = velocidade * tempo
        problema = f"Um objeto se move com velocidade constante de {velocidade} m/s por {tempo} segundos. Qual a distância percorrida?"
        resposta = distancia
    return problema, resposta

def apresentar_problema(problema):
    print(problema)
    jogador_resposta = float(input("Sua reposta: "))
    return jogador_resposta
  
    
def verificar_resposta(jogador_resposta, resposta_correta):
    if abs (jogador_resposta - resposta_correta) < 0.01:
        
        return True
    else:
        return False
  
def jogo():
    pontuacao = 0
    for _ in range(5):
        problema, resposta_correta = gerar_problema()
        resposta_jogador = apresentar_problema(problema)
        if verificar_resposta(resposta_jogador, resposta_correta):
            print("RESPOSTA CORRETA! +10 pontos\n")
            pontuacao += 10
        else:
            print(f"RESPOSTA INCORRETA. A resposta correta era:{resposta_correta}\n")
    
    print(f"FIM DE JOGO. Sua pontuacao total é: {pontuacao}")
    
jogo()
