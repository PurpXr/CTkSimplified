
# Current version

> Late beta

# How to use

## How to use CTkSimplified

#### You can see an example code in [[example.py]] 
(CTkSimplified is imported as **ctk**) 

#### Basic code example:

```
isRunning = False

username = "PurpXr"
password = "PurpXr"

def login(name, pass):
	if isRunning:
		if name=username and pass=password:
			label.configure(text=f"Logged in as {name}")

import CTkSimplified as ctk

ctk.starter_config(appearance_mode='System', default_color_theme='blue')
# sets appearance mode and default app color theme

root = ctk.CTkSimplified(title="Application", geometry='500x450')
# If you don't fill title and geometry values than it will set them automaticly to
# title="App", geometry='400x400'

label = ctk.CTkSimplifiedLabel(master=root, text="Login", font=("Monospace", 25))
label.create(relx=0.5, rely=0.1)

button = ctk.CTkSimplifiedButton(master=root, text="Log in", font=("Monospace", 25), height=50, width=100, corner_radius=8, fg_color='blue', hover_color='purple', text_color='black', command=lambda: login(username, password))


root.mainloop()
# root.mainloop() is required for refreshing the app
```

#### Labels usage:

```
label = CTkSimplified.CTkSimplifiedLabel(master=app, text="Text")
# app is ctksimplified.CTkSimplified instance
label.create(relx=0.5, rely=0.5) 
# relx and rely are percentage of windows height and width 
```

#### Buttons usage:

```
def cmd(arguments):
	# commands logic here

button = CTkSimplified.CTkSimplifiedButton(master=app, text="Button", height=50, width=100, font=("Monospace", 25), command=cmd(arguments))
```

# Changes 

## Alpha --> Beta:

>Labels were added
>Frames weren't compatible with other objects such as labels or buttons

## Beta --> 1.0.0v:

> Buttons were added

# Work in progress...

- [x] Adding Lsabels
- [x] Adding Buttons
- [ ] Adding Textboxes
- [ ] Reworking frames
