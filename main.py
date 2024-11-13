"""

    Calculator program

"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font

import math


class Restriction:

    """input text restrictions"""

    @staticmethod
    def text_rest_deco(func) -> None:
        def wrapper(string: any) -> None:

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
    def __text_rest__(self, string: any) -> bool:
        return True


class Display(tk.Frame):
    def __init__(self, master: any) -> None:

        """Generate the display"""
        """Generate text box and set content"""
        """Change text style"""

        tk.Frame.__init__(self, master)

        self.master = master

        self.master.geometry("320x450+450+100")
        self.master.title("Calculator")

        text_font = tk.font.Font(
            slant="italic", weight="normal",
            underline=False, size=20
        )

        validata = self.master.register(Restriction.__text_rest__)
        self.text = tk.Entry(
            self.master,
            background="black", foreground="lime", insertbackground="lime",
            font=text_font,
            validate="key", validatecommand=(validata, "%P")
        )

        self.master.columnconfigure(0, weight=1)
        self.text.grid(
            column=0, row=0, columnspan=4, sticky="ew"
        )

        self._button = Button(self.master)
        self._button.make_button()


class Button(tk.Button):
    def __init__(self, master: any) -> None:

        super().__init__(master)
        self.master = master

    def make_button(self) -> None:

        """generate calc button"""

        # str button
        _str_button = ["+", "-", "×", "÷"]

        for i in range(1, 10):
            _num_button = tk.Button(self.master, text=i, width=10, height=5)
            _num_button.grid(row=3-(i-1)//3, column=(i-1)%3, sticky=tk.W)
            _num_button.bind("<Button-1>", self.click_button)

        for i, j in enumerate(_str_button):
            _str_btn = tk.Button(self.master, text=j, width=10, height=5)
            _str_btn.grid(row=i+1, column=3)
            _str_btn.bind("<Button-1>", self.click_button)
            continue

    def click_button(self, event: any) -> None:

        """button click function"""

        event.widget.config()
        print(
            f"button clicked: {(event.widget["text"])}"
        )


class Calculation(tk.Frame):
    def __init__(self, master: any) -> None:

        tk.Frame.__init__(self, master)
        self.master = master

    def input(self):
        ...


def main():
    root = tk.Tk()
    App = Display(master=root)
    App.mainloop()


if __name__ == "__main__":
    main()