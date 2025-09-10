import socket
import requests
import pyfiglet
import sys
import os

def get_local_ip():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception as e:
        return f"Error: {e}"

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json().get("ip")
    except Exception as e:
        return f"Error: {e}"

def get_domain_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        return f"Error: {e}"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    ascii_banner = pyfiglet.figlet_format("Yeka Look IP")
    print(ascii_banner)
    print("===============================")
    print(" Tools sederhana untuk cek IP ")
    print("===============================\n")

def menu():
    while True:
        clear_screen()
        banner()
        print("1. Cek IP Lokal")
        print("2. Cek IP Publik")
        print("3. Cek IP Domain/Web")
        print("4. Keluar\n")

        choice = input("Pilih menu (1-4): ")

        if choice == "1":
            print(f"\n👉 IP Lokal: {get_local_ip()}\n")
        elif choice == "2":
            print(f"\n👉 IP Publik: {get_public_ip()}\n")
        elif choice == "3":
            domain = input("Masukkan domain (contoh: google.com): ")
            print(f"👉 IP {domain}: {get_domain_ip(domain)}\n")
        elif choice == "4":
            print("\nTerima kasih telah menggunakan Yeka Look IP 👋\n")
            sys.exit()
        else:
            print("\n⚠️ Pilihan tidak valid!\n")

        input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    menu()
