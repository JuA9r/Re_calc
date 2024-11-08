"""

    calculator program

"""


import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

import math


def __decorator__(func) -> None:

    """
    :param func:
    :return:
    """

    def wrapper(string: any):

        """
        :param string:
        :return:
        """

        """Text box input restrictions"""

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

    return wrapper


@__decorator__
def __input_rest__() -> bool:

    """
    :param string:
    :return:
    """

    return True


class Window(tk.Frame):
    def __init__(self, master: any) -> None:

        """
        :param master:
        """

        """Generate the window"""
        """Generate text box and set content"""

        tk.Frame.__init__(self, master)

        self.master = master

        self.master.geometry("350x450+500+100")
        self.master.title("Calculator")

        text_font = tk.font.Font(
            slant="italic", weight="normal",
            underline=False, size=20
        )

        validata = self.master.register(__input_rest__)
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


class Button(tk.Button):
    def __init__(self, master: any) -> None:

        """
        :param master:
        """

        super().__init__(master)
        self.master = __master

    def __make_button__(self) -> None: ...


def main():
    root = tk.Tk()
    App = Window(master=root)
    App.mainloop()


if __name__ == "__main__":
    main()

