import CTkSimplified as ctk

isRunning = False

username_val = "Admin"
password_val = "admin"

def login():
    if isRunning:
        nick = username_textbox.get('0.0', 'end')
        username_textbox.delete('0.0', 'end')

        passwd = password_textbox.get('0.0', 'end')
        password_textbox.delete('0.0', 'end')

        if nick.startswith(username_val) and passwd.startswith(password_val):
            button1.configure(text="Logged in as Admin!")
            username_textbox.configure(state='disabled')
            password_textbox.configure(state='disabled')
        else:
            print("Incorect username or  password")

            


ctk.starter_config(appearance_mode='Dark', default_color_theme='blue')

root = ctk.CTkSimplified(title="Application", geometry='500x450')

label1 = ctk.CTkSimplifiedLabel(master=root, text="Login page", text_color='#3971A8', font=("Monospace", 25))
label1.create(relx=0.5, rely=0.1)

label2 = ctk.CTkSimplifiedLabel(master=root, text="Username", text_color='#3971A8', font=("Monospace", 15))
label2.create(relx=0.5, rely=0.26)

username_textbox = ctk.CTkSimplifiedTextbox(master=root, width=200, height=40, corner_radius=0, fg_color="#6C747C", state="normal", font=("Monospace", 25), activate_scrollbars=False)
username_textbox.create(relx=0.3, rely=0.3)

label3 = ctk.CTkSimplifiedLabel(master=root, text="Password", text_color='#3971A8', font=("Monospace", 15))
label3.create(relx=0.5, rely=0.42)

password_textbox = ctk.CTkSimplifiedTextbox(master=root, width=200, height=40, corner_radius=0, fg_color="#6C747C", state="normal", font=("Monospace", 25), activate_scrollbars=False)
password_textbox.create(relx=0.3, rely=0.45)

button1 = ctk.CTkSimplifiedButton(master=root, height=50, width=150, corner_radius=8, fg_color='#2684CE', hover_color='#2496F2', text="Login", text_color="black", font=("Monospace", 25), command=lambda: login())
button1.create(relx=0.5, rely=0.8)

isRunning = True

root.mainloop()
