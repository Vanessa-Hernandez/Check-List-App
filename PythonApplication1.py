import customtkinter


app = customtkinter.CTk()
app.title("Vanessa Check List App")
app.geometry("400x150")




entry = customtkinter.CTkEntry(app, placeholder_text="Add to List")
entry.grid(padx=40, pady=(20, 10), columnspan=4, rowspan=2)
state = entry.cget("state")







checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=6, column=1, padx=20, pady=(0, 20), sticky="w")


def button_callback():
    print("button pressed")

    button = customtkinter.CTkButton(app, text="CTkCheckBox", command=checkbox_event, row =2, width=5,  padx=20, pady=20)


app.grid_columnconfigure(0, weight=1)
customtkinter.set_appearance_mode("Dark")

button = customtkinter.CTkButton(app, text="Submit", command=button_callback)
button.grid(row=3, padx=40, pady=(20, 10), columnspan=4, rowspan=2)


#test add
app.mainloop()