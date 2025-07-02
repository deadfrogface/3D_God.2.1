from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtWidgets import QApplication

class StyleManager:
    @staticmethod
    def apply_theme(theme):
        app = QApplication.instance()
        if theme == "dark":
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(30,30,30))
            palette.setColor(QPalette.WindowText, QColor(220,220,220))
            app.setPalette(palette)
        elif theme=="light":
            app.setPalette(app.style().standardPalette())
        font = QFont("Segoe UI", 10)
        app.setFont(font)