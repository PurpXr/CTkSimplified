
# Current version

> 1.0.1

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
# app is CTkSimplified.CTkSimplifiedLabel instance
label.create(relx=0.5, rely=0.5) 
# relx and rely are percentage of windows height and width 
```

#### Buttons usage:

```
def cmd(arguments):
	# commands logic here

button = CTkSimplified.CTkSimplifiedButton(master=app, text="Button", height=50, width=100, font=("Monospace", 25), command=cmd(arguments))
button.create(relx=0.5, rely-0.8)
```

#### Textbox usage:

```
val = "value"

def check():
	textbox_val = textbox.get('0.0', 'end') 
	if textbox_val.startswith(val):
		button.configure(text="Logged in!")
		textbox.configure(state='disabled')

# .get('0.0', 'end') means that the value is being checked from line 0, character 0, to the end
# Remember that in val.startswith(val) startswith is required because it counts free space as characters
# You can check it by cliking on the textbox and pressing control + a

textbox = CTkSimplified.CTkSimplifiedTextbox(master=app, width=200, height=50, font=("Monospace", 25))
textbox.create(relx=0.3, 0.3)

button = CTkSimplified.CTkSimplifiedButton(master=app, text="Button", width=150, height=50, font=("Monospace", 25), command=lambda: check())
button.create(relx=0.5, rely=0.8)

# textboxes and buttons mixed are really useful
```

### If buttons commands=cmd() doesn't work then use

`command=lambda: cmd()`

# Features 

## Alpha --> Beta:

>Labels were added
>
>Frames weren't compatible with other objects such as labels or buttons

## Beta --> 1.0.0v:

> Buttons were added

## 1.0.0v --> 1.0.1v:

> Textboxes were added
# Work in progress...

- [x] Add Labels
- [x] Add Buttons
- [x] Add Textboxes
- [ ] Rework frames
