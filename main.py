# İTÜ RAKE Sürü İHA Takımı Arayüz Çalışması

from PyQt5 import QtCore
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from uav_manager import UAVManager
from PyQt5.QtWidgets import QComboBox, QErrorMessage, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget, QApplication, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from lists import formations, missions

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
        main_layout = QGridLayout()
        main_layout.setSpacing(50)

        uav_management_layout = QVBoxLayout()

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
        uav_management_layout.addLayout(uav_count_layout, 1)

        # Creating UAV address layout for this section
        uav_address_layout = QHBoxLayout()

        # Creating the set address button
        set_address_button = QPushButton('Set address to UAV')
        set_address_button.clicked.connect(self.set_address)

        # Adding current UAV ComboBox to layout
        uav_address_layout.addWidget(self.current_uav_address)
        uav_address_layout.addWidget(self.current_uav)
        uav_address_layout.addWidget(set_address_button)

        uav_management_layout.addLayout(uav_address_layout, 1)

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
        set_parameters_button.clicked.connect(self.set_parameters)
        set_parameters_layout.addWidget(set_parameters_button)
        set_parameters_layout.addStretch()

        #
        uav_parameters_layout.addLayout(d_layout)
        uav_parameters_layout.addLayout(z_layout)
        uav_parameters_layout.addLayout(set_parameters_layout)

        #
        uav_management_layout.addLayout(uav_parameters_layout, 1)
        uav_management_layout.setSpacing(10)

        # Adding required fields to the parameters layout

        #
        main_layout.addLayout(uav_management_layout, 0, 0)

        #
        mission_management_layout = QGridLayout()
        take_off_button = QPushButton('Take-Off')
        land_button = QPushButton('Land')
        formation_menu = QComboBox()
        self.populate_combobox(formation_menu, formations)
        run_button = QPushButton('RUN')
        mission_menu = QComboBox()
        self.populate_combobox(mission_menu, missions)
        select_mission_button = QPushButton('SELECT')
        altitude_label = QLabel('Altitude: ')
        altitude_edit = QLineEdit()

        #
        mission_management_layout.addWidget(take_off_button, 0, 0)
        mission_management_layout.addWidget(land_button, 0, 1)
        mission_management_layout.addWidget(formation_menu, 1, 0)
        mission_management_layout.addWidget(run_button, 1, 1)
        mission_management_layout.addWidget(mission_menu, 2, 0)
        mission_management_layout.addWidget(select_mission_button, 2, 1)
        mission_management_layout.addWidget(altitude_label, 3, 0)
        mission_management_layout.addWidget(altitude_edit, 3, 1)
        mission_management_layout.setSpacing(10)

        #
        main_layout.addLayout(mission_management_layout, 1, 0)

        #
        third_layout = QGridLayout()
        main_layout.addLayout(third_layout, 0, 1)

        #
        manual_control_layout = QVBoxLayout()

        #
        direct_commands_layout = QHBoxLayout()
        position_goals_layout = QHBoxLayout()

        #
        roll_layout = QVBoxLayout()
        pitch_layout = QVBoxLayout()
        yaw_layout = QVBoxLayout()
        thrust_layout = QVBoxLayout()
        send_commands_button_layout = QVBoxLayout()

        #
        roll_label = QLabel('Roll')
        pitch_label = QLabel('Pitch')
        yaw_label = QLabel('Yaw')
        thrust_label = QLabel('Thrust')

        #
        roll_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        pitch_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        yaw_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        thrust_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        #
        roll_edit = QLineEdit()
        pitch_edit = QLineEdit()
        yaw_edit = QLineEdit()
        thrust_edit = QLineEdit()

        #
        roll_edit.setValidator(QDoubleValidator())
        pitch_edit.setValidator(QDoubleValidator())
        yaw_edit.setValidator(QDoubleValidator())
        thrust_edit.setValidator(QDoubleValidator())

        #
        roll_layout.setSpacing(10)
        roll_layout.addStretch()
        roll_layout.addWidget(roll_label)
        roll_layout.addWidget(roll_edit)
        pitch_layout.setSpacing(10)
        pitch_layout.addStretch()
        pitch_layout.addWidget(pitch_label)
        pitch_layout.addWidget(pitch_edit)
        yaw_layout.setSpacing(10)
        yaw_layout.addStretch()
        yaw_layout.addWidget(yaw_label)
        yaw_layout.addWidget(yaw_edit)
        thrust_layout.setSpacing(10)
        thrust_layout.addStretch()
        thrust_layout.addWidget(thrust_label)
        thrust_layout.addWidget(thrust_edit)
        send_commands_button_layout.addStretch()
        send_commands_button_layout.addWidget(QPushButton('Send Commands'))

        #
        direct_commands_layout.addLayout(roll_layout)
        direct_commands_layout.addLayout(pitch_layout)
        direct_commands_layout.addLayout(yaw_layout)
        direct_commands_layout.addLayout(thrust_layout)
        direct_commands_layout.addLayout(send_commands_button_layout)

        #
        x_layout = QVBoxLayout()
        y_layout = QVBoxLayout()
        z_layout = QVBoxLayout()
        send_position_goals_layout = QVBoxLayout()

        #
        x_label = QLabel('X')
        y_label = QLabel('Y')
        z_label = QLabel('Z')

        #
        x_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        y_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        z_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        #
        x_edit = QLineEdit()
        y_edit = QLineEdit()
        z_edit = QLineEdit()
        send_position_goals_button = QPushButton('Send Position Goals')

        #
        x_edit.setValidator(QDoubleValidator())
        y_edit.setValidator(QDoubleValidator())
        z_edit.setValidator(QDoubleValidator())

        #
        x_layout.setSpacing(10)
        x_layout.addStretch()
        x_layout.addWidget(x_label)
        x_layout.addWidget(x_edit)
        y_layout.setSpacing(10)
        y_layout.addStretch()
        y_layout.addWidget(y_label)
        y_layout.addWidget(y_edit)
        z_layout.setSpacing(10)
        z_layout.addStretch()
        z_layout.addWidget(z_label)
        z_layout.addWidget(z_edit)
        send_position_goals_layout.setSpacing(10)
        send_position_goals_layout.addStretch()
        send_position_goals_layout.addWidget(send_position_goals_button)

        #
        position_goals_layout.addLayout(x_layout)
        position_goals_layout.addLayout(y_layout)
        position_goals_layout.addLayout(z_layout)
        position_goals_layout.addLayout(send_position_goals_layout)

        #
        manual_control_layout.addLayout(position_goals_layout)
        manual_control_layout.addLayout(direct_commands_layout)

        #
        main_layout.addLayout(manual_control_layout, 1, 1)

        self.setLayout(main_layout)

    def setup_combo_box(self):
        for i in range(uav_manager.real_uav_count):
            self.current_uav.addItem(str(i + 1))
        self.current_uav.currentIndexChanged.connect(self.current_uav_changed)

    def populate_combobox(self, combobox, list_of_items):
        for item in list_of_items:
            combobox.addItem(str(item))
        # combobox.addItem('Circle')
        # combobox.addItem('Triangle')
        # combobox.addItem('Square')
        # combobox.addItem('Pentagon')
        # combobox.addItem('Hexagon')
        # combobox.addItem('V')
        # combobox.addItem('Inverse-V')
        # combobox.addItem('Crescent')
        # combobox.addItem('Star')

    def set_address(self):
        uav_index = self.current_uav.currentIndex()
        uav_address = self.current_uav_address.text()
        uav_manager.set_real_uav_address(uav_index, uav_address)

    def set_parameters(self):
        d = self.d_edit.text()
        z = self.z_edit.text()
        uav_index = self.current_uav.currentIndex()
        uav_manager.set_uav_parameters(uav_index, d, z)

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