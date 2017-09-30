# Created by: Peter Zhu
# Created on: 15-sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-04
# This program displays Hello, program, but with 3 buttons

import ui

def english_touch_up_inside(sender):
	#displays the English version
	view['hello_world_label'].text = ('Hello, World!')
	
def french_touch_up_inside(sender):
	#displays the French version
	view['hello_world_label'].text = ('Bonjour le monde!')
	
def spanish_touch_up_inside(sender):
	#displays the spanish version
	view['hello_world_label'].text = ('Hola Mundo!')

view = ui.load_view()
view.present('sheet')
