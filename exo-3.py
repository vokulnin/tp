from tkinter import *
from threading import Thread, RLock
from random import *
from math import *
import time

color=['blue' , 'green' , 'red' , 'yellow' , 'black' , 'grey']

largeur=500
hauteur=500
taille=((largeur+hauteur)/2)/10

class main(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.fenetre=Tk()
		self.nb=0
		self.score = 0
		self.daemon=True
		self.do=True

		#texte nombre de ball
		self.nb_ball=Label(self.fenetre,text="nombre de balle: {}".format(self.nb))
		self.nb_ball.pack()
		#score
		self.n_score=Label(self.fenetre,text="score: {}".format(self.score))
		self.n_score.pack() 
		#temps
		self.temps=Label(self.fenetre,text="temps: {}".format(0))
		self.temps.pack()
		#Canvas
		self.canvas = Canvas(self.fenetre, width=largeur, height=hauteur, background='white')
		self.canvas.pack()
		#boutton quitter
		self.bouton_quitter = Button(self.fenetre, text="Quitter", command=self.close)
		self.bouton_quitter.pack(side="bottom")
		
		self.Frame_balle=Frame(self.fenetre, borderwidth=2, relief=GROOVE)
		self.Frame_balle.pack()

		#boutton ajout
		self.ajout= Button(self.Frame_balle,text="+",command=self.ajout)
		self.ajout.pack(side=LEFT)
		#boutton retirer
		self.retrait= Button(self.Frame_balle,text="-",command=self.retrait)
		self.retrait.pack(side=RIGHT)
		#boutton pause
		self.pause= Button(self.fenetre,text="pause",command=self.pause)
		self.pause.pack()
	
	def pause(self):
		if c.do:
			c.do=False
			self.pause["text"]=("play")
		else:
			c.do=True
			self.pause["text"]=("pause")


	def ajout(self):
		if self.nb<20:
			x=randint(taille,hauteur-taille)
			y=randint(taille,largeur-taille)
			col=choice(color)
			name=self.canvas.create_oval(x,y,x+taille,y+taille,fill=col)
			ball(name,x,y,col)
			self.nb+=1
			self.nb_ball["text"]=("nombre de balle: {}".format(self.nb))

	def retrait(self):
		if ball.liste!=[]:
			supp=self.canvas.find_all()
			self.canvas.delete(supp[len(supp)-1])
			ball.liste.pop(len(ball.liste)-1)
			self.nb-=1
			self.nb_ball["text"]=("nombre de balle: {}".format(self.nb))

	def close(self):
		self.do=False
		self.fenetre.quit()
		

class ball(object):
	liste=list()
	def __init__(self,name,x,y,col=choice(color)):
		ball.liste.append(self)
		self.name = name
		self.x = x
		self.y = y
		self.col=col
		self.dirx=randint(0,1)
		self.diry=randint(0,1)
		if self.dirx==0:
			self.dirx=-1
		if self.diry==0:
			self.diry=-1

	def collision(self,p):
		x=p.x-self.x
		y=p.y-self.y
		dist=x*x+y*y
		if (sqrt(dist))<=(taille):
			fenetre.nb-=2
			fenetre.nb_ball["text"]=("nombre de balle: {}".format(fenetre.nb))
			fenetre.score+=2
			fenetre.n_score["text"]=("score: {}".format(fenetre.score))
			fenetre.canvas.delete(self.name)
			ball.liste.remove(self)
			fenetre.canvas.delete(p.name)
			ball.liste.remove(p)
		
		
		
class calcul(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.daemon=True
		self.do=True
		self.temps=0
		self.temps2=0
	def run(self):
		while 1:
			if self.do:
				fenetre.temps["text"]=("temps: {}".format(self.temps))
				self.temps=int(time.clock())-self.temps2
				for i in ball.liste:
					fenetre.canvas.coords(i.name,i.x+i.dirx,i.y+i.diry,i.x+i.dirx+taille,i.y+i.diry+taille)
					i.x+=i.dirx
					i.y+=i.diry
					if i.x<=0 or i.x>=largeur-taille:
						i.dirx=-i.dirx
					if i.y<=0 or i.y>=hauteur-taille:
						i.diry=-i.diry
					for element in ball.liste:
						if element!=i:
							element.collision(i)
			else:
				self.temps2=int(time.clock())-self.temps
			time.sleep(0.01)


fenetre=main()
c=calcul()

fenetre.start()
c.start()
fenetre.fenetre.mainloop()
fenetre.do=False
