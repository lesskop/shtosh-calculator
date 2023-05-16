from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal


class CustomLabel(QLabel):
    textChanged = Signal()

    def setText(self, text):
        super().setText(text)
        self.textChanged.emit()
