import pygame
import sys
import random



pygame.init()



WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_RADIUS = 15
BALL_SPEED = 5
PADDLE_SPEED = 7
GAME_TIME_SECONDS = 60



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tennis Game")



paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)



ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])]



score1 = 0
score2 = 0


font = pygame.font.Font(None, 36)


start_time = pygame.time.get_ticks()
game_over = False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_z] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED


    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]


    if paddle1.colliderect(pygame.Rect(ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
        ball_speed[0] = abs(ball_speed[0])
    if paddle2.colliderect(pygame.Rect(ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
        ball_speed[0] = -abs(ball_speed[0])


    if ball_pos[1] - BALL_RADIUS < 0 or ball_pos[1] + BALL_RADIUS > HEIGHT:
        ball_speed[1] = -ball_speed[1]


    if ball_pos[0] - BALL_RADIUS < 0:
        
        score2 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])]
    elif ball_pos[0] + BALL_RADIUS > WIDTH:
        score1 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.choice([-BALL_SPEED, BALL_SPEED]), random.choice([-BALL_SPEED, BALL_SPEED])]

    screen.fill(BLACK)

    
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)


    score_display = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 20))


    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_display = font.render(f"Time: {GAME_TIME_SECONDS - elapsed_time}", True, WHITE)
    screen.blit(time_display, (20, 20))


    if elapsed_time >= GAME_TIME_SECONDS:
        game_over = True


    pygame.display.flip()


    pygame.time.Clock().tick(30)


final_score_display = font.render(f"Final Score: {score1} - {score2}", True, WHITE)
game_over_display = font.render("Game Over", True, WHITE)

screen.fill(BLACK)
screen.blit(final_score_display, (WIDTH // 2 - final_score_display.get_width() // 2, HEIGHT // 2 - 50))
screen.blit(game_over_display, (WIDTH // 2 - game_over_display.get_width() // 2, HEIGHT // 2 + 50))
pygame.display.flip()


pygame.time.delay(3000)

pygame.quit()
sys.exit()
