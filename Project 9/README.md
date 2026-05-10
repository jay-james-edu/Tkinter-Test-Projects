# Temperature Converter MVC App

## Description

This project is a simple desktop **Temperature Converter** application built with **Python**, **PySide6**, and the **Model-View-Controller (MVC)** design pattern.

The application lets the user enter a temperature in **Celsius**, click a button, and see the converted temperature in **Fahrenheit**. It is meant to be a small proof-of-concept GUI application that demonstrates clean project structure, basic input validation, signal-slot connections, and separation of responsibilities between the Model, View, and Controller.

## Features

- Desktop GUI built with PySide6
- Celsius to Fahrenheit conversion
- Clear MVC project organization
- Cross-platform structure for Windows, macOS, and Linux

## Project Structure

```text
project_root/
│
├── main.py          # Application entry point
├── model.py         # Model logic and temperature conversion
├── controller.py    # Controller logic and signal-slot connections
├── view.py          # Python file generated from the Qt Designer UI
└── README.md        # Project documentation
```

## MVC Overview

This project follows the **Model-View-Controller** pattern.

### Model

The **Model** is located in `model.py`.

It stores the Celsius value, validates user input by converting the string input into a number, and performs the Celsius-to-Fahrenheit calculation.

Responsibilities:

- Store application data
- Validate numeric input
- Convert Celsius to Fahrenheit

### View

The **View** is located in `view.py`.

It contains the user interface elements, including:

- A label asking the user to enter Celsius
- A text input box for Celsius
- A conversion button
- A Fahrenheit output label

The View is responsible for displaying the GUI layout and widgets. It does not contain the temperature conversion logic.

### Controller

The **Controller** is located in `controller.py`.

It connects the button click signal to the conversion method, reads the input from the View, sends the input to the Model, and updates the View with either the converted Fahrenheit value or an error message.

Responsibilities:

- Connect GUI events to application logic
- Pass user input from the View to the Model

### Entry Point

The application starts in `main.py`.

`main.py` creates the `QApplication`, creates the `TemperatureController`, shows the main window, and starts the PySide6 event loop.

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check by running:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Install PySide6

Install the required PySide6 package:

```bash
pip install PySide6
```

### 3. Run the Application

From the project folder, run:

```bash
python main.py
```

or, depending on your system:

```bash
python3 main.py
```

## How to Use

1. Open the application.
2. Enter a Celsius temperature into the text box.
3. Click **Convert to Fahrenheit**.
4. The Fahrenheit result will appear below the button.
5. If the input is not a valid number, an error message will appear.

## Example

Input:

```text
0
```

Output:

```text
32.00 °F
```

Input:

```text
100
```

Output:

```text
212.00 °F
```

## Requirements

- Python 3
- PySide6
- Qt Designer used to create the original UI file
