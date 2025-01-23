'''
#       Extended Essay ─ Mathematics
#       Luis Enrique Villegas Rodríguez ─ A01287303
#
#       Copyright (C) Tecnologico de Monterrey
#
#       File: main.py
#
#       Created on:                  16/01/2024
#       Last edited on:              16/01/2024
'''
import time
start_time = time.time()

# Variable control
index_list= 10_000 # O(n^2) time complexity, reduce the index list to have faster results
N = 1234
G = 3

# List 1
data_list = []
for i in range(1, index_list+1):
    data_list.append(G ** i)

def main():
    for i, data in enumerate(data_list):
        if data % N == 1:
            print(f"Found MOD {data % N} at r = {i+1}")
            break
        elif i == len(data_list)-1:
            print(f"No MOD found with {index_list} iterations")
            return

# Execution
if __name__ == '__main__':
    main()
    print(f"--- {time.time() - start_time} seconds ---")
