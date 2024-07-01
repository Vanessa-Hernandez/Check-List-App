import customtkinter


app = customtkinter.CTk()
app.title("Vanessa Check List App")
app.geometry("300x550")

app.grid_columnconfigure(0, weight=1)
customtkinter.set_appearance_mode("Dark")


entry = customtkinter.CTkEntry(app, placeholder_text="Add to List")
entry.grid(padx=40, pady=(20, 10), columnspan=4, rowspan=2,  sticky="ew")
state = entry.cget("state")




def button_callback():
    List=[]
    text = entry.get()
    item =input(text)
    List.append(item)
    print(List)
    loop()
    
   
button = customtkinter.CTkButton(app, text="Add", command=button_callback)
button.grid(row=3, padx=40, pady=(20, 10), columnspan=4, rowspan=2)



#List=[]

#List=["soup", "fruit"]

#def update_Lsit()
#for List i


###### click Add, IF text then take entry text from user, add in anew value as a checklist with user text
##################################################################################################################


checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=6, column=1, padx=20, pady=(0, 20), sticky="w")


##################################################################################################################
#second button = complete
###### Click Completed , if checklist is clicked delete from list.
##################################################################################################################

def button2_callback():
    print("button2 pressed")

    


button2 = customtkinter.CTkButton(app, text="Completed", command=button2_callback)
button2.grid(row=7, padx=40, pady=(20, 10), columnspan=4, rowspan=2)


###### type into entry textfield








#test add
app.mainloop()