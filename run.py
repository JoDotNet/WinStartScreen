import datetime
import ctypes


# Config_Variables
Monday_Path = r""
Tuesday_Path = r""
Wednesday_Path = r""
Thursday_Path = r""
Friday_Path = r""


# On Start
now = datetime.datetime.now()
today = now.strftime("%A")


# Changing Wallpaper
def Change_Wallpaper(day):
    if day == "Monday" and Monday_Path !="":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Monday_Path , 0)
    elif day == "Tuesday" and Tuesday_Path !="":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Tuesday_Path , 0)
    elif day == "Wednesday" and Wednesday_Path !="":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Wednesday_Path , 0)
    elif day == "Thursday" and Thursday_Path !="":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Thursday_Path , 0)
    elif day == "Friday" and Friday_Path !="":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Friday_Path , 0)
    else:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, Friday_Path , 0)


Change_Wallpaper(today)