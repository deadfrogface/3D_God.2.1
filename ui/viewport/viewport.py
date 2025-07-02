from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
class Viewport3D(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("3D Viewport Placeholder")
        layout.addWidget(self.label)

    def display_model(self, model_path):
        self.label.setText(f"3D Model: {model_path}")