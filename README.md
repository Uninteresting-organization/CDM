# 📥 SDM - Custom Download Manager

**SDM** is a lightweight and customizable download manager built by a student using Python and PyQt5.  
It features a user-friendly graphical interface and supports multithreaded downloading for improved speed and flexibility.

## 🔧 Features

- 🖼️ GUI built with PyQt5
- 📡 Supports multiple concurrent threads (up to 64)
- 🗂️ Save path selector
- 📊 Download progress indicator
- 🧠 Configurable thread count via GUI
- 📝 Built-in logging system
- 🚀 Future-ready structure for expansion (batch downloading, protocol support, etc.)

## 💡 How it works

Users input a URL, choose where to save the file, and start the download using SDM’s interface.  
Behind the scenes, the tool splits the file into parts based on the selected thread count and downloads each segment concurrently, dramatically increasing performance for supported servers.

## 🚀 Getting Started

To run the application:

```bash
python main.py
```

# 📥 SDM - 自訂式下載管理器（Simple Download Manager）

**SDM** 是一款由學生以 Python 和 PyQt5 開發的輕量型下載管理器，  
具備直覺式使用介面，並支援多執行緒下載，讓檔案下載更快速、更彈性。

## 🔧 主要功能

- 🖼️ 使用 PyQt5 建立的圖形化介面
- 📡 支援最多 64 條執行緒並行下載
- 🗂️ 自訂儲存路徑
- 📊 顯示下載進度
- 🎛️ GUI 可調整執行緒數量
- 📝 內建日誌記錄功能
- 🧩 架構簡潔，易於擴充（未來可加入批次下載、協定支援等）

## 💡 使用方式

使用者輸入下載網址、選擇儲存位置，即可開始下載。  
SDM 將檔案依執行緒數量切割為多個區段，並以多執行緒方式並行下載，大幅提升效率（伺服器需支援 Range 標頭）。

## 🚀 快速開始

執行主程式：

```bash
python main.py
