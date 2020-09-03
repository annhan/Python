# Package trong Python.

Package trong Python là một thư mục chứa một hoặc nhiều modules hay các package khác nhau, nó được tạo ra  nhằm mục đích phân bố các modules có cùng chức năng hay một cái gì đó, để dễ quản lý source code. 

Để tạo package ta tạo thư mục mới. Với tên folder là tên package. Trong thư mục này tạo file ```__init__.py.``` file này giống như constructor nó sẽ được khởi tạo và chạy khi ta import package.

VD ta tạo package có tên demopackage với file ```__init__.py```
```
|demopackage/__init__.py
|main.py
```

File ```__init__.py```

```
# __init__.py
print("Print frome file __init__py")
```

Hàm main.py

```
# main.py
import demopackage
```
Lúc này màn hình sẽ in ra ```Print frome file __init__py``` do file được chạy ngay khi import package.

# Import packgage

```
|--demopackage/
|             |--lib.py
|             └── __init__py
|--main.py
```

File lib.py

```
# demopackage/lib.py
def hello():
    print("Hello!")

def goodbye():
    print("Goodbye!")

```

Lúc này ta muốn import lib.py vào main.py ta làm như sau

```
# main.py
from demopackage.lib import *
hello()
# Hello!

goodbye()
# Goodbye!
```

Hoặc

```
# main.py
import demopackage.lib
# Duoc in tu file __init__py

demopackage.lib.hello()
# Hello!

demopackage.lib.goodbye()
# Goodbye!

```

Hoặc

```
# main.py
import demopackage.lib as lib
# Duoc in tu file __init__py

lib.hello()
# Hello!

lib.goodbye()
# Goodbye!
```