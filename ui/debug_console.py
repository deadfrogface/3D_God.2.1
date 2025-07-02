from PySide6.QtWidgets import QDockWidget, QTextEdit

class DebugConsole(QDockWidget):
    def __init__(self):
        super().__init__("Debug Console")
        self.setAllowedAreas()
        text = QTextEdit()
        text.setReadOnly(True)
        self.setWidget(text)
        self.visible = False

    def toggle(self):
        self.visible = not self.visible
        self.setVisible(self.visible)