import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from design import Ui_MainWindow

operations = {
    '+': add,
    '−': sub,
    '×': mul,
    '/': truediv
}

error_zero_div = 'Division by zero'
error_undefined = 'Result is undefined'

default_font_size = 16
default_entry_font_size = 40


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.entry = self.ui.le_entry
        self.temp = self.ui.lbl_temp
        self.entry_max_len = self.entry.maxLength()

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

        # digits
        self.ui.btn_0.clicked.connect(self.add_digit)
        self.ui.btn_1.clicked.connect(self.add_digit)
        self.ui.btn_2.clicked.connect(self.add_digit)
        self.ui.btn_3.clicked.connect(self.add_digit)
        self.ui.btn_4.clicked.connect(self.add_digit)
        self.ui.btn_5.clicked.connect(self.add_digit)
        self.ui.btn_6.clicked.connect(self.add_digit)
        self.ui.btn_7.clicked.connect(self.add_digit)
        self.ui.btn_8.clicked.connect(self.add_digit)
        self.ui.btn_9.clicked.connect(self.add_digit)

        # actions
        self.ui.btn_clear.clicked.connect(self.clear_all)
        self.ui.btn_ce.clicked.connect(self.clear_entry)
        self.ui.btn_point.clicked.connect(self.add_point)
        self.ui.btn_neg.clicked.connect(self.negate)
        self.ui.btn_backspace.clicked.connect(self.backspace)

        # math
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_add.clicked.connect(self.math_operation)
        self.ui.btn_sub.clicked.connect(self.math_operation)
        self.ui.btn_mul.clicked.connect(self.math_operation)
        self.ui.btn_div.clicked.connect(self.math_operation)

    def add_digit(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        btn = self.sender()

        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')

        if btn.objectName() in digit_buttons:
            if self.entry.text() == '0':
                self.entry.setText(btn.text())
            else:
                self.entry.setText(self.entry.text() + btn.text())

        self.adjust_entry_font_size()

    def add_point(self) -> None:
        self.clear_temp_if_equality()
        if '.' not in self.entry.text():
            self.entry.setText(self.entry.text() + '.')
            self.adjust_entry_font_size()

    def negate(self) -> None:
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if '-' not in entry:
            if entry != '0':
                entry = '-' + entry
        else:
            entry = entry[1:]

        if len(entry) == self.entry_max_len + 1 and '-' in entry:
            self.entry.setMaxLength(self.entry_max_len + 1)
        else:
            self.entry.setMaxLength(self.entry_max_len)

        self.entry.setText(entry)
        self.adjust_entry_font_size()

    def backspace(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        entry = self.entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.entry.setText('0')
            else:
                self.entry.setText(entry.replace('0', ''))  # entry[:-1]
        else:
            self.entry.setText('0')

        self.adjust_entry_font_size()

    def clear_all(self) -> None:
        self.remove_error()
        self.entry.setText('0')
        self.adjust_entry_font_size()
        self.temp.clear()
        self.adjust_temp_font_size()

    def clear_entry(self) -> None:
        self.remove_error()
        self.clear_temp_if_equality()
        self.entry.setText('0')
        self.adjust_entry_font_size()

    def clear_temp_if_equality(self) -> None:
        if self.get_math_sign() == '=':
            self.temp.clear()
            self.adjust_temp_font_size()

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n.replace('.0', '') if n.endswith('.0') else n
        # return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.entry.text())

        if not self.temp.text() or self.get_math_sign() == '=':
            self.temp.setText(entry + f' {btn.text()} ')
            self.adjust_temp_font_size()
            self.entry.setText('0')
            self.adjust_entry_font_size()

    def get_entry_num(self) -> Union[int, float]:
        entry = self.entry.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.temp.text():
            temp = self.temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.temp.text():
            return self.temp.text().strip('.').split()[-1]

    def get_entry_text_width(self) -> int:
        return self.entry.fontMetrics().boundingRect(self.entry.text()).width()

    def get_temp_text_width(self) -> int:
        return self.temp.fontMetrics().boundingRect(self.temp.text()).width()

    def calculate(self) -> Optional[str]:
        entry = self.entry.text()
        temp = self.temp.text()

        if temp:
            try:
                result = self.remove_trailing_zeros(
                    str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
                )
                self.temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
                self.adjust_temp_font_size()
                self.entry.setText(result)
                self.adjust_entry_font_size()
                return result

            except KeyError:
                pass

            except ZeroDivisionError:
                if self.get_temp_num() == 0:
                    self.show_error(error_undefined)
                else:
                    self.show_error(error_zero_div)

    def math_operation(self) -> None:
        temp = self.temp.text()
        btn = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.temp.setText(temp[:-2] + f'{btn.text()} ')  # replace sign
            else:
                try:
                    self.temp.setText(self.calculate() + f' {btn.text()} ')
                except TypeError:
                    pass

        self.adjust_temp_font_size()

    def show_error(self, text: str) -> None:
        self.entry.setMaxLength(len(text))
        self.entry.setText(text)
        self.adjust_entry_font_size()
        self.disable_buttons(True)

    def remove_error(self) -> None:
        if self.entry.text() in (error_undefined, error_zero_div):
            self.entry.setMaxLength(self.entry_max_len)
            self.entry.setText('0')
            self.adjust_entry_font_size()
            self.disable_buttons(False)

    def disable_buttons(self, disable: bool) -> None:
        self.ui.btn_calc.setDisabled(disable)
        self.ui.btn_add.setDisabled(disable)
        self.ui.btn_sub.setDisabled(disable)
        self.ui.btn_mul.setDisabled(disable)
        self.ui.btn_div.setDisabled(disable)
        self.ui.btn_neg.setDisabled(disable)
        self.ui.btn_point.setDisabled(disable)

        color = 'color: #888;' if disable else 'color: white;'
        self.change_buttons_color(color)

    def change_buttons_color(self, css_color: str) -> None:
        self.ui.btn_calc.setStyleSheet(css_color)
        self.ui.btn_add.setStyleSheet(css_color)
        self.ui.btn_sub.setStyleSheet(css_color)
        self.ui.btn_mul.setStyleSheet(css_color)
        self.ui.btn_div.setStyleSheet(css_color)
        self.ui.btn_neg.setStyleSheet(css_color)
        self.ui.btn_point.setStyleSheet(css_color)

    def adjust_entry_font_size(self) -> None:
        font_size = default_entry_font_size
        while self.get_entry_text_width() > self.entry.width() - 15:
            font_size -= 1
            self.entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

        font_size = 1
        while self.get_entry_text_width() < self.entry.width() - 60:
            font_size += 1

            if font_size > default_entry_font_size:
                break

            self.entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = default_font_size
        while self.get_temp_text_width() > self.temp.width() - 10:
            font_size -= 1
            self.temp.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.temp.width() - 60:
            font_size += 1

            if font_size > default_font_size:
                break

            self.temp.setStyleSheet('font-size: ' + str(font_size) + 'pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_entry_font_size()
        self.adjust_temp_font_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
