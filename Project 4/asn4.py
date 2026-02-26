# asn4.py - Food Viewer GUI Application

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class FoodViewerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x300")
        
        self.img_frame = tk.Frame(self.root)
        self.rbdBtn_frame = tk.Frame(self.root)
        
        self.var = tk.IntVar()
        self.var.set(1)
        
        self.load_images()
        
        self.lbl = tk.Label(self.img_frame, image=self.imgOne)
        
        self.create_radio_buttons()
        
        self.lbl.pack()
        self.img_frame.pack()
        self.rbdBtn_frame.pack()
        
        tk.mainloop()
    
    def load_images(self):
        try:
            image1 = Image.open("chicken.jpg")
            image1 = image1.resize((400, 300))
            self.imgOne = ImageTk.PhotoImage(image1)
            
            image2 = Image.open("pie.jpg")
            image2 = image2.resize((400, 300))
            self.imgTwo = ImageTk.PhotoImage(image2)
            
            image3 = Image.open("pizza.jpg")
            image3 = image3.resize((350, 300))
            self.imgThree = ImageTk.PhotoImage(image3)
            
            image4 = Image.open("steak.jpg")
            image4 = image4.resize((300, 300))
            self.imgFour = ImageTk.PhotoImage(image4)
            
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Image file not found: {e}")
    
    def create_radio_buttons(self):
        self.radio_a = tk.Radiobutton(
            self.rbdBtn_frame, 
            text="Chicken", 
            variable=self.var, 
            value=1,
            command=self.on_radio_select
        )
        self.radio_a.pack(side="left", padx=10)
        
        self.radio_b = tk.Radiobutton(
            self.rbdBtn_frame, 
            text="Pie", 
            variable=self.var, 
            value=2,
            command=self.on_radio_select
        )
        self.radio_b.pack(side="left", padx=10)
        
        self.radio_c = tk.Radiobutton(
            self.rbdBtn_frame, 
            text="Pizza", 
            variable=self.var, 
            value=3,
            command=self.on_radio_select
        )
        self.radio_c.pack(side="left", padx=10)
        
        self.radio_d = tk.Radiobutton(
            self.rbdBtn_frame, 
            text="Steak", 
            variable=self.var, 
            value=4,
            command=self.on_radio_select
        )
        self.radio_d.pack(side="left", padx=10)
    
    def on_radio_select(self):
        choice = self.var.get()
        
        food_names = {1: "Chicken", 2: "Pie", 3: "Pizza", 4: "Steak"}
        messagebox.showinfo("Selection", f"You selected: {food_names[choice]}")
        
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)


class FoodViewerGUILoop:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x300")
        
        self.img_frame = tk.Frame(self.root)
        self.rbdBtn_frame = tk.Frame(self.root)
        
        self.var = tk.IntVar()
        self.var.set(1)
        
        self.load_images()
        
        self.lbl = tk.Label(self.img_frame, image=self.imgOne)
        
        self.food_items = [
            ("Chicken", 1, self.imgOne),
            ("Pie", 2, self.imgTwo),
            ("Pizza", 3, self.imgThree),
            ("Steak", 4, self.imgFour)
        ]
        
        for text, value, img in self.food_items:
            rb = tk.Radiobutton(
                self.rbdBtn_frame,
                text=text,
                variable=self.var,
                value=value,
                command=self.on_radio_select
            )
            rb.pack(side="left", padx=10)
        
        self.lbl.pack()
        self.img_frame.pack()
        self.rbdBtn_frame.pack()
        
        tk.mainloop()
    
    def load_images(self):
        try:
            image1 = Image.open("chicken.jpg")
            image1 = image1.resize((400, 300))
            self.imgOne = ImageTk.PhotoImage(image1)
            
            image2 = Image.open("pie.jpg")
            image2 = image2.resize((400, 300))
            self.imgTwo = ImageTk.PhotoImage(image2)
            
            image3 = Image.open("pizza.jpg")
            image3 = image3.resize((350, 300))
            self.imgThree = ImageTk.PhotoImage(image3)
            
            image4 = Image.open("steak.jpg")
            image4 = image4.resize((300, 300))
            self.imgFour = ImageTk.PhotoImage(image4)
            
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"Image file not found: {e}")
            self.create_fallback_images()
    
    def create_fallback_images(self):
        from PIL import ImageDraw
        
        img1 = Image.new('RGB', (400, 300), color='red')
        draw = ImageDraw.Draw(img1)
        draw.text((150, 150), "Chicken", fill='white')
        self.imgOne = ImageTk.PhotoImage(img1)
        
        img2 = Image.new('RGB', (400, 300), color='blue')
        draw = ImageDraw.Draw(img2)
        draw.text((150, 150), "Pie", fill='white')
        self.imgTwo = ImageTk.PhotoImage(img2)
        
        img3 = Image.new('RGB', (350, 300), color='green')
        draw = ImageDraw.Draw(img3)
        draw.text((150, 150), "Pizza", fill='white')
        self.imgThree = ImageTk.PhotoImage(img3)
        
        img4 = Image.new('RGB', (300, 300), color='yellow')
        draw = ImageDraw.Draw(img4)
        draw.text((100, 150), "Steak", fill='black')
        self.imgFour = ImageTk.PhotoImage(img4)
    
    def on_radio_select(self):
        choice = self.var.get()
        
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)


if __name__ == '__main__':
    app = FoodViewerGUI()
