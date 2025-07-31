from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Спонтаника")
        self.resize(800, 600)

        self.statusBar().showMessage("Готово")

        # центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # вертикальный макет для текста
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # текстовая метка
        label = QLabel("Так начиналась спонтаника")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) # выравнивает текст по центру строки
        label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            margin: 20px;
        """)

        layout.addWidget(label)
        # Добавляет гибкое пространство, которое "растягивается";
        # Прижимает предыдущие элементы к верху окна
        layout.addStretch() # без этого текст будет по центру виджета;

        self.show()
