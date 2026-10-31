## Interface of e-drums
import pygame as pg
import sys
from button import Button
# pygame setup
pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Mayhem Drums")

BG = pg.image.load('assets/images/background/menu1.jpg')
BG = pg.transform.scale(BG,(1280,720))

running = True
clock = pg.time.Clock()

# Cursor
stick = pg.image.load('assets/images/cursors/drumsticks1.png')
stick = pg.transform.scale(stick,(64,64))
stick_hit = pg.image.load('assets/images/cursors/drumstick_hit.png') 
stick_hit = pg.transform.flip(stick_hit, True, False)
stick_hit = pg.transform.scale(stick_hit,(32,32))

stick = pg.cursors.Cursor((32,32), stick)
hit = pg.cursors.Cursor((32, 32), stick_hit)

cursors = [stick, hit]
cursor_index = 0
pg.mouse.set_cursor(cursors[cursor_index])

def get_font(index_f,size):
    title_font = 'assets/fonts/ROUGD___.TTF'
    menu_font = 'assets/fonts/DeterminationMonoWeb.woff'
    font = [title_font, menu_font]
    return pg.font.Font(font[index_f],size)
pg.font.init()

scene = [0] 

def play():
    while True:

            PLAY_MOUSE_POS = pg.mouse.get_pos()
        
            screen.fill('black')


            PLAY_TEXT = get_font(1,32).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            screen.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(1,24), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        scene == 0
                        main_menu()

            pg.display.update()

    
def options():
    while True:
        
            OPTIONS_MOUSE_POS = pg.mouse.get_pos()

            screen.fill('white')

            OPTIONS_TEXT = get_font(1,32).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(1,24), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(screen)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            pg.display.update()


def main_menu():

    while running:
        clock.tick(60)
        screen.blit(BG,(0,0))

        menu_mouse_pos = pg.mouse.get_pos()

        menu_text = get_font(0,64).render("MAYHEM DRUMS",True, 'White')
        menu_rect = menu_text.get_rect(center=(640, 100))

        textbox = pg.image.load("assets/images/menu/textbox.png")
        textbox = pg.transform.scale_by(textbox,(0.75, 0.5))

        play_button = Button(image=textbox, pos=(640, 250), 
                            text_input="PLAY", font=get_font(1,40), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=textbox, pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(1,40), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=textbox, pos=(640, 550), 
                            text_input="QUIT", font=get_font(1,40), base_color="#d7fcd4", hovering_color="Red")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        
        for event in pg.event.get():
                            
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:

                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pg.quit()
                    sys.exit()
            

        pg.display.update()

main_menu()