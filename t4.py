from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

def plot_graph():
    try:
        name = ent_name.get()  
        phy = float(ent_physics.get())  
        chem = float(ent_chemistry.get())  
        math = float(ent_maths.get())  
        
        subjects = ['Physics', 'Chemistry', 'Math']
        marks = [phy, chem, math]
        
        plt.figure(figsize=(6,4))
        plt.bar(subjects, marks, color=['blue', 'green', 'red'])
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.title(f'Marks of {name}')
        
        plt.savefig(f'{name}_marks.pdf')
	#plt.savefig("pizza.pdf")
        plt.show()
        messagebox.showinfo("Success", f"Graph saved as {name}_marks.pdf")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for marks.")


root = Tk()
root.title("Marks Bar Graph")
root.geometry("1100x600+200+40")
f = ("Cambria", 25, "bold")

# Labels and Entry Widgets
lab_name = Label(root, text="Enter name", font=f)
ent_name = Entry(root, font=f)

lab_physics = Label(root, text="Enter Physics marks", font=f)
ent_physics = Entry(root, font=f)

lab_chemistry = Label(root, text="Enter Chemistry marks", font=f)
ent_chemistry = Entry(root, font=f)

lab_maths = Label(root, text="Enter Maths marks", font=f)
ent_maths = Entry(root, font=f)

btn_plot = Button(root, text="Plot Graph", font=f, command=plot_graph)

lab_name.pack(pady=10)
ent_name.pack(pady=10)

lab_physics.pack(pady=10)
ent_physics.pack(pady=10)

lab_chemistry.pack(pady=10)
ent_chemistry.pack(pady=10)

lab_maths.pack(pady=10)
ent_maths.pack(pady=10)

btn_plot.pack(pady=10)

root.mainloop()
