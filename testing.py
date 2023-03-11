import CTkSimplified as ctk

ctk.starter_config(appearance_mode='Dark', default_color_theme='blue')

root = ctk.CTkSimplified(title="aplikacja", geometry='500x450')

frame1 = ctk.CTkSimplifiedFrame(root)
root.place_frame(frame=frame1, master=root, row=0, column=0, padx=20, pady=20)

label1 = ctk.CTkSimplifiedLabel(root)
root.place_label(label=label1, master=root, row=0, column=0, padx=20, text="text!")

root.mainloop()
