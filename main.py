import pygame, random, tkinter

# ARROW - PLAYER 1
# WASD - PLAYER 2

# CREATE SKINS FOR BOTH P1 AND P2
# TAG GAME

x = pygame.init()
root = tkinter.Tk()
pcspecs = (root.winfo_screenwidth(),root.winfo_screenheight())
           
pygame.mixer.init()
character_index_1 = 0
character_index_2 = 1

pygame.font.get_fonts()
font = pygame.font.SysFont('arialblue', 60)

def tex(text, greenor, x, y) : 
    screen_text = font.render(str(text), True, greenor)
    win.blit(screen_text, [x,y])


# BASIC SETTING 
win = pygame.display.set_mode(pcspecs, pygame.FULLSCREEN)
pygame.display.set_caption("Something, I don't know")
pygame.display.update()
clock = pygame.time.Clock()

# IMAGE SETUP
menu_bg = pygame.transform.scale(pygame.image.load("images/background.jpg"), (pcspecs[0], pcspecs[1])).convert_alpha()
blimg = pygame.transform.scale(pygame.image.load("images/blur.png"), (pcspecs[0], pcspecs[1])).convert_alpha()
start = pygame.transform.scale(pygame.image.load("images/title.png"), (pcspecs[0]/1.7, pcspecs[1]/9)).convert_alpha()
volumeimg = pygame.transform.scale(pygame.image.load("images/vol.png"), (pcspecs[0]/34, pcspecs[1]/18)).convert_alpha()
no_volumeimg = pygame.transform.scale(pygame.image.load("images/novol.png"), (pcspecs[0]/34, pcspecs[1]/18)).convert_alpha()
gameoverimg = pygame.transform.scale(pygame.image.load("images/over.png"), (650,90)).convert_alpha() 
resetimg = pygame.transform.scale(pygame.image.load("images/reset.png") , (pcspecs[0]/2,pcspecs[1]/30)).convert_alpha()
menuimg = pygame.transform.scale(pygame.image.load("images/menu.png") , (pcspecs[0]/2,pcspecs[1]/30)).convert_alpha()
arrowimg = pygame.transform.scale(pygame.image.load("images/arrow.png"), (35, 35)).convert_alpha()

# PLATFORMS
platformlong = pygame.transform.scale(pygame.image.load("images/g1.png"), (700, 80)).convert_alpha()
platformmedium = pygame.transform.scale(pygame.image.load("images/g2.png"), (350, 80)).convert_alpha()
platformshort = pygame.transform.scale(pygame.image.load("images/g3.png"), (175, 80)).convert_alpha()

# CHARACTERS
char1_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_1}.png"), (40, 40)).convert_alpha()
char2_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_2}.png"), (40, 40)).convert_alpha()

default_volume = True                   # Volume button boolean

def loadscreen() : 
    global character_index_1, character_index_2
    exit_game = False 
    char1_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_1}.png"), (60, 60)).convert_alpha()
    char2_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_2}.png"), (60, 60)).convert_alpha()
    playbutton_img = pygame.transform.scale(pygame.image.load("images/playbutton1.png"), (pcspecs[0]/6.8,pcspecs[1]/25)).convert_alpha()
    playbutton_dimension = (pcspecs[0]//3+10, pcspecs[1]//2+200)
    volumebutton_dimension = (pcspecs[0]-100, 50)
    leftarrow1_dimension = (pcspecs[0]//2+100, pcspecs[1]//2-90)
    rightarrow1_dimension = (pcspecs[0]//2+225, leftarrow1_dimension[1])
    leftarrow2_dimension = (pcspecs[0]//2-200, leftarrow1_dimension[1])
    rightarrow2_dimension = (pcspecs[0]//2-75, leftarrow1_dimension[1])
    playbutton_rect = pygame.Rect(playbutton_dimension[0], playbutton_dimension[1], pcspecs[0]/3, pcspecs[1]/15)
    volumebutton_rect = pygame.Rect(volumebutton_dimension[0], volumebutton_dimension[1], pcspecs[0]/27, pcspecs[1]/14.5)
    leftbutton1_rect = pygame.Rect(leftarrow1_dimension[0], leftarrow1_dimension[1], 35, 35)
    rightbutton1_rect = pygame.Rect(rightarrow1_dimension[0], rightarrow1_dimension[1], 35, 35)
    leftbutton2_rect = pygame.Rect(leftarrow2_dimension[0], leftarrow2_dimension[1], 35, 35)
    rightbutton2_rect = pygame.Rect(rightarrow2_dimension[0], rightarrow2_dimension[1], 35, 35)
    leftarrow1 = pygame.transform.scale(pygame.image.load("images/left1.png"), (35,35)).convert_alpha() 
    leftarrow2 = pygame.transform.scale(pygame.image.load("images/left2.png"), (35,35)).convert_alpha() 
    rightarrow1 = pygame.transform.scale(pygame.image.load("images/right1.png"), (35,35)).convert_alpha() 
    rightarrow2 = pygame.transform.scale(pygame.image.load("images/right2.png"), (35,35)).convert_alpha() 
    pygame.mixer.music.load("music/game sound3.mp3")
    global default_volume
    pygame.mixer.music.play()
    while not exit_game : 
        win.blit(menu_bg, (0,0))
        win.blit(char2_img, (pcspecs[0]//2-150, pcspecs[1]//2-100))
        win.blit(char1_img, (pcspecs[0]//2+150, pcspecs[1]//2-100))
        win.blit(start, (pcspecs[0]//5, pcspecs[1]/7.2))
        pygame.draw.rect(win, (63, 0, 93), playbutton_rect)
        pygame.draw.rect(win, (255,255,255), volumebutton_rect)
        pygame.draw.rect(win, (0, 0, 0), leftbutton1_rect)
        pygame.draw.rect(win, (0, 0, 0), rightbutton1_rect)
        pygame.draw.rect(win, (0, 0, 0), leftbutton2_rect)
        pygame.draw.rect(win, (0, 0, 0), rightbutton2_rect)
        win.blit(leftarrow1, leftarrow1_dimension)
        win.blit(rightarrow1, rightarrow1_dimension)
        win.blit(leftarrow2, leftarrow2_dimension)
        win.blit(rightarrow2, rightarrow2_dimension)
        win.blit(playbutton_img, (playbutton_dimension[0]+(playbutton_dimension[0]/3-10), playbutton_dimension[1]+10))

        if default_volume:
            win.blit(volumeimg, (volumebutton_dimension[0]+5, volumebutton_dimension[1]+5))
            pygame.mixer.music.unpause()
        else:
            win.blit(no_volumeimg, (volumebutton_dimension[0]+5, volumebutton_dimension[1]+5))
            pygame.mixer.music.pause()

        # BUTTON FUNCTIONALITY
        pygame.time.delay(100)
        for event in pygame.event.get():
            mloc = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if volumebutton_rect.collidepoint(mloc):
                    default_volume = not default_volume
                elif playbutton_rect.collidepoint(mloc): 
                    gameloop()
                if leftbutton1_rect.collidepoint(mloc) :
                    character_index_1 -= 1
                    if character_index_1 == character_index_2 : 
                        character_index_1 -= 1
                    if character_index_1 < 0 :
                        character_index_1 = 9
                if leftbutton2_rect.collidepoint(mloc) :
                    character_index_2 -= 1
                    if character_index_1 == character_index_2 : 
                        character_index_2 -= 1
                    if character_index_2 < 0 :
                        character_index_2 = 9
                if rightbutton1_rect.collidepoint(mloc) :
                    character_index_1 += 1
                    if character_index_1 == character_index_2 : 
                        character_index_1 += 1
                    if character_index_1 > 9 :
                        character_index_1 = 0
                if rightbutton2_rect.collidepoint(mloc) :
                    character_index_2 += 1
                    if character_index_1 == character_index_2 : 
                        character_index_2 += 1
                    if character_index_2 > 9 :
                        character_index_2 = 0
                char1_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_1}.png"), (60, 60)).convert_alpha()
                char2_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_2}.png"), (60, 60)).convert_alpha()
                

            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_ESCAPE : 
                    quit()

        pygame.display.update()
        clock.tick(60)



def gameloop() : 
    global char1_img, char2_img
    turn = random.randint(0, 1)
    clock = pygame.time.Clock()
    counter, countdown = 30, '30'
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    jump1 = False
    jump2 = False
    jumpHeight = 40
    velocity1 = jumpHeight
    velocity2 = jumpHeight
    gravity = 7
    platformlist = [
        (pcspecs[0] // 4, 75, 700, 80),
        (pcspecs[0] // 2, 175, 350, 80),
        (pcspecs[0] // 5, 300, 350, 80),
        (pcspecs[0] // 2 + 100, 300, 350, 80),
        (pcspecs[0] // 7, 450, 175, 80),
        (pcspecs[0] // 2, 450, 175, 80),
        (pcspecs[0] // 4, 550, 350, 80),
        (pcspecs[0] // 2 + 200, 550, 175, 80)
    ]
    ingame_bg = pygame.transform.scale(pygame.image.load("images/image.jpg"), (pcspecs[0], pcspecs[1])).convert_alpha()
    char1_pos_x, char1_pos_y = 10, 700
    char2_pos_x, char2_pos_y = 500, 700
    char1_speed = 0 
    char2_speed = 0 
    exit_game = False 
    game_over = False 
    char1_pos_list = []
    char2_pos_list = []
    last = pygame.time.get_ticks()

    global default_volume, in_air1, in_air2
    if default_volume :
        pygame.mixer.music.load("music/ingame music3.mp3")
        pygame.mixer.music.play()
    
    while not exit_game :
        if game_over : 
            if turn == 0 :
                winimg = pygame.image.load("images/winner1.png")
            else : 
                winimg = pygame.image.load("images/winner2.png")

            winimg = pygame.transform.scale(winimg, (400, 50))

            win.blit(gameoverimg, (360,120))
            win.blit(blimg, (0,0))
            win.blit(winimg, (pcspecs[0]/4, pcspecs[1]/3))
            win.blit(resetimg, (pcspecs[0]/4, 1.5*pcspecs[1]/3))
            win.blit(menuimg, ((pcspecs[0]/4, 1.8*pcspecs[1]/3)))
            
            for event in pygame.event.get() : 
                if event.type == pygame.QUIT : 
                    exit_game = True
                
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_RETURN : 
                        gameloop()
                        
                    if event.key == pygame.K_ESCAPE : 
                        loadscreen()
        else : 
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    if counter > 0 :
                        countdown = str(counter)
                    else :
                        game_over = True

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loadscreen()

                if event.type == pygame.KEYDOWN:
                    if turn == 1 :
                        speed = 3
                    else :
                        speed = 0
                    if event.key == pygame.K_d:
                        char2_speed = 10 + speed
                    elif event.key == pygame.K_a:
                        char2_speed = -10 - speed
                    elif event.key == pygame.K_w:
                        if not jump2 :
                            jump2 = True

                if event.type == pygame.KEYDOWN:
                    if turn == 0 :
                        speed = 3
                    else :
                        speed = 0
                    if event.key == pygame.K_RIGHT:
                        char1_speed = 10+speed
                    elif event.key == pygame.K_LEFT:
                        char1_speed = -10-speed
                    elif event.key == pygame.K_UP:
                        if not jump1 :
                            jump1 = True
                        
            char1_pos_x = char1_pos_x + char1_speed
            char2_pos_x = char2_pos_x + char2_speed
            if jump1 : 
                char1_pos_y -= velocity1
                velocity1 -= gravity
                if velocity1 < -jumpHeight :
                    jump1 = False
                    velocity1 = jumpHeight
            else :
                if char1_pos_y < 700 :
                    char1_pos_y += gravity

            if jump2 : 
                char2_pos_y -= velocity2
                velocity2 -= gravity
                if velocity2 < -jumpHeight :
                    jump2 = False
                    velocity2 = jumpHeight

            else : 
                if char2_pos_y < 700 :
                    char2_pos_y += gravity

            def check_collision(player_x, player_y, platforms):
                for platform in platforms:
                    px, py, pw, ph = platform
                    if player_x + 10 > px and player_x < px + pw-10 and player_y + 10 > py and player_y < py + ph:
                        return platform
                return None

            def handle_platform_collision(player_x, player_y, velocity, platforms):
                platform = check_collision(player_x, player_y, platforms)
                if platform:
                    _, py, _, _ = platform
                    if velocity < 0:
                        return player_y, False, velocity
                    else: 
                        return py - 10, False, jumpHeight
                return player_y, True, velocity

            char1_pos_y, in_air1, velocity1 = handle_platform_collision(char1_pos_x, char1_pos_y, velocity1, platformlist)
            char2_pos_y, in_air2, velocity2 = handle_platform_collision(char2_pos_x, char2_pos_y, velocity2, platformlist)

            win.blit(ingame_bg, (0,0))
            tex(countdown, (0, 0, 0), pcspecs[0]//2-50, 10)


            if len(char1_pos_list) != 0 :
                del char1_pos_list[0]
                del char1_pos_list[0]
            char1_pos_list.append(char1_pos_x)
            char1_pos_list.append(char1_pos_y)

            if len(char2_pos_list) != 0 :
                del char2_pos_list[0]
                del char2_pos_list[0]
            char2_pos_list.append(char2_pos_x)
            char2_pos_list.append(char2_pos_y)

            if char1_pos_x < 0:
                char1_pos_x = pcspecs[0]
            elif char1_pos_x > pcspecs[0]:
                char1_pos_x = 0

            if char2_pos_x < 0:
                char2_pos_x = pcspecs[0]
            elif char2_pos_x > pcspecs[0]:
                char2_pos_x = 0

            if turn == 0 and abs(char1_pos_list[0]-char2_pos_list[0])<30 and abs(char1_pos_list[1]-char2_pos_list[1])<40:
                now = pygame.time.get_ticks()
                if now - last >= 2000 :
                    turn = 1
                
                
            elif turn == 1 and abs(char1_pos_list[0]-char2_pos_list[0])<30 and abs(char1_pos_list[1]-char2_pos_list[1])<40 :
                now = pygame.time.get_ticks()
                if now - last >= 2000 :
                    turn = 0
                
            for platform in platformlist:
                px, py, pw, ph = platform
                if pw == 700:
                    win.blit(platformlong, (px, py))
                elif pw == 350:
                    win.blit(platformmedium, (px, py))
                elif pw == 175:
                    win.blit(platformshort, (px, py))
            win.blit(char1_img, tuple(char1_pos_list))
            win.blit(char2_img, tuple(char2_pos_list))
            if turn == 0 :
                win.blit(arrowimg, (char1_pos_list[0], char1_pos_list[1]-50))

            elif turn == 1 :
                win.blit(arrowimg, (char2_pos_list[0], char2_pos_list[1]-50))

        pygame.display.update()
        clock.tick(60)
      
    
loadscreen()
    
    
    