import pygame
import sys

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("ENERGIA CINÉTICA")

Borgonha = (128, 0, 32)
Âmbar = (255, 191, 0)

fonte = pygame.font.Font(None, 32)

def calcular_energia_cinetica(massa, velocidade):
    energia_cinetica = 0.5 * massa * velocidade ** 2
    return energia_cinetica

def main():
    objeto = "selecione um objeto"
    massa = 0
    velocidade = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill(Borgonha)

        texto_objeto = fonte.render(objeto, True, Âmbar)
        tela.blit(texto_objeto, (50, 50))
        
        texto_massa = fonte.render(f"Massa: {massa} kg", True, Âmbar)
        tela.blit(texto_massa, (50, 100))
        
        texto_velocidade = fonte.render(f"Velocidade: {velocidade} m\s", True, Âmbar)
        tela.blit(texto_velocidade, (50, 150))
        
        if objeto != "Selecione um objeto":
            energia = calcular_energia_cinetica(massa, velocidade)
            texto_energia = fonte.render(f"Energia Cinética: {energia:.2f} Joules", True, Âmbar)
            tela.blit(texto_energia, (50, 200))
        
        pygame.display.update()

if __name__ == "__main__": 
  main()
