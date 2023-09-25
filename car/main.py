import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setWindowTitle("Car Parking Management")
        self.setGeometry(100, 100, 400, 200)
        self.label = QLabel("Car Number:", self)
        self.label.move(20, 30)
        self.car_number_input = QLineEdit(self)
        self.car_number_input.move(120, 30)
        self.entry_button = QPushButton("Entry", self)
        self.entry_button.move(120, 70)
        self.entry_button.clicked.connect(self.entry)
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.move(220, 70)
        self.exit_button.clicked.connect(self.exit)
        self.result_label = QLabel(self)
        self.result_label.move(120, 110)
        self.result_label.setText("Result will be displayed here.")

    def entry(self):
        car_number = self.car_number_input.text()
        self.result_label.setText(f"Entry for car {car_number}")

    def exit(self):
        car_number = self.car_number_input.text()
        self.result_label.setText(f"Exit for car {car_number}")

def main():
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
