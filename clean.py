import os
import shutil


if __name__ == "__main__":
    try:
        shutil.rmtree("output")
    except FileNotFoundError:
        print("Folder not found!")
    except PermissionError:
        print(f"Permission error while deleting")

    try:
        os.remove("masterbagels_console.spec")
    except FileNotFoundError:
        pass

    print("Done!")