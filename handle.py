# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:24:19 2022

@author: kaish
"""

import tkinter as tk
from tkinter import ttk
import random

from english_words import english_words_lower_set

from PIL import Image
import glob

image_list = []
for filename in glob.glob('Letters/*.png'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
    
root = tk.Tk()
root['bg'] = 'black'
root.geometry('800x800')

def chooseword():
    fiveset = []
    for i in english_words_lower_set:
        if(len(i) == 5):
            fiveset.append(i)
    choice = random.choice(fiveset)
    print(choice)
    return choice

class game_interface:
    def __init__(self, root, word):
        self.currentTry = 0
        self.letterList = []
        self.labelList = []
        self.frameList = []
        
        self.label = ttk.Label(
                root, 
                text = "HANDLE",
                font = ("Karnak Condensed", 30),
                foreground = 'white',
                background = 'black',
                padding = 50
                )
        self.label.pack()
        
        self.tryFrame = tk.Frame(
                root,
                bg = 'black'
                )
        
        for i in range(6):
            for j in range(5):
                self.frame = tk.Frame(
                    self.tryFrame,
                    borderwidth=3,
                    width = 50,
                    height = 50,
                    bg = 'dimgray'
                )
                self.frame.pack_propagate(False)
                self.innerframe = tk.Frame(
                    self.frame,
                    #relief=tk.RAISED,
                    #borderwidth=1,
                    width = 45,
                    height = 45,
                    bg = 'black'
                )
                self.frameList.append(self.innerframe)
                
                self.innerframe.pack()
                self.innerframe.pack_propagate(False)
                
                self.frame.grid(row=i, column=j, padx = 3, pady = 3)
                self.letterList.append(tk.StringVar())
                self.letterList[-1].set("")
                
                self.label = ttk.Label(
                        master=self.frameList[-1], 
                        textvariable = self.letterList[-1],
                        foreground = 'white', 
                        background = 'black',
                        image = image_list[0],
                        font = ("Karnak Condensed", 24),
                        )
                self.labelList.append(self.label)
                self.label.pack()
                #frame.pack()
        
        self.tryFrame.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        def tryGuess():
            self.guess = self.entry.get().upper()
            if(self.guess.lower() in english_words_lower_set):
                
                for i in range(5):
                    self.letterList[self.currentTry * 5 + i].set(self.guess[i])
                    
                    color = 'dimgray'
                    if(self.guess[i].upper() in word.upper()):
                        color = "gold"
                    if(self.guess[i].upper() == word[i].upper()):
                        color = "limegreen"
                    
                    self.frameList[self.currentTry * 5 + i]['bg'] = color
                    self.frameList[self.currentTry * 5 + i].master['bg'] = color
                    self.labelList[self.currentTry * 5 + i]['background'] = color
                self.currentTry += 1
            self.entry.delete(0, 5)
        
        self.checkButton = tk.Button(text = "Check", command = tryGuess)
        self.checkButton.pack()
        

root.title("Test application")

word = chooseword()
gui = game_interface(root, word)
root.mainloop()