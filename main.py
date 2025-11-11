import os
import sys
import platform
import base64
import hashlib
import random
import time
import threading
from datetime import datetime

class MeraukeTerminal:
    def __init__(self):
        self.running = True
        self.commands = {
            'help': 'Menampilkan bantuan',
            'sysinfo': 'Informasi sistem',
            'encode64': 'Encode base64',
            'decode64': 'Decode base64',
            'md5': 'Hash MD5',
            'sha256': 'Hash SHA-256',
            'genpass': 'Generate password',
            'rain': 'Efek hujan matrix',
            'clear': 'Bersihkan terminal',
            'exit': 'Keluar dari program'
        }
        
    def display_banner(self):
        banner = r"""
███╗   ███╗███████╗██████╗  █████╗ ██╗   ██╗██╗  ██╗███████╗
████╗ ████║██╔════╝██╔══██╗██╔══██╗██║   ██║██║ ██╔╝██╔════╝
██╔████╔██║█████╗  ██████╔╝███████║██║   ██║█████╔╝ █████╗  
██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██╔═██╗ ██╔══╝  
██║ ╚═╝ ██║███████╗██║  ██║██║  ██║╚██████╔╝██║  ██╗███████╗
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
        """
        print("\033[1;32m" + banner + "\033[0m")
        print("Cyber Education Terminal - Ketik 'help' untuk bantuan\n")
    
    def show_help(self):
        print("\nDaftar Perintah Tersedia:")
        print("-" * 40)
        for cmd, desc in self.commands.items():
            print(f"{cmd:15} - {desc}")
        print()
    
    def system_info(self):
        print("\nInformasi Sistem:")
        print("-" * 30)
        print(f"Sistem Operasi: {platform.system()} {platform.release()}")
        print(f"Versi OS: {platform.version()}")
        print(f"Arsitektur: {platform.architecture()[0]}")
        print(f"Processor: {platform.processor()}")
        print(f"Python: {platform.python_version()}")
        print()
    
    def base64_encode(self):
        text = input("Masukkan teks untuk encode: ")
        encoded = base64.b64encode(text.encode()).decode()
        print(f"Hasil encode: {encoded}\n")
    
    def base64_decode(self):
        text = input("Masukkan teks untuk decode: ")
        try:
            decoded = base64.b64decode(text.encode()).decode()
            print(f"Hasil decode: {decoded}\n")
        except:
            print("Error: Input bukan base64 valid!\n")
    
    def hash_md5(self):
        text = input("Masukkan teks untuk hash MD5: ")
        hashed = hashlib.md5(text.encode()).hexdigest()
        print(f"MD5 Hash: {hashed}\n")
    
    def hash_sha256(self):
        text = input("Masukkan teks untuk hash SHA-256: ")
        hashed = hashlib.sha256(text.encode()).hexdigest()
        print(f"SHA-256 Hash: {hashed}\n")
    
    def generate_password(self):
        length = int(input("Panjang password: "))
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Password: {password}\n")
    
    def matrix_rain(self):
        print("Tekan Ctrl+C untuk menghentikan hujan matrix...")
        try:
            columns = os.get_terminal_size().columns
            lines = os.get_terminal_size().lines
            chars = "01"
            
            def rain_line():
                return [random.choice(chars) for _ in range(columns)]
            
            matrix = [rain_line() for _ in range(lines)]
            
            while True:
                os.system('clear' if os.name == 'posix' else 'cls')
                for i in range(lines):
                    print(''.join(matrix[i]), end='')
                    matrix[i] = matrix[(i + 1) % lines]
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("\nHujan matrix dihentikan\n")
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        self.display_banner()
    
    def run(self):
        self.clear_screen()
        
        while self.running:
            try:
                command = input("merauke> ").strip().lower()
                
                if command == 'help':
                    self.show_help()
                elif command == 'sysinfo':
                    self.system_info()
                elif command == 'encode64':
                    self.base64_encode()
                elif command == 'decode64':
                    self.base64_decode()
                elif command == 'md5':
                    self.hash_md5()
                elif command == 'sha256':
                    self.hash_sha256()
                elif command == 'genpass':
                    self.generate_password()
                elif command == 'rain':
                    self.matrix_rain()
                elif command == 'clear':
                    self.clear_screen()
                elif command == 'exit':
                    print("Keluar dari Merauke Terminal...")
                    self.running = False
                elif command == '':
                    continue
                else:
                    print(f"Perintah tidak dikenali: {command}\n")
                    
            except KeyboardInterrupt:
                print("\nGunakan 'exit' untuk keluar dari program\n")
            except Exception as e:
                print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    terminal = MeraukeTerminal()
    terminal.run()
