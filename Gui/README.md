# **Gui với python**

- Dùng module PyQt5 - một thư viện cho phép bạn sử dụng Qt GUI

- Cài đặt PyQt5 ```python -m pip install PyQt5 # pip install PyQt5```
- Cài [QTDesigner](https://build-system.fman.io/qt-designer-download) 

# **QT Designed**

Mở QT Disigner chọn main Windown.

- Các widget trong nhóm ```Layouts``` sẽ giúp các widget trên ứng dụng bạn co giãn tùy theo kích cỡ window.

- Đối với các Widget chúng ta cần truy xuất ở phần Back-end để xử lí thì các bạn nên thay đổi thuộc tính objectName để dễ dàng xử lí và gọi tên.
```
Label: Dùng để hiển thị nội dụng text đơn thuần. Double click để chỉnh sửa nội dung.

Group Box: Dùng để nhóm các Widget có cùng mục đích lại với nhau.
Line edit: Dùng để nhập dữ liệu dạng 1 dòng (tương tự thẻ <input> trong HTML).

Combo Box: Dùng để người dùng chọn các nội dung có sẵn. Các bạn double click vào để thêm các item lựa chọn.

Check Box: Cho phép người dụng chọn hoặc bỏ chọn 1 nội dung. Double click để chỉnh sửa label

Spin box: Tương tự như Line Edit nhưng chỉ được phép nhập số.

Push Button: Đơn giản là một cái nút nhấn. Double click để chỉnh sửa nội dung
```

- ```Ctrl + R``` để xem trước giao diện

- Tạo file ui.

```
python -m pyuic5 -x <duong_dan_file_giao_dien.ui> -o <duong_dan_file_ket_qua.py>

#vi du: python -m pyuic5 -x giaodien.ui -o main.py

#hoac pyuic5 -x giaodien.ui -o main.py
```

- Nếu khi tạo có lỗi ```qt platfirm plkugin could be init...```

```
Copy thư mục platforms của đường dẫn "C:\Python33\Lib\site-packages\PyQt5\plugins\platforms" (Mỗi phiên bản Python sẽ có đường dẫn khác nhau)

Paste thư mục đó vào thư mục chứa code của chúng ta

Cuối cùng thêm 2 dòng này vào trên cùng của chương trình:

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ".\\platform\\"

```

- Mặc định PyQt5 sử dụng giao diện cũ nên bạn có thể thêm lệnh setStyle()

```python
app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
```

# **Xây dựng back-end**

- Trong setup ui ta tạo liên kêt về click trong thuộc tính button bằng cách add ```self.calcBtn.clicked.connect(self.calcTotal)```

- Lệnh này sẽ gọi hàm ```calcTotal``` trong cùng class ui khi calcbtn được nhấn.

- Popup 1 tin nhắn
```python

msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Chào {} {}!".format("Ông" if self.sex.currentText() == "Nam" else "Bà", self.fullname.text()))
        msg.setInformativeText(" Tổng chi phí là {}vnđ".format(str(sum)))
        msg.setWindowTitle("Thống kê")
        msg.exec_()

```