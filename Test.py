import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class LinearRegressionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('gui_design.ui', self)  # Ubah 'gui_design.ui' dengan nama file desain GUI Anda

        self.openButton.clicked.connect(self.open_dataset)
        self.predictButton.clicked.connect(self.predict)
        self.aboutButton.clicked.connect(self.about)

    def open_dataset(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Dataset', '', 'Excel Files (*.xlsx)')
        if file_path:
            try:
                dataset = pd.read_excel(file_path)
                # Lakukan pengolahan data sesuai kebutuhan Anda
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to open dataset: {e}')

    def predict(self):
        # Lakukan prediksi menggunakan Regresi Linier
        # Tampilkan hasil prediksi dan plot jika diperlukan

    def about(self):
        QMessageBox.information(self, 'About', 'Linear Regression App\n\nAplikasi untuk melakukan prediksi menggunakan Regresi Linier.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LinearRegressionApp()
    window.show()
    sys.exit(app.exec_())
