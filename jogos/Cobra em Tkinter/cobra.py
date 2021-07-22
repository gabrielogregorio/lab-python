import sys
import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

WIDTH = 300
HEIGHT = 300
DOT_SIZE = 10
DELAY = 100


class Board(Canvas):
    def __init__(self, parent):
        super().__init__(width=WIDTH, height=HEIGHT,
                         background='black', highlightthickness=0, bd=0)

        self.parent = parent
        self.ini_game()
        self.pack()
        self.count_points = 5
        self.vitoria = False

    def ini_game(self):
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.in_game = True

        self.dot_x = 100
        self.dot_y = 190

        try:
            self.ibody = Image.open('dot.png')
            self.body = ImageTk.PhotoImage(self.ibody)

            self.ibody2 = Image.open('dot2.png')
            self.body2 = ImageTk.PhotoImage(self.ibody2)

            self.ibody3 = Image.open('dot3.png')
            self.body3 = ImageTk.PhotoImage(self.ibody3)

            self.ihead = Image.open('head.png')
            self.head = ImageTk.PhotoImage(self.ihead)

            self.idot = Image.open('dot.png')
            self.dot = ImageTk.PhotoImage(self.idot)



        except IOError as e:
            print(str(e))
            sys.exit(1)

        self.focus_get()
        self.create_objects()
        self.bind_all('<Key>', self.on_key_press)
        self.after(DELAY, self.on_time)

    def create_objects(self):
        self.create_image(20, 30, image=self.dot, anchor=NW, tag='dot')
        self.create_image(50, 50, image=self.head, anchor=NW, tag='head')
        self.create_image(40, 50, image=self.body, anchor=NW, tag='body')
        self.create_image(30, 50, image=self.body2, anchor=NW, tag='body')
        self.create_image(20, 50, image=self.body3, anchor=NW, tag='body')
        self.create_image(10, 50, image=self.body2, anchor=NW, tag='body')

    def check_limit_dot(self):
        # Parar game
        if (HEIGHT * WIDTH) <= self.count_points:
            print('vitória como derrota')
            self.in_game = False
            self.vitoria = True


    def check_dot(self):
        # Checar colisão
        # Cabeça sobrepos o ponto
        dot = self.find_withtag('dot')
        head = self.find_withtag('head')

        # Retorna uma tupla da posição
        x1, y1, x2, y2 = self.bbox(head)

        # Verificar colesao
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for ovr in overlap:
            if dot[0] == ovr:
                x, y = self.coords(head)
                image = random.choice([self.body, self.body2, self.body3])
                self.create_image(x, y, image=image, anchor=NW, tag='body')
                self.count_points += 1
                print('add+1')

                self.locate_dot()


    def locate_dot(self):
        # Deletar o ponto
        dot = self.find_withtag('dot')
        self.delete(dot[0])

        # Gerar posições aleatórias
        r = random.randint(0, int(WIDTH/DOT_SIZE))
        self.dot_x = r * DOT_SIZE

        r = random.randint(0, int(HEIGHT/DOT_SIZE))
        self.dot_y = r * DOT_SIZE


        if (self.dot_x == WIDTH):
            self.dot_x = self.dot_x - DOT_SIZE

        if (self.dot_y == HEIGHT):
            self.dot_y = self.dot_y - DOT_SIZE

        print(self.dot_x, self.dot_y)


        # Criar um novo
        self.create_image(self.dot_x, self.dot_y, image=self.dot, anchor=NW, tag='dot')

    def do_move(self):
        # Retorna a tupla do corpo da cobra
        bodys = self.find_withtag('body')
        head = self.find_withtag('head')

        items = bodys + head

        k = 0
        while(k<len(items) - 1):
            c1 = self.coords(items[k])
            c2 = self.coords(items[k+1])
            self.move(items[k], c2[0]-c1[0], c2[1]-c1[1])
            k += 1

        if self.left:
            self.move(head, -DOT_SIZE, 0)

        if self.right:
            self.move(head, DOT_SIZE, 0)

        if self.up:
            self.move(head, 0, -DOT_SIZE)

        if self.down:
            self.move(head, 0, DOT_SIZE)


    def check_collisions(self):
        bodys = self.find_withtag('body')
        head = self.find_withtag('head')

        # Retorna uma tupla da posição
        x1, y1, x2, y2 = self.bbox(head)

        # Verificar colesao
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for body in bodys:
            for ovr in overlap:
                if body == ovr:
                    self.in_game = False

        if x1 < 0:
            self.move(head, WIDTH, 0)

        if x1 > WIDTH - DOT_SIZE:
            self.move(head, -WIDTH, 0)

        if y1 < 0:
            self.move(head, 0, HEIGHT)

        if y1 > HEIGHT - DOT_SIZE:
            self.move(head, 0, -HEIGHT)

    
    def on_key_press(self, e):
        key = e.keysym

        if key == 'Left' and not self.right:
            self.left = True
            self.up = False
            self.down = False
            self.right = False

        if key == 'Right' and not self.left:
            self.right = True
            self.left = False
            self.up = False
            self.down = False

        if key == 'Up' and not self.down:
            self.up = True
            self.left = False
            self.down = False
            self.right = False

        if key == 'Down' and not self.up:
            self.down = True
            self.left = False
            self.up = False
            self.right = False

    def on_time(self):
        if self.in_game:
            self.check_collisions()
            self.check_dot()
            self.check_limit_dot()
            self.do_move()
            self.after(DELAY, self.on_time)

        elif self.vitoria:
            self.vitoria_msg()

        else:
            self.game_over()


    def game_over(self):
        self.delete(ALL)
        self.create_text(
            self.winfo_width()/2,
            self.winfo_height()/2, 
            text='Game Over',
            fill="white")


    def vitoria_msg(self):
        self.delete(ALL)
        self.create_text(
            self.winfo_width()/2,
            self.winfo_height()/2, 
            text='Vitoria!',
            fill="white")


class Snake(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title('Snake')
        self.board = Board(parent)
        self.pack()

def main():
    root = Tk()
    snake = Snake(root)
    root.mainloop()

if __name__ == '__main__':
    main()
