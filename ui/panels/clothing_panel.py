from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget

class ClothingPanel(QWidget):
    def __init__(self, system):
        super().__init__()
        self.system = system
        self.list = QListWidget()
        btn = QPushButton("Platzhalter Kleidung hinzufügen")
        btn.clicked.connect(self.add_dummy)
        layout = QVBoxLayout(self)
        layout.addWidget(self.list)
        layout.addWidget(btn)

    def add_dummy(self):
        name = self.system.add_clothing("DummyShirt")
        self.list.addItem(name)