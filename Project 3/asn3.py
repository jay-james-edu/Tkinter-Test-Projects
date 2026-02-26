import tkinter as tk
from tkinter import messagebox

#Pop-up Textbox
def displayData():
    first_name = entFirst.get().strip()
    last_name = entLast.get().strip()
    email = entEmail.get().strip()
    phone = entPhone.get().strip()
    
    formatted_text = f"Welcome to tkinter, {first_name if first_name else '[First Name]'}\n"
    formatted_text += "\nYou entered:\n"
    formatted_text += f"Name: {first_name if first_name else '[First Name]'} {last_name if last_name else '[Last Name]'}\n"
    formatted_text += f"Email: {email if email else '[Email]'}\n"
    formatted_text += f"Phone: {phone if phone else '[Phone]'}"
    
    messagebox.showinfo("", formatted_text)

#Clear Function
def clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)

#Main App
root = tk.Tk()
root.title("tkinter Form")
root.geometry("500x300")

lblFrPerson = tk.LabelFrame(root, text="Personal Info")
lblFrPerson.pack(padx=20, pady=10, fill="both", expand=True)


#First Name
lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg="blue", fg="white")
lblFirst.grid(column=0, row=0, padx=10, pady=5, sticky="w")
entFirst = tk.Entry(lblFrPerson, width=30)
entFirst.grid(column=1, row=0, padx=10, pady=5, sticky="w")

#Last Name
lblLast = tk.Label(lblFrPerson, text="*Last Name:", bg="blue", fg="white")
lblLast.grid(column=0, row=1, padx=10, pady=5, sticky="w")
entLast = tk.Entry(lblFrPerson, width=30)
entLast.grid(column=1, row=1, padx=10, pady=5, sticky="w")

#Email
lblEmail = tk.Label(lblFrPerson, text="Email:")
lblEmail.grid(column=0, row=2, padx=10, pady=5, sticky="w")
entEmail = tk.Entry(lblFrPerson, width=30)
entEmail.grid(column=1, row=2, padx=10, pady=5, sticky="w")

#Phone
lblPhone = tk.Label(lblFrPerson, text="Phone:")
lblPhone.grid(column=0, row=3, padx=10, pady=5, sticky="w")
entPhone = tk.Entry(lblFrPerson, width=30)
entPhone.grid(column=1, row=3, padx=10, pady=5, sticky="w")

#Frames Button
fraButtons = tk.Frame(root)
fraButtons.pack(pady=20)

#Submit
btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT, padx=10)

#Reset
btnR = tk.Button(fraButtons, text="Reset", width=5, command=clear)
btnR.pack(side=tk.LEFT, padx=10)

#Quit
btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=10)

lblFrPerson.grid_columnconfigure(1, weight=1)

root.mainloop()
