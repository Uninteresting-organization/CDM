from gui.main_ui import CDMApp
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CDMApp()
    window.show()
    sys.exit(app.exec_())
