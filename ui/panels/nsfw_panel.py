from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox

class NSFWPanel(QWidget):
    def __init__(self, system):
        super().__init__()
        self.system = system
        layout = QVBoxLayout(self)
        chk = QCheckBox("NSFW sichtbar")
        chk.setChecked(True)
        chk.toggled.connect(self.on_toggle)
        layout.addWidget(chk)

    def on_toggle(self, state):
        print(f"NSFW toggled: {state}")
        self.system.toggle_nsfw(state)