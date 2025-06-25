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
    # 'Backbone_Communication',\
    # 'Booting',\
    # 'Calibration',\
      'CAN',\
    # 'DataLogger',\
    #  'DebugCAN',\
    # 'DebugEthCom',\
    #  'Diagnostics',\
    # 'DoIP',\
    #  'E2E_CAN',\
    # 'E2E_EthCC',\
    # 'Error_Handler',\
    # 'EthCC',\
    # 'EthernetCom',\
    # 'EthNM_PN',\
    # 'EthTP',\
    # 'Full_Com',\
    # 'Host_Supervision',\
    # 'IO_SLEEP',\
    # 'LCS',\
    # 'Logging',\
    # 'MP_Build',\
    # 'Persistency',\
    # 'PPS_Capture',\
    # 'RA',\
    # 'ResetReason',\
    # 'RTE_Interface',\
    # 'SchedulingService',\
    # 'Security',\
    # 'SWUpdate',\
    # 'Task_Supervision',\
    # 'Time_Service',\
    # 'Tracing']
    ]


QE_CFG_DRV_PH00_QNX_MOTIONWISE_PATH='usr/local/MotionWise'
QE_CFG_PRK_PH00_QNX_MOTIONWISE_PATH='fs/ph00_qnx'
QE_CFG_PRK_PH01_QNX_MOTIONWISE_PATH='fs/ph01_qnx'
QE_CFG_VP_PH00_QNX_MOTIONWISE_PATH='fs/ph00_qnx'
QE_CFG_VP_PH01_QNX_MOTIONWISE_PATH='fs/ph01_qnx'
QE_CFG_QNX_SW_CENTER='C:/QNX/QNX SoftWare Center/qnxsoftwarecenter.exe'
QE_CFG_QNX_LICENSE_KEY='xxxx-xxxx-xxxx-xxxx-xxxx'

QE_CFG_HOTA_STUDIO='C:Program Files (x86)/GIT/H-OTA Studio GEN2'
QE_CFG_PY27_PATH = 'C:/Python27'

# SCHEDULE REPORT INFO
QE_CFG_SCHEDULE_REPORT_INFO={\
    'MOTION_WISE_RATOOLS': {
        'Py27Path': QE_CFG_PY27_PATH,
        'OutputLogTemp': 'Info: Output written to ',
        'Perform': {
            'ScriptPath': '%s/Scripts/MotionWise_Perf.py'%QE_CFG_PY27_PATH,
            'Cmd': 'python27 %s --host %s --trace-log --measurement-duration 30', \
        },
        'TraceFilter': {
            'ScriptPath': '%s/Scripts/MotionWise_Trace_Filter.py'%QE_CFG_PY27_PATH,
            'Cmd': 'python27 %s --host %s --enable-all-traces', \
        },
    },
    'TEST_REPORTS': {
        'ReportRootPath': '%s/0001_Documents/'%QE_CFG_PROJECT_PATH,
        'FileNameTemp': 'Schedule_PIE_SSWc-01_SSF-01', \
        'SheetNameTemp': '%s_SSWc-01_SSF-01', \
        'HeaderTemp': [ \
            'HOST','Core','SchedulableEntity','Period_ms','WCET_Value_ms', \
            'ActivationTime_ms','WCET_Act_Value_ms','Activation Act_Time_ms','P_F_Type' \
        ], \
        'CoreNameMapping': {
            'Core0': 0,'Core1': 1,'Core2': 2,'Core3': 3,'Core4': 4,'Core5': 5,'Core6': 6,'Core7': 7,'Core8': 8, \
            'Core9': 9,'Core10': 10,'Core11': 11,'Core12': 12,'Core13': 13,'Core14': 14,'Core15': 15,'A72': 0},
        'HeaderDetection': ['HOST','Core'],
    },
    'SCHEDULE_INPUT': {
        'ReportRootPath': '%s/0001_Documents/'%QE_CFG_PROJECT_PATH,
        'FileNameTemp': '_Schedule_input', \
        'SheetNameTemp': 'Scheduling Table', \
        'HeaderTemp': [ \
            'TASK','Period_ms','WCET_ms','Start_Time_ms','End_Time_ms','Priority','CPU_Load','Total_CPU_Load' \
            'Task_Type','WDG_Deadline' \
        ],
        'RunnablePrefix': {
            #'Prefix': {'StartId': number, 'StopId': number, 'ExceptId':[]}
            'R_SH00_MiddlewareQM': {'StartId':0, 'StopId': 9, 'ExceptId':[]},
            'R_SH00_MiddlewareASIL': {'StartId':0, 'StopId': 9, 'ExceptId':[]},
            'R_PH00_MiddlewareQM': {'StartId':0, 'StopId': 9, 'ExceptId':[]},
            'R_PH00_MiddlewareASIL': {'StartId':0, 'StopId': 9, 'ExceptId':[]},
        },
        'HeaderDetection': ['ECU','MCU/VPU']
    },\
    'RUNNABLE_SUMMARY': { \
        'FileNameTemp': '%s_runnable_summary.csv', \
        'HeaderTemp': { \
            'SH00': [ \
                'HostName','Core','SWCs','Task','Runnable','RunnableID','netto_CPU_time_cnt','netto_CPU_time_min_us', \
                'netto_CPU_time_avg_us','netto_CPU_time_max_ts','gross_CPU_time_cnt','gross_CPU_time_min_us', \
                'gross_CPU_time_avg_us','gross_CPU_time_max_us','cyclic_activation_cnt','cyclic_activation_min_us', \
                'cyclic_activation_avg_us','cyclic_activation_max_us','budget_usage_min_%','budget_usage_avg_%', \
                'budget_usage_max_%', \
                'platform_overhead_cnt','platform_overhead_min_us','platform_overhead_avg_us','platform_overhead_max_us' \
            ], \
            'PHXX': [ \
                'HostName','Core','SWCs','Task','Runnable','RunnableID','netto_CPU_time_cnt','netto_CPU_time_min_us', \
                'netto_CPU_time_avg_us','netto_CPU_time_max_ts','gross_CPU_time_cnt','gross_CPU_time_min_us', \
                'gross_CPU_time_avg_us','gross_CPU_time_max_us','cyclic_activation_cnt','cyclic_activation_min_us', \
                'cyclic_activation_avg_us','cyclic_activation_max_us','budget_usage_min_%','budget_usage_avg_%', \
                'budget_usage_max_%' \
            ], \
        'HeaderDetection': ['#HEADER host','core'] \
        }, \
    }, \
    'TRACE_EVENTS': { \
        'FileName': 'trace_events.csv', \
        'HeaderTemp': ['Timestamp','Counter','Host','Core','Type','SWCs','RunnableID','Data'], \
        'HeaderDetection': ['#HEADER time','count'], \
    }, \
    'TASK_SUMMARY': { \
        'FileName': 'SH00_tasks_summary.csv', \
        'HeaderTemp': [ \
            'HostName','Core','Task','TaskID','netto_CPU_time_cnt','netto_CPU_time_min_us','netto_CPU_time_avg_us', \
            'netto_CPU_time_max_ts','gross_CPU_time_cnt','gross_CPU_time_min_us','gross_CPU_time_avg_us', \
            'gross_CPU_time_max_us','cyclic_activation_cnt','cyclic_activation_min_us','cyclic_activation_avg_us', \
            'cyclic_activation_max_us','RAM_stack_usage_cnt','RAM_stack_usage_max_Byte','netto_CPU_usage_cnt', \
            'netto_CPU_usage_min_%','netto_CPU_usage_avg_%','netto_CPU_usage_max_%' \
        ], \
        'HeaderDetection': ['#HEADER host','core'] \
    }, \

}


# VECTOR HARDWARE CONFIG
QE_VECTOR_HARDWARE_CONFIG={\
    'CAN_FD_APPL_CHANNELS': ['CAN_1', 'CAN_2', 'CAN_3', 'CAN_4'], \
    'TIMER_RATE': 10000, \
    'CHECK_RX_MSG_STATUS': {'SAMPLING_NUM': 500, 'TIMEOUT': 20}, \
    'TX_DUMMY_MSG_NUM': 200, \
    'CAN_FD_DEVICE_1': { \
        'DeviceName':'VN1630A',\
        'TransceiverName':'On board CAN 1051cap(Highspeed)',\
        'TransceiverType':0x013C,\
        "CAN_1":{
            'ChannelId':1,\
            'BitTimingConfig': {
                'ArbitrationBitRate': 500000,\
                'SyncJumpWithAbr' : 2,\
                'TimeSegment1Abr' :7,\
                'TimeSegment2Abr' : 2,\
                'DataBitRate' : 2000000,\
                'SyncJumpWithDbr': 2,\
                'TimeSegment1Dbr':7,\
                'TimeSegment2Dbr' : 2,\
                'TimerRate' : 10000, \
            },\
            
        },\
        'CAN_2': { \
            'Channelld': 2, \
            'BitTimingConfig': { \
                'ArbitrationBitRate': 500000, \
                'SyncJumpWithAbr': 2,\
                'TimeSegment1Abr':7,\
                'TimeSegment2Abr': 2,\
                'DataBitRate' : 2000000,\
                'SyncJumpWithDbr': 2,\
                'TimeSegment1Dbr' :7,\
                'TimeSegment2Dbr': 2,\
                'TimerRate' : 10000
            },\
        }, \
    },
    'CAN_FD_DEVICE_2': { \
        'DeviceName':'VN1630A',\
        'TransceiverName':'On board CAN 1057G (Highspeed)',\
        'TransceiverType':0x0146,\
        "CAN_3":{
            'ChannelId':10,\
            'BitTimingConfig': {
                'ArbitrationBitRate': 500000,\
                'SyncJumpWithAbr' : 2,\
                'TimeSegment1Abr' :7,\
                'TimeSegment2Abr' : 2,\
                'DataBitRate' : 2000000,\
                'SyncJumpWithDbr': 2,\
                'TimeSegment1Dbr':7,\
                'TimeSegment2Dbr' : 2,\
                'TimerRate' : 10000, \
            },\
            
        },\
        'CAN_4': { \
            'Channelld': 11, \
            'BitTimingConfig': { \
                'ArbitrationBitRate': 500000, \
                'SyncJumpWithAbr': 2,\
                'TimeSegment1Abr':7,\
                'TimeSegment2Abr': 2,\
                'DataBitRate' : 2000000,\
                'SyncJumpWithDbr': 2,\
                'TimeSegment1Dbr' :7,\
                'TimeSegment2Dbr': 2,\
                'TimerRate' : 10000
            },\
        }, \
    },
    'CHANNEL_MAPPING': {\
        'ChannelName': { \
            'CAN_1': 'A_CAN1', \
            'CAN_2': 'A_CAN2', \
            'CAN_3': 'R_CAN', \
            'CAN_4': 'E_CAN', \
            'A_CAN1': 'CAN_1', \
            'A_CAN2': 'CAN_2', \
            'R_CAN' : 'CAN_3', \
            'E_CAN' : 'CAN_4', \
        },\
        'Channelld': {
            'CANA': 1, \
            'CAN_2': 2, \
            'CAN_3': 3, \
            'CAN_4': 4, \
            'A_CAN1': 1,\
            'A_CAN2': 2,\
            'R_CAN' : 3,\
            'E_CAN' : 4,\
        },\
    },
    'DBC_MAPPING': { \
        'CANIF_CFG_H':{\
            'PATH':QE_CFG_PROJECT_PATH+'/0900_System/02_configout/rte/SH00/mIC/Common/BSW_Output/inc/CanIf_Cfg.h',\
            'TX_LPDU_HANDLE_TEMP':'#define CanIfConf_CanIfTxPduCfg_CanIfTxPduCfg_',\
            'RX_LPDU_HANDLE_TEMP':'#define CanIfConf_CanIfRxPduCfg_CanIfRxPduCfg_',\
        },\
        'CAN_1':{\
            'NODE_NAME':'ADAS_DRV2',\
            'CAN_IF_LPDU_NAME':'ACANFD1',\
            'MSG_ID_NO_REQUEST':{
                'TX':[],\
                'RX':[],\
            },\
            'FILE_PATH': QE_CFG_PROJECT_PATH+'/0000_Architecture/CAN_DBC/RS4_DRV_2_X053.07.01_ACAN1.dbc'\
        },\
        'CAN_2':{\
            'NODE_NAME':'ADAS_DRV2',\
            'CAN_IF_LPDU_NAME':'ACANFD2',\
            'MSG_ID_NO_REQUEST':{
                'TX':[],\
                'RX':[],\
            },\
        'FILE_PATH': QE_CFG_PROJECT_PATH+'/0000_Architecture/CAN_DBC/RS4_DRV_2_X053.07.01_ACAN2.dbc'\
        },\
        'CAN_3':{\
            'NODE_NAME':'ADAS_DRV2',\
            'CAN_IF_LPDU_NAME':'RCANFD',\
            'MSG_ID_NO_REQUEST':{
                'TX':[],\
                'RX':[],\
            },\
        'FILE_PATH': QE_CFG_PROJECT_PATH+'/0000_Architecture/CAN_DBC/RS4_DRV_2_X053.07.01_RCAN.dbc'\
        },\
        'CAN_4':{\
            'NODE_NAME':'ADAS_DRV2',\
            'CAN_IF_LPDU_NAME':'ECANFD',\
            'MSG_ID_NO_REQUEST':{
                'TX':[],\
                'RX':[],\
            },\
        'FILE_PATH': QE_CFG_PROJECT_PATH+'/0000_Architecture/CAN_DBC/RS4_DRV_2_X053.07.01_ECAN.dbc'\
        },\
    }
}

QE_CFG_CAN_CRC_DATA_INIT    = 0xF800
QE_CFG_CAN_CRC16_INIT       = 0xFF
QE_CFG_CAN_CRC8_INI         = 0x00
# CRC 16 TABLE
QE_CFG_CAN_CRC16_TABLE=[\
    0x0000,0x1021,0x2042,0x3063 #8열 32행 = 256개
]
# CRC 8 TABLE
QE_CFG_CAN_CRC8_TABLE=[\
    0X00, 0X1D,0X3A,0X27 #16얄 16행 = 256개
]
####################################################################################################
# ETHERNET DATABASE
####################################################################################################
QE_CFG_ADDRESS_TABLE = { \
    'DRV': { \
        'SH00'     : {'IP': '10.32.0.0',   'MAC': '02:00:00:20:00:00'}, \
        'PH00'     : {'IP': '10.32.32.0',  'MAC': '02:00:00:20:20:00'}, \
        'LIDAR_R'  : {'IP': '10.1.0.100',  'MAC': '02:00:00:01:00:64'}, \
        'LIDAR_L'  : {'IP': '10.2.0.100',  'MAC': '02:00:00:02:00:64'}, \
        'SWITCH'   : {'IP': '10.32.8.0',   'MAC': '02:00:00:20:08:00'} \
    }, \
    'PRK': { \
        'SH00'     : {'IP': '10.0.0.16',   'MAC': '02:00:00:00:00:10'}, \
        'PH00'     : {'IP': '10.0.32.16',  'MAC': '02:00:00:00:20:10'}, \
        'PH01'     : {'IP': '10.0.16.16',  'MAC': '02:00:00:00:10:10'}, \
        'SWITCH'   : {'IP': '10.0.8.16',   'MAC': '02:00:00:00:08:10'} \
    }, \
    'VP': { \
        'SH00'     : {'IP': '10.16.0.0',   'MAC': '02:00:00:10:00:00'}, \
        'PH00'     : {'IP': '10.16.32.0',  'MAC': '02:00:00:10:20:00'}, \
        'PH01'     : {'IP': '10.16.16.0',  'MAC': '02:00:00:10:10:00'}, \
        'SWITCH'   : {'IP': '10.16.8.0',   'MAC': '02:00:00:10:08:00'} \
    }, \
    'DEBUG_PORT'  : {'IP': '10.32.32.40',  'MAC': '02:00:00:20:20:28'}, \
    'CCU_AP'      : {'IP': '10.0.6.0',     'MAC': '02:00:00:00:06:00'}, \
    'CCU_MCU'     : {'IP': '10.0.5.0',     'MAC': '02:00:00:00:05:00'}, \
    'FR_C_LIDAR_L': {'IP': '10.2.0.1',     'MAC': '88:96:F2:01:00:02'}, \
    'FR_C_LIDAR_R': {'IP': '10.1.0.1',     'MAC': '88:96:F2:01:00:01'}, \
    'HDM'         : {'IP': '10.0.0.2',     'MAC': '02:00:00:00:00:02'}, \
    'CCIC_HU'     : {'IP': '10.0.3.0',     'MAC': '02:00:00:00:03:00'}, \
    'DATA_LOGGER' : {'IP': '10.32.0.255',  'MAC': '02:00:00:20:00:FF'} \
}

# UDS_ON_ETHERNET
QE_CFG_COMPLEMENTARY_SWUPDATE_PATH = QE_CFG_PROJECT_PATH + '/9000_Complementary/SWUpdate'
QE_CFG_UDS_ON_ETHERNET_SEED2KEY_PATH = QE_CFG_PROJECT_PATH + '/0000_Architecture/Seed2KeyDll'

QE_CFG_COMPLEMENTARY_SWUPDATE_MCU_PATH = QE_CFG_COMPLEMENTARY_SWUPDATE_PATH + '/MCU(MemorySwap)/hcfg/ReprogramConfig_GEN2_PRK_MCU_MSWAP_HSM_ON.hcfg-r'
QE_CFG_COMPLEMENTARY_SWUPDATE_CPU_PATH = QE_CFG_COMPLEMENTARY_SWUPDATE_PATH + '/VPU/hcfg/ReprogramConfig_GEN2_PRK2_VPU.hcfg-r'

QE_CFG_COMPLEMENTARY_SWUPDATE_MCU_DLL_PATH = QE_CFG_UDS_ON_ETHERNET_SEED2KEY_PATH + '/HKMC_AdvancedSeedKey_Win32_PRK2.dll'
QE_CFG_COMPLEMENTARY_SWUPDATE_CPU_DLL_PATH = QE_CFG_UDS_ON_ETHERNET_SEED2KEY_PATH + '/HKMC_AdvancedSeedKey_Win32.dll'


QE_CFG_COMPLEMENTARY_RESETREASON_DB ={\
    ' RID HEX': bytearray(b'\x42\x72'), \
    ' RoutineControl':{\
        'SubFunctionType' :'ROUTINE 0B CTRL', \
        'StartRoutine' : {\
            'REQ': True,
            'OPT BYTE': 1},\
        'StopRoutine' :{\
            'REQ': False, \
            'OPT_BYTE': 0},\
        'RequestRoutineResu1ts' :{\
            'REQ': False, \
            'OPT_BYTE': 0}},\
    'Security': True, \
    'ExtendedSession' : True,\
    'Name': 'ResetReason '}

QE_CFG_UDS_ON_ETHERNET_CONFIG = {
    'HEADER': bytearray([0xCA, 0x35, 0xFC, 0xBC]),
    'CCU_PHYSICAL_ID': {'REQ_ID': [0x05, 0xD1], 'RSP_ID': [0x05, 0xD9]},
    'LIDAR_PHYSICAL_ID': {
        'LIDAR_L': {'REQ_ID': [0x07, 0x13], 'RSP_ID': [0x07, 0x1B], 'DST_PORT': 13410},
        'LIDAR_R': {'REQ_ID': [0x07, 0x14], 'RSP_ID': [0x07, 0x1C], 'DST_PORT': 13411},
    },
    'ADAPTER_IP': QE_CFG_ADDRESS_TABLE['CCU_AP']['IP'],
    'RECEIVE_TIMEOUT': 10,
    'RETRY_GET_RESPONSE': 2,
    'REQUEST_CORRECTLY_RECV_RESP_PENDING_TIMEOUT': 20,
    'HOTA_CONFIG': {
        'HOTA_STUDIO_PATH': QE_CFG_HOTA_STUDIO,
        'SH00': {
            'CONFIG_PATH': QE_CFG_COMPLEMENTARY_SWUPDATE_MCU_PATH,
            'DLL_PATH': QE_CFG_COMPLEMENTARY_SWUPDATE_MCU_DLL_PATH,
        },
        'PHXX': {
            'CONFIG_PATH': QE_CFG_COMPLEMENTARY_SWUPDATE_CPU_PATH,
            'DLL_PATH': QE_CFG_COMPLEMENTARY_SWUPDATE_CPU_DLL_PATH,
        }
    },
    'RESET_REASON_DB': QE_CFG_COMPLEMENTARY_RESETREASON_DB
}


QE_CFG_HOTA_UDS_HEADER = QE_CFG_UDS_ON_ETHERNET_CONFIG['HEADER']

# UDS_ON_DOIP
QE_CFG_UDS_ON_DOIP_CONFIG = { \
    'HEADER': bytearray([0x00], [0xFC]), \
    'ROUTING_ACTIVATE': { \
        'TYPE' : bytearray([0x00]), \
        'PAYLOAD_LEN' : bytearray([0x00,0x00,0x00,0xe7]), \
        'OEM_SPECIFIC' : bytearray([0x00,0x00,0x00,0x00]) \
    }, \
    'CCU_PHYSICAL_ID': { \
        'SH00': {'REQ_ID': bytearray([0x0E, 0x81]), 'RSP_ID': bytearray([0x0E, 0x81])}, \
        'PHXX': {'REQ_ID': bytearray([0x0F, 0x00]), 'RSP_ID': bytearray([0x0F, 0x00])}, \
    }, \
    'LIDAR_PHYSICAL_ID': { \
    'LIDAR_L': {'REQ_ID': bytearray([0x07, 0x13]), 'RSP_ID': bytearray([0x07, 0x1B]), 'DST_PORT': 13410}, \
    'LIDAR_R': {'REQ_ID': bytearray([0x07, 0x14]), 'RSP_ID': bytearray([0x07, 0x1C]), 'DST_PORT': 13411}, \
    }, \
    'ADAPTER_IP': QE_CFG_ADDRESS_TABLE['CCU_AP']['IP'], \
    'RECEIVE_TIMEOUT'       : 10, \
    'REFRESH_TIMEOUT'       : 68, \
    'RETRY_GET_RESPONSE'    : 2, \
    'REQUEST_CORRECTLY_RECV_RESP_PENDING_TIMEOUT': 45, \
    'HOTA_CONFIG': { \
        'MANUAL_MODE': True, \
        'HOTA_STUDIO_PATH' : QE_CFG_HOTA_STUDIO, \
        'SH00': { \
            'CONFIG_PATH' : QE_CFG_COMPLEMENTARY_SWUPDATE_MCU_PATH, \
            'DLL_PATH' : QE_CFG_COMPLEMENTARY_SWUPDATE_MCU_DLL_PATH, \
        }, \
        'PHXX': { \
            'CONFIG_PATH' : QE_CFG_COMPLEMENTARY_SWUPDATE_CPU_PATH, \
            'DLL_PATH' : QE_CFG_COMPLEMENTARY_SWUPDATE_CPU_DLL_PATH, \
        }, \
        'MANUAL': { \
            'SH00': { \
                'moduleId': bytearray([0x07, 0xB1]), \
                'testerId': bytearray([0x07, 0xB1]), \
                'destinationIP': QE_CFG_ADDRESS_TABLE['PRK']['SH00']['IP'], \
                'sourcePort': 51011, \
                'destinationPort': 13400\
            }, \
            'PHXX': { \
                'moduleId': bytearray([0xe5, 0x900]), \
                'testerId': bytearray([0xe5, 0x90]), \
                'destinationIP': QE_CFG_ADDRESS_TABLE['PRK']['PH00']['IP'], \
                'sourcePort': 51011, \
                'destinationPort': 13400 \
            },\
        }\
    },\
    'UDP_SRC_PORT':{
        'SH00': 51021,
        'PH00': 51021,
    },\
    'RESET_REASON_DB': QE_CFG_COMPLEMENTARY_RESETREASON_DB \
}
###############################################################
# FEATURE TESTING CONFIGURATION
###############################################################

QE_CFG_DUMMY_CONFIG = {}
#--------------------------------------------------------------------------------
# ETHERNETCOM CONFIGURATION START
#--------------------------------------------------------------------------------
QE_CFG_LIDAR_DATA_R_PAYLOAD_LENGTH = 1472
QE_CFG_LIDAR_DATA_L_PAYLOAD_LENGTH = 1472
QE_CFG_LIDAR_DATA_R_BUFFER_SIZE = 300
QE_CFG_LIDAR_DATA_L_BUFFER_SIZE = 300

QE_CFG_ETHERNETCOM_UART_LOG_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/EthernetCom/%s/__raw_data__'
QE_CFG_ETHERNETCOM_UDP_CSV_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/EthernetCom/%s/__raw_data__'
QE_CFG_ETHERNETCOM_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/EthernetCom'
QE_CFG_ETHERNETCOM_HEADER_PATH = QE_CFG_PROJECT_PATH + '/0900_System/02_configout/rte/PH00/CtApFR_LSP_PRE/Contract_Header/Rte_Type.h'
QE_CFG_ETHERNETCOM_CHMOD_CMD = 'chmod -R 777 %s'

QE_CFG_ETHERNETCOM_GET_CONFIG_PATH = '/usr/local/bin'
QE_CFG_ETHERNETCOM_TC_ACCESS_PATH = '/usr/local'
QE_CFG_ETHERNETCOM_IDEAL_RANGE = 100
QE_CFG_ETHERNETCOM_HEADER_LEN = 8
QE_CFG_ETHERNETCOM_TYPE_ADDRESS = 'src'
QE_CFG_ETHERNETCOM_TC_ACCESS = [
    'cd /', \
    'mount -uw ./', \
    QE_CFG_ETHERNETCOM_CHMOD_CMD % QE_CFG_ETHERNETCOM_TC_ACCESS_PATH, \
    QE_CFG_ETHERNETCOM_CHMOD_CMD % ('%s' % QE_CFG_ETHERNETCOM_TC_ACCESS_PATH), \
    'sync' \
]
QE_CFG_ETHERNETCOM_GET_CONFIG_ACCESS = [
    'cd /', \
    'mount -uw ./', \
    QE_CFG_ETHERNETCOM_CHMOD_CMD % QE_CFG_ETHERNETCOM_GET_CONFIG_PATH, \
    QE_CFG_ETHERNETCOM_CHMOD_CMD % ('%s' % QE_CFG_ETHERNETCOM_GET_CONFIG_PATH), \
    'sync' \
]

QE_CFG_ETHERNETCOM = { \
    'LIDAR_DATA_R_BUFFER_SIZE': QE_CFG_LIDAR_DATA_R_BUFFER_SIZE, \
    'LIDAR_DATA_L_BUFFER_SIZE': QE_CFG_LIDAR_DATA_L_BUFFER_SIZE, \
    'LIDAR_R_MSG': 'LidarDataR' , \
    'CONFIG_INFO': {\
        'Ideal_Range': QE_CFG_ETHERNETCOM_IDEAL_RANGE, \
        'HEADER': QE_CFG_ETHERNETCOM_HEADER_LEN, \
        'Type_Addr': QE_CFG_ETHERNETCOM_TYPE_ADDRESS, \
        'TEST_PATH': QE_CFG_ETHERNETCOM_TEST_PATH.replace('/', '\\'), \
        'TESTCASE_ACCESS_PATH_DEFAULT': '%s/ethComTC*'%QE_CFG_ETHERNETCOM_TC_ACCESS_PATH, \
        'TESTCASE_ACCESS_PATH': '%s'%QE_CFG_ETHERNETCOM_TC_ACCESS_PATH, \
        'PERMISSION_ACCESS_CMD': { \
            'TC_ACCESS': QE_CFG_ETHERNETCOM_TC_ACCESS, \
            'CFG_ACCESS': QE_CFG_ETHERNETCOM_GET_CONFIG_ACCESS}, \
        'CCU_Addr_Adapter': QE_CFG_ADDRESS_TABLE['CCU_AP']['IP'], \
        'DEBUG_Port_Addr_Adapter': QE_CFG_ADDRESS_TABLE[ 'DEBUG_PORT']['IP'], \
        'PHeEe': {\
            'DRV': QE_CFG_ADDRESS_TABLE[ 'DRV']['PH00']['IP'], \
            'PRK': QE_CFG_ADDRESS_TABLE[ 'PRK']['PH00']['IP']}, \
        'sH00': {\
            'DRV': QE_CFG_ADDRESS_TABLE[ 'DRV']['SH00']['IP'], \
            'PRK': QE_CFG_ADDRESS_TABLE[ 'PRK']['SH00']['IP']}, \
    }, \
    
    'UDP_MESSAGE'{\
        ?
    }
}
#--------------------------------------------------------------------------------
# BACKBONE_COMMUNICATION CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_BACKBONE_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/Backbone_Communication/PRK'
QE_CFG_BUILD_PATH = QE_CFG_BACKBONE_TEST_PATH + '/_reprogram_'
QE_CFG_BACKBONE_LOG_PATH = QE_CFG_BACKBONE_TEST_PATH + '/__raw_data__'
QE_CFG_MN_DESTINATION_IP = '239.0.127.255'
QE_CFG_MN_DESTINATION_MAC = '01:00:5e:00:7f:ff'
QE_CFG_HW_DESTINATION_MAC = '01:00:5e:00:20:00'
QE_CFG_MW_DESTINATION_IP = '238'
QE_CFG_MW_DESTINATION_MAC = '01:00:5e'
QE_CFG_LOCAL_PORT = {'DRV': 52081, 'PRK': 52048, 'VP': 52082}

#--------------------------------------------------------------------------------
# CALIBRATION CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_CALIBRATION={\
    'TESTCASE_COFING':{}\
}
#--------------------------------------------------------------------------------
# CAN CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_CAN_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/CAN/PRK'
QE_CFG_CANOE_PRJ_PATH = '%s/__canoe_config__' % QE_CFG_CAN_TEST_PATH
QE_CFG_CAN_ARCHITECTURE_PATH = QE_CFG_PROJECT_PATH + '/0000_Architecture/'
QE_CFG_CAN_RP_PATH = QE_CFG_CAN_TEST_PATH + '/__reprogram__'
QE_CFG_CAN_RP_VERIFY_MSG_TRANSMISSSION_PATH = QE_CFG_CAN_RP_PATH + '/VERIFY_MSG_TRANSMISSSION'

QE_CFG_CAN = {?}
#--------------------------------------------------------------------------------
# DATALOGGER CONFIGURATION
#--------------------------------------------------------------------------------
# QE have to confirm/modify the below information related to Paths
QE_CFG_DATALOGGER_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/DataLogger/DRV'
QE_CFG_DATALOGGER_QNX_PATH = 'c:/appdata/DataLogger'
QE_CFG_MOWI_SCRIPTS_PATH = 'C:/Python27/Scripts'
QE_CFG_MOWI_OUT_PATH = 'C:/Users/Administrator/MotionWise_Perf'
QE_CFG_PC_TOOL_PATH = 'D:/003_Packages/RS4_DRV_2_X53.06.01/0600_Toolkit/DataLogger_PCTOOL_CANoeConfig/PC_TOOL'
QE_CFG_DLL_FILE_PATH = '<T.B.D>'

# QE have to confirm/modify the below information related to UDS
QE_CFG_LOCAL_PORT = {'DRV': 52081}
QE_CFG_REMOTE_ADDR_DRV = (QE_CFG_ADDRESS_TABLE['DRV']['SH00']['IP'], 13402)
QE_CFG_IP_ADDR_CCU_MCU = (QE_CFG_ADDRESS_TABLE['CCU_MCU']['IP'])
QE_CFG_IP_ADDR_DEBUG_PORT = (QE_CFG_ADDRESS_TABLE['DEBUG_PORT']['IP'])
QE_CFG_LOCAL_ADDR_DRV = (QE_CFG_ADDRESS_TABLE['CCU_MCU']['IP'], QE_CFG_LOCAL_PORT['DRV'])

QE_CFG_PHYS_CCU_REQID = [0x05, 0xD1]
QE_CFG_PHYS_CCU_RSPID = [0x05, 0xD9]
QE_CFG_PHYS_ECU_REQID_DRV = [0x05, 0xD5]
QE_CFG_PHYS_ECU_RSPID_DRV = [0x05, 0xDD]

# QE have to confirm/modify the below information related to the DataLogger log files
QE_CFG_DSSAD_FILE_NAME = 'DL_DataStored.dssad'
QE_CFG_HDP_STORAGE_FILE_NAME = {
    'HDP_STORAGE_BEFORE_30S': 'HDP_HdpExtDataStored_M30.dat',
    'HDP_STORAGE_AFTER_30S': 'HDP_HdpExtDataStored_P30.dat'
}


QE_CFG_DSSAD_HEADER_TEMPLATE ={\
    'File version:', \
    'EGT Timestamp', \
    'Date:', \
    'Timestamp:', \
    'SW Version:', \
    'Hardware Version:', \
    'Data type:' \
}\
QE_CFG_HDP_HEADER_TEMPLATE = { \
    'File Version:', \
    'EGT Timestamp', \
    'Date:', \
    'Timestamp:', \
    'SW Version:', \
    'Hardware Version:' \
}
QE_CFG_DSSAD_VARIABLE_NAME = 'Data'
QE_CFG_DL_TRIGGER_FLAGS = ['DCN_u8DataStoreReqFlag', 'DCN_u8HdpExtDataStoreReq', 'DCN_u8HdpActvStaFlag']

# QE have to confirm/modify the below information related to MotionWise test case
QE_CFG_MOWI_ENABLE_ALL_TRACES = 'python MotionWise_Trace_Filter.py --host PH00 --enable-all-traces'
QE_CFG_MOWI_TRACE_LOG_60S = 'python MotionWise_Perf.py --host PH00 --trace-log --measurement-duration 60'

QE_CFG_CHECK_CYC_ACT_AVG_TOLERANCE = 10

# QE have to confirm/modify the below information related to checking the file size test case
QE_CFG_CHECK_FILE_SIZE_TOLERANCE = 0

QE_CFG_DATALOGGER = {?}

#--------------------------------------------------------------------------------
# DEBUGCAN CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_DEBUGCAN={\
    'TESTCASE_COFING':{}\
}
#--------------------------------------------------------------------------------
# DEBUGETHCOM CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_DEBUGETHCOM_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/DebugEthCom/DRV/'
QE_CFG_DEBUGETHCOM_UART_LOG_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/DebugEthCom/DRV/__raw_data__'
QE_CFG_DEBUGETHCOM_UDP_CSV_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/DebugEthCom/DRV/__raw_data__'
QE_CFG_DEBUGETHCOM_RTE_DH_HEADER_PATH = QE_CFG_PROJECT_PATH + '/0900_System/02_configout/rte/dh/Common/include/Rte_Type.h'
QE_CFG_DEBUGETHCOM_TC_ACCESS_PATH = 'usr/local'
QE_CFG_DEBUGETHCOM_GET_CONFIG_PATH = 'opt/conf'
QE_CFG_DEBUGETHCOM_CHMOD_CMD = 'chmod -R 777 %s'

QE_CFG_DBGETHCAM_CSV_HEADER = '''Runnable Name,Number of BP,BP Number
{runnable_config}'''

QE_CFG_DBGETHCOM_CSV_CONFIG_RUNNABLE = '''{runnable},{bp_number},{bp_list}'''

QE_CFG_DEBUGETHCOM_FTP_SET_CONFIG = '''open {hostip}'''

QE_CFG_DEBUGETHCOM_FTP_GET_CONFIG = '''open {hostip}'''

QE_CFG_DEBUGETHCOM_FTP_RECOVERY_CONFIG = '''open {hostip}'''

QE_CFG_DEBUGETHCOM_TC_ACCESS = [ \
    'cd /', \
    'mount -uw ./.', \
    QE_CFG_DEBUGETHCOM_CHMOD_CMD%QE_CFG_DEBUGETHCOM_TC_ACCESS_PATH, \
    QE_CFG_DEBUGETHCOM_CHMOD_CMD%('%s/'%QE_CFG_DEBUGETHCOM_TC_ACCESS_PATH), \
    'sync' \
]

QE_CFG_DEBUGETHCOM_GET_CONFIG_ACCESS = [ \
    'cd /', \
    'mount -uw ./.', \
    QE_CFG_DEBUGETHCOM_CHMOD_CMD%QE_CFG_DEBUGETHCOM_GET_CONFIG_PATH, \
    QE_CFG_DEBUGETHCOM_CHMOD_CMD%('%s/'%QE_CFG_DEBUGETHCOM_GET_CONFIG_PATH), \
    'sync' \
]

# Requirement_LEVEL: INTERGRITY_PORT_RECV, REPRESENT_PORT_RECV
QE_CFG_DEBUGETHCOM_VERIFY_OVER_MAX_SIZE_LEVEL = 'REPRESENT_PORT_RECV'
QE_CFG_DEBUGETHCOM_VERIFY_UNDER_MAX_SIZE_LEVEL = 'REPRESENT_PORT_RECV'

# REQUIREMENT_LEVEL: INTERGRITY_PORT_RECV, REPRESENT_PORT_RECV
QE_CFG_DEBUGETHCOM_VERIFY_OVER_ACTIVATION_LEVEL = 'REPRESENT_PORT_RECV'
QE_CFG_DEBUGETHCOM_VERIFY_UNDER_ACTIVATION_LEVEL = 'REPRESENT_PORT_RECV'

# [ NORMAL ] REQUIREMENT_LEVEL: PORT_RECV_COMPLTED, PORT_RECV_MINIMAL
# [ABNORMAL] REQUIREMENT_LEVEL: PORT_RECV_ZERO_NUM, PORT_RECV_NOT_ENOUGH
QE_CFG_DEBUGETHCOM_VERIFY_ABNORMAL_BD_SIZE_LEVEL = 'PORT_RECV_COMPLTED'
QE_CFG_DEBUGETHCOM_VERIFY_ABNORMAL_BD_SIZE_LEVEL = 'PORT_RECV_ZERO_NUM'

# [ NORMAL ] REQUIREMENT_LEVEL: PORT_RECV_COMPLTED, PORT_RECV_MINIMAL
# [ABNORMAL] REQUIREMENT_LEVEL: PORT_RECV_ZERO_NUM, PORT_RECV_NOT_ENOUGH
QE_CFG_DEBUGETHCOM_VERIFY_NORMAL_ACTIVATION_LEVEL = 'PORT_RECV_COMPLTED'
QE_CFG_DEBUGETHCOM_VERIFY_ABNORMAL_ACTIVATION_LEVEL = 'PORT_RECV_NOT_ENOUGH'

QE_CFG_DEBUGETHCOM = {?}
#--------------------------------------------------------------------------------
# DIAGNOSTICS CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_DIAG_TEST_PATH               = QE_CFG_PROJECT_PATH + '/1000_Test/Diagnostics/PRK'
QE_CFG_DIAG_LOG_PATH                = QE_CFG_DIAG_TEST_PATH + '/__rawdata__'
QE_CFG_DIAG_RP_PATH                 = QE_CFG_DIAG_TEST_PATH + '/__reprogram__'
QE_CFG_DIAG_ARXML_PATH              = QE_CFG_PROJECT_PATH + '/0000_Architecture/Ecud_Dcm_Dem'
QE_CFG_DIAG_RP_VERIFY_DID_PATH      = QE_CFG_DIAG_RP_PATH + '/VERIFY_DID'
QE_CFG_DIAG_RP_VERIFY_RID_PATH      = QE_CFG_DIAG_RP_PATH + '/VERIFY_RID'
QE_CFG_DIAG_RP_VERIFY_IO_CTRL_PATH  = QE_CFG_DIAG_RP_PATH + '/VERIFY_IO_CTRL'
QE_CFG_DIAG_TIER_PATH               = QE_CFG_PROJECT_PATH + '/9000_Complementary/SwUpdate/VPU/TierLib'
QE_CFG_DIAG_TIER_CODE_PATH          = QE_CFG_DIAG_TIER_PATH + '/src/VPU_SwLib_tier.c'
QE_CFG_DIAG_TIER_BUILD_PATH         = QE_CFG_DIAG_TIER_PATH + '/build/aarch64le-debug'
QE_CFG_DIAG_TESCODE_TC145_PATH      = QE_CFG_DIAG_RP_VERIFY_DID_PATH + '/MAD_QTC_Diagnostics_145/VPU_SwLib_tier.c'
QE_CFG_DIAG_TESCODE_TC147_PATH      = QE_CFG_DIAG_RP_VERIFY_DID_PATH + '/MAD_QTC_Diagnostics_147/VPU_SwLib_tier.c'

# Alive msg structure: Defined in Ethdiag_Intypes.h
# ETHDIAG_DIAGNOSIS_PROTOCOL_VERSION (1 Byte)
# ETHDIAG_DIAGNOSIS_INVERSE_PROTOCOL_VERSION (1 Byte)
# ETHDIAG_ALIVE_MESSAGE_PAYLOAD_TYPE (2 Byte)
# ETHDIAG_PAYLOAD_LENGTH_INDEX (4 Byte)

QE_CFG_DIAG_FILE_SETUP = '''open {hostip}
user qnxuser
qnxuser
bi
cd {motionwise_path}
{backup_file}
{lcd_build_path}
{update_file}
quit
'''
QE_CFG_DIAG_SAMPL_CFG_TCP_TYPE = 'tcp and src port {src_port} or dst port {src_port} or src port {dst_port} or dst port {dst_port}'
QE_CFG_DIAG_MAKE_FILE_CONTENT = ['#', 'Target=', '$(OUTPUT_DIR)/$(ARTIFACT)']
QE_CFG_DIAG_BUILD_FILE_CMD = ['[D:]\\QNX\\qnx_x50\\qnxsdp-env.bat', "make"]
QE_CFG_DIAG_FILE_PATH = {
    'DRV': './usr/lib', \
    'PRC': './fs/lib', \
    'VP': './fs/lib', \
}

QE_CFG_DIAG_ALIVE_MSG = [
    [0xCA, 0x35,0X00,0x07, 0x00,0x00,0x00,0x00],
    [0xCC, 0X33,0x00,0x07, 0x00,0x00,0x00,0x00]]

QE_CFG_DIAGNOSTICS = {?}

#--------------------------------------------------------------------------------
# DOIP CONFIGURATION
#--------------------------------------------------------------------------------
#기본 경로 설정
QE_CFG_DOIP_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/DoIP/PRK'
QE_CFG_DOIP_LOG_PATH = QE_CFG_DOIP_PATH + '/__raw_data__'
QE_CFG_DOIP_RP_PATH = QE_CFG_DOIP_PATH + '/__reprogram__'
QE_CFG_DOIP_ARXML_PATH = QE_CFG_PROJECT_PATH + '/0000_Architecture/Ecud_Dcm_Dem'
QE_CFG_DOIP_TIER_PATH = QE_CFG_PROJECT_PATH + '/9000_Complementary/SWUpdate/VPU/Tierlib'
QE_CFG_DOIP_TIER_CODE_PATH = QE_CFG_DOIP_TIER_PATH + '/src/VPU_SwLib_tier.c'
QE_CFG_DOIP_TIER_BUILD_PATH = QE_CFG_DOIP_TIER_PATH + '/build/aarch64le-debug'

#테스트 케이스 경로 설정
QE_CFG_DOIP_RP_TC20 = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_020'
QE_CFG_DOIP_RP_TC21 = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_021'
QE_CFG_DOIP_RP_TC22 = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_022'
QE_CFG_DOIP_TESCODE_TC22_PATH = QE_CFG_DOIP_RP_TC22 + '/Dcm_Callout_User.c'
QE_CFG_DOIP_TESCODE_TC24_PATH = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_024/VPU_SwLib_tier.c'
QE_CFG_DOIP_TESCODE_TC25_PATH = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_025/VPU_SwLib_tier.c'
QE_CFG_DOIP_RP_TC29 = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_029'
QE_CFG_DOIP_TESCODE_TC29_PATH = QE_CFG_DOIP_RP_TC29 + '/Dcm_Callout_User.c'
QE_CFG_DOIP_RP_TC103 = QE_CFG_DOIP_RP_PATH + '/mAD_QTC_DoIP_103'

#필터 및 네트워크 설정
QE_CFG_DOIP_SAMPL_CFG_TCP_TYPE = 'tcp or udp and src port {src_port} or dst port {dst_port}'
QE_CFG_DOIP_SAMPL_CFG_UDP_TYPE = 'udp and src port {src_port} or dst port {dst_port}'
QE_CFG_DOIP_MAC_ADDR_TABLE = {}

#빌드 및 실행 관련
QE_CFG_DOIP_MAKE_FILE_CONTENT = ['#', 'TARGET =', '$(OUTPUT_DIR)/$(ARTIFACT)']
QE_CFG_DOIP_RESERVED_IP = '10.255.255.255'
QE_CFG_DOIP_BROADCAST_IP = '255.255.255.255'
QE_CFG_DOIP_BUILD_FILE_CMD = ["D:\\QNX\\qnx_x50\\qnxsdp-env.bat", "make"]



QE_CFG_DOIP_VA_INFO = {
    'MCU':{
        'dst':13400,'src':13400,'cycle':{'min':0.45,'max':0.55}},# cylce -> cycle
    'VPU1':{
        'dst':13400,'src':13400,'cycle':{'min':0.45,'max':0.55}},# cylce -> cycle
    'VPU2':{
        'dst':13400,'src':13400,'cycle':{'min':0.45,'max':0.55}},# cylce -> cycle
}
QE_CFG_DOIP_FILE_PATH = {
    'DRV':'./usr/lib',\
    'PRK':'./fs/lib',\
    'VP':'./fs/lib'

}
QE_CFG_DOIP_FILE_SETUP = '''open {hostip}
user qnxuser
qnxuser
bi
cd {motionwise_path}
{backup_file}
{lcd_build_path}
{update_file}
quit
'''
QE_CFG_DOIP_RR_SERVICE_INFO = {\
    'RR_Option': ['Request', 'Read', 'Clear'],\
    'Host_List': ['SH00', 'PHXX'], \
    'Service_Name': 'RoutineControl', \
    'Sub_Func': { \
        'Request': 'StartRoutine', \
        'Read': 'RequestRoutineResults', \
        'Clear': 'StartRoutine', \
        'SecurityAccess': ['SeedKey', 'SendKey'], \
        'ExtendedSession': 'ExtendedSession', \
        'ECUReset': 'HardReset'}, \
    'OB_Val': { \
        'Request': 0x01, \
        'Read': None, \
        'Clear': 0x02, \
        'SecurityAccess': None, \
        'ExtendedSession': None, \
        'ECUReset': None \
        }, \
    'RoutineControl_Mapping': { \
        'StartRoutine'          : 0x01, \
        'StopRoutine'           : 0x02, \
        'RequestRoutineResults' : 0x03},\
}

QE_CFG_DOIP = {?}

#--------------------------------------------------------------------------------
# E2E_CAN CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_E2E_CAN={\
    'TESTCASE_COFING':{}\
}
#--------------------------------------------------------------------------------
# E2E_ETHCC CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_E2E_ETHCC={\
    'TESTCASE_COFING':{}\
}
#--------------------------------------------------------------------------------
# ERROR_HANDLER CONFIGURATION
#--------------------------------------------------------------------------------

QE_CFG_EH_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/Error_Handler/PRK'
QE_CFG_EH_LOG_PATH = QE_CFG_EH_PATH + '/__raw_data__'
QE_CFG_EH_RP_PATH = QE_CFG_EH_PATH + '/__reprogram__'
QE_CFG_EH_RP_DTC_RECORD_PATH = QE_CFG_EH_RP_PATH + '/VERIFY_DTC_RECORD'
QE_CFG_EH_RP_CPU_LOAD_PATH = QE_CFG_EH_RP_PATH + '/VERIFY_CPU_LOAD'
QE_CFG_EH_RP_ERROR_QUEUE_PATH = QE_CFG_EH_RP_PATH + '/VERIFY_ERROR_QUEUE'
QE_CFG_EH_RP_WCET_PATH = QE_CFG_EH_RP_PATH + '/VERIFY_DTC_RECORD_WCET'
QE_CFG_EH_RP_TOKEN_PATH = QE_CFG_EH_RP_PATH + '/VERIFY_DTC_RECORD_TOKEN'
QE_CFG_EH_WCET_TABLE_PATH = QE_CFG_PROJECT_PATH + '/0001_Documents/MV_DRV_2_X40_Test_Reports/Architecture_TestReport/'
QE_CFG_EH_HEADER_PATH = QE_CFG_PROJECT_PATH + '/0900_System/01_core/safetyhealth/errorhandler'
QE_CFG_RTE_SH00 = QE_CFG_PROJECT_PATH + '/0900_System/02_configout/rte/SH00'
QE_CFG_EH_DSC = QE_CFG_EH_HEADER_PATH + '/CpCdErrorHandlerMaster_SH00/units/EHM_DSC_SH00/inc'
QE_CFG_EH_INTERNAL = QE_CFG_EH_HEADER_PATH + '/CpCdErrorHandlerMaster_SH00/units/EHM_Internal_SH00/api'
QE_CFG_EHM_CONFIG = QE_CFG_EH_HEADER_PATH + '/ErrorHandlerMaster/units/EHM_Configuration/api'
QE_CFG_EH_REPORT_ERROR = QE_CFG_EH_HEADER_PATH + '/CpCdErrorHandlerMaster_SH00/units/EH_API_SH00/api'

QE_CFG_EH_RR_DATA_DELIMITER = [0xFF, 0xFF]
QE_CFG_EH_RR_MSG_DELIMITER = [0xEE, 0xEE]

QE_CFG_EH_CPU_LOAD_PATH = './opt'
QE_CFG_EH_EXE_CPU_LOAD_CMD = 'on -C%s -p 80 ./opt/%s'
QE_CFG_EH_ACCESS_PATH = {
    'DRV': 'usr/local/',
    'PRK': 'fs/rem/',
    'VP': 'fs/rem/'
}

QE_CFG_EH_CPULOAD_TRANSFER_CMD = '''open {hostip}
    user qnxuser
    qnxuser
    bi
    cd {motionwise_path}
    {delete_old_file}
    {transfer_cmd}
    quit
    '''

QE_CFG_EH_CPULOAD_RECOVERY_CMD = '''open {hostip}
    user qnxuser
    qnxuser
    bi
    cd {motionwise_path}
    {delete_file
    quit
    '''
QE_CFG_EH_RR_ERROR_ID = {?}


#--------------------------------------------------------------------------------
# ETHCC CONFIGURATION
#--------------------------------------------------------------------------------

QE_CFG_ETHCC_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/EthCC'
QE_CFG_ETHCC_UART_LOG_PATH = '/%s/%s/__log__/Uart_log.log'
QE_CFG_ETHCC_UDP_LOG_PATH = '/%s/%s/__udp_msg__/UDP_Messages.csv'
QE_CFG_ETHCC_DESTINATION_IP = '239.0.127.255'
QE_CFG_ETHCC_DESTINATION_MAC = '01:00:5e:00:7f:ff'
QE_CFG_UDPNC_CFG_PATH = QE_CFG_PROJECT_PATH + "/0900_System/02_configout/rte/SH00/mIC/Common/BSW_Output/inc/UdpNm_Cfg.h"
QE_CFG_PDU_MAX_LEN_DEF = '#define UDPNM_MAX_PDU_LENGTH'
QE_CFG_PDU_INFO_LEN_DEF = '#define UDPNM_PN_INFO_LENGTH'
QE_CFG_PDU_INFO_OFFSET_DEF = '#define UDPNM_PN_INFO_OFFSET'
QE_CFG_LOCAL_PORT = {'DRV': 52081, 'PRK': 52048, 'VP': 52082}

QE_CFG_ETHCC = {?}

#--------------------------------------------------------------------------------
# ETHNM_PN CONFIGURATION
#--------------------------------------------------------------------------------

QE_CFG_ETHNM_PN_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/EthNM_PN/PRK'
QE_CFG_ETHNM_PN_RP_PATH = QE_CFG_ETHNM_PN_TEST_PATH + '/__reprogram__'
QE_CFG_ETHNM_PN_TEST_LOG_PATH = QE_CFG_ETHNM_PN_TEST_PATH + '/__raw_data__'
QE_CFG_ETHNM_PN_LOG_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/EthNM_PN/__Testing__'
QE_CFG_UDPNM_CFG_PATH = QE_CFG_PROJECT_PATH + "/0900_System/02_configout/rte/SH00/mIC/Common/BSW_Output/inc/UdpNm_Cfg.h"
QE_CFG_ETHNM_PN_DESTINATION_IP = '239.0.127.255'
QE_CFG_ETHNM_PN_DESTINATION_MAC = '01:00:5e:00:7f:ff'
QE_CFG_PDU_MAX_LEN_DEF = '#define UDPNM_MAX_PDU_LENGTH'
QE_CFG_PDU_INFO_LEN_DEF = '#define UDPNM_PN_INFO_LENGTH'
QE_CFG_PDU_INFO_OFFSET_DEF = '#define UDPNM_PN_INFO_OFFSET'
QE_CFG_LOCAL_PORT = {'DRV': 52081, 'PRK': 52048, 'VP': 52082}

QE_CFG_ETHNM_PN = { ?}

#--------------------------------------------------------------------------------
# ETHTP CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_ETHTP={\
    'TESTCASE_COFING':{}\
}
#--------------------------------------------------------------------------------
# FULL_COM CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_FULL_COM={\
    'TESTCASE_COFING':{}\
}

#--------------------------------------------------------------------------------
# HOST_SUPERVISION CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_HSV_TEST_PATH= QE_CFG_PROJECT_PATH + '/1000_TEST/HostSupervision/PRK'
QE_CFG_HSV_TEST_CODE_PATH = QE_CFG_HSV_TEST_PATH + '/__reprogram__'
QE_CFG_HSV_TEST_LOG = QE_CFG_HSV_TEST_PATH + '/__raw_data__'

QE_CFG_HOST_SUPERVISION={?}
#--------------------------------------------------------------------------------
# IO_SLEEP CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_IO_SLEEP_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/IO_Sleep'
QE_CFG_IO_SLEEP_TEST_LOG = QE_CFG_IO_SLEEP_TEST_PATH + '/__raw_data__'
QE_CFG_IO_SLEEP_REPROGRAM_PATH = QE_CFG_IO_SLEEP_TEST_PATH + '/__reprogram__'
QE_CFG_IO_SLEEP_CONNECTION_EST = 0
QE_CFG_PPS_RESPONSE = {
    '0000' : {'Result' : 'Positive', 'Description' : 'ACK'}, \
    '0001' : {'Result' : 'Positive', 'Description' : 'TCP is connected normally'}, \
    '5000' : {'Result' : 'Negative', 'Description' : 'File path is wrong '}, \
    '5001' : {'Result' : 'Negative', 'Description' : 'Syntax of transfer messenger is wrong'}, \
    '5004' : {'Result' : 'Negative', 'Description' : 'Receiving waveform output messenger while outputing waveform'}
}

QE_CFG_IO_SLEEP_POWER_CFG = {
    'PS_ON': {
        'Pattern': 'Single', \
        'Method': 1, \
        'Cycle_Pattern': 1, \
        'Timeout': 1, \
        'Voltage': 12
    }, \
    'PS_OFF': {
        'Pattern': 'Single', \
        'Method': 1, \
        'Cycle_Pattern': 1, \
        'Timeout': 1, \
        'Voltage': 0
    }
}

QE_CFG_HW_MAPPING = {
    'HILS_ONLY'         : 'Connect Battery Powerline, IGN, ACC To HILS', \
    'HILS:B_EXT:IGNACC' : 'Connect Battery Powerline To HILS and IGN, ACC To 12V DC Power Supply', \
    'HILS:B_EXT:ACC'    : 'Connect Battery Powerline To HILS and ACC To 12V DC Power Supply, IGN not connect', \
    'HILS:B'            : 'Connect Battery Powerline To HILS and IGN, ACC not connect', \
    'HILS:IGNACC_EXT:B' : 'Connect IGN, ACC To HILS and Battery Powerline To 12V DC Power Supply', \
    'HILS:ACC_EXT:B'    : 'Connect ACC To HILS and Battery Powerline To 12V DC Power Supply, IGN not connect', \
    'HILS:IGN_EXT:BACC' : 'Connect IGN To HILS and Battery Powerline, ACC To 12V DC Power Supply', \
    'HILS:BIGN'         : 'Connect Battery Powerline, IGN To HILS and ACC not connect', \
    'HILS:BACC'         : 'Connect Battery Powerline, ACC To HILS and IGN not connect', \
    'EXT_1:B_EXT_2:ACC' : 'Connect Battery Powerline To Output 1 of 12V DC Power Supply and ACC to Output 2 of 12V DC Power Supply, IGN not connect', \
    'EXT_ONLY'          : 'Connect Battery Powerline, IGN, ACC To 12V DC Power Supply', \
}
QE_CFG_IO_SLEEP = { ?}

# -------------------------------------------------------------
# LCS CONFIGURATION
# -------------------------------------------------------------
QE_CFG_LCS_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/LCS/PRK'
QE_CFG_LCS_PREPROGRAM_PATH = QE_CFG_LCS_TEST_PATH + '/__reprogram__'
QE_CFG_LCS_PREPROGRAM_SOFT_TRIG_PATH = QE_CFG_LCS_PREPROGRAM_PATH + '/SOFT_TRIGER'
QE_CFG_LCS_PREPROGRAM_HARD_TRIG_PATH = QE_CFG_LCS_PREPROGRAM_PATH + '/HARD_TRIGER'
QE_CFG_LCS_PREPROGRAM_PREBOOTING_PATH = QE_CFG_LCS_PREPROGRAM_PATH + '/PREBOOTING'

QE_CFG_LCS_TC_CHANGE_STATE_TABLE_1 = [
    [[4,4,0]],\
    [[4,4,0],[6,6,0]]\
    [[4,4,0],[6,6,0],[4,4,0]],\
    [[4,4,0],[6,6,0],[4,4,0],[6,6,0]],\
    [[4,1,0],[6,1,0]],\
    [[4,1,0],[4,4,0]],\
    [[4,1,0],[4,4,0],[6,6,0]],\
    [[4,1,0],[6,1,0],[4,4,0],[6,6,0]],\
    [[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],\
    [4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],
    [4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],
    [4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0]],\
    [[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],\
    [4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],
    [4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],
    [4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0],[4,4,0],[6,6,0]],\
]
QE_CFG_LCS_TC_CHANGE_STATE_TABLE_2 = [
    [[4,4,4]],\
    [[4,4,4],[6,6,6]]\
    [[4,4,4],[6,6,6],[4,4,4]],\
    [[4,4,4],[6,6,6],[4,4,4],[6,6,6]],\
    [[4,1,1],[6,1,1]],\
    [[4,1,1],[4,4,4]],\
    [[4,1,1],[4,4,4],[6,6,6]],\
    [[4,1,1],[6,1,1],[4,4,4],[6,6,6]],\
    [[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],\
     [4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],\
     [4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],\
     [4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4]],\
    [[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],\
     [4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],\
     [4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],\
     [4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6],[4,4,4],[6,6,6]],\
]

QE_CFG_LCS = { ?}

#--------------------------------------------------------------------------------
# MP_BUILD CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_LOGGING={\
    'TESTCASE_CONFIG':{}\
}

#--------------------------------------------------------------------------------
# PERSISTENCY CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_PERSISTENCY_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/Persistency/PRK'
QE_CFG_PERSISTENCY_LOG_PATH = QE_CFG_PERSISTENCY_TEST_PATH + '/__rawdata__'
QE_CFG_PERSISTENCY_RP_PATH = QE_CFG_PERSISTENCY_TEST_PATH + '/__reprogram__'
QE_CFG_PERSISTENCY_RP_CRITICAL_PATH = QE_CFG_PERSISTENCY_RP_PATH + '/critical'
QE_CFG_PERSISTENCY_RP_NORMAL_PATH = QE_CFG_PERSISTENCY_RP_PATH + '/Normal'
QE_CFG_PERSISTENCY_RP_DEVERSION_PATH = QE_CFG_PERSISTENCY_RP_PATH + '/DeVersion'

QE_CFG_PERSISTENCY = { ?}


#--------------------------------------------------------------------------------
# PPS_CAPTURE CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_PPS_CAPTURE={\
    'TESTCASE_CONFIG':{}\
}

#--------------------------------------------------------------------------------
# RA CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_RA ={\
    'TESTCASE_CONFIG':{}\
}

#--------------------------------------------------------------------------------
# RESET_REASON CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_RESETREASON_SWC_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/ResetReason/_raw_data__'
QE_CFG_RESETREASON_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/ResetReason/__test_code__'
QE_CFG_RESETREASON_TEST_CONFIG_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/ResetReason/__hota_config__'
QE_CFG_RR_LOCAL_PORT = {'DRV': 53081, 'PRK': 53058, 'VP': 53082}
QE_CFG_RR_REMOTE_PORT = {'DRV': 13404, 'PRK': 13404, 'VP': 13404}
QE_CFG_RESETREASON_DATA_DELIMITER = [0xFF, 0xFF]
QE_CFG_RESETREASON_MSG_DELIMITER = [0xEE, 0xEE]
QE_CFG_RESETREASON_MSG_LINK = [0xFE, 0xFE]
QE_CFG_RESETREASON_CHMOD_CMD = 'chmod -R 777 %s'
QE_CFG_RESETREASON_TC_ACCESS_PATH = 'opt/RR_dir'
QE_CFG_RESETREASON_PERMISSION_ACCESS = 'ls ./opt/RR_dir\r'
QE_CFG_RESETREASON_RENAME_CMD = 'mv ./opt/RR_dir/%s ./opt/RR_dir/%s'

QE_CFG_RESETREASON_HOTA_PHXX_CONFIG_PATH = QE_CFG_RESETREASON_TEST_CONFIG_PATH+'/PHXX/ReprogramConfig_GEN2_PRK2_VPU.hcfg-r'
QE_CFG_RESETREASON_HOTA_PHXX_ROM_PATH = QE_CFG_RESETREASON_TEST_CONFIG_PATH+'/PHXX/VPU_GN7_PRK_1.5_X51.01.01.bin'
QE_CFG_RESETREASON_HOTA_PHXX_UDS_DLL_PATH = QE_CFG_RESETREASON_TEST_CONFIG_PATH+'/PHXX/HKMC_AdvancedSeedKey_Win32.dll'

QE_CFG_RESETREASON_HOTA_SH00_CONFIG_PATH = QE_CFG_RESETREASON_TEST_CONFIG_PATH+'/SH00/ReprogramConfig_GEN2_PRK_MCU_MSWAP_HSM_ON.hcfg-r'
QE_CFG_RESETREASON_HOTA_SH00_ROM_PATH = QE_CFG_RESETREASON_TEST_CONFIG_PATH+'/SH00/MCU_GN7_PRK_1.5_X51.01.01.bin'
QE_CFG_RESETREASON_HOTA_SH00_UDS_DLL_PATH = QE_CFG_RESETREASON_TEST_CONFIG_PATH+'/SH00/GN7_PRK15.dll'

QE_CFG_RESETREASON_SWC_NAME = 'SWC_NAME#' # will be change name by QE
QE_CFG_RESETREASON_FLAG = 'SWC_FLAG#' # will be change name by QE

QE_CFG_RESETREASON_ERROR_ID = {\
    'ECUM_RESETREASON'      : 0x01, \
    'EH_RESET_INFO'      : 0x02, \
    'HSV_RESET_INFO'      : 0x03, \
    'MW_ASILCOMENABLED'      : 0x04, \
    'MW_LCSMHOSTSTATE'      : 0x05, \
    'EH_REQUESTRESET_STATE' : 0x06, \
    'WDGM_FIRSTEXPIREDSEID'      : 0x07, \
    'COMM_CURCOMMODE'      : 0x08, \
    'EH_DISABLED_BY_OTA'      : 0x09, \
    'TLF_STARTUP_REQ'      : 0x0A, \
    'REPROGRAM_MCU'      : 0x0B, \
    'DROP_VOLATAGE'      : 0x0C, \
    0x01: 'ECUM_RESETREASON', \
    0x02: 'EH_RESET_INFO', \
    0x03: 'HSV_RESET_INFO', \
    0x04: 'MW_ASILCOMENABLED', \
    0x05: 'MW_LCSMHOSTSTATE', \
    0x06: 'EH_REQUESTRESET_STATE', \
    0x07: 'WDGM_FIRSTEXPIREDSEID', \
    0x08: 'COMM_CURCOMMODE', \
    0x09: 'EH_DISABLED_BY_OTA', \
    0x0A: 'TLF_STARTUP_REQ', \
    0x0B: 'REPROGRAM_MCU', \
    0x0C: 'DROP_VOLATAGE', \
}
QE_CFG_RESETREASON_TC_ACCESS = {
    'cd /',\
    'mount -uw ./opt',\
    QE_CFG_RESETREASON_CHMOD_CMD%QE_CFG_RESETREASON_TC_ACCESS_PATH,\
    QE_CFG_RESETREASON_CHMOD_CMD%('%s/'%QE_CFG_RESETREASON_TC_ACCESS_PATH),\
    'sync'\
}
QE_CFG_RESETREASON_EID_LEN_MAPPING = {
    'ECUM_RESETREASON'          : {'DRV':1,'VP':1,'PRK':1},\
    'EH_RESET_INFO'             : {'DRV':1,'VP':1,'PRK':1},\
    # IF DUIT HAVE EH_RESET error record info, Length will be change to 4 from 1
    'HSV_RESET_INFO'            : {'DRV':1,'VP':1,'PRK':1},\
    # IF DUIT HAVE EH_RESET error record info, Length will be change to 6 from 1
    'MW_ASILCOMENABLED'         : {'DRV':1,'VP':1,'PRK':1},\
    'MW_LCSMHOSTSTATE'          : {'DRV':2,'VP':3,'PRK':4},\
    'EH_REQUESTRESET_STATE'     : {'DRV':1,'VP':1,'PRK':1},\
    'WDGM_FIRSTEXPIREDSEID'     : {'DRV':2,'VP':2,'PRK':2},\
    'COMM_CURCOMMODE'           : {'DRV':6,'VP':2,'PRK':3},\
    'EH_DISABLED_BY_OTA'        : {'DRV':1,'VP':1,'PRK':1},\
    'TLF_STARTUP_REQ'           : 0x0A,\
    'REPROGRAM_MCU'             : 0x0B,\
    'DROP_VOLATAGE'             : 0x0C,\
}

QE_CFG_RESET_REASON = {?}

#--------------------------------------------------------------------------------
# RTE_INTERFACE CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_RTE_INTERFACE = {\
    'VALIDATE_CONFIG': {\
        'Project_path': QE_CFG_PROJECT_PATH,
        'Validate_path': QE_CFG_PROJECT_PATH + '/1000_Test/RTE_Interface/',
        'Validate_files': ['rte_tool_1_usr_config.py', 'rte_tool_2_int_config.py', 'rte_tool_3_read.py', \
                           'rte_tool_4_check.py', 'rte_tool_5_generate.py', 'rte_tool_6_report.py'],\
        'Validate_table': {
            'Rte_IWrite_IRead'      : {"Folder_Check": 'T010_Rte_IWrite_IRead', 'Port_Check' : 'Rte_IWriteIRead_PortCheck.xlsx'},
            'Rte_IWriteRef_IRead'   : {"Folder_Check": 'T010_Rte_IWriteRef_IRead', "Port_Check" : 'Rte_IWriteRef_IRead_PortCheck.xlsx'},
            'Rte_Call_Timestamp'    : {"Folder_Check": 'T010_Rte_Call_Timestamp', "Port_Check":  'Rte_Call_Timestamp_PortCheck.xlsx'},
            'Rte_Call_SwcInfo'      : {"Folder_Check": 'T010_Rte_Call_SwcInfo', "Port_Check":  'Rte_Call_SwcInfo_PortCheck.xlsx'},
            'Rte_BigData'           : {"Folder_Check": 'T010_Rte_BigData', "Port_Check":  'Rte_BigData_PortCheck.xlsx'},
            'Rte_PersistencyData'   : {"Folder_Check": 'T010_Rte_PersistencyData', "Port_Check":  'Rte_PersistencyData_PortCheck.xlsx'},
            'Rte_Can_IRead'         : {"Folder_Check": 'T010_Rte_Can_IRead', "Port_Check":  'Rte_Can_IRead_PortCheck.xlsx'},
            'Rte_Can_IWrite '       : {"Folder_Check": 'T010_Rte_Can_IWrite', "Port_Check":  'Rte_Can_IWrite_PortCheck.xlsx'},
            'Rte_Can_IWriteRef'     : {"Folder_Check": 'T010_Rte_Can_IWriteRef', "Port_Check" : 'Rte_Can_IWriteRef_PortCheck.xlsx'},
            'Rte_Ethcc_IRead'       : {"Folder_Check": 'T010_Rte_Ethcc_IRead', "Port_Check":  'Rte_Ethcc_IRead_PortCheck.xlsx'},
            'Rte_Ethcc_IWrite'      : {"Folder_Check": 'T010_Rte_Ethcc_IWrite', "Port_Check": 'Rte_Ethcc_IWrite_PortCheck.xlsx'},
            'Rte_Ethcc_IWriteRef'   : {"Folder_Check": 'T010_Rte_Ethcc_IWriteRef', "Port_Check" : 'Rte_Ethcc_IWriteRef_PortCheck.xlsx'}
        },\
    
        'ETH_ADAPTER': {
            'IP_ADDR': QE_CFG_ADDRESS_TABLE['CCU_AP']['IP']
        }, \
        'SH00': {
            'Test_Path': None, \
            'Reprogramming': {
                'Target': 'SH00', \
                'SWCs': [], \
                'DebugMode': True, \
                'DebugLevel': 2 \
            }
        }, \
        'PH00': {\
            'Test_Path': None, \
            'Reprogramming': {\
                'Target': 'PH00', \
                'SWCs': [], \
                'Option':'Specific',\
                'DebugMode': True, \
                'DebugLevel': 2 \
            }
        },\
        'PH01':{\
            'Test_Path': None, \
            'Reprogramming': {\
                'Target': 'PH01', \
                'SWCs': [], \
                'Option':'Specific',\
                'DebugMode': True, \
                'DebugLevel': 2 \
            },\
        }
        
    },\
    'TESTCASE_CONFIG':{?}
}

#--------------------------------------------------------------------------------
# SCHEDULING_SERVICE CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_SCHE_SER_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/SchedulingService/PRK'
QE_CFG_SCHE_SER_RP_PATH = QE_CFG_SCHE_SER_TEST_PATH + '/__reprogram__'
QE_CFG_SCHE_SER_RP_UART_LOG_INIT_PATH = QE_CFG_SCHE_SER_RP_PATH + '/VERIFY_UART_LOG_INIT'
QE_CFG_SCHE_SER_RP_RTE_WCET_PATH = QE_CFG_SCHE_SER_RP_PATH + '/VERIFY_RTE_WCET'
QE_CFG_SCHE_SER_RP_WCET_DEADLINE_PATH = QE_CFG_SCHE_SER_RP_PATH + '/VERIFY_WCET_DEADLINE'
QE_CFG_SCHE_SER_RP_UART_TIMESTAMP_PATH = QE_CFG_SCHE_SER_RP_PATH + '/VERIFY_UART_TIMESTAMP'
QE_CFG_SCHE_SER_PLF_CFG_PATH = QE_CFG_PROJECT_PATH + '/0900_System/02_configout/rte'
QE_CFG_SCHE_SER_ETHCC_DB_PATH = QE_CFG_PROJECT_PATH + '/0000_Architecture/ethcc.xlsx'
QE_CFG_SCHE_SER_CAN_DB_PATH = QE_CFG_PROJECT_PATH + '/0000_Architecture/'

QE_CFG_SCHE_SER_UART_CMD ={\
    'VERIFY_RTE_WCET':'top',\
    'VERIFY_WCET_DEADLINE':{\
        'Sampling_Process': ['Permission_Access', 'Remove_Access_Folder', 'Create_Access_Folder','Create_Folder_Trigger'],\
        'DRV' : {\
            'Permission_Access': 'mount -uw ./ & sync & chmod 777 ./usr/local/',\
            'Remove_Access_Folder' :'mkdir ./usr/local/access_folder & sync',\
            'Create_Access_Folder' :'mkdir ./usr/local/access_folder/%s & sync',\
            'Create_Folder_Trigger' :'rm -R ./usr/local/access_folder & sync',\
        },\
        'VP': {\
            'Permission_Access': 'mount -uw ./fs & sync & chmod 777 ./fs',\
            'Remove_Access_Folder' :'mkdir ./fs/local/access_folder & sync',\
            'Create_Access_Folder' :'mkdir ./fs/local/access_folder/%s & sync',\
            'Create_Folder_Trigger' :'rm -R ./fs/local/access_folder & sync',\
        },\
        'PRK': {\
            'Permission_Access': 'mount -uw ./fs & sync & chmod 777 ./fs',\
            'Remove_Access_Folder' :'mkdir ./fs/local/access_folder & sync',\
            'Create_Access_Folder' :'mkdir ./fs/local/access_folder/%s & sync',\
            'Create_Folder_Trigger' :'rm -R ./fs/local/access_folder & sync',\
        },\
    }
}

QE_CFG_SCHE_SER_PH00_RUNNABLE_INIT_LIST = [
    'RCtApIPSV_FreeRunning_Init','RCtApCC_FreeRunning_Init',
    'RCtApIDSV_FreeRunning_Init','RCtApSR_OD_FreeRunning_Init',
    'RCtApVFS_FreeRunning_Init','RCtApVPU1_NFR_Init',
]

QE_CFG_SCHEDULING_SERVICE = {?}


#--------------------------------------------------------------------------------
# SECURITY CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_SECURITY={\
    'TESTCASE_CONFIG':{?}\
}
#--------------------------------------------------------------------------------
# SWUPDATE CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_SWUPDATE_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/SWUpdate/Drv'
QE_CFG_SWUPDATE_NM_DEST_IP = '239.0.127.255'

QE_CFG_SWUPDATE_TEST_CONFIG_PATH = QE_CFG_SWUPDATE_TEST_PATH+'/_HOTA_Config_'
QE_CFG_SWUPDATE_NM_CFG_BUILD_PATH = QE_CFG_SWUPDATE_TEST_PATH+'/_NM_Config_'
QE_CFG_SWUPDATE_HOTA_SH00_CONFIG_PATH = QE_CFG_SWUPDATE_TEST_CONFIG_PATH+' /SH00/ReprogramConfig_GEN2_DRV2_MCU_HSWAP_HSM_ON.hcfg-r'
QE_CFG_SWUPDATE_HOTA_SH00_ROM_PATH = QE_CFG_SWUPDATE_TEST_CONFIG_PATH+' /SH00/MCU_MV1_DRV_2_X40.03.01.bin'
QE_CFG_SWUPDATE_HOTA_SH00_UDS_DLL_PATH = QE_CFG_SWUPDATE_TEST_CONFIG_PATH+' /SH00/DRVII_MCU.dll'

QE_CFG_SWUPDATE_HOTA_PHXX_CONFIG_PATH = QE_CFG_SWUPDATE_TEST_CONFIG_PATH+' /PHXX/ReprogramConfig_GEN2_DRV2_CPU.hcfg-r'
QE_CFG_SWUPDATE_HOTA_PHXX_ROM_PATH = QE_CFG_SWUPDATE_TEST_CONFIG_PATH+' /PHXX/VPU_MV1_DRV_2_X40.03.01.bin'
QE_CFG_SWUPDATE_HOTA_PHXX_UDS_DLL_PATH = QE_CFG_SWUPDATE_TEST_CONFIG_PATH+' /PHXX/HKMC_AdvancedSeedKey_Win32.dll'

QE_CFG_SWUPDATE_NORMAL_VOLTAGES = 9.5
QE_CFG_SWUPDATE_ABNORMAL_VOLTAGES = 4.5
QE_CFG_SWUPDATE_PROCESS_TIMEOUT = 360

QE_CFG_SWUPDATE_ROUTINE_CONTROL_SH00_START = 'RoutineControl_0210_F1B1'
QE_CFG_SWUPDATE_ROUTINE_CONTROL_SH00_END = 'RoutineControl_FF01_0Aor0B_F1B1'
QE_CFG_SWUPDATE_SECURITY_ACCESS_SH00 = 'SecurityAccessPrevent'

QE_CFG_SWUPDATE_ROUTINE_CONTROL_PHXX_START = 'RoutineControl_FF00_F1B2'
QE_CFG_SWUPDATE_ROUTINE_CONTROL_PHXX_END = 'RoutineControl_FF01_00F1B2'
QE_CFG_SWUPDATE_ROUTINE_CONTROL_PH00_RB = 'RoutineControl_RB_0213_00F1B2'
QE_CFG_SWUPDATE_SECURITY_ACCESS_PHXX = 'SecurityAccess'

QE_CFG_SWUPDATE = {\
    'POWER_ONLINE' : QE_CFG_POWER_ONLINE,\
    'COMPLETED_AT_F187': False,\
    'ECU_STARTUP_TIME': QE_CFG_REBOOT_ECU_TIMEOUT,\
    'TEST_PATH':QE_CFG_SWUPDATE_TEST_PATH,\
    'PDU_FRAME':QE_CFG_ETHNM_PN['PDU_FRAME'],\
    'TRANSFER_TIME_MAX': 300,\
    'CONFIG_INPUT':{
        'SH00':{
            'TARGET':'SH00','ADPTER_IP':'10.0.6.0',\
            'INPUT':{
                'CONFIG_PATH' : QE_CFG_SWUPDATE_HOTA_SH00_CONFIG_PATH,
                'ROM_PATH':QE_CFG_SWUPDATE_HOTA_SH00_ROM_PATH,
                'DLL_PATH':QE_CFG_SWUPDATE_HOTA_SH00_UDS_DLL_PATH,
            }
        },\
        'PHXX':{
                'CONFIG_PATH' : QE_CFG_SWUPDATE_HOTA_PHXX_CONFIG_PATH,
                'ROM_PATH': QE_CFG_SWUPDATE_HOTA_PHXX_ROM_PATH,
                'DLL_PATH': QE_CFG_SWUPDATE_HOTA_PHXX_UDS_DLL_PATH,
        },\
    }
    ?
}
#--------------------------------------------------------------------------------
# TASK_SUPERVISION CONFIGURATION
#--------------------------------------------------------------------------------
QE_CFG_TSV_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/TaskSupervision'
QE_CFG_TSV_CONFIG_PDEBUG_PATH = QE_CFG_TSV_TEST_PATH + '/__Config__'
QE_CFG_TSV_LIST_HEADER = ['EH_ErrorIDMappingSH00.h', 'EH_ErrorIDMapping_Error_Handler.h', 'EH_ErrorIDMapping_HostSupervision.h']
QE_CFG_TSV_CONTRACTHEADER_PATH = QE_CFG_PROJECT_PATH + '/0900_System/02_configout/rte/SH00/Contract_Header/%s'
QE_CFG_TSV_HEADER_SRC_PATH = QE_CFG_PROJECT_PATH + '/0900_System/01_core/safetyhealth/errorhandler/CpcDErrorHandlerMaster_SH00/units/EH_API_SH00.api'
QE_CFG_TSV_PDEBUG_SETUP = {
    'DRV': 'D:/QNX/qnx_x50/target/qnx7/x86_64/usr/bin', \
    'PRK': 'D:/QNX/qnx_x50/target/qnx7/aarch64le/usr/bin', \
    'VP': 'D:/QNX/qnx_x50/target/qnx7/aarch64le/usr/bin' \
}

QE_CFG_TSV_PDEBUG_CMD = {\
    'DRV':'./usr/sbin',\
    'PRK':'.fs/rem',\
    'VP':'.fs/rem',\
}
QE_CFG_TSV_PDEBUG_CMD = {\
    'DRV':'pdebug 1234',\
    'PRK':'./fs/rem/pdebug 1234',\
    'VP':'.fs/rem/pdebug 1234',\
}
QE_CFG_TSV_PDEBUG_TRANSFER_CMD = '''open {hostip}
user qnxuser
qnxuser
bi
cd {motionwise_path}
{deleted_old_file}
{lcd_pdedug_path}
{transfer_cmd}
quit
'''

QE_CFG_TSV_GDB_REMOTE = 'target(SPACE)qnx(SPACE)%s:1234'
QE_CFG_TSV_GDB_READ = 'file(SPACE)%s'
QE_CFG_TSV_GDB_ATTACH = 'attach(SPACE)%s'

QE_CFG_TSV_GDB_REMOTE_RESULT_EXPECTED = 'Remote debugging using %s:1234'
QE_CFG_TSV_GDB_READ_RESULT_EXPECTED = 'Reading symbols from %s'
QE_CFG_TSV_GDB_ATTACH_RESULT_EXPECTED = 'Attaching to pid %s'

QE_CFG_TSV_PDEBUG_SETUP = '''open {hostip}
user qnxuser
qnxuser
bi
cd {pdebug_path}
{lcd_pdedug_path}
{transfer_cmd}
quit
'''

QE_CFG_TSV_DEFAULT_FLASHING_PATH = QE_CFG_PROJECT_PATH + '/0900_System/03_flashing'
QE_CFG_TASK_SUPERVISION = {?}
#--------------------------------------------------------------------------------
# TIME_SERVICE CONFIGURATION 
#--------------------------------------------------------------------------------
QE_CFG_TIME_SERVICE_TEST_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/Time_Service/'
QE_CFG_TIME_SERVICE_UART_LOG_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/Time_Service/%s/__raw_data__'
QE_CFG_TIME_SERVICE_PTP_CSV_PATH = QE_CFG_PROJECT_PATH + '/1000_Test/Time_Service/%s/__raw_data__'

QE_CFG_TS_SYS_CONFIGOUT_RTE_PATH = QE_CFG_PROJECT_PATH + '/0900_System/02_configout/rte/'
QE_CFG_TS_RTE_SWC_PATH_TEMPLATE = QE_CFG_TS_SYS_CONFIGOUT_RTE_PATH + '/{HOST_NAME}/Implementation_Templates/{SWC_NAME}.c'
QE_CFG_TS_STBM_AUTOSAR_HEADER = QE_CFG_TS_SYS_CONFIGOUT_RTE_PATH + '/SH00/MIC/Common/BSW/StbM/StbM_Autosar.h'
QE_CFG_TS_STBM_CONFIG_HEADER = QE_CFG_TS_SYS_CONFIGOUT_RTE_PATH + '/SH00/MIC/Common/BSW/StbM/StbM_Config.h'
QE_CFG_TS_STBM_CONFIG_TYPES_HEADER = QE_CFG_TS_SYS_CONFIGOUT_RTE_PATH + '/SH00/MIC/Common/BSW/StbM/StbM_Config_Types.h'
QE_CFG_TS_PPPPSERVER_TS_GETEGTTMESTAMP_TEMPLATE = 'Rte_CALL_{SWC_NAME}_PPPServer_TS_GetEgtTimestamp'
QE_CFG_TS_UART_LOG_TEMPLATE = '[TimeService]CtAp'
QE_CFG_TS_GET_EGT_TIMESTAMP = '[TimeService]{SWC_NAME}_TS_GetEgtTimestamp'
QE_CFG_TS_GET_REMAINING_TIME_BUDGET = '[TimeService]{SWC_NAME}_TS_GetRemainingTimeBudget'
QE_CFG_TS_SH00_UART_TRIGGER_VAR_TEMPLATE = 'TS_{SWC_NAME}_Trigger'
QE_CFG_TS_TIMESTAMP_RESOLUTION = {'Difference': 500000, 'Tolerance': 0.15}

QE_CFG_TS_PTP_SYNC_MSG_ID = '0x0'
QE_CFG_TS_PTP_FOLLOW_UP_MSG_ID = '0x8'
QE_CFG_TS_PTP_PEER_DELAY_REQ_MSG_ID = '0x2'
QE_CFG_TS_PTP_PEER_DELAY_RESP_MSG_ID = '0x3'
QE_CFG_TS_PTP_PEER_DELAY_RESP_FOLLOW_UP_MSG_ID = '0xa'

QE_CFG_TIME_SERVICE = {?}
#--------------------------------------------------------------------------------
# TRACING CONFIGURATION 
#--------------------------------------------------------------------------------
QE_CFG_TRACING ={?}
#--------------------------------------------------------------------------------
# BOOTING CONFIGURATION 
#--------------------------------------------------------------------------------
QE_CFG_BOOTING_TEST_PATH            = QE_CFG_PROJECT_PATH + '1000_TEST/Booting/PRK'
QE_CFG_BOOTING_REPROGRAM_PATH       = QE_CFG_BOOTING_TEST_PATH + '/__reprogram__'
QE_CFG_BOOTING_RAWDATA_PATH         = QE_CFG_BOOTING_TEST_PATH + '/__rawdata__'
QE_CFG_BOOTING_FLASHING_PATH        = QE_CFG_PROJECT_PATH +'/0900_System/03_flashing'
QE_CFG_BOOTING_MP_BUILD_PATH        = QE_CFG_PROJECT_PATH + '/0500_Build/MP'
QE_CFG_BOOTING_IMAGE_DEFAULT_PATH   = QE_CFG_BOOTING_FLASHING_PATH +'/01_Debug/SH00/image'
QE_CFG_BOOTING_IMAGE_BUILDED_PATH   = QE_CFG_BOOTING_MP_BUILD_PATH +'/Release/SH00/bin/Debug'


QE_CFG_BOOTING_BMHD_DATABASE ={
    'BMHD_Data':['FE0059B3000000A0705579318FAA86CE','FF0059B3000000A0C07C190C3F83E6F3'],
    'UCB_BMHD_ORIG':['S325AF400000','S325AF400200','S325AF400400','S325AF400800'],
    'UCB_BMHD_COPY':['S325AF401000','S325AF401200','S325AF401400','S325AF401600'],
    'BMHD_MAPPING':['bmhd_%s_orig','bmhd_%s_copy']
}

QE_CFG_BOOTING_UART_CONTENT_VERIFY ={

    'SH00':[
        'HSVM: HOST PH00 is in handshake state',
        'HSVM: HOST PH00 is in running state'
    ],
    'PH00':[
        'LCS PH00 : Entering Running State!',
    ],
    'PH01':[
        'LCS PH01 : Entering Running State!',
    ]
}

QE_CFG_BOOTING ={?}
#--------------------------------------------------------------------------------