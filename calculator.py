from tkinter import *

#Root settings

root = Tk()
root.title("Calculator")
root.minsize(width=350 , height=500)
root.config(bg="#250902")

display_text = StringVar()
display_text.set("0")

calculate_label = Label(root , textvariable=display_text)
calculate_label.config(font=("Arial" , 35 , "normal") , fg="#FFFFFF" , bg="#250902" ,  width="11" , padx=20 ,  anchor="e")
calculate_label.grid(row=0, column=0, columnspan=4, sticky="we", pady=(50, 20)) 

#----------------FUNCTİONS---------------------------#

def click_button(value):
    
    current = display_text.get()
    operators = ["+" , "-" , "/" , "*" , "X"]

    if current == "0":
        
        if value in operators:
            display_text.set("0" + ("*" if value == "X" else value))
        else:
            display_text.set(value)
    
    elif value in operators and current[-1] in ["+" , "-" , "/" , "*" , "X"]:
        
        new_value = "*" if value == "X" else value
        display_text.set(current[:-1] + new_value)      

    else:
        
        if value == "X":
            display_text.set(current + "*")
        else:
            display_text.set(current + value)

def clean_button():
    display_text.set("0")

def calculate_result():
    try:
        
        result = eval(display_text.get())
        display_text.set(result)
    
    except Exception:
        
        display_text.set("Error")


#---------------Uİ SETTİNGS-------------------------------#

#Buttons
button_settings = {"font": ("Arial", 14, "normal"), "bg": "#38040E", "fg": "#E0E1DD", "width": 8, "height": 3}

# First Row

btn_7 = Button(root , text="7" , **button_settings , command=lambda: click_button("7"))
btn_7.grid(row=2, column=0, padx=0, pady=3)

btn_8 = Button(root, text="8", **button_settings, command=lambda: click_button("8"))
btn_8.grid(row=2, column=1, padx=0, pady=3)

btn_9 = Button(root, text="9", **button_settings, command=lambda: click_button("9"))
btn_9.grid(row=2, column=2, padx=0, pady=3)

btn_divide = Button(root, text="/", **button_settings, command=lambda: click_button("/"))
btn_divide.grid(row=2, column=3, padx=0, pady=3)


# Second Row

btn_4 = Button(root, text="4", **button_settings, command=lambda: click_button("4"))
btn_4.grid(row=3, column=0, padx=2, pady=3)

btn_5 = Button(root, text="5", **button_settings, command=lambda: click_button("5"))
btn_5.grid(row=3, column=1, padx=2, pady=3)

btn_6 = Button(root, text="6", **button_settings, command=lambda: click_button("6"))
btn_6.grid(row=3, column=2, padx=2, pady=3)

btn_multiply = Button(root, text="X", **button_settings, command=lambda: click_button("X"))
btn_multiply.grid(row=3, column=3, padx=2, pady=3)


# Third Row

btn_1 = Button(root, text="1", **button_settings, command=lambda: click_button("1"))
btn_1.grid(row=4, column=0, padx=2, pady=3)

btn_2 = Button(root, text="2", **button_settings, command=lambda: click_button("2"))
btn_2.grid(row=4, column=1, padx=2, pady=3)

btn_3 = Button(root, text="3", **button_settings, command=lambda: click_button("3"))
btn_3.grid(row=4, column=2, padx=2, pady=3)

minus_btn = Button(root, text="-", **button_settings, command=lambda: click_button("-"))
minus_btn.grid(row=4, column=3, padx=2, pady=3)


# Fourth Row

delete_button = Button(root, text="C", **button_settings, command=clean_button)
delete_button.grid(row=5, column=0, padx=2, pady=3)

btn_0 = Button(root, text="0", **button_settings, command=lambda: click_button("0"))
btn_0.grid(row=5, column=1, padx=2, pady=3)

btn_equal = Button(root, text="=", **button_settings, command=calculate_result)
btn_equal.grid(row=5, column=2, padx=2, pady=3)

sum_button = Button(root, text="+", **button_settings, command=lambda: click_button("+"))
sum_button.grid(row=5, column=3, padx=2, pady=3)


root.mainloop()