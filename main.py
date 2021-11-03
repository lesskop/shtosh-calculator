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


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        # math
        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_add.clicked.connect(self.math_operation)
        self.ui.btn_sub.clicked.connect(self.math_operation)
        self.ui.btn_mul.clicked.connect(self.math_operation)
        self.ui.btn_div.clicked.connect(self.math_operation)

    def add_digit(self):
        btn = self.sender()

        digit_buttons = ('btn_0', 'btn_1', 'btn_2', 'btn_3', 'btn_4',
                         'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9')

        if btn.objectName() in digit_buttons:
            if self.ui.le_entry.text() == '0':
                self.ui.le_entry.setText(btn.text())
            else:
                self.ui.le_entry.setText(self.ui.le_entry.text() + btn.text())

    def add_point(self) -> None:
        if '.' not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + '.')

    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lbl_temp.clear()

    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def add_temp(self) -> None:
        btn = self.sender()
        entry = self.remove_trailing_zeros(self.ui.le_entry.text())

        if not self.ui.lbl_temp.text() or self.get_math_sign() == '=':
            self.ui.lbl_temp.setText(entry + f' {btn.text()} ')
            self.ui.le_entry.setText('0')

    def get_entry_num(self) -> Union[int, float]:
        entry = self.ui.le_entry.text().strip('.')
        return float(entry) if '.' in entry else int(entry)

    def get_temp_num(self) -> Union[int, float, None]:
        if self.ui.lbl_temp.text():
            temp = self.ui.lbl_temp.text().strip('.').split()[0]
            return float(temp) if '.' in temp else int(temp)

    def get_math_sign(self) -> Optional[str]:
        if self.ui.lbl_temp.text():
            return self.ui.lbl_temp.text().strip('.').split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lbl_temp.text()

        if temp:
            result = self.remove_trailing_zeros(
                str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
            )
            self.ui.lbl_temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
            self.ui.le_entry.setText(result)
            return result

    def math_operation(self) -> None:
        temp = self.ui.lbl_temp.text()
        btn = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_math_sign() != btn.text():
                if self.get_math_sign() == '=':
                    self.add_temp()
                else:
                    self.ui.lbl_temp.setText(temp[:-2] + f'{btn.text()} ')
            else:
                self.ui.lbl_temp.setText(self.calculate() + f' {btn.text()}')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
