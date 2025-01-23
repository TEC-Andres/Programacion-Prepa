'''
#       Extended Essay ─ Mathematics
#       Luis Enrique Villegas Rodríguez ─ A01287303
#
#       Copyright (C) Tecnologico de Monterrey
#
#       Archivo: main.py
#
#       Created on:                  16/01/2024
#       Last edited on:              16/01/2024
'''
import time
start_time = time.time()

# Variable control
index_list = 100_000_000  # O(n) time complexity
N = 438743373
G = 3

# G ** R % N
def main():
    data = 1
    for i in range(1, index_list + 1):
        data = (data * G) % N
        if data == 1:
            print(f"Found MOD {data} at r = {i}")
            break
        elif i == index_list:
            print(f"No MOD found with {index_list} iterations")
            return

# Execution
if __name__ == '__main__':
    main()
    print(f"--- {time.time() - start_time} seconds ---")