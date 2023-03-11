import tkinter

import customtkinter as ctk


def starter_config(appearance_mode, default_color_theme):
    ctk.set_appearance_mode(appearance_mode)
    ctk.set_default_color_theme(default_color_theme)


# class CTkSimplifiedFrame(ctk.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
#         self.master = master
#
#     def create(self, row, column, padx=0, pady=0, stick=None, **kwargs):
#         self = CTkSimplifiedFrame(master=self.master, **kwargs)
#         self.grid(row=row, column=column, padx=padx, pady=pady, stick=stick)
#
#     def create_label(self, row, column, padx=0, pady=0, **kwargs):
#         label = CTkSimplifiedLabel(master=self, **kwargs)
#         label.grid(row=row, column=column, padx=padx, pady=pady)


class CTkSimplifiedLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

    def create(self, relx, rely, anchor=tkinter.CENTER, **kwargs):
        self.place(relx=relx, rely=rely, anchor=anchor, **kwargs)


class CTkSimplified(ctk.CTk):
    def __init__(self, title="App", geometry='400x400'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
