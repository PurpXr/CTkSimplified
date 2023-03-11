import customtkinter as ctk

def starter_config(appearance_mode, default_color_theme):
    ctk.set_appearance_mode(appearance_mode)
    ctk.set_default_color_theme(default_color_theme)

class CTkSimplifiedFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class CTkSimplifiedLabel(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class CTkSimplified(ctk.CTk):
    def __init__(self, title="App", geometry='400x400'):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def place_frame(self, frame, master, row, column, padx=0, pady=0, **kwargs):
        frame = CTkSimplifiedFrame(master=master, **kwargs)
        frame.grid(row=row, column=column, padx=padx, pady=pady, stick='nsew')

    def place_label(self, label, master, row, column, padx=0, pady=0, **kwargs):
        label = CTkSimplifiedLabel(master=master, **kwargs)
        label.grid(row=row, column=column, padx=padx, pady=pady)



