import random
import math
import random

def gerar_problema():
    tipos_problema = ['movimento_uniforme', 'movimento_variado', 'lancamento_projeteis']
    tipo = random.choice(tipos_problema)
    if tipo == 'movimento_uniforme':
        velocidade = random.uniform(5, 20)
        tempo = random.uniform(1, 10)
        distancia = velocidade * tempo
        problema = f"Um objeto se move com velocidade constante de {velocidade:.2f} m/s por {tempo:.2f} segundos. Qual a distância percorrida?"
        resposta = distancia
    elif tipo == 'movimento_variado':
        aceleracao = random.uniform(1, 5)
        tempo = random.uniform(1, 10)
        velocidade_inicial = random.uniform(0, 10)
        distancia = velocidade_inicial * tempo + 0.5 * aceleracao * tempo ** 2
        problema = f"Um objeto parte com velocidade inicial de {velocidade_inicial:.2f} m/s e acelera a {aceleracao:.2f} m/s² por {tempo:.2f} segundos. Qual a distância percorrida?"
        resposta = distancia
    elif tipo == 'lancamento_projeteis':
        velocidade_inicial = random.uniform(10, 30)
        angulo = random.uniform(20, 70)
        g = 9.8
        alcance = (velocidade_inicial ** 2) * (math.sin(2 * math.radians(angulo))) / g
        problema = f"Um projétil é lançado com velocidade inicial de {velocidade_inicial:.2f} m/s a um ângulo de {angulo:.2f}°. Qual o alcance horizontal? (g = 9.8 m/s²)"
        resposta = alcance
    else:
        problema = "Problema não definido."
        resposta = 0
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
