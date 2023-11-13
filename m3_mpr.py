import tkinter as tk

root = tk.Tk()
root.title("Logical Operations")
global_canvas = None

def display_img(root1,filepath):
    global global_canvas
    
    if global_canvas is not None:
        global_canvas.delete("all")
    else:
        global_canvas = tk.Canvas(root1, height=700, width=1100)
        global_canvas.grid()

    img = tk.PhotoImage(file=filepath)  # Specify the path to the image file
    global_canvas.create_image(700, 200, image=img)  # Adjust the coordinates to center the image
    root1.mainloop()

# Username
l1 = tk.Label(root, 
              text="Select the operation you want to perform: ", 
              font=("Times New Roman", 25), 
              width=40)
l1.grid(row=0, 
        column=0, 
        padx=10, 
        pady=10, 
        columnspan=3)

def and_opr():
    root.destroy()
    NW1 = tk.Tk()
    NW1.title("AND Operation")

    w1_l1 = tk.Label(NW1, 
                     text="Input 1 : ", 
                     font=("Times New Roman", 25), 
                     width=30)
    w1_l1.grid(row=0, 
               column=0, 
               padx=10, 
               pady=10)

    w1_e1 = tk.Entry(NW1, 
                     font=("Times New Roman", 25), 
                     width=30)
    w1_e1.grid(row=0, 
               column=1, 
               padx=10, 
               pady=10)

    w1_l2 = tk.Label(NW1, text="Input 2 : ", 
                     font=("Times New Roman", 25), 
                     width=30)
    w1_l2.grid(row=1,
                column=0, 
                padx=10, 
                pady=10)

    w1_e2 = tk.Entry(NW1, 
                     font=("Times New Roman", 25), 
                     width=30)
    w1_e2.grid(row=1,
                column=1, 
                padx=10, 
                pady=10)
     
      
    def submit():
        input1 = w1_e1.get()
        input2 = w1_e2.get()      
        
        if input1 == '0' and input2 == '0':
           display_img(NW1,"and_0_0.png")

        elif input1 == '0' and input2 == '1':
            display_img(NW1,"and_0_1.png")

        elif input1 == '1' and input2 == '0':
            display_img(NW1,"and_1_0.png")

        else:
           display_img(NW1,"Main.png")
        

    b = tk.Button(NW1, text="submit", 
                  font=("Times New Roman", 25), 
                  bg="orange", 
                  activebackground="yellow",
                  command=submit)
    
    b.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    NW1.mainloop()


def or_opr():
    root.destroy()
    NW2 = tk.Tk()
    NW2.title("OR Operation")

    w2_l1 = tk.Label(NW2, 
                     text="Input 1 : ", 
                     font=("Times New Roman", 25), 
                     width=30)
    w2_l1.grid(row=0, 
               column=0, 
               padx=10, 
               pady=10)

    w2_e1 = tk.Entry(NW2, 
                     font=("Times New Roman", 25), 
                     width=30)
    w2_e1.grid(row=0, 
               column=1, 
               padx=10, 
               pady=10)

    w2_l2 = tk.Label(NW2, text="Input 2 : ", 
                     font=("Times New Roman", 25), 
                     width=30)
    w2_l2.grid(row=1,
                column=0, 
                padx=10, 
                pady=10)

    w2_e2 = tk.Entry(NW2, 
                     font=("Times New Roman", 25), 
                     width=30)
    w2_e2.grid(row=1,
                column=1, 
                padx=10, 
                pady=10)

    def submit():
        input1 = w2_e1.get()
        input2 = w2_e2.get()

        if input1 == '0' and input2 == '0':
            display_img(NW2,"or_0_0.png")


        elif input1 == '0' and input2 == '1':
            display_img(NW2,"or_0_1.png")

        elif input1 == '1' and input2 == '0':
            display_img(NW2,"or_1_0.png")

        else:
            display_img(NW2,"or_1_1.png")

    b = tk.Button(NW2, text="submit", 
                  font=("Times New Roman", 25), 
                  bg="orange", 
                  activebackground="yellow",
                  command=submit)
    
    b.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    NW2.mainloop()


def not_opr():
    root.destroy()
    NW3 = tk.Tk()
    NW3.title("NOT Operation")

    w3_l1 = tk.Label(NW3, 
                     text="Input : ", 
                     font=("Times New Roman", 25), 
                     width=30)
    w3_l1.grid(row=0, 
               column=0, 
               padx=10, 
               pady=10)

    w3_e1 = tk.Entry(NW3, 
                     font=("Times New Roman", 25), 
                     width=30)
    w3_e1.grid(row=0, 
               column=1, 
               padx=10, 
               pady=10)

    def submit():
        input1 = w3_e1.get()

        if input1 == '0':
            display_img(NW3,"not_0.png")

        else:
            display_img(NW3,"not_1.png")

    b = tk.Button(NW3, text="submit", 
                  font=("Times New Roman", 25), 
                  bg="orange", 
                  activebackground="yellow",
                  command=submit)
    
    b.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    NW3.mainloop()



# Button
b1 = tk.Button(root, text="AND", font=("Times New Roman", 25), bg="orange", activebackground="yellow", command=and_opr)
b1.grid(row=1, column=0, padx=10, pady=10)

b2 = tk.Button(root, text="OR", font=("Times New Roman", 25), bg="orange", activebackground="yellow", command=or_opr)
b2.grid(row=1, column=1, padx=10, pady=10)

b3 = tk.Button(root, text="NOT", font=("Times New Roman", 25), bg="orange", activebackground="yellow", command=not_opr)
b3.grid(row=1, column=2, padx=10, pady=10)

root.mainloop()
