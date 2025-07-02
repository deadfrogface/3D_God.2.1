from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class ExportPanel(QWidget):
    def __init__(self, system):
        super().__init__()
        self.system = system
        layout = QVBoxLayout(self)
        btn = QPushButton("Export FBX")
        btn.clicked.connect(self.on_export)
        layout.addWidget(btn)

    def on_export(self):
        self.system.export_character()