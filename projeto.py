import pygame
import random 
import os

#iniciando o pygame e a fonte
pygame.init() 
pygame.font.init()

largura=870
altura=700
#Criando a tela do jogo com as variáveis acima e criando a variável screen para manipulá-la
screen=pygame.display.set_mode((largura,altura)) 
pygame.display.set_caption("Jogo Maze Runner")

#Verificando se é possível acessar o arquivo da fonte, senão usa a fonte padrão do pygame
NOME_FONTE = "font/PressStart2P-Regular.ttf"
if os.path.exists(NOME_FONTE):
    font = pygame.font.Font(NOME_FONTE, 13) #Configuração do texto acima do tabuleiro
    font_vida = pygame.font.Font(NOME_FONTE, 15) #Configuração do texto da vida dos jogadores
    font_dado = pygame.font.Font(NOME_FONTE, 18) #Configuração do texto do dado
else:
    print(f"Aviso: Arquivo '{NOME_FONTE}' não encontrado. Usando fonte padrão do sistema.")
    font = pygame.font.Font(None, 30)
    font_vida = pygame.font.Font(None, 30)
    font_dado = pygame.font.Font(None, 35)

#Função para desenhar os jogadores com sombra cinza, cor do jogador e borda branca
def desenhar_peao(tela, cor, pos_x, pos_y):
    pygame.draw.circle(tela, (50, 50, 50), (pos_x + 27, pos_y + 27), 15) #Sombra cinza
    pygame.draw.circle(tela, cor, (pos_x + 25, pos_y + 25), 15) #Cor do jogador
    pygame.draw.circle(tela, (255, 255, 255), (pos_x + 25, pos_y + 25), 15, 3) #Borda branca

#Variáveis de texto que são modificadas ao longo do jogo 
x='Pressione espaço para jogar'
a=''
b=''

#Dicionários que armazenam as posiçoes do tabuleiro, cores equivalentes a cada posição e rgb equivalente a cada cor
#Utilizamos o tabuleiro inicial que fizemos (armazenado na pasta "tabuleiro") para obter as posições e cores
posicoes = {0:  (20, 50),1:  (100, 50),2:  (180, 50),3:  (260, 50),4:  (340, 50),5:  (420, 50),6:  (500, 50),7:  (580, 50),8:  (660, 50),
            9:  (740, 50),10: (740, 130),11: (740, 210),12: (740, 290),13: (740, 370),14: (740, 450),15: (740, 530),16: (660, 530),17: (580, 530),
            18: (500, 530),19: (420, 530),20: (340, 530),21: (260, 530),22: (180, 530),23: (100, 530),24: (20, 530),25: (20, 450),26: (20, 370),27: (20, 290)}
cores_tabuleiro = {0: "INICIO", 1: "BRANCO", 2: "VERMELHO", 3: "VERDE", 4: "BRANCO", 5: "AZUL", 6: "BRANCO", 7: "AMARELO", 8: "BRANCO", 9: "VERMELHO", 
    10: "VERDE", 11: "PRETO", 12: "AZUL", 13: "BRANCO", 14: "BRANCO", 15: "VERMELHO", 16: "VERDE", 17: "BRANCO", 18: "AMARELO", 19: "BRANCO", 
    20: "VERMELHO", 21: "VERDE", 22: "BRANCO", 23: "AZUL", 24: "VERMELHO", 25: "AMARELO", 26: "VERDE", 27: "FIM"}
rgb={"VERMELHO": (225, 0, 0), "VERDE": (0, 225, 0), "PRETO": (0, 0, 0), "AZUL": (0, 0, 225), "AMARELO": (225, 225, 0), "BRANCO": (225, 225, 225), "INICIO": (0,0,0), "FIM": (0,0,0)}

#Dicionários que guardam informações importantes sobre os jogadores
#As chaves "cor" e "rgb" são imutáveis, usadas ,principalmente, pra se referir ao jogador no texto e para desenhá-lo no tabuleiro, respectivamente
jog1={'vida':10, 'posicao':0, 'pos':posicoes[0], 'cor':'Verde', 'rgb':(0, 255, 170)}
jog2={'vida':10, 'posicao':0, 'pos':posicoes[0], 'cor':'Rosa', 'rgb':(255, 20, 147)}

jogadores_presos=[0,0] #Lista que guarda a informação se um jogogador está preso
jogadores=[jog1, jog2] #Lista que determina a ordem dos jogadores, modificada no início do jogo
turno=0 #Variável que garante que jogue um jogador por vez, varia entre 0 e 1
y=0 #Variável que representa o dado

#Variáveis bool que controlam as ações do usuário, evitando erros, garantindo que o jogo funcione corretamente 
jogo_iniciado=False
fim=False
running=True

#Loop principal do jogo
while running:
    screen.fill((255,255,255))
    #Loop para desenhar o tabuleiro com as informações dos dicionários
    for p, cord in posicoes.items():
        pygame.draw.rect(screen, rgb[cores_tabuleiro[p]], (cord[0], cord[1], 80, 80))

    screen.blit(font.render('Início', True, (255,255,255)), (20, 55))
    screen.blit(font.render('Fim', True, (255,255,255)), (22,295))
    screen.blit(font.render(x, True, (0,0,0)), (5,15))
    screen.blit(font_vida.render(a, True, (0,0,0)), (230, 300))
    screen.blit(font_vida.render(b, True, (0,0,0)), (230, 350))

    #Linha e retângulo desenhados em baixo do tabuleiro para fins estéticos
    pygame.draw.rect(screen, (57, 62, 70), (0, 620, largura, 80))
    pygame.draw.line(screen, (255, 211, 105), (0, 620), (largura, 620), 4)

    #Configuraçoes dos textos
    texto_vida_jog1 = font_vida.render(f'Vida Jogador {jog1["cor"]}: {jog1["vida"]}', True, (255, 211, 105))
    texto_vida_jog2 = font_vida.render(f'Vida Jogador {jog2["cor"]}: {jog2["vida"]}', True, (255, 211, 105))
    texto_dado = font_dado.render(f'DADO: {y}', True, (255, 211, 105))

    #Escrevendo os textos de vida e do dado
    screen.blit(texto_vida_jog1, (30, 635))
    screen.blit(texto_vida_jog2, (30, 665))
    screen.blit(texto_dado, (640, 645))
   
    #Chamando a função para desenhar os jogadores com as informações dos dicionários
    desenhar_peao(screen, jog1['rgb'], jog1['pos'][0], jog1['pos'][1])
    desenhar_peao(screen, jog2['rgb'], jog2['pos'][0], jog2['pos'][1] + 32)

    #Loop interno para verificar os eventos do usuário 
    for eventos in pygame.event.get():
        #Se clicar no "X" da tela
        if eventos.type == pygame.QUIT:
            running=False

        #Se clicar em alguma tecla 
        if eventos.type == pygame.KEYDOWN:
            
            #Se clicar no espaço e o jogo não tiver começado nem terminado
            if eventos.key == pygame.K_SPACE and not jogo_iniciado and not fim:
                #Sorteia quem começa primeiro, garantido que a soma dos dois sorteados não seja igual
                s1 = random.randint(1,6) + random.randint(1,6)
                s2 = random.randint(1,6) + random.randint(1,6) 
                while s1 == s2:
                    s1 = random.randint(1,6) + random.randint(1,6)
                    s2 = random.randint(1,6) + random.randint(1,6)
                #Muda a variável de texto para exibir o resultado da soma na tela
                a=f'Jogador {jog1["cor"]} tirou {s1}'
                b=f'Jogador {jog2["cor"]} tirou {s2}'    
                #Muda a ordem da lista jogadores
                if s1 > s2:
                    jogadores=[jog1, jog2]
                else:
                    jogadores=[jog2, jog1]
                #Muda a variável de texto para exibir quem começa primeiro e muda uma das variáveis de controle
                x=f'Jogador {jogadores[0]["cor"]} começa. Clique em A para continuar'
                jogo_iniciado=True

            #Se a tecla for "A" e o jogo tiver começado, mas não acabado
            if eventos.key == pygame.K_a and jogo_iniciado and not fim:
                #Esvazia as variáveis de texto do meio do tabuleiro
                a = ''
                b = ''

                #Verifica se há algum jogador preso nesse turno antes de permitir que ele jogue, caso tenha garante que ele perca a vez e jogue na próxima
                if jogadores_presos[turno] > 0:
                    jogadores_presos[turno] -= 1
                    x=f'Jogador {jogadores[turno]["cor"]} está preso e perdeu a vez!'
                    turno = (turno + 1) % 2
                    continue
                
                #Sorteia o dado e atualiza a posição do jogador
                y = random.randint(1,6)
                jogadores[turno]['posicao'] += y

                #Garante que o jogador não passe do fim e acaba o jogo caso ele esteja no fim 
                if jogadores[turno]['posicao'] >= 27:
                    jogadores[turno]['posicao'] = 27
                    x=f'Jogador {jogadores[turno]["cor"]} venceu! Pressione: ESC para sair / R para reiniciar.' 
                    fim=True   
                jogadores[turno]['pos'] = posicoes[jogadores[turno]['posicao']]

                #Verificacao das cores do tabuleiro

                #Condicao vermelho: perde 3 vidas. E se chegar a 0 vidas ou menos, o jogador perde tudo e o jogo acaba.
                if cores_tabuleiro[jogadores[turno]['posicao']] == 'VERMELHO':
                    jogadores[turno]['vida'] -= 3
                    if jogadores[turno]['vida'] <= 0:
                        jogadores[turno]['vida'] = 0
                        x=f'Jogador {jogadores[turno]["cor"]} perdeu todas as vidas!.'
                        a='ESC para sair'
                        b='R para reiniciar'
                        fim=True
                    else:
                        x=f'Jogador {jogadores[turno]["cor"]} caiu no vermelho e perdeu 3 vidas!'
                
                #Condicao verde: ganha 1 vida. Não permite que a vida ultrapasse o limite máximo 10.
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'VERDE':
                    jogadores[turno]['vida'] += 1
                    if jogadores[turno]['vida'] >= 10:
                        jogadores[turno]['vida'] = 10
                        x=f'Jogador {jogadores[turno]["cor"]} está com vida máxima!'
                    else:
                        x=f'Jogador {jogadores[turno]["cor"]} caiu no verde e ganhou 1 vida!'

                #Condicao preto: reinicia o trajeto do jogador, voltando para a posicao 0.
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'PRETO':
                    jogadores[turno]['posicao'] = 0
                    jogadores[turno]['pos'] = posicoes[0]
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no preto e voltou para o início!'

                #Condicao azul: o jogador ganha o direito de jogar novamente. O jogo inverte a passagem de turno que acontece no fim do loop.
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'AZUL':
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no azul e ganhou uma jogada extra!'
                    if turno == 0:
                        turno = 1
                    else:
                        turno = 0

                #Condicao amarelo: o jogador fica uma rodada sem jogar. Ativa a restricao na lista 'jogador_presos'.
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'AMARELO':
                    jogadores_presos[turno] = 1
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no amarelo e ficou preso por um turno!'
                    
                #Condicao branco: nada afeta o jogador.
                elif cores_tabuleiro[jogadores[turno]['posicao']] == 'BRANCO':
                    x=f'Jogador {jogadores[turno]["cor"]} caiu no branco e não acontece nada!'

                #Passa a vez para o próximo jogador, se o jogo ainda não tiver acabado.
                if not fim:
                    turno = (turno + 1) % 2

            #Reinicia o jogo (reset de posicoes, vidas, textos e variáveis de controle) caso o jogo tenha acabado e o usuário aperte "R".
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

            #Fecha o jogo se Esc for apertado e o jogo estiver finalizado.
            if eventos.key == pygame.K_ESCAPE and fim and jogo_iniciado:
                running=False


    pygame.display.update()

pygame.quit()
