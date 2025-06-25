## Automation Libraries
## Version   Date         Created/Modified by   Ticket Num
## 1.0.0     2022.08.01   GTS                    -

# PROJECT PATH
QE_CFG_PROJECT_PATH = 'D:/workspace/PRK/LX3_X70.05.07/LX3_PRK_1_5_X70.05.07_pre5'

QE_CFG_POWER_ONLINE= False
QE_CFG_POWER_ONLINE_IP={
    'POWER' :'xxx.xxx.xxx.xxx',\
    'IGN'   :'xxx.xxx.xxx.xxx'
}

# UART SPECIFIC CONFIG
QE_CFG_REBOOT_ECU_TIMEOUT=5
QE_CFG_UART_NO_RESPONSE_MAX=15

# HSAC OFF CONFIG
QE_CFG_HSAC_OFF=False

# FEATURE LIST

QE_CFG_TESTING_FEATURES = [ \
    'Backbone_Communication',\
    'Booting',\
    'Calibration',\
    'CAN',\
    'DataLogger',\
    'DebugCAN',\
    'DebugEthCom',\
    'Diagnostics',\
    'DoIP',\
    'E2E_CAN',\
    'E2E_EthCC',\
    'Error_Handler',\
    'EthCC',\
    'EthernetCom',\
    'EthNM_PN',\
    'EthTP',\
    'Full_Com',\
    'Host_Supervision',\
    'IO_SLEEP',\
    'LCS',\
    'Logging',\
    'MP_Build',\
    'Persistency',\
    'PPS_Capture',\
    'RA',\
    'ResetReason',\
    'RTE_Interface',\
    'SchedulingService',\
    'Security',\
    'SWUpdate',\
    'Task_Supervision',\
    'Time_Service',\
    'Tracing']
    
QE_CFG_TESTING_FEATURES_CHOICED = []


QE_CFG_TESTING_FEATURES_Selected = ['Backbone_Communication', 'Booting', 'Calibration', 'CAN', 'DataLogger', 'DebugCAN', 'DebugEthCom', 'Diagnostics', 'DoIP', 'E2E_CAN', 'E2E_EthCC', 'Error_Handler', 'EthCC', 'EthernetCom', 'EthNM_PN', 'EthTP', 'Full_Com', 'Host_Supervision', 'IO_SLEEP', 'LCS', 'Logging', 'MP_Build', 'Persistency', 'PPS_Capture', 'RA', 'ResetReason', 'RTE_Interface', 'Security', 'SWUpdate', 'Task_Supervision', 'Time_Service', 'Tracing']
