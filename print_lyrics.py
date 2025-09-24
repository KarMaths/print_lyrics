import sys 
import time

def printLyrics(file_path):
    print()
    print("------------------------------------")
    print(" Skeng - Gvnman Shif")
    
    # line_delays = []

    with open(file_path, "r") as file:
        lines = file.readlines()

        char_delay = 0.05  # Adjust this value to control the speed of the lyrics

        for i, line in enumerate(lines):
            line = line.strip()
            if not lines:
                continue
            for char in line:
                print(char, end="")
                sys.stdout.flush()
                time.sleep(char_delay)
            print()
            time.sleep(0.05)  # Add a delay between lines

printLyrics("gvnman_shift.txt")