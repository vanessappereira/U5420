import os
import shutil  # SHell UTILities

print("File management commands")
cmd_args = input(">> ").split()
match cmd_args:
    case ["help"]:
        print("Available commands:")
        print("     delete file")
        print("     deletedir")
        print("     copy file")
        print("     move file")
        print("     rename file")

    case ["delete" | "rm", file_name]:
        resp = input(f"Do you want to delete {file_name}? (yes/no): ")
        if resp.lower() == "yes":
            try:
                os.remove(file_name)
                print(f"File {file_name} deleted")
            except FileNotFoundError:
                print(f"File {file_name} not found")

    case ["deletedir" | "rmdir", dir_]:
        resp = input(f"Do you want to delete {dir_}? (yes/no): ")
        if resp.lower() == "yes":
            try:
                shutil.rmtree(dir_)
                print(f"Directory {dir_} deleted")
            except FileNotFoundError:
                print(f"Directory {dir_} not found")

    case ["copy" | "cp", file_name, dest_dir]:
        try:
            shutil.copy(file_name, dest_dir)
            print(f"File {file_name} copied to {dest_dir}")
        except FileNotFoundError:
            if not os.path.exists(dest_dir):
                print(f"Destination directory {dest_dir} not found")
            else:
                print(f"File {file_name} not found")

    case ["move" | "mv", file_name, dest_dir]:
        resp = input(f"Do you want to move {file_name} to {dest_dir}?")
        if resp.lower() == "yes":
            try:
                shutil.move(file_name, dest_dir)
                print(f"File {file_name} moved to {dest_dir}")
            except FileNotFoundError:
                if not os.path.exists(dest_dir):
                    print(f"Destination directory {dest_dir} not found")
                else:
                    print(f"File {file_name} not found")

    case ["rename" | "ren", file_name, new_name]:
        resp = input(f"Do you want to rename {file_name} to {new_name}?")
        if resp.lower() == "yes":
            try:
                os.rename(file_name, new_name)
                print(f"File {file_name} renamed to {new_name}")
            except FileNotFoundError:
                print(f"File {file_name} not found")

    case _:
        print(f"Invalid command\n\t{cmd_args}")
