import sympy as sp # imports SymPy library for symbolic math (integrals, algebra, etc.)
import numpy as np # imports NumPy for working with arrays (used in plotting graphs)
import matplotlib.pyplot as plt # imports matplotlib for drawing graphs
import tkinter as tk # imports Tkinter for creating GUI (buttons, inputs, window)
from tkinter import messagebox # imports popup message windows (for results and errors)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # allows matplotlib graphs to be displayed inside Tkinter window


# DEFINING SYMBOL

x = sp.symbols('x')
# defines mathematical variable x for all expressions


# CREATING MAIN WINDOW

root = tk.Tk() # creates main application window (GUU)
#root = main window controller
root.title("Simple Math Calculator") # sets window title


# INPUT FIELDS (USER INPUT AREA)


tk.Label(root, text="Function f(x):").grid(row=0, column=0)
# creates label for first function input and places it in row 0 column 0
# A geometry manager like grid controls where in the user interface they are placed.
function_f_entry = tk.Entry(root) # creates input box for function f(x)
function_f_entry.grid(row=0, column=1) # places f(x) input box next to label (row 0, column 1)

tk.Label(root, text="Function g(x):").grid(row=1, column=0)
# label for second function g(x)
function_g_entry = tk.Entry(root)
#it creates a text input box inside the main window (root) and stores it in a variable called function_g_entry.
# input box for g(x)
function_g_entry.grid(row=1, column=1)
# places g(x) input box

tk.Label(root, text="Lower limit (a):").grid(row=2, column=0)
# label for lower limit of integration
lower_limit_entry = tk.Entry(root)
# input box for lower limit
lower_limit_entry.grid(row=2, column=1)
# places lower limit input box


tk.Label(root, text="Upper limit (b):").grid(row=3, column=0)
# label for upper limit of integration

upper_limit_entry = tk.Entry(root)
# input box for upper limit

upper_limit_entry.grid(row=3, column=1)
# places upper limit input box



# FUNCTION: CONVERT TEXT TO MATH

def to_math_expression(expression):
    # function that converts string input into math expression

    return sp.sympify(expression, convert_xor=True)
    # converts text like "x^2" into proper math "x**2" (instead of XOR)



# INTEGRAL FUNCTION

def calculate_integral(): # function to calculate definite integral
    try:
        # Starting error-safe block
        f = to_math_expression(function_f_entry.get())
        # ets f(x) input and converts to math expression

        a = sp.sympify(lower_limit_entry.get()).evalf() #lower limit of the function 
        b = sp.sympify(upper_limit_entry.get()).evalf() #upper limit
        #sp.simplify() makes a mathematical expression easier or more “clean”
        #evalf() converts an exact symbolic math answer into a decimal approximation
        
        a = float(a) #converting values into real Python numbers (decimals)
        b = float(b)
        if a == b: #checking if lower limit is equal to upper limit
            messagebox.showinfo("Info", "Lower and upper limits are the same, result is 0")
            return

        result = (sp.integrate(f, (x, a, b))).evalf()
        # calculating definite integral
        
        # Using evalf to evaluate using floating-point arithmetic
        messagebox.showinfo("Integral Result", result)
        # showing result in popup window

    except:
        # if anything goes wrong
        messagebox.showerror("Error", "Invalid input")
        # show error message



# AREA BETWEEN CURVES FUNCTION

def calculate_area():
    # calculates area between f(x) and g(x)

    try:
        f1 = to_math_expression(function_f_entry.get())
        # first function (converts string input into math expression for f(x))
        f2 = to_math_expression(function_g_entry.get())
        # second function (converts string input into math expression for g(x))
        a = sp.sympify(lower_limit_entry.get()).evalf() #lower limit of the function 
        b = sp.sympify(upper_limit_entry.get()).evalf() #upper limit
        #sp.simplify() makes a mathematical expression easier or more “clean”
        #using evalf() for converting an exact symbolic math answer into a decimal approximation
        a = float(a)
        b = float(b)
        #converting values into real Python numbers (decimals)
        if a == b: #checking if lower limit is equal to upper limit
            messagebox.showinfo("Info", "Lower and upper limits are the same, result is 0")
            return
        result = (sp.integrate(abs(f1 - f2), (x, a, b))).evalf()
        # computes area between curves
        # abs - module, calculating the difference
        if sp.simplify(f1 - f2) == 0:
            messagebox.showinfo("Info", "Functions are identical, area is 0")
            return

        messagebox.showinfo("Area Result", result)
        # show result

    except:
        messagebox.showerror("Error", "Invalid input")
        # show error if input is wrong



# VOLUME FUNCTION 

def calculate_volume():
    # calculates volume of revolution

    try:
        f = to_math_expression(function_f_entry.get())
        # get function

        a = sp.sympify(lower_limit_entry.get()).evalf() #lower limit of the function 
        b = sp.sympify(upper_limit_entry.get()).evalf() #upper limit
        #sp.simplify() makes a mathematical expression easier or more “clean”
        a = float(a)
        b = float(b)
        if a == b: #checking if lower limit is equal to upper limit
            messagebox.showinfo("Info", "Lower and upper limits are the same, result is 0")
            return
        result = (sp.integrate(sp.pi * f**2, (x, a, b))).evalf()
        # disk method formula
        

        messagebox.showinfo("Volume Result", result)
        # show result

    except:
        messagebox.showerror("Error", "Invalid input")
        # show error



# AREA GRAPH FUNCTION

def show_area_graph():
    # shows graph of two functions and shaded area between them

    try:
        
        # GETTING AND CONVERTING INPUTS
        

        f1 = to_math_expression(function_f_entry.get())
        # convert first function input (for SymPy expression)

        f2 = to_math_expression(function_g_entry.get())
        # convert second function input (for SymPy expression)

        a = sp.sympify(lower_limit_entry.get()).evalf() #lower limit of the function 
        b = sp.sympify(upper_limit_entry.get()).evalf() #upper limit

        a = float(a)
        b = float(b)

        # check if limits are the same
        if a == b:
            messagebox.showinfo("Info", "Lower and upper limits are the same, result is 0")
            return

        
        # CONVERTING FUNCTIONS FOR NUMPY PLOTTING
        

        f1_num = sp.lambdify(x, f1, "numpy")
        # convert SymPy function f1 into a NumPy-compatible function

        f2_num = sp.lambdify(x, f2, "numpy")
        # convert SymPy function f2 into a NumPy-compatible function

        
        # CREATING X VALUES
        

        X = np.linspace(a, b, 300)
        # generate 300 equally spaced points between a and b

       
        # FIXING FOR CONSTANT FUNCTIONS (for example f(x)=5)
        

        if f1.free_symbols == set():
            Y1 = np.full_like(X, float(f1)) #makes an array like X but filled with number
            # if f1 is constant, creates flat array with same value
        else:
            Y1 = f1_num(X)
            # otherwise evaluate normally

        if f2.free_symbols == set():
            Y2 = np.full_like(X, float(f2))
            # if f2 is constant, creates flat array
        else:
            Y2 = f2_num(X)
            # otherwise evaluate normally

        
        # PLOTING GRAPH
        

        fig, ax = plt.subplots()
        # create figure and axes for plotting
        # fig is the whole image, ax are axes

        ax.plot(X, Y1)
        # plot first function

        ax.plot(X, Y2)
        # plot second function

        ax.fill_between(X, Y1, Y2, alpha=0.3) #light transparent
        # shade area between curves

       
        # EMBED IN TKINTER
        

        canvas = FigureCanvasTkAgg(fig, master=root)
        # create canvas to embed matplotlib graph into Tkinter window

        canvas.draw()
        # render the graph, creating the picture

        canvas.get_tk_widget().grid(row=7, column=0, columnspan=2) #graph stretching across two colymns
        # place graph in GUI layout
        #get_tk_widget() converts canvas into a Tkinter element
        #.grid() places it in the window

        # showing graph of two functions and shaded area

    except:
       
        # ERROR HANDLING
      
        messagebox.showerror("Error", "Invalid input")
        # showing error if anything fails


# VOLUME GRAPH FUNCTION

def show_volume_graph():
    # shows graph of function and area under curve

    try:
        f = to_math_expression(function_f_entry.get())
        # getting function

        a = sp.sympify(lower_limit_entry.get()).evalf() #lower limit of the function 
        b = sp.sympify(upper_limit_entry.get()).evalf() #upper limit

        a = float(a)
        b = float(b)
        if a == b: #checking if limits are the same
            messagebox.showinfo("Info", "Lower and upper limits are the same, result is 0")
            return

        f_num = sp.lambdify(x, f, "numpy")
        # lamdify() converting to numeric function

        X = np.linspace(a, b, 300)
        # x values
        #creates 300 evenly spaced points between lower and upper limits

        Y = f_num(X)
        # y values, applies function to every x-value

        fig, ax = plt.subplots()
        # create plot

        ax.plot(X, Y)
        # plot function, connects all points into a smooth curve

        ax.fill_between(X, 0, Y, alpha=0.3)
        # shade under curve

        canvas = FigureCanvasTkAgg(fig, master=root)
        # embed graph

        canvas.draw()
        # draw graph

        canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)
        # place graph

    except:
        messagebox.showerror("Error", "Invalid input")
        # error handling



# BUTTONS (COMMANDS)


tk.Button(root, text="Integral", command=calculate_integral).grid(row=4, column=0)
# button for integral
# A geometry manager like grid controls where in the user interface they are placed.
tk.Button(root, text="Area", command=calculate_area).grid(row=4, column=1)
# button for area

tk.Button(root, text="Volume", command=calculate_volume).grid(row=5, column=0)
# button for volume

tk.Button(root, text="Show Area Graph", command=show_area_graph).grid(row=5, column=1)
# button for area graph

tk.Button(root, text="Show Volume Graph", command=show_volume_graph).grid(
    row=6,
    column=0,
    columnspan=2 #is used to make the button stretch across the full width of the window
)
#full width button for volume graph



# RUNNING PROGRAM

root.mainloop()
# Starts the GUI and keep it running until the user closes the window
