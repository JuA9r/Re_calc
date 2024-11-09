"""

    Calculator program

"""


import tkinter as tk
import tkinter.ttk as ttk
from random import random
from tkinter.font import Font

import math


def text_rest_deco(func) -> None:

    """
    :param func:
    :return:
    """

    """decorator function"""

    def wrapper(string: any) -> None:

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


@text_rest_deco
def text_rest(string: any) -> bool:

    """
    :param string:
    :return: bool
    """

    return True


class Window(tk.Frame):
    def __init__(self, master: any) -> None:

        """
        :param master:
        :return: None
        """

        """Generate the window"""
        """Generate text box and set content"""
        """Change text style"""

        tk.Frame.__init__(self, master)

        self.master = master

        self.master.geometry("350x450+450+100")
        self.master.title("Calculator")

        text_font = tk.font.Font(
            slant="italic", weight="normal",
            underline=False, size=20
        )

        validata = self.master.register(text_rest)
        self.text = tk.Entry(
            self.master,
            background="black", foreground="lime", insertbackground="lime",
            font=text_font,
            validate="key", validatecommand=(validata, "%P")
        )

        self.master.columnconfigure(0, weight=1)
        self.text.grid(
            column=0, row=0, columnspan=3, sticky="ew"
        )

        self._button = Button(self.master)
        self._button.make_button()


class Button(tk.Button):
    def __init__(self, master: any) -> None:

        """
        Generate button
        :param master:
        :return: None
        """

        super().__init__(master)
        self.master = master

    def make_button(self) -> None:

        """
        :return: None
        """

        """generate calc button"""

        for i in range(1, 10):
            _button = tk.Button(self.master, text=i, width=10, height=5)
            _button.grid(row=(i-1)//3+1, column=(i-1)%3, sticky=tk.W)
            _button.bind("<Button-1>", self.click_button)

    def click_button(self, event) -> None:

        """
        :param event:
        :return: None
        """

        """button click function"""

        print(f"Button clicked: {event.widget["text"]}")


def main():
    root = tk.Tk()
    App = Window(master=root)
    App.mainloop()


if __name__ == "__main__":
    main()