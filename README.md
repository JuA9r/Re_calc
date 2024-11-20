# **Calculator Application**

## **Execution Environment**
- **Python**: 3.12  
- **Tkinter**: 8.6  

---

## **Overview**
- This project implements a **simple calculator** using the `tkinter` library in Python. 
- This calculator is capable of basic mathematical operations and allows user input via the keyboard.

### **Features**
- Intuitive GUI with buttons for input and operations.
- Supports numerical input using both mouse clicks and keyboard.
- Performs:
  - **Addition (+)**  
  - **Subtraction (-)**  
  - **Multiplication (×)**  
  - **Division (÷)**  
  - **Power calculation (^)**  
  - **Square root (√)**  
  - **Input clearing options**: clear last (C) and All Clear (AC).

---

## **Code Structure**
### **Main Functionalities**
1. **Window Creation**  
   - Use `tkinter` to create a calculator with a formula and a text input box to display the result.

2. **Button Generation**  
   - Generates numeric buttons (`0-9`), operator buttons (`+`, `-`, `×`, `÷`), and additional functionality buttons (`C`, `AC`, `^`, `√`).

3. **Text Box Input Restrictions**  
   - Ensures only valid characters (numbers, operators, parentheses, etc.) can be entered.

4. **Arithmetic Operations**  
   - Supports basic four arithmetic operations and advanced power calculation.

5. **Error Handling**  
   - Displays an appropriate error message when an error occurs.

---

## **How to Use**
1. Run the program with Python 3.12 or later.
2. Use the GUI buttons or keyboard to input numbers and operations.
3. Click `=` to calculate the result.
4. Use `C` to delete the last input character and `AC` to clear the entire formula.

---

## **ToDo**
### **Completed**
- [x] Create the main calculator window.
- [x] Generate numeric and operator buttons.
- [x] Restrict invalid characters in the input box.
- [x] Enable numerical input and basic operations.
- [x] Clear formulas (`C` and `AC`).
- [x] Display calculation results.
- [x] Power calculation using `^`.

### **Pending**
- [ ] Add factorial calculation functionality (`n!`).

---

## **Future Improvements**
- Allow parentheses for more complex expressions.
- Improve error messages to be more descriptive.

---
