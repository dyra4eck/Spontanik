from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QVBoxLayout, QWidget,
    QPushButton, QHBoxLayout
                             )
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.seconds_left = 60
        self.timer_running = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Спонтаника")
        self.resize(800, 600)

        self.statusBar().showMessage("Готово")

        # центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # вертикальный макет для текста
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # верхняя панель: таймер и кнопки
        top_panel = QWidget()
        top_layout = QHBoxLayout()
        top_panel.setLayout(top_layout)

        # виджет для таймера
        timer_widget = QWidget()
        timer_layout = QVBoxLayout()
        timer_widget.setLayout(timer_layout)

        self.timer_label = QLabel(self.format_time(self.seconds_left))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.timer_label.setStyleSheet("""
            color: #2c3e50;
            background-color: #ecf0f1;
            border: 2px solid #bdc3c7;
            border-radius: 10px;
            padding: 15px;
        """)
        timer_layout.addWidget(self.timer_label)

        top_layout.addStretch(1)
        top_layout.addWidget(timer_widget)

        # кнопки управления
        buttons_widget = QWidget()
        buttons_layout = QVBoxLayout()
        buttons_widget.setLayout(buttons_layout)

        # старт
        self.start_button = QPushButton("Старт")
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        self.start_button.clicked.connect(self.start_timer)
        buttons_layout.addWidget(self.start_button)

        # стоп
        self.stop_button = QPushButton("Пауза")
        self.stop_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        self.stop_button.clicked.connect(self.stop_timer)
        buttons_layout.addWidget(self.stop_button)

        # сброс
        self.reset_button = QPushButton("Сброс")
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.reset_button.clicked.connect(self.reset_timer)
        buttons_layout.addWidget(self.reset_button)

        # добавление виджета с кнопками в верхний макет
        top_layout.addWidget(buttons_widget)
        main_layout.addWidget(top_panel)

        # QTimer
        self.timer = QTimer()
        self.timer.setInterval(1000) # каждую секунду (1000 мсек)
        self.timer.timeout.connect(self.update_timer)

        # растягивающий элемент внизу
        main_layout.addStretch(1)

        self.show()

    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"

    def start_timer(self):
        if not self.timer_running and self.seconds_left > 0:
            self.timer_running = True
            self.timer.start()
            self.statusBar().showMessage("Таймер запущен")
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.timer.stop()
            self.statusBar().showMessage("Таймер остановлен")
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)

    def reset_timer(self):
        self.stop_timer()
        self.seconds_left = 60
        self.timer_label.setText(self.format_time(self.seconds_left))
        self.statusBar().showMessage("Таймер сброшен")
        self.start_button.setEnabled(True)

    def update_timer(self):
        if  self.seconds_left > 0:
            self.seconds_left -= 1
            self.timer_label.setText(self.format_time(self.seconds_left))

            if self.seconds_left <= 5:
                self.timer_label.setStyleSheet("""
                    color: #c0392b;
                    background-color: #fadbd8;
                    border: 2px solid #e74c3c;
                    border-radius: 10px;
                    padding: 15px;
                    font-weight: bold;
                """)
        else:
            self.stop_timer()
            self.statusBar().showMessage("Время вышло")
            self.timer_label.setStyleSheet("""
                color: #2c3e50;
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                padding: 15px;
            """)