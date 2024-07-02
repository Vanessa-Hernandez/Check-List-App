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
    List=[] #the list of items is empty
    while True:
        text = entry.get() #gets the text from user 
        item =input(text)
        if item == 'done':
            break #makes variable item = text from user
       
    List.append(int(item)) # appends item into list

    print(List)
   
    
   
button = customtkinter.CTkButton(app, text="Add", command=lambda:button_callback)
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