import sys
from PyQt5.QtWidgets import *

'''
Tugas:
1. Munculkan setiap karakter yang ada pada variabel `_nim` menjadi pilihan combobox
2. Sesuaikan variabel `_nim` sesuai dengan NIM masing-masing
3. Hubungkan signal `currentIndexChanged()` pada `cb` dengan method `_on_select()`
'''
_nim = 'F1D022126'


class ComboBox(QWidget):

    def __init__(self, parent=None):
        super(ComboBox, self).__init__(parent)

        layout = QHBoxLayout()
        self.cb = QComboBox()
        self.cb.addItems(list(_nim))

        self.cb.currentIndexChanged.connect(self._on_select)
        self.cb.highlighted.connect(self._on_highlighted)

        layout.addWidget(self.cb)
        self.setLayout(layout)
        self.setWindowTitle("ComboBox")

    def _on_select(self, i):
        print('Dipilih:', i, '(', self.cb.currentText(), ')')

    def _on_highlighted(self, i):
        print('Dihighlight:', i, '(', self.cb.itemText(i), ')')


def main():
    app = QApplication(sys.argv)
    cb = ComboBox()
    cb.setGeometry(100, 100, 300, 200)
    cb.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
