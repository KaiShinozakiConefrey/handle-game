# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:24:19 2022

@author: kaish
"""

import tkinter as tk
from tkinter import ttk
import random

from PIL import ImageTk, Image
import glob
    
root = tk.Tk()
root['bg'] = 'black'
root.geometry('1000x900')

answers = set(line.strip() for line in open('answers.txt'))
dictionary = set(line.strip() for line in open('dictionary.txt'))


def chooseword():
    fiveset = []
    for i in answers:
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
        
        self.recordFrameList = []
        self.recordLabelList = []
        
        self.image_list = []
        self.ref_list = []
        
        for filename in glob.glob('Letters/*.png'):
            self.image_list.append(filename)
        
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
                    width = 70,
                    height = 70,
                    bg = 'dimgray'
                )
                self.frame.pack_propagate(False)
                self.innerframe = tk.Frame(
                    self.frame,
                    #relief=tk.RAISED,
                    #borderwidth=1,
                    width = 70,
                    height = 70,
                    bg = 'black'
                )
                self.frameList.append(self.innerframe)
                
                self.innerframe.pack()
                self.innerframe.pack_propagate(False)
                
                self.frame.grid(row=i, column=j, padx = 3, pady = 3)
                self.letterList.append(tk.StringVar())
                self.letterList[-1].set("")
                
                
                label = ttk.Label(
                        master=self.frameList[-1], 
                        textvariable = self.letterList[-1],
                        foreground = 'white', 
                        background = 'black',
                        #image = render,
                        font = ("Karnak Condensed", 24),
                        )
                
                self.labelList.append(label)
                label.pack()
                #frame.pack()
        
        self.tryFrame.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        def tryGuess():
            self.guess = self.entry.get().upper()

            if(self.guess.lower() in dictionary or self.guess.lower() in answers):
                
                for i in range(5):
                    self.letterList[self.currentTry * 5 + i].set(self.guess[i])
                    
                    img = Image.open(self.image_list[ord(self.guess[i]) - 91])
                    img = img.resize((60, 60), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(img)
                    
                    self.labelList[self.currentTry * 5 + i].configure(image = render)
                    self.labelList[self.currentTry * 5 + i].image = render
                    
                    color = 'dimgray'
                    if(self.guess[i].upper() in word.upper()):
                        color = "gold"
                    if(self.guess[i].upper() == word[i].upper()):
                        color = "limegreen"
                    
                    self.frameList[self.currentTry * 5 + i]['bg'] = color
                    self.frameList[self.currentTry * 5 + i].master['bg'] = color
                    self.labelList[self.currentTry * 5 + i]['background'] = color
                    
                    if color == 'dimgray':
                        color = 'red'
                        
                    self.recordFrameList[ord(self.guess[i]) - 91]['bg'] = color
                    
                self.currentTry += 1
            self.entry.delete(0, 5)
            
        self.checkButton = tk.Button(text = "Check", command = tryGuess)
        self.checkButton.pack()
        
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.letters = self.letters.upper()
        self.recordFrame = tk.Frame(
                root,
                bg = 'black'
                )
        
        for j in range(26):
            self.frame = tk.Frame(
                self.recordFrame,
                borderwidth=3,
                width = 70,
                height = 70,
                bg = 'dimgray'
            )
            self.recordFrameList.append(self.frame)
            
            self.frame.pack_propagate(False)
            self.innerframe = tk.Frame(
                self.frame,
                #relief=tk.RAISED,
                #borderwidth=1,
                width = 70,
                height = 70,
                bg = 'black'
            )
            
            self.innerframe.pack()
            self.innerframe.pack_propagate(False)
            
            col = j
            rw = 0
            if(col >= 9):
               col -= 9
               rw += 1
            if(col >= 9):
                col -= 9
                rw += 1
            
                
            self.frame.grid(row=rw, column=col, padx = 3, pady = 3)
            
            img = Image.open(self.image_list[ord(self.letters[j]) - 91])
            img = img.resize((60, 60), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(img)
            self.ref_list.append(render)
            
            label = ttk.Label(
                    master=self.innerframe, 
                    foreground = 'white', 
                    background = 'black',
                    #image = self.ref_list[-1],
                    )
            label.configure(image = self.ref_list[-1])
            label.image = self.ref_list[-1]
            
            self.recordLabelList.append(label)
            label.pack()
            #frame.pack()
        
        self.recordFrame.pack()
        
        
        
        
        

root.title("Test application")

word = chooseword()
gui = game_interface(root, word)
root.mainloop()