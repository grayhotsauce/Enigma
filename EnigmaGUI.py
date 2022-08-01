import Enigma
import pygame

pygame.font.init()
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('green')
FONT = pygame.font.Font(None, 32)

num_of_tabs = 0


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.next = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = color_active if self.active else color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_TAB:
                    self.active = not self.active
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width // 2 - text.get_width() // 2), self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


#-------------------------
#
#set up the window
#


pygame.font.init()
pg = pygame.display.set_mode((850, 500))
pygame.display.set_caption("Encryption Device")
green = pygame.Color("green")
red = pygame.Color("red")
blue = pygame.Color("blue")


#------------------------
#
#Runs the GUI
#


def main():
    pg.fill((0, 0, 0))
    run = True
    eButton = Button(green, 100, 400, 200, 40, "Encrypt")
    dButton = Button(red, 500, 400, 200, 40, "Decrypt")


    def redraw_window():
        eButton.draw(pg)
        dButton.draw(pg)
        pygame.display.update()

    while run:
        redraw_window()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if eButton.isOver(mouse):
                    run = False
                    encrypt()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dButton.isOver(mouse):
                    run = False
                    decrypt()
            if event.type == pygame.MOUSEMOTION:
                if eButton.isOver(mouse):
                    eButton.color = red
                else:
                    eButton.color = green
            if event.type == pygame.MOUSEMOTION:
                if dButton.isOver(mouse):
                    dButton.color = green
                else:
                    dButton.color = red


#----------------------
#
#runs the encrypt menu
#


pygame.font.init()
encrypt_menu = pygame.display.set_mode((850, 500))
pygame.display.set_caption("Encryption Device")



def encrypt():
    encryption = ''
    text_box1 = InputBox(300, 250, 140, 32)
    rotor1 = InputBox(100, 100, 10, 50)
    rotor2 = InputBox(300, 100, 10, 50)
    rotor3 = InputBox(500, 100, 10, 50)
    inputBoxes = [text_box1, rotor1, rotor2, rotor3]

    rotor1.next = rotor2
    rotor2.next = rotor3
    rotor3.next = text_box1
    text_box1.next = rotor1

    run = True
    encrypt_button = Button(green, 500, 400, 200, 40, "Encrypt")
    exit_Button = Button(green, 100, 400, 200, 40, "Exit")
    messageButton = Button(red, 200, 300, 400, 40, encryption)

    def redraw_window():
        encrypt_button.draw(encrypt_menu)
        exit_Button.draw(encrypt_menu)
        messageButton.draw(encrypt_menu)
        pygame.display.update()

    encrypt_menu.fill((0, 0, 0))

    while run:
        mouse = pygame.mouse.get_pos()
        redraw_window()
        for event in pygame.event.get():
            # # # # # # # #
            # Handles mouse click over exit or encrypt button
            # # # # # # # #
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_Button.isOver(mouse):
                    run = False
                    main()
                if encrypt_button.isOver(mouse):
                    t1 = rotor1.text
                    t2 = rotor2.text
                    t3 = rotor3.text
                    message = text_box1.text
                    encryption = Enigma.enigmaScramble(message, int(t1), int(t2), int(t3))
                    messageButton.text = encryption
                    messageButton.draw(encrypt_menu)

            if event.type == pygame.MOUSEMOTION:
                if exit_Button.isOver(mouse):
                    exit_Button.color = red
                else:
                    exit_Button.color = green
                if encrypt_button.isOver(mouse):
                    encrypt_button.color = red
                else:
                    encrypt_button.color = green

            if event.type == pygame.QUIT:
                run = False
            for box in inputBoxes:
                box.handle_event(event)
                redraw_window()


            for box in inputBoxes:
                box.update()

            encrypt_menu.fill((0, 0, 0))
            redraw_window()

            for box in inputBoxes:
                box.draw(encrypt_menu)

            pygame.display.flip()


#---------------------------------------
#
#sets up the decrypt menu
#


pygame.font.init()
decrypt_menu = pygame.display.set_mode((850, 500))
pygame.display.set_caption("Encryption Device")


def decrypt():
    decryption = ''
    text_box1 = InputBox(300, 250, 140, 32)
    rotor1 = InputBox(100, 100, 10, 50)
    rotor2 = InputBox(300, 100, 10, 50)
    rotor3 = InputBox(500, 100, 10, 50)
    inputBoxes = [text_box1, rotor1, rotor2, rotor3]
    run = True
    decrypt_button = Button(green, 500, 400, 200, 40, "Decrypt")
    exit_Button = Button(green, 100, 400, 200, 40, "Exit")
    messageButton = Button(red, 200, 300, 400, 40, decryption)

    rotor1.next = rotor2
    rotor2.next = rotor3
    rotor3.next = text_box1
    text_box1.next = rotor1

    def redraw_window():
        decrypt_button.draw(decrypt_menu)
        exit_Button.draw(decrypt_menu)
        messageButton.draw(decrypt_menu)
        pygame.display.update()

    decrypt_menu.fill((0, 0, 0))

    while run:
        mouse = pygame.mouse.get_pos()
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_Button.isOver(mouse):
                    run = False
                    main()
                if decrypt_button.isOver(mouse):
                    t1 = rotor1.text
                    t2 = rotor2.text
                    t3 = rotor3.text
                    message = text_box1.text
                    decryption = Enigma.enigmaUnscramble(message, int(t1), int(t2), int(t3))
                    messageButton.text = decryption
                    messageButton.draw(decrypt_menu)

            if event.type == pygame.MOUSEMOTION:
                if exit_Button.isOver(mouse):
                    exit_Button.color = red
                else:
                    exit_Button.color = green
                if decrypt_button.isOver(mouse):
                    decrypt_button.color = red
                else:
                    decrypt_button.color = green

            if event.type == pygame.QUIT:
                run = False
            for box in inputBoxes:
                box.handle_event(event)

            for box in inputBoxes:
                box.update()

            decrypt_menu.fill((0, 0, 0))
            redraw_window()
            for box in inputBoxes:
                box.draw(decrypt_menu)

            pygame.display.flip()


main()
