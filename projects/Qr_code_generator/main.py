from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from Ui_QrCode import Ui_Form
import sys
from PyQt5.QtWidgets import QWidget, QApplication
import qrcode
from io import BytesIO

class MyForm(QWidget, Ui_Form):
    def __init__(self):    
        super(MyForm, self).__init__()
        self.setupUi(self)
        self.resize(500, 300)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn.clicked.connect(self.btnstate)
        self.label.setScaledContents (True)
    
    def btnstate(self):
        str = self.edit.toPlainText()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=1,
        )
        qr.add_data(str)
        qr.make(fit=True)
        img = qr.make_image(fill_color="red", back_color="white")
        buf = BytesIO()
        img.save(buf,"PNG")
        qt_pixmap = QPixmap()
        qt_pixmap.loadFromData(buf.getvalue(),"PNG")
        
        self.label.setPixmap(qt_pixmap)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
