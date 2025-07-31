import sys
import os

os.environ["QT_QPA_PLATFORM"] = "wayland"

from PyQt6.QtWidgets import QApplication
from app_window import MainWindow

def run_app():
    app = QApplication(sys.argv)

    main_win = MainWindow()

    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()