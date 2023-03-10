import customtkinter as ctk

def starter_config(appearance_mode, default_color_theme):
    ctk.set_appearance_mode(appearance_mode)
    ctk.set_default_color_theme(default_color_theme)

class CTkSimplifiedFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self)
        self.label.pack(padx=20, pady=20)


class CTkSimplified(ctk.CTk):
    def __init__(self, title="App", geometry='400x400'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame1 = CTkSimplifiedFrame(master=self)
        self.frame1.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')



