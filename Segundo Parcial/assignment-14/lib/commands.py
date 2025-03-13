import os 
import sys
from lib.color import FG, Style, checkInfo

class Dict(dict):
    def __init__(self, *args, **kwargs):
        super(Dict, self).__init__(*args, **kwargs)
        self.help_messages = {
            'help': 'Muestra la lista de comandos disponibles.',
            'cls': 'Limpia la consola.',
            'exit': 'Cierra el programa.'
        }

class Cmd:
    def __init__(self):
        pass

    def init(self):
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Iniciando el programa.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Visualizando el siguiente archivo {FG.H00AA00 + os.path.basename(self.file_path) + FG.RESET}.{FG.RESET + Style.RESET_ALL}")
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Para ver la lista de comandos, escriba help en la consola.{FG.RESET + Style.RESET_ALL}")

    def help(self):
        print(f"{Style.BRIGHT + FG.H555555}[{FG.RESET + FG.HAAAAAA}CONSOLA{FG.RESET + Style.BRIGHT + FG.H555555}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Estos son los comandos que hay en la aplicación:{FG.RESET + Style.RESET_ALL}")
        for command, description in Dict().help_messages.items():
            print(f"{checkInfo(command, FG.H00AA00)}: {description}")
    
    def exit(self):
        print(f"{Style.BRIGHT + FG.H5555FF}[{FG.RESET + FG.H00AAAA}INFO{FG.RESET + Style.BRIGHT + FG.H5555FF}] {FG.RESET + FG.H443A3B}―{FG.RESET + Style.RESET_ALL} Programa cerrado con éxito.{FG.RESET + Style.RESET_ALL}")
        sys.exit()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')