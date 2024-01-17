import tkinter as tk

WIDTH:int = 360
HEIGHT:int = 100

TITLE = "Miles 2 Kilometers"

def main():
    window = tk.Tk()

    window.title(TITLE)
    window.geometry(f"{WIDTH}x{HEIGHT}")

    def convert():
        input_value = input_variable.get()

        try:
            var = float(input_value) * 1.609
            input_variable.set("")
            converted_variable.set(f"That's about {round(var,2)} kilometers")
        except:
            input_variable.set("")
            pass

    label_title = tk.Label(text=TITLE, font="Bold 24")
    label_title.pack()

    frame_convert = tk.Frame()

    input_variable = tk.StringVar()
    convert_input = tk.Entry(
        master=frame_convert,
        textvariable=input_variable
    )
    convert_input.pack(side="left")

    convert_input = convert()
    convert_button = tk.Button(
        master=frame_convert,
        text="Convert",
        command=convert
    )
    convert_button.pack(side='right')

    frame_convert.pack()

    converted_variable = tk.StringVar()
    convert_output = tk.Label(textvariable=converted_variable, font="bold 16")
    convert_output.pack()

    window.mainloop()

if __name__ == '__main__':
    main()