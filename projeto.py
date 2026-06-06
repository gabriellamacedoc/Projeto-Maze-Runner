import pygame
import random
import os

pygame.init()
pygame.font.init()

largura=840
altura=700
screen=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Maze Runner")


NOME_FONTE = "font/PressStart2P-Regular.ttf"
if os.path.exists(NOME_FONTE):
    font = pygame.font.Font(NOME_FONTE, 12)
    font_vida = pygame.font.Font(NOME_FONTE, 15)
    font_dado = pygame.font.Font(NOME_FONTE, 18)
else:
    print(f"Aviso: Arquivo '{NOME_FONTE}' não encontrado. Usando fonte padrão do sistema.")
    font = pygame.font.Font(None, 30)
    font_vida = pygame.font.Font(None, 30)
    font_dado = pygame.font.Font(None, 35)

def desenhar_peao(tela, cor, pos_x, pos_y):
    pygame.draw.circle(tela, (50, 50, 50), (pos_x + 27, pos_y + 27), 15)
    pygame.draw.circle(tela, cor, (pos_x + 25, pos_y + 25), 15)
    pygame.draw.circle(tela, (255, 255, 255), (pos_x + 25, pos_y + 25), 15, 3)

colour = (255, 255, 255)
x='Pressione espaço para jogar'
a=''
b=''

posicoes = {0:  (20, 50),1:  (100, 50),2:  (180, 50),3:  (260, 50),4:  (340, 50),5:  (420, 50),6:  (500, 50),7:  (580, 50),8:  (660, 50),
            9:  (740, 50),10: (740, 130),11: (740, 210),12: (740, 290),13: (740, 370),14: (740, 450),15: (740, 530),16: (660, 530),17: (580, 530),
            18: (500, 530),19: (420, 530),20: (340, 530),21: (260, 530),22: (180, 530),23: (100, 530),24: (20, 530),25: (20, 450),26: (20, 370),27: (20, 290)}
cores_tabuleiro = {0: "INICIO", 1: "BRANCO", 2: "VERMELHO", 3: "VERDE", 4: "BRANCO", 5: "AZUL", 6: "BRANCO", 7: "AMARELO", 8: "BRANCO", 9: "VERMELHO", 
    10: "VERDE", 11: "PRETO", 12: "AZUL", 13: "BRANCO", 14: "BRANCO", 15: "VERMELHO", 16: "VERDE", 17: "BRANCO", 18: "AMARELO", 19: "BRANCO", 
    20: "VERMELHO", 21: "VERDE", 22: "BRANCO", 23: "AZUL", 24: "VERMELHO", 25: "AMARELO", 26: "VERDE", 27: "FIM"}
rgb={"VERMELHO": (225, 0, 0), "VERDE": (0, 225, 0), "PRETO": (0, 0, 0), "AZUL": (0, 0, 225), "AMARELO": (225, 225, 0), "BRANCO": (225, 225, 225), "INICIO": (0,0,0), "FIM": (0,0,0)}

jog1={'vida':10, 'posicao':0, 'pos':posicoes[0], 'cor':'Verde', 'rgb':(0, 255, 170)}
jog2={'vida':10, 'posicao':0, 'pos':posicoes[0], 'cor':'Rosa', 'rgb':(255, 20, 147)}

jogadores_presos=[0,0]
jogadores=[jog1, jog2]
turno=0
y=0

jogo_iniciado=False
fim=False
running=True

while running:
    screen.fill((255,255,255))
    for p, cord in posicoes.items():
        pygame.draw.rect(screen, rgb[cores_tabuleiro[p]], (cord[0], cord[1], 80, 80))

    screen.blit(font.render('Início', True, colour), (20, 55))
    screen.blit(font.render('Fim', True, colour), (22,295))
    screen.blit(font.render(x, True, (0,0,0)), (5,15))
    screen.blit(font_vida.render(a, True, (255,103,0)), (250, 300))
    screen.blit(font_vida.render(b, True, (255,103,0)), (250, 350))

    pygame.draw.rect(screen, (57, 62, 70), (0, 620, largura, 80))
    pygame.draw.line(screen, (255, 211, 105), (0, 620), (largura, 620), 4)

    texto_vida_jog1 = font_vida.render(f'Vida Jogador {jog1["cor"]}: {jog1["vida"]}', True, (255, 103, 0))
    texto_vida_jog2 = font_vida.render(f'Vida Jogador {jog2["cor"]}: {jog2["vida"]}', True, (255, 103, 0))
    texto_dado = font_dado.render(f'DADO: {y}', True, (255, 89, 0))


    screen.blit(texto_vida_jog1, (30, 635))
    screen.blit(texto_vida_jog2, (30, 665))
    screen.blit(texto_dado, (640, 645))
   
    desenhar_peao(screen, jog1['rgb'], jog1['pos'][0], jog1['pos'][1])
    desenhar_peao(screen, jog2['rgb'], jog2['pos'][0], jog2['pos'][1] + 32)

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            running=False

        if eventos.type == pygame.KEYDOWN:

            if eventos.key == pygame.K_r  and  fim and jogo_iniciado:
                    jog1['pos'] = posicoes[0]
                    jog2['pos'] = posicoes[0]
                    jog1['vida'] = 10
                    jog2['vida'] = 10
                    jog1['posicao'] = 0
                    jog2['posicao'] = 0
                    jogadores_presos = [0,0]
                    y=0
                    x='Pressione espaço'
                    jogo_iniciado=False
                    fim=False

            if eventos.key == pygame.K_ESCAPE and fim and jogo_iniciado:
                running=False

            if eventos.key == pygame.K_SPACE and not jogo_iniciado and not fim:
                s1 = random.randint(1,6) + random.randint(1,6)
                s2 = random.randint(1,6) + random.randint(1,6) 
                while s1 == s2:
                    s1 = random.randint(1,6) + random.randint(1,6)
                    s2 = random.randint(1,6) + random.randint(1,6)
                a=f'Jogador {jog1["cor"]} tirou {s1}'
                b=f'Jogador {jog2["cor"]} tirou {s2}'    
                if s1 > s2:
                    jogadores=[jog1, jog2]
                else:
                    jogadores=[jog2, jog1]
                x=f'Jogador {jogadores[0]["cor"]} começa. Clique em A para continuar'
                jogo_iniciado=True

            if eventos.key == pygame.K_a and jogo_iniciado and not fim:
                a = ''
                b = ''
                if jogadores_presos[turno] > 0:
                    jogadores_presos[turno] -= 1
                    x=f'Jogador {jogadores[turno]["cor"]} está preso e perdeu a vez!'
                    turno = (turno + 1) % 2
                    continue
                
                y = random.randint(1,6)
                jogadores[turno]['posicao'] += y

                if jogadores[turno]['posicao'] >= 27:
                    jogadores[turno]['posicao'] = 27
                    x=f'Jogador {jogadores[turno]["cor"]} venceu! Pressione: ESC para sair / R para reiniciar.' 
                    fim=True   
                jogadores[turno]['pos'] = posicoes[jogadores[turno]['posicao']]


                if cores_tabuleiro[jogadores[turno]['posicao']] == 'VERMELHO':
                    jogadores[turno]['vida'] -= 3
                    if jogadores[turno]['vida'] <= 0:
                        jogadores[turno]['vida'] = 0
                        x=f'Jogador {jogadores[turno]["cor"]} perdeu todas as vidas! Pressione: ESC para sair / R para reiniciar.'
                        fim=True
                    else:
                        x=f'Jogador {jogadores[turno]["cor"]} caiu no vermelho e perdeu 3 vidas!'
                
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'VERDE':
                    jogadores[turno]['vida'] += 1
                    if jogadores[turno]['vida'] >= 10:
                        jogadores[turno]['vida'] = 10
                        x=f'Jogador {jogadores[turno]["cor"]} está com vida máxima!'
                    else:
                        x=f'Jogador {jogadores[turno]["cor"]} caiu no verde e ganhou 1 vida!'
                
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'PRETO':
                    jogadores[turno]['posicao'] = 0
                    jogadores[turno]['pos'] = posicoes[0]
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no preto e voltou para o início!'

                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'AZUL':
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no azul e ganhou uma jogada extra!'
                    if turno == 0:
                        turno = 1
                    else:
                        turno = 0
                
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'AMARELO':
                    jogadores_presos[turno] = 1
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no amarelo e ficou preso por um turno!'

                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'BRANCO':
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no branco e não acontece nada!'

                if not fim:
                    turno = (turno + 1) % 2

    pygame.display.update()

pygame.quit()
