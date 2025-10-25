def aplicar_estilos(self):
    self.setStyleSheet("""
            QPushButton {
                background-color: #30343f;
                color: white;
                font-size: 14px;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #778da9;    
            }
            QLabel {
                background-color: #373f51;
                width: 130px;
                height: 30px;
                border-radius: 10px;
                color: white;
                font-size: 14px;
                padding: 8px;
            }
            QLineEdit {
                background-color: #373f51;
                width: 130px;
                height: 30px;
                border-radius: 10px;
                color: white;
            }
        """)
