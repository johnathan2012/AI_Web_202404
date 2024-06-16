# Text元件

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Text元件')
txt = tk.Text(root, width = 35, height = 7)

txt.pack(padx = 5, pady = 5)

#設定Text的屬性來各別使用
txt.tag_config('ft_bold',
    font =('Verdana', 14, 'bold', 'italic'))

txt.tag_config('title', justify = 'center',
    underline= 1, font =('Arial', 24, 'bold'))

txt.tag_config('tine', foreground = 'blue',
    font = ('Lucida Bright', 14))

txt.tag_config('bd', relief = 'groove',
    borderwidth = 4, font = ('Levenim MT', 20))

# insert()方法從最後一個字元插入字串
txt.insert('end', 'A Coat\n', 'title')
txt.insert('end', 'I made my song a coat\n',
    'ft_bold')
txt.insert('end', 'Covered with embroideries\n', 'tine')
txt.insert('end', 'From heel to throat\n', 'bd')
root.mainloop()
