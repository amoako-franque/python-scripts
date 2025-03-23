import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
)
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet(
            """
            QPushButton, QLabel{
            font-family: Operator Mono;
            font-weight: bold;
            padding: 20px;
            }
                           QPushButton{
                           background-color: gray;
                           font-size: 40px;
                           }

                           QLabel{
                           font-size: 80px;
                           color: gray;
                           background-color: light-gray;
                           border-radius: 20px;
                           }

                           """
        )

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_timer(self.time))

    def format_timer(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_timer(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_clock = StopWatch()
    stop_clock.show()
    sys.exit(app.exec_())
