import pygame
import sys
import random

pygame.init()

# screen size
WIDTH = 800
HIGHT = 600

#colour
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_CLR = (0,0,0)

#position and size of player

player_shap = 50
player_pos = [WIDTH/2,HIGHT-2*player_shap]

#position and size of enemy
enemy_shap = 50
enemy_pos =  [random.randint(0,WIDTH-enemy_shap),0]
enemy_list = [enemy_pos]

#screen setup in pygame

screen = pygame.display.set_mode((WIDTH, HIGHT))
my_font = pygame.font.SysFont("monospace", 35)


#seting up the speed and score
clock = pygame.time.Clock()
game_over = False
score = 0
SPEED = 5

#seting the level
def set_level(score, SPEED):
    if score < 20:
        SPEED = 8
    elif score < 50:
        SPEED = 13
    elif score < 50:
        SPEED = 15
    else:
        SPEED = 20
    return SPEED

#initilizing the enemy
def drop_enemy(enemy_list):

    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH-enemy_shap)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

 #drawing the enemy
def draw_enemys(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_shap, enemy_shap))

#unpadting the position
def enemy_update_pos(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1]>=0 and enemy_pos[1] < HIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score


    #collision checking between player and enemy
def collision_check(enemy_list , player_pos):
    for enemy_pos in enemy_list:
        if dectect_collision(enemy_pos, player_pos):
            return True     
    return False

#decting the collision
def dectect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_shap)) or (p_x >= e_x and p_x <  (e_x+enemy_shap)):
        if (e_y >= p_y and e_y < (p_y + player_shap)) or (p_y >= e_y and p_y <(e_y+enemy_shap)):
            return True
    return False


#loop
while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x = player_pos[0]
                y = player_pos[1]
                if event.key == pygame.K_LEFT:
                    x-= player_shap
                elif event.key == pygame.K_RIGHT:
                    x+= player_shap

                player_pos = [x,y]


        #screen colour

        screen.fill(BACKGROUND_CLR)

        drop_enemy(enemy_list)
        score = enemy_update_pos(enemy_list , score)
        SPEED = set_level(score,SPEED)

        #score setting up
        text = "Score:" + str(score)
        label = my_font.render(text, 1 ,YELLOW)
        screen.blit(label,(WIDTH-200,HIGHT-40))

        #game over
        if collision_check(enemy_list,player_pos):
            game_over = True
            break

        #function calling
        draw_enemys(enemy_list)

        pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_shap,player_shap))

        clock.tick(30)

        pygame.display.update()