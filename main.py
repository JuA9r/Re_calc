"""

    Calculator program

"""

import tkinter as tk
from tkinter.font import Font

import math
import sys


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

        super().__init__(master)

        self.master = master

        self.master.geometry("320x465+450+100")
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

        self._calc = Calculation(self.text)
        self._button = Button(self.master, self._calc)
        self._button.make_button()


class Button:
    def __init__(self, master, _calc) -> None:
        self.master = master
        self._calc = _calc

    def handle_button_click(self, event) -> None:

        """Wrapper to handle multiple button clicks"""

        self._calc.__setitem__(event)
        self.button_click(event)

    def make_button(self) -> None:

        """generate calc button"""

        # operator button list
        _ope_button = ["+", "-", "×", "÷"]
        _ope_button2 = ["^", "√", "C", "AC"]

        # str button list
        _str_button = [".", "0", "="]

        # Generate buttons 1 to 9 with 3×3
        for i in range(1, 10):
            _num_button = tk.Button(self.master, text=i, width=10, height=5)
            _num_button.grid(row=3-(i-1)//3, column=(i-1)%3, sticky=tk.W)
            _num_button.bind("<Button-1>", self.handle_button_click)

        # Generate buttons in a vertical column on the right edge
        for i, j in enumerate(_ope_button):
            _ope_button = tk.Button(self.master, text=j, width=10, height=5)
            _ope_button.grid(row=i+1, column=3)
            _ope_button.bind("<Button-1>", self.handle_button_click)

        # Generate a button in the second row below
        for i, k in enumerate(_str_button):
            _str_button = tk.Button(self.master, text=k, width=10, height=5)
            _str_button.grid(row=4, column=i)
            _str_button.bind("<Button-1>", self.handle_button_click)

        # Generate a button in the first row below
        for i, k in enumerate(_ope_button2):
            _ope_button2 = tk.Button(self.master, text=k, width=10, height=5)
            _ope_button2.grid(row=5, column=i)
            _ope_button2.bind("<Button-1>", self.handle_button_click)

    @staticmethod
    def button_click(event: any) -> None:

        """button click function"""

        event.widget.config()
        print(
            f"button clicked: {([event.widget["text"]])}"
        )


class Calculation:
    def __init__(self, entry_widget) -> None:
        self.entry_widget = entry_widget
        print(entry_widget, "\n"+"-"*20)

    def __get__(self, instance, owner) -> any:
        return self.entry_widget.get()

    def __set__(self, instance, value) -> None:
        self.entry_widget.delete(0, tk.END)
        self.entry_widget.insert(tk.END, value)

    def __setitem__(self, event) -> None:
        value = event.widget["text"]
        return self.entry_widget.insert(tk.END, value)

    def __delete__(self, instance) -> None:
        return self.entry_widget.delete(tk.END)

    def __one_delete__(self) -> None:
        return self.entry_widget.delete(
            len(self.entry_widget.get())-1, tk.END
        )

    def __equal__(self) -> bool:
        _replace = str.maketrans(
            {
                "＋": "+", "－": "-", "×": "*", "÷": "/", "^": "**", "√": "**0.5"
            }
        )

        self.entry_widget.delete(0, tk.END)
        result = eval(
            self.entry_widget.get().translate(_replace)
        )
        self.entry_widget.insert(tk.END, str(result))
        print("-" * 20, "\n", f"Answer: {result}")


def main():
    root = tk.Tk()
    App = Display(master=root)
    App.mainloop()
    if sys.exit:
        print("-"*20+"\nProcess terminated")


if __name__ == "__main__":
    main()