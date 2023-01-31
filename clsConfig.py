
import os
import platform as pl

class clsConfig(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'REPORT_PATH': Curr_Path + sep + 'report',
        'SRC_PATH': Curr_Path + sep + 'data' + sep,
        'FINAL_PATH': Curr_Path + sep + 'Target' + sep,
        'APP_DESC_1': 'Hand Gesture Zoom Control!',
        'DEBUG_IND': 'N',
        'INIT_PATH': Curr_Path,
        'SUBDIR': 'data',
        'SEP': sep,
        'TITLE': "Human Hand Gesture Controlling App",
        'minVal':0.01,
        'maxVal':1
    }
