
"""

    Calculator program

"""

# import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

# import math
import math


# textbox input restriction
def input_restriction(string: any) -> None:
    if len(string) == 0:
        return True

    types: tuple[any, any] = (int, float)
    for type_ in types:
        try:
            type_(string[-1])
            return True

        except ValueError:
            continue

    for _str in [
        "+", "-", "×", "÷", "=",
        ".", "(", ")", "^", "√"
    ]:
        if string[-1] == _str:
            return True

    return False


class Calculator:

    # generate calculator window
    class Window(tk.Frame):
        def __init__(self, master: any) -> None:
            super().__init__(master)

            self.master = master

            self.master.geometry("350x450+500+100")
            self.master.title("Calculator")

            text_font = tk.font.Font(
                slant="italic", weight="normal",
                underline=False, size=20
            )

            validata = self.master.register(input_restriction)
            self.text = tk.Entry(
                self.master,
                background="black", foreground="lime", insertbackground="lime",
                font=text_font,
                validate="key", validatecommand=(validata, "%P")
            )

            self.master.columnconfigure(0, weight=1)
            self.text.grid(
                column=0, row=0, columnspan=2, sticky="ew"
            )

    # generate calculator button
    class Button(tk.Button):
        def __init__(self, master: any) -> None:
            super().__init__(master)
            self.master = __master

        def button_init(self) -> None:
            for i in range(1, 10):
                _num_button = tk.Button(self.__master, text=i, width=10, height=3)
                _num_button.grid(row=3-(i-1)//3, column=(i-1)%3, columnspan=2, sticky="ew")
                _num_button.bind("<Button-1>", self.callback)

        def callback(self, event: any) -> None:
            event.widget.config()

            _input_txt = event.widget["text"]

            print(
                f"button pressed : + {(event.widget["text"])}"
            )

            if _input_txt == "=":
                ...

            else:
                ...


def main():
    root = tk.Tk()
    application = Calculator.Window(master=root)
    application.mainloop()


if __name__ == "__main__":
    main()
