"""
    Calculator.run

This file is what powers the calculator.
"""

import tkinter as tk
from tkinter.font import Font
import sys


class Restriction:

    @staticmethod
    def text_rest_deco(func) -> None:

        def wrapper(string: str) -> None:
            if len(string) == 0:
                return True

            types: tuple[any, any] = (int, float)
            for type_ in types:
                try:
                    type_(string[-1])
                    return True

                except ValueError:
                    continue

            _str = "+-×÷=.()^√"
            if string[-1] in _str:
                if string[-1] == "(":
                    if len(string) > 1 and string[-2].isdigit():
                        return False

                elif string[-1] == ")":
                    if len(string) > 1 and string[-2] in "+-×÷(^":
                        return False

                return True
            return False

        return wrapper

    @text_rest_deco
    def __text_rest__(self, string) -> bool:
        return True


class Display(tk.Frame):
    def __init__(self, master: any) -> None:
        """Generate the display"""
        """Generate text box and set content"""
        """Change text style"""

        super().__init__(master)

        self.master = master

        self.master.geometry("320x460+450+80")
        self.master.title("Calculator")

        text_font = tk.font.Font(
            slant="roman", weight="normal",
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

        """wrapper to handle multiple button clicks"""

        self.button_click(event)
        action = event.widget["text"]
        self._calc.__perform_action__(action)

    def make_button(self) -> None:

        """generate calc button"""

        operator_button = ["+", "-", "×", "÷"]
        additional_button = ["^", "√", "C", "AC"]
        string_button = [".", "0", "="]

        # Generate buttons 1 to 9 with 3×3
        for i in range(1, 10):
            button = tk.Button(self.master, text=i, width=10, height=5)
            button.grid(row=3 - (i - 1) // 3, column=(i - 1) % 3, sticky=tk.W)
            button.bind("<Button-1>", self.handle_button_click)

        # Generate buttons in a vertical column on the right edge
        for i, j in enumerate(operator_button):
            ope_button = tk.Button(self.master, text=j, width=10, height=5)
            ope_button.grid(row=i + 1, column=3)
            ope_button.bind("<Button-1>", self.handle_button_click)

        # Generate a button in the second row below
        for i, k in enumerate(string_button):
            str_button = tk.Button(self.master, text=k, width=10, height=5)
            str_button.grid(row=4, column=i)
            str_button.bind("<Button-1>", self.handle_button_click)

        # Generate a button in the first row below
        for i, k in enumerate(additional_button):
            add_button = tk.Button(self.master, text=k, width=10, height=5)
            add_button.grid(row=5, column=i)
            add_button.bind("<Button-1>", self.handle_button_click)

    @staticmethod
    def button_click(event: any) -> list[list[str]]:

        """button click function"""

        event.widget.config()
        print(
            f"button clicked: {(event.widget["text"])}"
        )


class Calculation:
    def __init__(self, entry_widget) -> None:
        self.entry_widget = entry_widget
        print("Process started!", "\n" + "-" * 20)

    def __get_text(self) -> str:
        return self.entry_widget.get()

    def __insert_text(self, text: str) -> None:
        return self.entry_widget.insert(tk.END, text)

    def __clear(self) -> None:
        return self.entry_widget.delete(0, tk.END)

    def __one_delete(self) -> None:
        del_text = self.__get_text()
        return self.entry_widget.delete(len(del_text) - 1, tk.END)

    def __evaluate(self) -> bool:
        _replace = str.maketrans(
            {
                "+": "+", "-": "-", "×": "*", "÷": "/", "^": "**", "√": "**0.5"
            }
        )

        expression = self.__get_text().translate(_replace)
        try:
            result = eval(expression)
            self.__clear()
            self.__insert_text(str(result))
            print(
                "-" * 20, "\n" + f"Answer: {result}", "\n" + "-" * 20
            )

        except Exception as exception:
            self.__clear()
            self.__insert_text(f"(Error)")
            print(
                "-" * 20, "\n" + f"Error: {exception}", "\n" + "-" * 20
            )

    def __perform_action__(self, action: str) -> list[list[str]]:
        _action = {
            "=": self.__evaluate,
            "AC": self.__clear,
            "C": self.__one_delete,
        }

        act_func = _action.get(action, lambda: self.__insert_text(action))
        act_func()


def main():
    root = tk.Tk()
    App = Display(master=root)
    App.mainloop()
    if sys.exit:
        print("\n\n" + "Process terminated!")


if __name__ == "__main__":
    main()
