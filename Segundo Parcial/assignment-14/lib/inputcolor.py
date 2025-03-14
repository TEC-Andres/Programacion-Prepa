'''
#       Sesión 14: Proyecto Parcial 2
#       Andrés Rodríguez Cantú ─ A01287002
#       Roberto André Guevara Martínez ─ A01287324
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: lib/inputcolor.py
#
#       Creado:                   13/03/2024
#       Última Modificación:      13/03/2024
'''
import sys
import msvcrt
from color import FG, Style

class InputColor:
    def __init__(self, prompt="Escribe algo: "):
        self.prompt = prompt
        self.user_input = ""

    def start_input(self):
        sys.stdout.write(self.prompt)
        sys.stdout.flush()

        while True:
            key = msvcrt.getch()

            # Allow Ctrl+C (ETX, b'\x03') to raise KeyboardInterrupt
            if key == b'\x03':
                raise KeyboardInterrupt

            if key == b"\r":  # Enter key (carriage return)
                break
            elif key == b"\x08":  # Backspace
                if self.user_input:
                    self.user_input = self.user_input[:-1]
                    self._update_display()
            elif key.isascii() and key.decode("utf-8").isprintable():
                char = key.decode("utf-8")
                self.user_input += char
                self._update_display()

        print()  # Move to next line after input
        return self.user_input

    def _update_display(self):
        # Choose colored input if exactly 'test', else use uncolored input
        if self.user_input == "exit":
            colored_input = f"{FG.H00AAAA}{self.user_input}{Style.RESET_ALL}"
        else:
            colored_input = self.user_input

        colored_line = self.prompt + colored_input
        # \033[K clears from the cursor to the end of line,
        # ensuring no extra characters remain from previous longer output.
        sys.stdout.write("\r" + colored_line + "\033[K")
        sys.stdout.flush()

'''if __name__ == "__main__":
    try:
        inputColor = InputColor()
        while True:
            final_text = inputColor.start_input()
            print(f"You entered: {final_text}") 
            if final_text == "exit":
                break
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting.")
'''