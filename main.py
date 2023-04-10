import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


def convert_string_to_ascii(s):
    """Convert a string to its ASCII representation"""
    return [ord(c) for c in s]


def convert_decimal_to_binary(decimal):
    """Convert a decimal number to binary"""
    return bin(decimal)


def convert_decimal_to_hexadecimal(decimal):
    """Convert a decimal number to hexadecimal"""
    return hex(decimal)


def convert_decimal_to_octal(decimal):
    """Convert a decimal number to octal"""
    return oct(decimal)


class ConverterGUI(QWidget):

    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Number Converter")
        self.setGeometry(100, 100, 600, 400)

        # Create widgets
        self.type_label = QLabel("Select type:", self)
        self.type_label.setGeometry(50, 50, 100, 30)
        self.type_combo = QComboBox(self)
        self.type_combo.setGeometry(150, 50, 150, 30)
        self.type_combo.addItem("String")
        self.type_combo.addItem("Decimal")
        self.type_combo.addItem("Exit")
        self.input_label = QLabel("Input:", self)
        self.input_label.setGeometry(50, 100, 100, 30)
        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(150, 100, 150, 30)
        self.output_label = QLabel("Output:", self)
        self.output_label.setGeometry(50, 150, 100, 30)
        self.output_box = QTextEdit(self)
        self.output_box.setGeometry(150, 150, 400, 200)
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setGeometry(350, 100, 100, 30)

        # Connect signal to slot
        self.convert_button.clicked.connect(self.convert)

        # Set font
        font = QFont()
        font.setPointSize(12)
        self.type_label.setFont(font)
        self.input_label.setFont(font)
        self.output_label.setFont(font)

    def convert(self):
        input_type = self.type_combo.currentText().lower()
        input_value = self.input_box.text()

        if input_type == "string":
            ascii_values = convert_string_to_ascii(input_value)
            output_value = "ASCII representation: " + str(ascii_values)
        elif input_type == "decimal":
            decimal = int(input_value)
            binary = convert_decimal_to_binary(decimal)
            hexadecimal = convert_decimal_to_hexadecimal(decimal)
            octal = convert_decimal_to_octal(decimal)
            output_value = f"Binary representation: {binary}\nHexadecimal representation: {hexadecimal}\nOctal representation: {octal}"
        elif input_type == "exit":
            sys.exit()

        self.output_box.setText(output_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = ConverterGUI()
    converter.show()
    sys.exit(app.exec_())
