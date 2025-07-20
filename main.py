from gui.main_ui import CDMApp
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CDMApp()
    window.show()
    sys.exit(app.exec_())

# 你可以在這裡加入更多功能，例如訊息提示或初始化設定
# 例如：
# print("CDM 應用程式已啟動")
