import os
import shutil
import subprocess

DIST_PATH = r"C:\Users\PC\Desktop\demo\dist\main\_internal"
BACKUP_PATH = DIST_PATH + "_backup"

def run_app():
    try:
        result = subprocess.run(
            [r"C:\Users\PC\Desktop\demo\dist\main\main.exe"],
            timeout=20,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        return result.returncode == 0
    except Exception as e:
        return False

def safe_remove_folder(folder_path):
    try:
        print(f"Testing without: {folder_path}")
        shutil.move(folder_path, folder_path + "_bak")
        if run_app():
            print(f"✅ Safe to remove: {os.path.basename(folder_path)}")
        else:
            print(f"❌ Needed: {os.path.basename(folder_path)}")
            shutil.move(folder_path + "_bak", folder_path)
    except Exception as e:
        print(f"⚠️ Error testing {folder_path}: {e}")
        if os.path.exists(folder_path + "_bak"):
            shutil.move(folder_path + "_bak", folder_path)

def main():
    if not os.path.exists(BACKUP_PATH):
        shutil.copytree(DIST_PATH, BACKUP_PATH)

    for name in os.listdir(DIST_PATH):
        folder = os.path.join(DIST_PATH, name)
        if os.path.isdir(folder):
            safe_remove_folder(folder)

    print("✅ Done. You can now manually delete unused *_bak folders if you want.")

if __name__ == "__main__":
    main()
