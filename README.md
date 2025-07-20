# 📥 CDM - Custom Download Manager

**CDM** is a lightweight and customizable download manager built by a student using Python and PyQt5.  
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

Users input a URL, choose where to save the file, and start the download using CDM’s interface.  
Behind the scenes, the tool splits the file into parts based on the selected thread count and downloads each segment concurrently, dramatically increasing performance for supported servers.

## 🚀 Getting Started

To run the application:

```bash
python main.py
