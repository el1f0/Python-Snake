import pygame
import time
import random

pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))

pygame.display.update()
pygame.display.set_caption("Snake game by el1f0")

blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

# Variables

has_paused = False
snake_speed = 20
snake_block = 10

# Sound
pygame.mixer.init()
sound_path = "E:\Python\Sounds\\"
apple_crunch = pygame.mixer.Sound(sound_path + "apple_crunch.wav")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 40)
title_font = pygame.font.SysFont(None, 60)
score_font = pygame.font.SysFont(None, 40)

def our_snake (snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
        
def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0,0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect()
    mesg_rect.center = (dis_width/2, dis_height/2)
    dis.blit(mesg, mesg_rect)
    
def title(title_text, color):
    title = title_font.render(title_text, True, color)
    title_rect = title.get_rect()
    title_rect.midbottom = (dis_width/2, dis_height/4)
    dis.blit(title, title_rect)

def spawn_apple(x, y):
    
    foodx = round(random.randrange(0, dis_width - snake_block)/snake_block)*snake_block
    foody = round(random.randrange(0, dis_height - snake_block)/snake_block)*snake_block
            
    return (foodx, foody)

def main_menu():
    game_close = False
    
    dis.fill(white)
    
    while not game_close:
        title("Snake", blue)
        message("P-Play or Q-Quit", blue)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop(False)
                elif event.key == pygame.K_q:
                    game_close = True
    pygame.display.update()
    pygame.quit()
    quit()


def save(x, y, length_of_snake, snake_list, snake_head, foodx, foody, x1_change, y1_change):
    global old_x
    global old_y
    global old_length_of_snake
    global old_snake_list
    global old_snake_head
    global old_foodx
    global old_foody
    global old_x1_change
    global old_y1_change
    
    old_x = x
    old_y = y
    old_length_of_snake = length_of_snake
    old_snake_list = snake_list
    old_snake_head = snake_head
    old_foodx = foodx
    old_foody = foody
    old_x1_change = x1_change
    old_y1_change = y1_change
    
    # del old_snake_list[len(old_snake_list)-1]
    
    print("Saved position: ", old_x, old_y)
    print("Saved snake list:", old_snake_list)
    print("Saved snake head: ", old_snake_head)


def pause_menu():
    has_paused = True
    game_close = False
    
    dis.fill(black)
    
    while not game_close:
        title("Paused", white)
        message("P-Unpause or Q-Quit or M-Menu", white)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    gameloop(True)
                    
                elif event.key == pygame.K_m:
                    main_menu()
                    
                elif event.key == pygame.K_q:
                    game_close = True
                    
    pygame.display.update()
    pygame.quit()
    quit()
    
def gameloop(has_paused):
    game_over = False
    game_close = False
    direction = ""
    if has_paused:
        x1 = old_x
        y1 = old_y
        snake_list = old_snake_list
        length_of_snake = old_length_of_snake
        
        foodx = old_foodx
        foody = old_foody
        
        x1_change = old_x1_change
        y1_change = old_y1_change
        
    else:
        x1 = dis_width/2
        y1 = dis_height/2
        snake_list = []
        length_of_snake = 1

        (foodx, foody) = spawn_apple(x1, y1)

        x1_change = 0
        y1_change = 0

    while not game_close:
        can_turn = True
        while game_over == True:
            dis.fill(black)
            title("Game Over!", red)
            message("Q-Quit or P-Play or M-Menu", white)
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop(False)
                    elif event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    elif event.key == pygame.K_m:
                        main_menu()
                        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save(x1, y1, length_of_snake, snake_list, snake_head, foodx, foody, x1_change, y1_change)
                    pause_menu()
                if can_turn:    
                    if event.key == pygame.K_LEFT and direction != "right":
                        x1_change = -snake_block
                        y1_change = 0
                        direction = "left"
                        can_turn = False
                        
                    elif event.key == pygame.K_RIGHT and direction != "left":
                        x1_change = snake_block
                        y1_change = 0
                        direction = "right"
                        can_turn = False
                        
                    elif event.key == pygame.K_DOWN  and direction != "up":
                        x1_change = 0
                        y1_change = snake_block
                        direction = "down"
                        can_turn = False
                        
                    elif event.key == pygame.K_UP and direction != "down":   
                        x1_change = 0
                        y1_change = -snake_block
                        direction = "up"
                        can_turn = False
                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True    
                
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(black)

        # Draw snake
        pygame.draw.rect(dis, green, [x1,y1,snake_block,snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1) 
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list [:-1]:
            if x == snake_head:
                game_over = True
        
        our_snake(snake_block, snake_list)
        your_score(length_of_snake-1)
        # Draw apple
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        pygame.display.update()
        
        if  foodx - snake_block < x1 < foodx + snake_block and foody - snake_block < y1 < foody + snake_block:
            (foodx, foody) = spawn_apple(x1, y1)
            pygame.mixer.Sound.play(apple_crunch)
            length_of_snake += 1
            
        clock.tick(snake_speed)

    pygame.display.update()
    pygame.quit()
    quit()

main_menu()