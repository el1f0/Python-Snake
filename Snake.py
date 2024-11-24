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

snake_speed = 20
snake_block = 10

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
                            gameloop()
                        if event.key == pygame.K_q:
                            game_close = True
    pygame.display.update()
    pygame.quit()
    quit()
def gameloop():
    game_over = False
    game_close = False
    
    direction = ""
    
    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0
    
    snake_list = []
    length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_width-snake_block)/snake_block-1)*snake_block
    foody = round(random.randrange(0, dis_height - snake_block)/snake_block)*snake_block
    print(foodx, foody)


    while not game_close:
        
        while game_over == True:
            dis.fill(black)
            title("Game Over!", red)
            message("Q-Quit or P-Play or M-Menu", white)
            pygame.display.update()
        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_m:
                        main_menu()
                        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "left"
                    
                elif event.key == pygame.K_RIGHT and direction != "left":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "right"
                    
                elif event.key == pygame.K_DOWN  and direction != "up":
                    x1_change = 0
                    y1_change = snake_block
                    direction = "down"
                    
                elif event.key == pygame.K_UP and direction != "down":   
                    x1_change = 0
                    y1_change = -snake_block
                    direction = "up"
                    
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
            print("Yummy!")
            foodx = round(random.randrange(0, dis_width-snake_block)/snake_block-1)*snake_block
            foody = round(random.randrange(0, dis_height - snake_block)/snake_block)*snake_block
            
            print(foodx, foody)
            
            length_of_snake += 1
            
        
        clock.tick(snake_speed)

    pygame.display.update()
    pygame.quit()
    quit()

main_menu()