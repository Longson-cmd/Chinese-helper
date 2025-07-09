import os
import shutil

INTERNAL_PATH = r"C:\Users\PC\Desktop\demo\dist\main\_internal"

def delete_bak_folders():
    deleted = []

    for name in os.listdir(INTERNAL_PATH):
        folder = os.path.join(INTERNAL_PATH, name)

        if os.path.isdir(folder) and folder.endswith("_bak"):
            try:
                print(f"🗑️ Deleting: {folder}")
                shutil.rmtree(folder)

                deleted.append(name)

            except Exception as e:
                print(f"❌ Error deleting {name}: {e}")

    if deleted:
        print("\n✅ Deleted folders:")
        for name in deleted:
            print(f" - {name}")

        else:
            print("⚠️ No _bak folders found to delete.")

if __name__ == "__main__":
    delete_bak_folders()
    