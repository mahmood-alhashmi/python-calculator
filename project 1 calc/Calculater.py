import tkinter as tk
from PIL import Image, ImageTk
import numpy as np




equation = ""

def load_images(image_paths):
    images = {}
    for key, path in image_paths.items():
        image = Image.open(path)
        images[key] = ImageTk.PhotoImage(image)
    return images

def on_button_click(value):
    global equation
    if value == "=":
        equation = equation.replace('√', 'np.sqrt').replace('e**', 'np.exp').replace('ln(', 'np.log(')
        equation = equation.replace('sin(', 'np.sin(').replace('cos(', 'np.cos(').replace('tan(', 'np.tan(')
        equation = equation.replace('ln(', 'np.log(').replace('log(', 'np.log10(')


        try:
            equation = str(eval(equation))
            equation_display.delete(0, tk.END)
            equation_display.insert(tk.END,equation)  
            print(equation)
            equation = ""
        except Exception as e:
            print ("Error:", e)
            equation = ""
            equation_display.delete(0, tk.END)
            equation_display.insert(tk.END,"error")  
    elif value == "clear":
        equation = ""
        equation_display.delete(0, tk.END)
        equation_display.insert(tk.END, equation)
    else:
        equation += value
        equation_display.delete(0, tk.END)
        equation_display.insert(tk.END, equation)
    print(f"the current equation is: {equation}")


    


def create_button(root, image, row, col, **kwargs):
    button = tk.Button(root, image=image, **kwargs)
    button.grid(row=row, column=col, padx=0 ,pady=0)
    return button


# create a window
root = tk.Tk()
root.title("Calculator")
root.configure(bg='black')


equation_display = tk.Entry(root, font=("Arial", 20), bg="black", fg="purple")
equation_display.grid(row=0, column=0, columnspan=5, padx=0, pady=0, sticky="ew")

for i in range(4):  # Assuming you have 4 columns as per the code you provided
    root.grid_columnconfigure(i, weight=1)


image_paths = {
    "clear" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\clear.png",
    "to th power of" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\to the power of.png",
    "square root" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\square root.png",
    "e to the power of" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\e.png",
    "sin" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\sin.png",
    "cos" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\cos.png",
    "tan" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\tan.png",
    "ln" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\ln.png",
    "log()" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\log.png",
    "(" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\(.png",
    ")" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\).png",
    "devision" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\divide.png",
    "seven" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\7.png",
    "eight" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\8.png",
    "nine" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\9.png",
    "multiplication" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\multiply.png",
    "four" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\4.png",
    "five" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\5.png",
    "six" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\6.png",
    "minus" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\minus.png",
    "one" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\1.png",
    "two" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\2.png",
    "three" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\3.png",
    "addition" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\plus.png",
    "zero" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\0.png",
    "decimal" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\decimal.png",
    "equal" : r"C:\Users\hp\OneDrive\Desktop\project 1 calc\calc ymbols\equals.png",

}

image_values = {
    'clear' : '',
    'to th power of': '**',
    'square root':'√',
    'devision':'/',
    'e to the power of' : 'e**',
    'sin' : 'sin(',
    'cos' : 'cos(',
    'tan' : 'tan(',
    'ln' : 'ln(',
    'log()' : 'log(',
    '(' : '(',
    ')' : ')',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'multiplication':'*',
    'four':'4',
    'five':'5',
    'six':'6',
    'minus':'-',
    'one':'1',
    'two':'2',
    'three':'3',
    'addition':'+',
    'zero':'0',
    'decimal':'.',
    'equal':'=',
    }

# put the dictionary into a list
photo_keys = list(image_paths.keys())

# calculate the number of rows and columns based on the number of photos in the dictionary
columns = 4
row = len(photo_keys) // columns + (len(photo_keys) % columns > 0)
photos = load_images(image_paths)






#create the button grid structure
index = 0
for r in range(row):
    for c in range(columns):
        if index < len(photo_keys):
            key = photo_keys[index]
            value = image_values[key]
            create_button(root, text=value, command=lambda val = value: on_button_click(val), image=photos[photo_keys[index]], row = r + 1, col = c)
            index += 1


# run the application
root.mainloop()

