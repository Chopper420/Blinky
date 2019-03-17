#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 08, 2019 03:00:52 AM +0200  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    
import LogicGui
from functools import partial




w = None
def create_InfoFrame(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = InfoFrame (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_InfoFrame():
    global w
    w.destroy()
    w = None

class InfoFrame:
    def create_InfoWin(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 20"
        font9 = "-family {Segoe UI} -size 20 -weight bold"

        top.geometry("1032x741+544+110")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.097, rely=0.027, relheight=0.81, relwidth=0.775)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=275)

        self.infoLabel = tk.Label(self.Frame1)
        self.infoLabel.place(relx=0.213, rely=0.033, height=91, width=425)
        self.infoLabel.configure(background="#d9d9d9")
        self.infoLabel.configure(disabledforeground="#a3a3a3")
        self.infoLabel.configure(font=font9)
        self.infoLabel.configure(foreground="#000000")
        self.infoLabel.configure(text='''Information and help''')
        self.infoLabel.configure(width=425)

        self.Contactinfo = tk.Label(self.Frame1)
        self.Contactinfo.place(relx=0.025, rely=0.533, height=51, width=242)
        self.Contactinfo.configure(background="#d9d9d9")
        self.Contactinfo.configure(disabledforeground="#a3a3a3")
        self.Contactinfo.configure(font=font10)
        self.Contactinfo.configure(foreground="#000000")
        self.Contactinfo.configure(text='''Contact:''')
        self.Contactinfo.configure(width=242)

        self.TechLabel = tk.Label(self.Frame1)
        self.TechLabel.place(relx=0.088, rely=0.667, height=51, width=289)
        self.TechLabel.configure(background="#d9d9d9")
        self.TechLabel.configure(disabledforeground="#a3a3a3")
        self.TechLabel.configure(font=font10)
        self.TechLabel.configure(foreground="#000000")
        self.TechLabel.configure(text='''Technical support:''')
        self.TechLabel.configure(width=289)

        self.rick = tk.Label(self.Frame1)
        self.rick.place(relx=0.45, rely=0.567, height=26, width=282)
        self.rick.configure(background="#d9d9d9")
        self.rick.configure(disabledforeground="#a3a3a3")
        self.rick.configure(foreground="#000000")
        self.rick.configure(text='''professor Sanchez Rick : 050-000-0000''')
        self.rick.configure(width=282)

        self.mortysanchez = tk.Label(self.Frame1)
        self.mortysanchez.place(relx=0.463, rely=0.683, height=26, width=269)
        self.mortysanchez.configure(background="#d9d9d9")
        self.mortysanchez.configure(disabledforeground="#a3a3a3")
        self.mortysanchez.configure(foreground="#000000")
        self.mortysanchez.configure(text='''Doctor Sanchez Morty : 050-000-0001''')
        self.mortysanchez.configure(width=269)

        self.infolabel = tk.Label(self.Frame1)
        self.infolabel.place(relx=0.2, rely=0.183, height=46, width=462)
        self.infolabel.configure(background="#d9d9d9")
        self.infolabel.configure(disabledforeground="#a3a3a3")
        self.infolabel.configure(foreground="#000000")
        self.infolabel.configure(text='''We started in 2016 and we're still going strong.''')
        self.infolabel.configure(width=462)

        self.blinky = tk.Label(self.Frame1)
        self.blinky.place(relx=0.238, rely=0.267, height=46, width=394)
        self.blinky.configure(background="#d9d9d9")
        self.blinky.configure(disabledforeground="#a3a3a3")
        self.blinky.configure(foreground="#000000")
        self.blinky.configure(text='''Easy to use, accurate. 
Learn why the Bllinky is the eye-tracking device of choice''')
        
        action_with_args = partial(LogicGui.LogicGui.InfoBackToMain,self,top)

        self.Back = tk.Button(self.Frame1, command = action_with_args)
        self.Back.place(relx=0.538, rely=0.833, height=83, width=196)
        self.Back.configure(activebackground="#ececec")
        self.Back.configure(activeforeground="#000000")
        self.Back.configure(background="#d9d9d9")
        self.Back.configure(disabledforeground="#a3a3a3")
        self.Back.configure(foreground="#000000")
        self.Back.configure(highlightbackground="#d9d9d9")
        self.Back.configure(highlightcolor="black")
        self.Back.configure(pady="0")
        self.Back.configure(text='''Back''')
        self.Back.configure(width=196)
        
        action_with_args = partial(LogicGui.LogicGui.FeedBackWin,self,top)

        self.feedbackbutton = tk.Button(self.Frame1, command = action_with_args)
        self.feedbackbutton.place(relx=0.113, rely=0.833, height=83, width=236)
        self.feedbackbutton.configure(activebackground="#ececec")
        self.feedbackbutton.configure(activeforeground="#000000")
        self.feedbackbutton.configure(background="#d9d9d9")
        self.feedbackbutton.configure(disabledforeground="#a3a3a3")
        self.feedbackbutton.configure(foreground="#000000")
        self.feedbackbutton.configure(highlightbackground="#d9d9d9")
        self.feedbackbutton.configure(highlightcolor="black")
        self.feedbackbutton.configure(pady="0")
        self.feedbackbutton.configure(text='''Feedback''')
        self.feedbackbutton.configure(width=236)

        self.powerlabel = tk.Label(self.Frame1)
        self.powerlabel.place(relx=0.125, rely=0.367, height=26, width=567)
        self.powerlabel.configure(background="#d9d9d9")
        self.powerlabel.configure(disabledforeground="#a3a3a3")
        self.powerlabel.configure(foreground="#000000")
        self.powerlabel.configure(text='''combines powerful processing with the worlds most advanced eye tracking platform''')





