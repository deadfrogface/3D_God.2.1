from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class RiggingPanel(QWidget):
    def __init__(self, system):
        super().__init__()
        self.system = system
        layout = QVBoxLayout(self)
        btn = QPushButton("Auto Rig & Skin")
        btn.clicked.connect(self.on_rig)
        layout.addWidget(btn)

    def on_rig(self):
        self.system.auto_rig_character()