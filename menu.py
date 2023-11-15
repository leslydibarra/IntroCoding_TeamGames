import pygame
import sys


class Button(): #sets the button and auto updates it 
	def __init__(self, image, pos, text_input, font, base_color, hovering_color): #intializes the button
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

pygame.init()

SCREEN = pygame.display.set_mode((1200,750))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/purpleBackgroundResized.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def connect4(): # what happens when you press the play button
    while True:

        import connect4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu()
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
    
def hangman():
    while True:
        import hangman

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               main_menu()
               pygame.quit()
               sys.exit()

        pygame.display.update()

def snake():
    while True:
           import snake

           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu()
                    pygame.quit()
                    sys.exit()

           pygame.display.update()

           
     
def main_menu(): #main screen
     SCREEN = pygame.display.set_mode((1200,800))
     pygame.display.set_caption("Menu")

     while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(90).render("MAIN MENU", True, "#ed5fa1")
        MENU_RECT = MENU_TEXT.get_rect(center=(600, 100))

        CONNECT4_BUTTON = Button(image=pygame.image.load("assets/purpleCircle.png"), pos=(600, 350), 
                            text_input="Connect4", font=get_font(50), base_color="#d7fcd4", hovering_color="Purple")
        HANGMAN_BUTTON = Button(image=pygame.image.load("assets/greenCircle.png"), pos=(1000, 500), 
                            text_input="Hangman", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")
        SNAKE_BUTTON = Button(image=pygame.image.load("assets/pinkCircle.png"), pos=(200, 500), 
                            text_input="Snake", font=get_font(50), base_color="#d7fcd4", hovering_color="Pink")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/redCircle.png"), pos=(600, 700), 
                            text_input="Quit", font=get_font(50), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CONNECT4_BUTTON, HANGMAN_BUTTON, SNAKE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONNECT4_BUTTON.checkForInput(MENU_MOUSE_POS):
                    connect4()
                    pygame.quit()
                    sys.exit()
                if HANGMAN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    hangman()
                    pygame.quit()
                    sys.exit()
                if SNAKE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    snake()
                    pygame.quit()
                    sys.exit()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()