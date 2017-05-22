#! /usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

from random import SystemRandom



class PasswordGen(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self, title="Password Generator")
		self.characters = [
						"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", 
						"S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", 
						"V", "B", "N", "M", "0", "1", "2", "3", "4", "5", "6", 
						"7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", 
						"o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", 
						"z", "x", "c", "v", "b", "n", "m"
						]

		self.special_characters = ["#", "#", "@", "@", "$", "$", "!", "!", "%", "%", "?", "?", "&", "&"]

		self._sysrand = SystemRandom()

		self.specialChars = False
		self.entryContent = ""

		grid = gtk.Grid()
		self.add(grid)

		self.lenLabel = gtk.Label("Password length: ")
		self.buttonLabel = gtk.Label("   Include special characters  ")


		self.generateButton = gtk.Button(label="Generate")
		self.checkButton = gtk.CheckButton()

		self.entry = gtk.Entry()
		self.entry.set_text("16")

		self.entryOut = gtk.Entry()
		self.entryOut.set_editable(False)

		# To add an image in the empty space
		# image = gtk.Image()
		# image.set_from_file("")

		self.generateButton.connect("clicked", self.brain)
		self.checkButton.connect("toggled", self.onButtonToggled)


		grid.add(self.lenLabel)
		grid.attach_next_to(self.entry, self.lenLabel, gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(self.generateButton, self.entry, gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(self.buttonLabel, self.generateButton, gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(self.checkButton, self.buttonLabel, gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(self.entryOut, self.lenLabel, gtk.PositionType.BOTTOM, 5, 1)
		# grid.attach_next_to(image, self.entryOut, gtk.PositionType.BOTTOM, 5, 1)



	def brain (self, widget):

		def generate (array):
			char_list = []
			try:
				for x in range(int(self.entry.get_text())):
					char_list.append(self._sysrand.choice(array))
			except ValueError:
				pass

			password = "".join(char_list)
			self.entryOut.set_text(password)


		if self.specialChars:
			listUsed = self.characters + self.special_characters
		else:
			listUsed = self.characters

		generate(listUsed)

	
	def onButtonToggled (self, button):
		self.specialChars ^= True




window = PasswordGen()
window.set_default_size(600, 300)
window.connect("delete-event", gtk.main_quit)
window.show_all()
gtk.main()
