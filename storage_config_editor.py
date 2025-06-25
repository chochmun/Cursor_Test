import sys
import json
import os
import serial.tools.list_ports
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QLineEdit, QCheckBox, QComboBox, 
                             QPushButton, QFileDialog, QMessageBox, QGroupBox, 
                             QScrollArea, QFrame, QSplitter, QTextEdit, QDialog, 
                             QDialogButtonBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor
import QE_Config

class FeatureSelectionDialog(QDialog):
    def __init__(self, features, selected_features, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Test Service Selection")
        self.selected_features = set(selected_features)
        self.checkboxes = []
        layout = QVBoxLayout(self)
        for feature in features:
            hbox = QHBoxLayout()
            cb = QCheckBox()
            cb.setChecked(feature in self.selected_features)
            label = QLabel(feature)
            hbox.addWidget(cb)
            hbox.addWidget(label)
            layout.addLayout(hbox)
            self.checkboxes.append((cb, feature))
        # 버튼
        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def get_selected(self):
        return [feature for cb, feature in self.checkboxes if cb.isChecked()]

class ConfigEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_file = "Storages_Cfg.json"
        self.qe_config_path = "QE_Config.py"
        self.original_config = {}
        self.current_config = {}
        self.has_changes = False
        self.qe_features = []
        self.qe_features_selected = []
        self.load_qe_features()
        self.init_ui()
        self.load_config()
        
    def load_qe_features(self):
        try:
            self.qe_features = list(getattr(QE_Config, "QE_CFG_TESTING_FEATURES", []))
            self.qe_features_selected = list(getattr(QE_Config, "QE_CFG_TESTING_FEATURES_Selected", self.qe_features))
            if not self.qe_features_selected:
                self.qe_features_selected = self.qe_features
        except Exception:
            self.qe_features = []
            self.qe_features_selected = []

    def save_qe_features_selected(self, selected):
        # QE_Config.py에 QE_CFG_TESTING_FEATURES_Selected 저장 (append or overwrite)
        try:
            with open(self.qe_config_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            found = False
            for i, line in enumerate(lines):
                if line.strip().startswith('QE_CFG_TESTING_FEATURES_Selected'):
                    lines[i] = f'QE_CFG_TESTING_FEATURES_Selected = {repr(selected)}\n'
                    found = True
                    break
            if not found:
                # 마지막에 추가
                lines.append(f'\nQE_CFG_TESTING_FEATURES_Selected = {repr(selected)}\n')
            with open(self.qe_config_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"QE_Config.py 저장 중 오류: {str(e)}")

    def init_ui(self):
        self.setWindowTitle("Automation Testing Configuration")
        self.setGeometry(100, 100, 960, 640)
        self.setStyleSheet("""
            QMainWindow { background-color: #f8f9fa; }
            QGroupBox { font-weight: bold; border: 2px solid #dee2e6; border-radius: 5px; margin-top: 1ex; padding-top: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px 0 5px; }
            QPushButton { background-color: #007bff; color: white; border: none; padding: 8px 16px; border-radius: 4px; font-weight: bold; }
            QPushButton:hover { background-color: #0056b3; }
            QPushButton:disabled { background-color: #6c757d; }
            QLineEdit { padding: 5px; border: 1px solid #ced4da; border-radius: 4px; background-color: white; }
            QComboBox { padding: 5px; border: 1px solid #ced4da; border-radius: 4px; background-color: white; }
        """)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        # 제목
        title_label = QLabel("Automation Testing Configuration")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #495057; margin: 2px 0 2px 0;")
        main_layout.addWidget(title_label)
        # 구분선
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        main_layout.addWidget(line)
        # 2열 레이아웃
        columns_layout = QHBoxLayout()
        # 좌측 열
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        # Test Service Selection (QGroupBox)
        tss_group = QGroupBox("Test Service Selection")
        tss_layout = QHBoxLayout(tss_group)
        tss_layout.addStretch()
        setting_btn = QPushButton("Setting")
        setting_btn.setFixedWidth(160)
        setting_btn.clicked.connect(self.open_feature_selection)
        tss_layout.addWidget(setting_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        tss_layout.addStretch()
        left_layout.addWidget(tss_group)
        self.create_ecu_variant_section(left_layout)
        self.create_project_path_section(left_layout)
        self.create_dual_performance_section(left_layout)
        self.create_qnx_license_section(left_layout)
        self.create_trace32_config_section(left_layout)
        # 우측 열
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        self.create_uart_config_section(right_layout)
        self.create_power_supply_config_section(right_layout)
        # 열을 columns_layout에 추가
        columns_layout.addWidget(left_widget, 1)
        columns_layout.addWidget(right_widget, 1)
        main_layout.addLayout(columns_layout)
        # 버튼 영역
        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_config)
        self.save_button.setEnabled(False)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_com_ports)
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.save_button)
        main_layout.addLayout(button_layout)
        
    def create_ecu_variant_section(self, parent_layout):
        group_box = QGroupBox("ECU Variant")
        layout = QVBoxLayout(group_box)
        
        self.ecu_variant_combo = QComboBox()
        self.ecu_variant_combo.addItems(["DRV", "PRK_1_5", "PRK_2", "VP"])
        self.ecu_variant_combo.currentTextChanged.connect(self.on_config_changed)
        
        layout.addWidget(self.ecu_variant_combo)
        parent_layout.addWidget(group_box)
        
    def create_project_path_section(self, parent_layout):
        group_box = QGroupBox("Project Path")
        layout = QHBoxLayout(group_box)
        
        self.project_path_edit = QLineEdit()
        self.project_path_edit.textChanged.connect(self.on_config_changed)
        
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_project_path)
        
        layout.addWidget(self.project_path_edit)
        layout.addWidget(browse_button)
        parent_layout.addWidget(group_box)
        
    def create_dual_performance_section(self, parent_layout):
        group_box = QGroupBox("Dual Performance")
        layout = QVBoxLayout(group_box)
        
        self.dual_performance_checkbox = QCheckBox("Enable Dual Performance")
        self.dual_performance_checkbox.stateChanged.connect(self.on_config_changed)
        
        layout.addWidget(self.dual_performance_checkbox)
        parent_layout.addWidget(group_box)
        
    def create_qnx_license_section(self, parent_layout):
        group_box = QGroupBox("QNX License")
        layout = QVBoxLayout(group_box)
        
        # Licenses
        license_layout = QHBoxLayout()
        license_layout.addWidget(QLabel("Licenses:"))
        self.licenses_edit = QLineEdit()
        self.licenses_edit.textChanged.connect(self.on_config_changed)
        license_layout.addWidget(self.licenses_edit)
        layout.addLayout(license_layout)
        
        # Licenses Timestamp
        timestamp_layout = QHBoxLayout()
        timestamp_layout.addWidget(QLabel("Licenses Timestamp:"))
        self.licenses_timestamp_edit = QLineEdit()
        self.licenses_timestamp_edit.textChanged.connect(self.on_config_changed)
        timestamp_layout.addWidget(self.licenses_timestamp_edit)
        layout.addLayout(timestamp_layout)
        
        # Expiry Days
        expiry_layout = QHBoxLayout()
        expiry_layout.addWidget(QLabel("Expiry Days:"))
        self.expiry_days_edit = QLineEdit()
        self.expiry_days_edit.textChanged.connect(self.on_config_changed)
        expiry_layout.addWidget(self.expiry_days_edit)
        layout.addLayout(expiry_layout)
        
        # Status
        self.qnx_status_checkbox = QCheckBox("Status")
        self.qnx_status_checkbox.stateChanged.connect(self.on_config_changed)
        layout.addWidget(self.qnx_status_checkbox)
        
        parent_layout.addWidget(group_box)
        
    def create_trace32_config_section(self, parent_layout):
        group_box = QGroupBox("Trace32 Configuration")
        layout = QVBoxLayout(group_box)
        
        self.verify_dll_path_checkbox = QCheckBox("Verify Dll Path")
        self.verify_dll_path_checkbox.stateChanged.connect(self.on_config_changed)
        layout.addWidget(self.verify_dll_path_checkbox)
        
        self.trace32_status_checkbox = QCheckBox("Status")
        self.trace32_status_checkbox.stateChanged.connect(self.on_config_changed)
        layout.addWidget(self.trace32_status_checkbox)
        
        parent_layout.addWidget(group_box)
        
    def create_uart_config_section(self, parent_layout):
        group_box = QGroupBox("UART Configuration")
        layout = QVBoxLayout(group_box)
        
        # 안내 텍스트 (가장 위에 위치)
        self.comport_info_label = QLabel()
        layout.addWidget(self.comport_info_label)
        self.update_comport_info_label()

        # COM 포트 목록 가져오기 (함수로 분리)
        self.com_ports = self.get_com_ports()
        
        # POWER_SUPPLY_COM_PORT
        power_layout = QHBoxLayout()
        power_layout.addWidget(QLabel("Power Supply COM Port:"))
        self.power_com_combo = QComboBox()
        self.power_com_combo.addItems(self.com_ports)
        self.power_com_combo.currentTextChanged.connect(self.on_config_changed)
        power_layout.addWidget(self.power_com_combo)
        layout.addLayout(power_layout)
        
        # SH00_COM_PORT
        sh00_layout = QHBoxLayout()
        sh00_layout.addWidget(QLabel("SH00 COM Port:"))
        self.sh00_com_combo = QComboBox()
        self.sh00_com_combo.addItems(self.com_ports)
        self.sh00_com_combo.currentTextChanged.connect(self.on_config_changed)
        sh00_layout.addWidget(self.sh00_com_combo)
        layout.addLayout(sh00_layout)
        
        # PH00_COM_PORT
        ph00_layout = QHBoxLayout()
        ph00_layout.addWidget(QLabel("PH00 COM Port:"))
        self.ph00_com_combo = QComboBox()
        self.ph00_com_combo.addItems(self.com_ports)
        self.ph00_com_combo.currentTextChanged.connect(self.on_config_changed)
        ph00_layout.addWidget(self.ph00_com_combo)
        layout.addLayout(ph00_layout)
        
        # PH01_COM_PORT
        ph01_layout = QHBoxLayout()
        ph01_layout.addWidget(QLabel("PH01 COM Port:"))
        self.ph01_com_combo = QComboBox()
        self.ph01_com_combo.addItems(self.com_ports)
        self.ph01_com_combo.currentTextChanged.connect(self.on_config_changed)
        ph01_layout.addWidget(self.ph01_com_combo)
        layout.addLayout(ph01_layout)
        
        # Status
        self.uart_status_checkbox = QCheckBox("Status")
        self.uart_status_checkbox.stateChanged.connect(self.on_config_changed)
        layout.addWidget(self.uart_status_checkbox)
        
        parent_layout.addWidget(group_box)
        
    def create_power_supply_config_section(self, parent_layout):
        group_box = QGroupBox("Power Supply Configuration")
        layout = QVBoxLayout(group_box)
        
        # ECU Channel
        ecu_layout = QHBoxLayout()
        ecu_layout.addWidget(QLabel("ECU Channel:"))
        self.ecu_channel_edit = QLineEdit()
        self.ecu_channel_edit.textChanged.connect(self.on_config_changed)
        ecu_layout.addWidget(self.ecu_channel_edit)
        layout.addLayout(ecu_layout)
        
        # Check Response
        self.check_response_checkbox = QCheckBox("Check Response")
        self.check_response_checkbox.stateChanged.connect(self.on_config_changed)
        layout.addWidget(self.check_response_checkbox)
        
        # Output1
        output1_group = QGroupBox("Output1")
        output1_layout = QVBoxLayout(output1_group)
        
        output1_voltage_layout = QHBoxLayout()
        output1_voltage_layout.addWidget(QLabel("Voltages:"))
        self.output1_voltage_edit = QLineEdit()
        self.output1_voltage_edit.textChanged.connect(self.on_config_changed)
        output1_voltage_layout.addWidget(self.output1_voltage_edit)
        output1_layout.addLayout(output1_voltage_layout)
        
        output1_current_layout = QHBoxLayout()
        output1_current_layout.addWidget(QLabel("Currents:"))
        self.output1_current_edit = QLineEdit()
        self.output1_current_edit.textChanged.connect(self.on_config_changed)
        output1_current_layout.addWidget(self.output1_current_edit)
        output1_layout.addLayout(output1_current_layout)
        
        layout.addWidget(output1_group)
        
        # Output2
        output2_group = QGroupBox("Output2")
        output2_layout = QVBoxLayout(output2_group)
        
        output2_voltage_layout = QHBoxLayout()
        output2_voltage_layout.addWidget(QLabel("Voltages:"))
        self.output2_voltage_edit = QLineEdit()
        self.output2_voltage_edit.textChanged.connect(self.on_config_changed)
        output2_voltage_layout.addWidget(self.output2_voltage_edit)
        output2_layout.addLayout(output2_voltage_layout)
        
        output2_current_layout = QHBoxLayout()
        output2_current_layout.addWidget(QLabel("Currents:"))
        self.output2_current_edit = QLineEdit()
        self.output2_current_edit.textChanged.connect(self.on_config_changed)
        output2_current_layout.addWidget(self.output2_current_edit)
        output2_layout.addLayout(output2_current_layout)
        
        layout.addWidget(output2_group)
        
        # Status
        self.power_status_checkbox = QCheckBox("Status")
        self.power_status_checkbox.stateChanged.connect(self.on_config_changed)
        layout.addWidget(self.power_status_checkbox)
        
        parent_layout.addWidget(group_box)
        
    def browse_project_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if folder:
            self.project_path_edit.setText(folder)
            
    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.original_config = json.load(f)
                self.current_config = json.loads(json.dumps(self.original_config))  # Deep copy
                
            # UI에 값 설정
            self.ecu_variant_combo.setCurrentText(self.current_config.get("ECU_Variant", ""))
            self.project_path_edit.setText(self.current_config.get("Project_Path", ""))
            self.dual_performance_checkbox.setChecked(self.current_config.get("Dual_Performance", False))
            
            # QNX License
            qnx_license = self.current_config.get("QNX_License", {})
            self.licenses_edit.setText(qnx_license.get("Licenses", ""))
            self.licenses_timestamp_edit.setText(str(qnx_license.get("Licenses_Timestamp", "")))
            self.expiry_days_edit.setText(str(qnx_license.get("Expiry_Days", "")))
            self.qnx_status_checkbox.setChecked(qnx_license.get("Status", False))
            
            # UART Config
            uart_config = self.current_config.get("Uart_Config", {})
            for combo, key in zip(
                [self.power_com_combo, self.sh00_com_combo, self.ph00_com_combo, self.ph01_com_combo],
                ["POWER_SUPPLY_COM_PORT", "SH00_COM_PORT", "PH00_COM_PORT", "PH01_COM_PORT"]):
                value = uart_config.get(key, "NO_REQUEST")
                if value in self.com_ports:
                    combo.setCurrentText(value)
                else:
                    combo.setCurrentText("NO_REQUEST")
            self.uart_status_checkbox.setChecked(uart_config.get("Status", False))
            self.update_comport_info_label()
            
            # Trace32 Config
            trace32_config = self.current_config.get("Trace32_Config", {})
            self.verify_dll_path_checkbox.setChecked(trace32_config.get("Verify_Dll_Path", False))
            self.trace32_status_checkbox.setChecked(trace32_config.get("Status", False))
            
            # Power Supply Config
            power_config = self.current_config.get("PowerSupply_ Config", {})
            self.ecu_channel_edit.setText(power_config.get("ECU_CHANNEL", ""))
            self.check_response_checkbox.setChecked(power_config.get("Check_Response", False))
            
            output1 = power_config.get("Outputi", {})
            self.output1_voltage_edit.setText(str(output1.get("Voltages", "")))
            self.output1_current_edit.setText(str(output1.get("Currents", "")))
            
            output2 = power_config.get("Output2", {})
            self.output2_voltage_edit.setText(str(output2.get("Voltages", "")))
            self.output2_current_edit.setText(str(output2.get("Currents", "")))
            
            self.power_status_checkbox.setChecked(power_config.get("Status", False))
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"설정 파일을 로드하는 중 오류가 발생했습니다: {str(e)}")
            
    def on_config_changed(self, *args):
        self.has_changes = True
        self.save_button.setEnabled(True)
        
    def save_config(self):
        try:
            # 현재 UI 값들을 config에 저장
            self.current_config["ECU_Variant"] = self.ecu_variant_combo.currentText()
            self.current_config["Project_Path"] = self.project_path_edit.text()
            self.current_config["Dual_Performance"] = self.dual_performance_checkbox.isChecked()
            
            # QNX License
            self.current_config["QNX_License"] = {
                "Licenses": self.licenses_edit.text(),
                "Licenses_Timestamp": float(self.licenses_timestamp_edit.text()) if self.licenses_timestamp_edit.text() else 0.0,
                "Expiry_Days": int(self.expiry_days_edit.text()) if self.expiry_days_edit.text() else 0,
                "Status": self.qnx_status_checkbox.isChecked()
            }
            
            # UART Config
            self.current_config["Uart_Config"] = {
                "POWER_SUPPLY_COM_PORT": self.power_com_combo.currentText(),
                "HOST_NO_REQUEST": [],
                "SH00_COM_PORT": self.sh00_com_combo.currentText(),
                "PH00_COM_PORT": self.ph00_com_combo.currentText(),
                "PH01_COM_PORT": self.ph01_com_combo.currentText(),
                "Status": self.uart_status_checkbox.isChecked()
            }
            
            # Trace32 Config
            self.current_config["Trace32_Config"] = {
                "Verify_Dll_Path": self.verify_dll_path_checkbox.isChecked(),
                "Status": self.trace32_status_checkbox.isChecked()
            }
            
            # Power Supply Config
            self.current_config["PowerSupply_ Config"] = {
                "ECU_CHANNEL": self.ecu_channel_edit.text(),
                "Check_Response": self.check_response_checkbox.isChecked(),
                "Outputi": {
                    "Voltages": float(self.output1_voltage_edit.text()) if self.output1_voltage_edit.text() else 0.0,
                    "Currents": float(self.output1_current_edit.text()) if self.output1_current_edit.text() else 0.0
                },
                "Output2": {
                    "Voltages": float(self.output2_voltage_edit.text()) if self.output2_voltage_edit.text() else 0.0,
                    "Currents": float(self.output2_current_edit.text()) if self.output2_current_edit.text() else 0.0
                },
                "Status": self.power_status_checkbox.isChecked()
            }
            
            # 파일에 저장
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.current_config, f, indent=4, ensure_ascii=False)
                
            self.original_config = json.loads(json.dumps(self.current_config))
            self.has_changes = False
            self.save_button.setEnabled(False)
            
            QMessageBox.information(self, "Success", "설정이 성공적으로 저장되었습니다.")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"설정을 저장하는 중 오류가 발생했습니다: {str(e)}")
            
    def closeEvent(self, event):
        if self.has_changes:
            reply = QMessageBox.question(self, "변경사항 확인", 
                                       "변경사항이 있습니다.\n정말로 종료하시겠습니까?",
                                       QMessageBox.Yes | QMessageBox.Cancel)
            
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    def get_com_ports(self):
        ports = [port.device for port in serial.tools.list_ports.comports()]
        ports.append("NO_REQUEST")
        return ports

    def update_comport_info_label(self):
        ports = self.get_com_ports()
        self.comport_info_label.setText(f"현재 사용 가능한 COM 포트: {', '.join(ports)}")

    def refresh_com_ports(self):
        self.com_ports = self.get_com_ports()
        # 각 콤보박스의 아이템을 새로고침
        for combo, key in zip(
            [self.power_com_combo, self.sh00_com_combo, self.ph00_com_combo, self.ph01_com_combo],
            ["POWER_SUPPLY_COM_PORT", "SH00_COM_PORT", "PH00_COM_PORT", "PH01_COM_PORT"]):
            current_value = self.current_config.get("Uart_Config", {}).get(key, "NO_REQUEST")
            combo.blockSignals(True)
            combo.clear()
            combo.addItems(self.com_ports)
            # 저장된 값이 현재 포트에 없으면 NO_REQUEST로
            if current_value in self.com_ports:
                combo.setCurrentText(current_value)
            else:
                combo.setCurrentText("NO_REQUEST")
            combo.blockSignals(False)
        self.update_comport_info_label()

    def open_feature_selection(self):
        dialog = FeatureSelectionDialog(self.qe_features, self.qe_features_selected, self)
        if dialog.exec_() == QDialog.Accepted:
            selected = dialog.get_selected()
            self.qe_features_selected = selected
            self.save_qe_features_selected(selected)
            QMessageBox.information(self, "Success", "테스트 서비스 선택이 저장되었습니다.")
        # 취소 시 아무 동작 없음

def main():
    app = QApplication(sys.argv)
    window = ConfigEditor()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 