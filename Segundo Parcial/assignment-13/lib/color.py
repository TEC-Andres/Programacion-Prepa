'''
#       Sesión 12: Assignment 12
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: lib/color.py
#
#       Creado:                   28/02/2024
#       Última Modificación:      09/03/2024
'''

class CustomColor:
    def __init__(self, hex_color):
        self.rgb = self.hex_to_rgb(hex_color)
        self.color_code = f'\033[38;2;{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}m'

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

class FG:
    H00AA00 = CustomColor("#00AA00").color_code # Green
    H00AAAA = CustomColor("#00AAAA").color_code # Lapis Lazuli Blue
    H443A3B = CustomColor("#443A3B").color_code # Dark Gray
    H555555 = CustomColor("#555555").color_code # Gray
    H55FF55 = CustomColor("#55FF55").color_code # Light Green
    H5555FF = CustomColor("#5555FF").color_code # Light Blue
    HAAAAAA = CustomColor("#AAAAAA").color_code # Light Gray
    HFFFFFF = CustomColor("#FFFFFF").color_code # White
    HFF0000 = CustomColor("#FF0000").color_code # Red
    HFF5555 = CustomColor("#FF5555").color_code # Light Red
    HFFA500 = CustomColor("#FFA500").color_code # Orange
    HFFFF00 = CustomColor("#FFFF00").color_code # Yellow
    RESET = '\033[39m'
    
class Style:
    RESET_ALL = '\033[0m'
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'

class checkInfo:
    def __init__(self, message, color):
        self.message = message
        self.color = color

    def __str__(self):
        return f"{self.color}{self.message}{FG.RESET + Style.RESET_ALL}"

''' 
print(f"{Style.BRIGHT + FG.H00AA00}[{FG.RESET + FG.H55FF55}SUCCESS{FG.RESET + Style.BRIGHT + FG.H00AA00}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} All 20 tests passed!{FG.RESET + Style.RESET_ALL}")
print(f"{Style.BRIGHT + FG.HFF0000}[{FG.RESET + FG.HFF5555}ERROR{FG.RESET + Style.BRIGHT + FG.HFF0000}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} An error occurred: Division by zero.{FG.RESET + Style.RESET_ALL}")
print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Queued all 20 commits.{FG.RESET + Style.RESET_ALL}")
print(f"{Style.BRIGHT + FG.HFFA500}[{FG.RESET + FG.HFFFF00}WARNING{FG.RESET + Style.BRIGHT + FG.HFFA500}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} You are about to delete all files.{FG.RESET + Style.RESET_ALL}")
print(f"{Style.BRIGHT + FG.H555555}[{FG.RESET + FG.HAAAAAA}DEBUG{FG.RESET + Style.BRIGHT + FG.H555555}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} You've enter debugger mode.{FG.RESET + Style.RESET_ALL}")
'''