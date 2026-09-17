import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
LARGURA = 1000
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Of Jam")

# Cores
PRETO = (20, 20, 20)
AZUL = (0, 120, 255)
BRANCO = (255, 255, 255)
AZUL_ESCURO = (10, 30, 80)

# Fontes
titulo = pygame.font.SysFont("Arial", 80, bold=True)
texto = pygame.font.SysFont("Arial", 28)
botao_font = pygame.font.SysFont("Arial", 35, bold=True)

# Botão
botao = pygame.Rect(400, 360, 200, 70)

clock = pygame.time.Clock()

while True:

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao.collidepoint(evento.pos):
                print("O jogo começou!")

    # Fundo
    tela.fill(AZUL_ESCURO)

    # Título
    titulo_surface = titulo.render("OF JAM", True, BRANCO)
    tela.blit(
        titulo_surface,
        (LARGURA // 2 - titulo_surface.get_width() // 2, 120)
    )

    # Texto
    subtitulo = texto.render("Prepare-se para uma grande aventura!", True, BRANCO)
    tela.blit(
        subtitulo,
        (LARGURA // 2 - subtitulo.get_width() // 2, 230)
    )

    # Botão
    pygame.draw.rect(tela, AZUL, botao, border_radius=12)

    texto_botao = botao_font.render("JOGAR", True, BRANCO)
    tela.blit(
        texto_botao,
        (
            botao.centerx - texto_botao.get_width() // 2,
            botao.centery - texto_botao.get_height() // 2,
        ),
    )

    pygame.display.flip()
    clock.tick(60)