import CTkSimplified as ctk

ctk.starter_config(appearance_mode='Dark', default_color_theme='blue')

root = ctk.CTkSimplified(title="aplikacja", geometry='500x450')

label1 = ctk.CTkSimplifiedLabel(master=root, text="Text!", text_color='blue', font=("Monospace", 25))
label1.create(relx=0.5, rely=0.1)

root.mainloop()
