import pygame 

pygame.init()
largura=840
altura=700
screen=pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Maze Runner")

running=True

while running:
  screen.fill((255,255,255))
  
  for eventos in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
          
  pygame.draw.rect(screen, (0, 0, 0), (20, 50, 80, 80))#preto
  pygame.draw.rect(screen, (225,225,225), (100, 50, 80, 80))#branco
  pygame.draw.rect(screen, (225, 0, 0), (180, 50, 80, 80))#vermelho
  pygame.draw.rect(screen, (0, 225, 0), (260, 50, 80, 80))#verde
  pygame.draw.rect(screen, (225, 225, 225), (340, 50, 80, 80))#branco
  pygame.draw.rect(screen, (0, 0, 225), (420, 50, 80, 80))  #azul
  pygame.draw.rect(screen, (225, 225, 225), (500, 50, 80, 80))  #branco
  pygame.draw.rect(screen, (225, 225, 0), (580, 50, 80, 80))  #amarelo
  pygame.draw.rect(screen, (225, 225, 225), (660, 50, 80, 80))  # branco
  pygame.draw.rect(screen, (225, 0, 0), (740, 50, 80, 80))  #vermelho
  pygame.draw.rect(screen, (0, 225, 0), (740, 130, 80, 80))  # verde
  pygame.draw.rect(screen, (0, 0, 0), (740, 210, 80, 80))  # preto
  pygame.draw.rect(screen, (0, 0, 225), (740, 290, 80, 80))  # azul
  pygame.draw.rect(screen, (225, 225, 225), (740, 370, 80, 80))  # branco
  pygame.draw.rect(screen, (225, 225, 225), (740, 450, 80, 80))  # branco
  pygame.draw.rect(screen, (225, 0, 0), (740, 530, 80, 80))  # vermelho
  pygame.draw.rect(screen, (0, 225, 0), (660, 530, 80, 80))  # verde
  pygame.draw.rect(screen, (225, 225, 225), (580, 530, 80, 80))  # branco
  pygame.draw.rect(screen, (225, 225, 0), (500, 530, 80, 80))  # amarelo
  pygame.draw.rect(screen, (225, 225, 225), (420, 530, 80, 80))  #branco
  pygame.draw.rect(screen, (225, 0, 0), (340, 530, 80, 80))  # vermelho
  pygame.draw.rect(screen, (0, 225, 0), (260, 530, 80, 80))  # verde
  pygame.draw.rect(screen, (225, 225, 225), (180, 530, 80, 80))  # branco
  pygame.draw.rect(screen, (0, 0, 225), (100, 530, 80, 80))  # azul
  pygame.draw.rect(screen, (225, 0, 0), (20, 530, 80, 80))  # vermelho
  pygame.draw.rect(screen, (225, 225, 0), (20, 450, 80, 80))  # amarelo
  pygame.draw.rect(screen, (0, 225, 0), (20, 370, 80, 80))  # vermelho
  pygame.draw.rect(screen, (0, 0, 0), (20, 290, 80, 80))  # preto
  
  pygame.display.update()
  
pygame.quit()
