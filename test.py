import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from subprocess import Popen

def start_program():
    # Hier den Pfad zu deinem Python-Programm einfügen
    program_path = 'C:\Gebaerdenstuff\main.py'
    
    # Programm starten
    process = Popen(['python', program_path])

class BasicUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Layout erstellen
        layout = QVBoxLayout()

        # Start-Button hinzufügen
        start_button = QPushButton('Start')
        start_button.clicked.connect(start_program)
        layout.addWidget(start_button)

        # Widget konfigurieren
        self.setLayout(layout)
        self.setWindowTitle('Basic UI mit Start-Button')
        self.show()

def main():
    app = QApplication(sys.argv)
    ui = BasicUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
