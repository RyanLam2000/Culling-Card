class Text:
#     render_text("Full Screen",width/2,height/2,screen,font,white,black)
    def __init__(self,text,x,y,screen,font,c1,c2):
        self.text = text
        self.c1 = c1
        self.c2 = c2
        self.screen = screen
        self.x = x 
        self.y = y 
        self.font = font
        self.rect = None
        self.update(screen)
    
    def update(self,screen):
        
        width = screen.get_width()/2
        height = screen.get_height()/2
        text = self.font.render(self.text,True,self.c1,self.c2)
        text_rect = text.get_rect(center=(self.x+width,self.y+height))
        screen.blit(text,text_rect)
        self.rect=text_rect
    