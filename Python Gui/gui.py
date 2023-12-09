import tkinter as tk
root=tk.Tk()

root.title("PyCharm")
#widthxheight
root.geometry("733x434")
#width,height
root.minsize(700,400)
root.maxsize(800,500)
#image
canvas = tk.Canvas(root, width = 400, height = 400) 
canvas.pack()       
img = tk.PhotoImage(file="C:\\Users\\harsh\\OneDrive\\Desktop\\PYTHON PROJECTS\\Python Gui\\img\\pycharm.png")      
canvas.create_image(200,200,image=img)
canvas.place(relx=.25,rely=0)
#label
heading=tk.Label(text="PyCHARM Community Edition")
heading.pack()
ver=tk.Label(text="Version 2017.2")
ver.pack()
opt1=tk.Label(text="Create New Project")
opt1.place(relx=.43,rely=.40)
opt2=tk.Label(text="Open")
opt2.place(relx=.43,rely=.50)
opt3=tk.Label(text="Check out from Version Control")
opt3.place(relx=.43,rely=.60)

#gui logic
root.mainloop()