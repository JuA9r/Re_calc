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

    for s in [
        "+", "-", "×", "÷", "=",
        ".", "(", ")", "^", "√"
    ]:
        if string[-1] == s:
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
            self.master = master

        def button_init(self) -> None:
            _buttons = [
                "7", "8", "9", "÷",
                "6", "5", "4", "×",
                "1", "2", "3", "-",
                "=", "0", "00", "+",
                "AC", ".", "√", "^"
            ]
            row, column = 0, 1

            for i, _button_text in enumerate(_buttons):
                _button = tk.Button(self.master, text=_button_text, width=10, height=3)
                _button.grid(column=column, row=row, columnspan=2, sticky="ew")
                _button.brid("<button-1>", self.callback)

        def callback(self, event: any) -> None:
            _input_txt = event.widget["text"]

            print(
                f"button pressed : + {(event.widget["text"])}"
            )

            if _input_txt == "=":
                self.calculate()
            else:
                self.insert(_input_txt)


def main():
    root = tk.Tk()
    application = Calculator.Window(master=root)
    application.mainloop()


if __name__ == "__main__":
    main()
