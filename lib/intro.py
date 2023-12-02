from time import sleep
from os import system, name

class Intro:
	clear_screen = "'clear'" if name == "posix" else "'cls'"

	def __init__(self, string, color, end='\033[m'):
		self.string = string
		self.color = color
		self.end = end

	def show_logo(self, string, color='', end='\033[m',  secondary_color="\033[36m"):
		print(f"""{color}
\t\t                    &
\t\t                    &
\t\t           &        &        &
\t\t            &               &
\t\t    &&         &&&&   &&&&         &&
\t\t       &&   &&      &&&&&  &&   &&
\t\t           &              &  &
\t\t          &&               & &&
\t\t          &&                 &&
\t\t           &                 &          {end}{string}{color}
\t\t            &&             &&
\t\t              &&         &&
\t\t               &         &
\t\t               {end}{secondary_color}
\t\t               &&&&&&&&&&&
\t\t                &&&&&&&&&
\t\t{end}""")
	def writing_logo(self):
		for i in range(0, len(self.string)):
			self.show_logo(self.string[0:i+1])
			sleep(0.1) if self.string[i] != ' ' else sleep(0.35)
			system(self.clear_screen)
		self.show_logo(self.string, self.color)
		sleep(1.5)
	def erasing_logo(self):
		for i in range(len(self.string)-1, self.string.index(' '), -1):
    			self.show_logo(self.string[0:i], self.color)
    			sleep(0.1)
    			system(self.clear_screen)
		for i in range(self.string.index(' '), 0, -1):
    			self.show_logo(self.string[0:i], self.color)
    			sleep(0.35)
    			system(self.clear_screen)

Boot = Intro("PROJECT GERENTIA", "\033[1;33m", "\033[m")
Boot.writing_logo()
Boot.erasing_logo()


