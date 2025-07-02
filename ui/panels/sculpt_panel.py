from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class SculptPanel(QWidget):
    def __init__(self, system):
        super().__init__()
        self.system = system
        layout = QVBoxLayout(self)
        btn = QPushButton("Open Sculpt in Blender")
        btn.clicked.connect(self.on_sculpt)
        layout.addWidget(btn)

    def on_sculpt(self):
        self.system.open_sculpt_in_blender()