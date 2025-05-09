import pygame
import random

# Initializatie
pygame.init()
pygame.mixer.init()

# Ecranul
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piatra-Foarfece-Hartie")

# culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# font
FONT = pygame.font.Font(None, 40)
BIG_FONT = pygame.font.Font(None, 64)

# fon
background = pygame.image.load("images/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# imagini
rock_img = pygame.transform.scale(pygame.image.load("images/rock.png"), (100, 100))
scissors_img = pygame.transform.scale(pygame.image.load("images/scissors.png"), (100, 100))
paper_img = pygame.transform.scale(pygame.image.load("images/paper.png"), (100, 100))

# muzica
pygame.mixer.music.load("sounds/background_music.mp3")  # muzica fon
pygame.mixer.music.play(-1)  # ciclu
click_sound = pygame.mixer.Sound("sounds/click.wav")     # sound click

# Variabile
CHOICES = ["Piatra", "Foarfece", "Hartie"]
player_choice = None
ai_choice = None
result = "Alegeti actiunea!"
player_score = 0
ai_score = 0
game_over = False
show_menu = True  # Ecranul pentru inceput

# Logica jocului
def get_winner(player, ai):
    if player == ai:
        return "Remiza"
    elif (player == "Piatra" and ai == "Foarfece") or \
         (player == "Foarfece" and ai == "Hartie") or \
         (player == "Hartie" and ai == "Piatra"):
        return "Jucatorul a castigat!"
    else:
        return "AI a castigat!"

# Butonul de restart
def reset_game():
    global player_score, ai_score, result, player_choice, ai_choice, game_over
    player_score = 0
    ai_score = 0
    result = "Alegeti actiunea!"
    player_choice = None
    ai_choice = None
    game_over = False

# Ciclu de baza
running = True
while running:
    if show_menu:
        screen.fill(BLACK)
        title = BIG_FONT.render("Piatra-Foarfece-Hartie", True, WHITE)
        start_text = FONT.render("Apasati orice buton pentru a incepe jocul", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 200))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                show_menu = False
        continue

    # fon
    screen.blit(background, (0, 0))

    # textul de rezultat
    result_text = FONT.render(result, True, BLACK)
    screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 30))

    # scorul
    score_text = FONT.render(f"player: {player_score}  |  AI: {ai_score}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 70))

    # butoanele actiunilor
    screen.blit(rock_img, (150, 400))
    screen.blit(scissors_img, (350, 400))
    screen.blit(paper_img, (550, 400))

    # alegerea ai/jucator
    if player_choice:
        icon = rock_img if player_choice == "Piatra" else scissors_img if player_choice == "Foarfece" else paper_img
        screen.blit(icon, (200, 200))
    if ai_choice:
        icon = rock_img if ai_choice == "Piatra" else scissors_img if ai_choice == "Foarfece" else paper_img
        screen.blit(icon, (500, 200))

    # butonul restart
    reset_btn = pygame.Rect(WIDTH // 2 - 80, 520, 160, 40)
    pygame.draw.rect(screen, GRAY, reset_btn)
    reset_text = FONT.render("Restart", True, BLACK)
    screen.blit(reset_text, (reset_btn.x + 40, reset_btn.y + 5))

    # castigul
    if player_score == 3:
        result = " Jucatorul a castigat!"
        game_over = True
    elif ai_score == 3:
        result = "AI a castigat!"
        game_over = True

    pygame.display.flip()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            x, y = event.pos
            if reset_btn.collidepoint(x, y):
                reset_game()
                continue

            if game_over:
                continue

            if 150 <= x <= 250 and 400 <= y <= 500:
                player_choice = "Piatra"
            elif 350 <= x <= 450 and 400 <= y <= 500:
                player_choice = "Foarfece"
            elif 550 <= x <= 650 and 400 <= y <= 500:
                player_choice = "Hartie"
            else:
                continue

            if player_choice == "Piatra":
                ai_choice = "Hartie"
            elif player_choice == "Foarfece":
                ai_choice = "Piatra"
            elif player_choice == "Hartie":
                ai_choice = "Foarfece"
            result = get_winner(player_choice, ai_choice)

            if result == "Jucatorul a castigat!":
                player_score += 1
            elif result == "AI a castigat!":
                ai_score += 1

pygame.quit()