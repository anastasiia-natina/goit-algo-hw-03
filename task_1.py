import sys
import os
import shutil

def sort_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root,dest_dir, files in os.walk(source_dir):
        for file in files:
            full_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]
            ext_dir = os.path.join(dest_dir, ext[1:])

            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)

            shutil.copy(full_path, ext_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Необхідно вказати шлях до вихідної директорії.")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    try:
        sort_files(source_dir, dest_dir)
    except Exception as e:
        print(f"Помилка під час сортування файлів: {e}")