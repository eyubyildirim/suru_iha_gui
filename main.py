from PyQt5.QtGui import QIntValidator
from uav_manager import UAVManager
from PyQt5.QtWidgets import QComboBox, QErrorMessage, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget, QApplication, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt

# Getting the UAVManager instance
uav_manager = UAVManager()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Suru IHA')
        self.virtual_uav_count_edit = QLineEdit()
        self.real_uav_count_edit = QLineEdit()
        self.current_uav_address = QLineEdit()
        self.current_uav = QComboBox()
        self.z_edit = QLineEdit()
        self.d_edit = QLineEdit()
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Layouts needed for UAV count section
        uav_count_layout = QHBoxLayout()
        virtual_uav_count = QVBoxLayout()
        real_uav_count = QVBoxLayout()
        set_uav_count = QVBoxLayout()

        # Spacings of those layouts
        uav_count_layout.setSpacing(50)
        virtual_uav_count.setSpacing(10)
        real_uav_count.setSpacing(10)
        set_uav_count.setSpacing(10)

        # Creating virtual UAV count section
        self.virtual_uav_count_edit = QLineEdit()
        self.virtual_uav_count_edit.setValidator(QIntValidator(0, 10, self))
        virtual_uav_count.addWidget(QLabel('Virtual UAV Count'))
        virtual_uav_count.addWidget(self.virtual_uav_count_edit)
        virtual_uav_count.addStretch()

        # Creating real UAV count section
        self.real_uav_count_edit = QLineEdit()
        self.real_uav_count_edit.setValidator(QIntValidator(0, 10, self))
        real_uav_count.addWidget(QLabel('Real UAV Count'))
        real_uav_count.addWidget(self.real_uav_count_edit)
        real_uav_count.addStretch()

        # Creating set count button section
        set_count_button = QPushButton('Set Count')
        set_count_button.clicked.connect(self.set_uav_counts)
        set_uav_count.addWidget(set_count_button)
        set_uav_count.addStretch()

        # Bringing different sections together
        uav_count_layout.addLayout(virtual_uav_count)
        uav_count_layout.addLayout(real_uav_count)
        uav_count_layout.addLayout(set_uav_count)

        # Adding UAV count section to main layout
        main_layout.addLayout(uav_count_layout, 1)

        # Creating UAV address layout for this section
        uav_address_layout = QHBoxLayout()

        # Creating the set address button
        set_address_button = QPushButton('Set address to UAV')
        set_address_button.clicked.connect(self.set_address)

        # Adding current UAV ComboBox to layout
        uav_address_layout.addWidget(self.current_uav_address)
        uav_address_layout.addWidget(self.current_uav)
        uav_address_layout.addWidget(set_address_button)

        main_layout.addLayout(uav_address_layout, 1)

        # Creating UAV parameters layout for this section
        uav_parameters_layout = QHBoxLayout()

        #
        d_layout = QVBoxLayout()
        z_layout = QVBoxLayout()
        set_parameters_layout = QVBoxLayout()

        #
        uav_parameters_layout.setSpacing(50)
        d_layout.setSpacing(10)
        z_layout.setSpacing(10)
        set_parameters_layout.setSpacing(10)

        #
        d_layout.addWidget(QLabel('d'))
        d_layout.addWidget(self.d_edit)
        d_layout.addStretch()

        #
        z_layout.addWidget(QLabel('z'))
        z_layout.addWidget(self.z_edit)
        z_layout.addStretch()

        #
        set_parameters_button = QPushButton('Set Parameters')
        set_address_button.clicked.connect(self.set_parameters)
        set_parameters_layout.addWidget(set_parameters_button)
        set_parameters_layout.addStretch()

        #
        uav_parameters_layout.addLayout(d_layout)
        uav_parameters_layout.addLayout(z_layout)
        uav_parameters_layout.addLayout(set_parameters_layout)

        #
        main_layout.addLayout(uav_parameters_layout, 1)

        # Adding required fields to the parameters layout

        self.setLayout(main_layout)

    def setup_combo_box(self):
        for i in range(uav_manager.real_uav_count):
            self.current_uav.addItem(str(i + 1))
        self.current_uav.currentIndexChanged.connect(self.current_uav_changed)

    def set_address(self):
        uav_index = self.current_uav.currentIndex()
        uav_address = self.current_uav_address.text()
        uav_manager.set_real_uav_address(uav_index, uav_address)

    def set_parameters(self):
        d = self.d_edit.text()
        z = self.z_edit.text()
        uav_index = self.current_uav.currentIndex()
        uav_manager.real_uavs[uav_index].set_d(d)
        uav_manager.real_uavs[uav_index].set_z(z)

    def current_uav_changed(self, uav_index):
        self.current_uav_address.setText(
            uav_manager.real_uavs[uav_index].get_address())
        self.d_edit.setText(str(uav_manager.real_uavs[uav_index].get_d()))
        self.z_edit.setText(str(uav_manager.real_uavs[uav_index].get_z()))

    def set_uav_counts(self):
        # Check if any of the LineEdits is empty
        if len(self.virtual_uav_count_edit.text()) == 0 or len(
                self.real_uav_count_edit.text()) == 0:
            # If so, show a dialog
            msg = QMessageBox()
            msg.setText("Error")
            msg.setInformativeText('Please fill the blank LineEdit')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            # If not, first delete previous items
            self.current_uav.clear()

            # Now set the UAV counts of UAVManager to values inside LineEdits
            uav_manager.set_real_uav_count(int(
                self.real_uav_count_edit.text()))
            uav_manager.set_virtual_uav_count(
                int(self.virtual_uav_count_edit.text()))

        self.setup_combo_box()
        self.current_uav.setCurrentIndex(0)
        self.current_uav_changed(0)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())