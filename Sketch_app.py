#Modulos
import time
#Siempre es necesario este comando para iniciar la app
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter 
from kivy.uix.textinput import TextInput 

Window.size = (400, 700) #tamaño de celular


class myclock(Label):
	def update(self, *args):
		self.text = time.asctime()


class AstroApp(App):

	def build(self):
		layout = BoxLayout(orientation='vertical')

		clock1 = myclock()
		Clock.schedule_interval(clock1.update, 1)
		layout.add_widget(Label(text ="Hello! Im your new app for transients", font_size = 30) )
		layout.add_widget(clock1)
		layout.add_widget(Label(text ="Please enter your type of telescope", font_size = 30) )
		l = Label(text ="Ex: Galilean, Newtonian...", font_size = 20)
		layout.add_widget(l)
		input = TextInput(font_size = 30, size_hint_y = None, height = 70,multiline=False)
		layout.add_widget(input) 
		
		input.bind(text = l.setter('text'))  

		return layout


root = AstroApp()
root.run()

