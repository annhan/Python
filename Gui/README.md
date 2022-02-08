# **Gui với python**

- Dùng module PyQt5 - một thư viện cho phép bạn sử dụng Qt GUI

- Cài đặt PyQt5 ```python -m pip install PyQt5 # pip install PyQt5```
- Cài [QTDesigner](https://build-system.fman.io/qt-designer-download) 

# **QT Designed**

- Dùng QTDesigner thiết kế giao diện file UI.
- Dùng uic.loadUi để link file Ui tới Python.
- Link các event button

vd: self.btnPreLine.clicked.connect(lambda data,status="pre" : self.btnEditline_click(status)) 