#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#    Mar 15, 2019 04:02:57 AM +0200  platform: Windows NT

import sys
import BlinkyDataBaseManagment

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


import os.path
from functools import partial
import LogicGui
import BlinkyDataBaseManagment

w = None
def create_UserPanel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = UserPanel(w)
    init(w, top, *args, **kwargs)
    return(w, top)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def set_Tk_var():
    global combobox
    combobox = tk.StringVar()

def destroy_UserPanel():
    global w
    w.destroy()
    w = None

class UserPanel:

    def getChangeList(self):
        self.ChangeList.append(self.picIDcomboBox.get())
        self.ChangeList.append(self.NewPicsBox.get())

    def create_UserPanelWin(self,UserID, PicAndPharases, top=None):
        self.UserID = UserID
        self.ChangeList = {}
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        top.geometry("1200x943+356+22")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.LoginFrame = tk.Frame(top)
        self.LoginFrame.place(relx=0.1, rely=0.021, relheight=0.954
                , relwidth=0.833)
        self.LoginFrame.configure(relief='groove')
        self.LoginFrame.configure(borderwidth="2")
        self.LoginFrame.configure(relief='groove')
        self.LoginFrame.configure(background="#d9d9d9")
        self.LoginFrame.configure(highlightbackground="#d9d9d9")
        self.LoginFrame.configure(highlightcolor="black")
        self.LoginFrame.configure(width=505)

        action_with_args = partial(LogicGui.LogicGui.LogoutfromUser, self, top)

        self.Logout = tk.Button(self.LoginFrame,command=action_with_args)
        self.Logout.place(relx=0.89, rely=0.022, height=33, width=59)
        self.Logout.configure(activebackground="#ececec")
        self.Logout.configure(activeforeground="#000000")
        self.Logout.configure(background="#d9d9d9")
        self.Logout.configure(disabledforeground="#a3a3a3")
        self.Logout.configure(foreground="#000000")
        self.Logout.configure(highlightbackground="#d9d9d9")
        self.Logout.configure(highlightcolor="black")
        self.Logout.configure(pady="0")
        self.Logout.configure(text='''Logout''')

        self.SendMsg = tk.Button(self.LoginFrame)
        self.SendMsg.place(relx=0.03, rely=0.022, height=33, width=177)
        self.SendMsg.configure(activebackground="#ececec")
        self.SendMsg.configure(activeforeground="#000000")
        self.SendMsg.configure(background="#d9d9d9")
        self.SendMsg.configure(disabledforeground="#a3a3a3")
        self.SendMsg.configure(foreground="#000000")
        self.SendMsg.configure(highlightbackground="#d9d9d9")
        self.SendMsg.configure(highlightcolor="black")
        self.SendMsg.configure(pady="0")
        self.SendMsg.configure(text='''Send message to mentor''')

        self.medicalORdiet = ttk.Entry(self.LoginFrame)
        self.medicalORdiet.place(relx=0.26, rely=0.031, relheight=0.029
                , relwidth=0.166)
        self.medicalORdiet.configure(takefocus="")
        self.medicalORdiet.configure(cursor="ibeam")

        action_with_args = partial(BlinkyDataBaseManagment.updateMedical, self.UserID,self.ChangeList)

        self.medicalButton = tk.Button(self.LoginFrame,command=action_with_args)
        self.medicalButton.place(relx=0.57, rely=0.022, height=33, width=110)
        self.medicalButton.configure(activebackground="#ececec")
        self.medicalButton.configure(activeforeground="#000000")
        self.medicalButton.configure(background="#d9d9d9")
        self.medicalButton.configure(disabledforeground="#a3a3a3")
        self.medicalButton.configure(foreground="#000000")
        self.medicalButton.configure(highlightbackground="#d9d9d9")
        self.medicalButton.configure(highlightcolor="black")
        self.medicalButton.configure(pady="0")
        self.medicalButton.configure(text='''Add medical''')

        action_with_args = partial(BlinkyDataBaseManagment.updateDiet, self.UserID, self.ChangeList)

        self.dietButton = tk.Button(self.LoginFrame,command=action_with_args)
        self.dietButton.place(relx=0.45, rely=0.022, height=33, width=110)
        self.dietButton.configure(activebackground="#ececec")
        self.dietButton.configure(activeforeground="#000000")
        self.dietButton.configure(background="#d9d9d9")
        self.dietButton.configure(disabledforeground="#a3a3a3")
        self.dietButton.configure(foreground="#000000")
        self.dietButton.configure(highlightbackground="#d9d9d9")
        self.dietButton.configure(highlightcolor="black")
        self.dietButton.configure(pady="0")
        self.dietButton.configure(text='''Add diet''')

        self.Info = tk.Button(self.LoginFrame)
        self.Info.place(relx=0.7, rely=0.022, height=33, width=155)
        self.Info.configure(activebackground="#ececec")
        self.Info.configure(activeforeground="#000000")
        self.Info.configure(background="#d9d9d9")
        self.Info.configure(disabledforeground="#a3a3a3")
        self.Info.configure(foreground="#000000")
        self.Info.configure(highlightbackground="#d9d9d9")
        self.Info.configure(highlightcolor="black")
        self.Info.configure(pady="0")
        self.Info.configure(text='''information and Help''')

        self.pic1button = tk.Button(self.LoginFrame)
        self.pic1button.place(relx=0.06, rely=0.356, height=156, width=156)
        self.pic1button.configure(activebackground="#ececec")
        self.pic1button.configure(activeforeground="#000000")
        self.pic1button.configure(background="#d9d9d9")
        self.pic1button.configure(disabledforeground="#a3a3a3")
        self.pic1button.configure(foreground="#000000")
        self.pic1button.configure(highlightbackground="#d9d9d9")
        self.pic1button.configure(highlightcolor="black")
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        photo_location = os.path.join(prog_location, PicAndPharases["pic1button"])
        self._img0 = tk.PhotoImage(file=photo_location)
        self.pic1button.configure(image=self._img0)
        self.pic1button.configure(pady="0")
        self.pic1button.configure(text='''pic1button''')

        self.pic2button = tk.Button(self.LoginFrame)
        self.pic2button.place(relx=0.29, rely=0.356, height=156, width=156)
        self.pic2button.configure(activebackground="#ececec")
        self.pic2button.configure(activeforeground="#000000")
        self.pic2button.configure(background="#d9d9d9")
        self.pic2button.configure(disabledforeground="#a3a3a3")
        self.pic2button.configure(foreground="#000000")
        self.pic2button.configure(highlightbackground="#d9d9d9")
        self.pic2button.configure(highlightcolor="black")
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        photo_location = os.path.join(prog_location,PicAndPharases["pic2button"])
        self._img1 = tk.PhotoImage(file=photo_location)
        self.pic2button.configure(image=self._img1)
        self.pic2button.configure(pady="0")
        self.pic2button.configure(text='''pic2button''')

        self.pic3button = tk.Button(self.LoginFrame)
        self.pic3button.place(relx=0.51, rely=0.356, height=156, width=156)
        self.pic3button.configure(activebackground="#ececec")
        self.pic3button.configure(activeforeground="#000000")
        self.pic3button.configure(background="#d9d9d9")
        self.pic3button.configure(disabledforeground="#a3a3a3")
        self.pic3button.configure(foreground="#000000")
        self.pic3button.configure(highlightbackground="#d9d9d9")
        self.pic3button.configure(highlightcolor="black")
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        photo_location = os.path.join(prog_location,PicAndPharases["pic3button"])
        self._img2 = tk.PhotoImage(file=photo_location)
        self.pic3button.configure(image=self._img2)
        self.pic3button.configure(pady="0")
        self.pic3button.configure(text='''pic3button''')

        self.ImgLabel = tk.Label(self.LoginFrame)
        self.ImgLabel.place(relx=0.03, rely=0.267, height=37, width=92)
        self.ImgLabel.configure(activebackground="#f9f9f9")
        self.ImgLabel.configure(activeforeground="black")
        self.ImgLabel.configure(background="#d9d9d9")
        self.ImgLabel.configure(disabledforeground="#a3a3a3")
        self.ImgLabel.configure(font="-family {Segoe UI} -size 14")
        self.ImgLabel.configure(foreground="#000000")
        self.ImgLabel.configure(highlightbackground="#d9d9d9")
        self.ImgLabel.configure(highlightcolor="black")
        self.ImgLabel.configure(text='''Pictures:''')

        self.SentenceLabel = tk.Label(self.LoginFrame)
        self.SentenceLabel.place(relx=0.03, rely=0.6, height=37, width=89)
        self.SentenceLabel.configure(activebackground="#f9f9f9")
        self.SentenceLabel.configure(activeforeground="black")
        self.SentenceLabel.configure(background="#d9d9d9")
        self.SentenceLabel.configure(disabledforeground="#a3a3a3")
        self.SentenceLabel.configure(font="-family {Segoe UI} -size 14")
        self.SentenceLabel.configure(foreground="#000000")
        self.SentenceLabel.configure(highlightbackground="#d9d9d9")
        self.SentenceLabel.configure(highlightcolor="black")
        self.SentenceLabel.configure(text='''Phrases:''')

        self.Phrase1Button = tk.Button(self.LoginFrame)
        self.Phrase1Button.place(relx=0.16, rely=0.656, height=93, width=168)
        self.Phrase1Button.configure(activebackground="#ececec")
        self.Phrase1Button.configure(activeforeground="#000000")
        self.Phrase1Button.configure(background="#d9d9d9")
        self.Phrase1Button.configure(disabledforeground="#a3a3a3")
        self.Phrase1Button.configure(foreground="#000000")
        self.Phrase1Button.configure(highlightbackground="#d9d9d9")
        self.Phrase1Button.configure(highlightcolor="black")
        self.Phrase1Button.configure(pady="0")
        self.Phrase1Button.configure(text=PicAndPharases["Phrase1Button"])

        self.Phrase2Button = tk.Button(self.LoginFrame)
        self.Phrase2Button.place(relx=0.67, rely=0.656, height=83, width=176)
        self.Phrase2Button.configure(activebackground="#ececec")
        self.Phrase2Button.configure(activeforeground="#000000")
        self.Phrase2Button.configure(background="#d9d9d9")
        self.Phrase2Button.configure(disabledforeground="#a3a3a3")
        self.Phrase2Button.configure(foreground="#000000")
        self.Phrase2Button.configure(highlightbackground="#d9d9d9")
        self.Phrase2Button.configure(highlightcolor="black")
        self.Phrase2Button.configure(pady="0")
        self.Phrase2Button.configure(text=PicAndPharases["Phrase2Button"])

        self.Phrase3Button = tk.Button(self.LoginFrame)
        self.Phrase3Button.place(relx=0.17, rely=0.8, height=83, width=146)
        self.Phrase3Button.configure(activebackground="#ececec")
        self.Phrase3Button.configure(activeforeground="#000000")
        self.Phrase3Button.configure(background="#d9d9d9")
        self.Phrase3Button.configure(disabledforeground="#a3a3a3")
        self.Phrase3Button.configure(foreground="#000000")
        self.Phrase3Button.configure(highlightbackground="#d9d9d9")
        self.Phrase3Button.configure(highlightcolor="black")
        self.Phrase3Button.configure(pady="0")
        self.Phrase3Button.configure(text=PicAndPharases["Phrase3Button"])

        self.Phrase4Button = tk.Button(self.LoginFrame)
        self.Phrase4Button.place(relx=0.68, rely=0.778, height=93, width=166)
        self.Phrase4Button.configure(activebackground="#ececec")
        self.Phrase4Button.configure(activeforeground="#000000")
        self.Phrase4Button.configure(background="#d9d9d9")
        self.Phrase4Button.configure(disabledforeground="#a3a3a3")
        self.Phrase4Button.configure(foreground="#000000")
        self.Phrase4Button.configure(highlightbackground="#d9d9d9")
        self.Phrase4Button.configure(highlightcolor="black")
        self.Phrase4Button.configure(pady="0")
        self.Phrase4Button.configure(text=PicAndPharases["Phrase4Button"])

        self.pic4button = tk.Button(self.LoginFrame)
        self.pic4button.place(relx=0.74, rely=0.356, height=156, width=156)
        self.pic4button.configure(activebackground="#ececec")
        self.pic4button.configure(activeforeground="#000000")
        self.pic4button.configure(background="#d9d9d9")
        self.pic4button.configure(disabledforeground="#a3a3a3")
        self.pic4button.configure(foreground="#000000")
        self.pic4button.configure(highlightbackground="#d9d9d9")
        self.pic4button.configure(highlightcolor="black")
        prog_call = sys.argv[0]
        prog_location = os.path.split(prog_call)[0]
        photo_location = os.path.join(prog_location,PicAndPharases["pic4button"])
        self._img3 = tk.PhotoImage(file=photo_location)
        self.pic4button.configure(image=self._img3)
        self.pic4button.configure(pady="0")
        self.pic4button.configure(text='''pic4button''')

        self.ChangePicLabel = tk.Label(self.LoginFrame)
        self.ChangePicLabel.place(relx=0.21, rely=0.122, height=36, width=162)
        self.ChangePicLabel.configure(background="#d9d9d9")
        self.ChangePicLabel.configure(disabledforeground="#a3a3a3")
        self.ChangePicLabel.configure(font=font9)
        self.ChangePicLabel.configure(foreground="#000000")
        self.ChangePicLabel.configure(text='''Change pictures:''')
        self.ChangePicLabel.configure(width=162)

        self.ChangePhraseLabel = tk.Label(self.LoginFrame)
        self.ChangePhraseLabel.place(relx=0.21, rely=0.2, height=36, width=172)
        self.ChangePhraseLabel.configure(background="#d9d9d9")
        self.ChangePhraseLabel.configure(disabledforeground="#a3a3a3")
        self.ChangePhraseLabel.configure(font=font9)
        self.ChangePhraseLabel.configure(foreground="#000000")
        self.ChangePhraseLabel.configure(text='''Change Phrases:''')
        self.ChangePhraseLabel.configure(width=172)

        self.box_value = tk.StringVar()
        self.picIDcomboBox = ttk.Combobox(self.LoginFrame, textvariable=self.box_value)
        self.picIDcomboBox.place(relx=0.4, rely=0.133, relheight=0.029
                                 , relwidth=0.187)
        self.picIDcomboBox.configure(textvariable=set_Tk_var)
        self.picIDcomboBox.configure(takefocus="")
        self.picIDcomboBox['values'] = ("1", "2", "3", "4")

        self.box_value2 = tk.StringVar()
        self.PhraseIDCombobox = ttk.Combobox(self.LoginFrame, textvariable=self.box_value2)
        self.PhraseIDCombobox.place(relx=0.4, rely=0.2, relheight=0.029
                                    , relwidth=0.187)
        self.PhraseIDCombobox.configure(textvariable=set_Tk_var)
        self.PhraseIDCombobox.configure(takefocus="")
        self.PhraseIDCombobox['values'] = ("1", "2", "3", "4")

        self.box_value1 = tk.StringVar()
        self.NewPicsBox = ttk.Combobox(self.LoginFrame, textvariable=self.box_value1)
        self.NewPicsBox.place(relx=0.61, rely=0.133, relheight=0.029
                              , relwidth=0.187)
        self.NewPicsBox.configure(textvariable=set_Tk_var)
        self.NewPicsBox.configure(takefocus="")
        self.NewPicsBox['values'] = BlinkyDataBaseManagment.loadAllPic(self.UserID)

        action_with_args = partial(BlinkyDataBaseManagment.UpdateChosenPic, self.UserID,self.ChangeList,top)

        self.ChangePicButton = tk.Button(self.LoginFrame, command=action_with_args)
        self.ChangePicButton.place(relx=0.85, rely=0.122, height=63, width=106)
        self.ChangePicButton.configure(activebackground="#ececec")
        self.ChangePicButton.configure(activeforeground="#000000")
        self.ChangePicButton.configure(background="#d9d9d9")
        self.ChangePicButton.configure(disabledforeground="#a3a3a3")
        self.ChangePicButton.configure(foreground="#000000")
        self.ChangePicButton.configure(highlightbackground="#d9d9d9")
        self.ChangePicButton.configure(highlightcolor="black")
        self.ChangePicButton.configure(pady="0")
        self.ChangePicButton.configure(text='''Change''')
        self.ChangePicButton.configure(width=106)

        action_with_args = partial(BlinkyDataBaseManagment.UpdateChosenPhrase, self.UserID, self.ChangeList, top)
        self.ChangePhraseButton = tk.Button(self.LoginFrame, command=action_with_args)
        self.ChangePhraseButton.place(relx=0.85, rely=0.211, height=63
                , width=106)
        self.ChangePhraseButton.configure(activebackground="#ececec")
        self.ChangePhraseButton.configure(activeforeground="#000000")
        self.ChangePhraseButton.configure(background="#d9d9d9")
        self.ChangePhraseButton.configure(disabledforeground="#a3a3a3")
        self.ChangePhraseButton.configure(foreground="#000000")
        self.ChangePhraseButton.configure(highlightbackground="#d9d9d9")
        self.ChangePhraseButton.configure(highlightcolor="black")
        self.ChangePhraseButton.configure(pady="0")
        self.ChangePhraseButton.configure(text='''Change''')
        self.ChangePhraseButton.configure(width=106)

        self.box_value3 = tk.StringVar()
        self.NewPhrasesBox = ttk.Combobox(self.LoginFrame, textvariable=self.box_value3)
        self.NewPhrasesBox.place(relx=0.61, rely=0.2, relheight=0.029
                , relwidth=0.187)
        self.NewPhrasesBox.configure(textvariable=set_Tk_var)
        self.NewPhrasesBox.configure(takefocus="")
        self.NewPhrasesBox['values'] = BlinkyDataBaseManagment.loadAllPhrases(self.UserID)

        self.NewPhraseEntry = ttk.Entry(self.LoginFrame)
        self.NewPhraseEntry.place(relx=0.61, rely=0.278, relheight=0.029
                , relwidth=0.166)
        self.NewPhraseEntry.configure(takefocus="")
        self.NewPhraseEntry.configure(cursor="ibeam")

        self.picPhraseIDLabel = tk.Label(self.LoginFrame)
        self.picPhraseIDLabel.place(relx=0.41, rely=0.089, height=34, width=49)
        self.picPhraseIDLabel.configure(background="#d9d9d9")
        self.picPhraseIDLabel.configure(disabledforeground="#a3a3a3")
        self.picPhraseIDLabel.configure(font=font9)
        self.picPhraseIDLabel.configure(foreground="#000000")
        self.picPhraseIDLabel.configure(text='''ID:''')
        self.picPhraseIDLabel.configure(width=49)

        self.ChoosepicPhraseLabel = tk.Label(self.LoginFrame)
        self.ChoosepicPhraseLabel.place(relx=0.61, rely=0.089, height=34
                , width=85)
        self.ChoosepicPhraseLabel.configure(background="#d9d9d9")
        self.ChoosepicPhraseLabel.configure(disabledforeground="#a3a3a3")
        self.ChoosepicPhraseLabel.configure(font=font9)
        self.ChoosepicPhraseLabel.configure(foreground="#000000")
        self.ChoosepicPhraseLabel.configure(text='''Choose:''')
        self.ChoosepicPhraseLabel.configure(width=85)

        self.FreeTextLabel = tk.Label(self.LoginFrame)
        self.FreeTextLabel.place(relx=0.61, rely=0.233, height=34, width=95)
        self.FreeTextLabel.configure(background="#d9d9d9")
        self.FreeTextLabel.configure(disabledforeground="#a3a3a3")
        self.FreeTextLabel.configure(font=font9)
        self.FreeTextLabel.configure(foreground="#000000")
        self.FreeTextLabel.configure(text='''Free text:''')
        self.FreeTextLabel.configure(width=95)

        self.ChangeList["NewPicsBox"] = self.NewPicsBox
        self.ChangeList["picIDcomboBox"] = self.picIDcomboBox

        self.ChangeList["pic1button"] = self.pic1button
        self.ChangeList["pic2button"] = self.pic2button
        self.ChangeList["pic3button"] = self.pic3button
        self.ChangeList["pic4button"] = self.pic4button

        self.ChangeList["PhraseIDCombobox"] = self.PhraseIDCombobox
        self.ChangeList["NewPhrasesBox"] = self.NewPhrasesBox

        self.ChangeList["Phrase1Button"] = self.Phrase1Button
        self.ChangeList["Phrase2Button"] = self.Phrase2Button
        self.ChangeList["Phrase3Button"] = self.Phrase3Button
        self.ChangeList["Phrase4Button"] = self.Phrase4Button

        self.ChangeList["LoginFrame"] = self.LoginFrame
        self.ChangeList["MedicalOrDiet"] = self.medicalORdiet







