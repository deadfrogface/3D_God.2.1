import sys
from PySide6.QtWidgets import QApplication
from ui.gui_main_window import MainWindow
import json

if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {"theme": "dark", "nsfw_mode": True, "controller_enabled": True}

    window = MainWindow(config)
    window.show()
    sys.exit(app.exec())