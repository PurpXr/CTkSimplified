
# Current version

> Late beta

# How to use

## How to use CTkSimplified

#### You can see an example code in [[example.py]] 
(CTkSimplified is imported as **ctk**) 

#### Basic code example:

```
import CTkSimplified as ctk

ctk.starter_config(appearance_mode='System', default_color_theme='blue')
# sets appearance mode and default app color theme

root = ctk.CTkSimplified(title="Application", geometry='500x450')
# If you don't fill title and geometry values than it will set them automaticly to
# title="App", geometry='400x400'

label = ctk.CTkSimplified(master=root, text="Login", font=("Monospace", 25))
label.create(relx=0.5, rely=0.1)

root.mainloop()
# root.mainloop() is required for refreshing the app
```

#### Basic examples of label:

```
label = CTkSimplified.CTkSimplifiedLabel(master=app, text="Text")
# app is ctksimplified.CTkSimplified instance
label.create(relx=0.5, rely=0.5) 
# relx and rely are percentage of windows height and width 
```

# Errors

## Frames

>Frames aren't working because of incompatibility with other objects such as labels or buttons
>
>Frames will be reworked in future versions

# Work in progress...

- [x] Adding labels
- [ ] Reworking frames
- [ ] Adding Buttons
- [ ] Adding Textboxes
