from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QProgressBar, QFileDialog, QMainWindow
from downloader import DownloadWorker
import os

class CDMApp(QMainWindow):
    def __init__(self, max_lines=64):
        super().__init__()
        self.setWindowTitle("CDM - Custom Download Manager")
        self.setGeometry(200, 200, 400, 200)

        self.max_lines = max_lines

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter download URL")
        self.layout.addWidget(self.url_input)

        self.path_label = QLabel("Save Path: (default: ./downloads)")
        self.layout.addWidget(self.path_label)

        self.select_path_btn = QPushButton("Choose Save Folder")
        self.select_path_btn.clicked.connect(self.choose_path)
        self.layout.addWidget(self.select_path_btn)

        self.download_btn = QPushButton("Start Download")
        self.download_btn.clicked.connect(self.start_download)
        self.layout.addWidget(self.download_btn)

        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)

        self.status = QLabel("")
        self.layout.addWidget(self.status)
        self.setCentralWidget(self.central_widget)
        self.save_path = os.path.join(os.getcwd(), "downloads")
        os.makedirs(self.save_path, exist_ok=True)

        self.max_lines = max_lines

    def choose_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.save_path = folder
            self.path_label.setText(f"Save Path: {folder}")

    def start_download(self):
        url = self.url_input.text()
        if not url:
            self.status.setText("❗ URL cannot be empty")
            return

        self.worker = DownloadWorker(url, self.save_path)
        self.worker.progress.connect(self.progress.setValue)
        self.worker.finished.connect(self.download_finished)
        self.worker.start()
        self.status.setText("⬇️ Downloading...")

    def download_finished(self, message):
        self.status.setText(f"✅ {message}")
        self.progress.setValue(0)

    def append_text(self, text):
        self.text_edit.append(text)
        lines = self.text_edit.toPlainText().split('\n')
        if len(lines) > self.max_lines:
            # 只保留最後 max_lines 條
            self.text_edit.setPlainText('\n'.join(lines[-self.max_lines:]))

    def set_max_lines(self, lines):
        self.max_lines = lines
