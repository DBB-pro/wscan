# encoding: utf-8
'''
@Version:   V1.0
@Author:    JE2Se
@Contact:   admin@je2se.com
@Website:   https://www.je2se.com
@Github:    https://github.com/JE2Se/
@Time:  2020/6/10 10:57
@File:  Color.py
@Desc:  颜色模板
'''

import platform

#linux
if "Darwin" or "Linux"  in platform.system():
    class Vcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        RED = '\033[31m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        YELLOW= '\033[1;33m'
        DARKGRAY= "\033[1;30m"
        CYAN= "\033[0;36m"
        PURPLE= "\033[0;35m"
        BROWN= "\033[0;33m"
        WHITE= "\033[1;37m"
#其他情况
else:
    class Vcolors:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        RED = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''
        YELLOW= ''
        DARKGRAY= ""
        CYAN= ""
        PURPLE= ""
        BROWN= ""
        WHITE= ""