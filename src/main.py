import os
import platform
import shutil
import sys

from tkinter import filedialog


def __get_apps_folder():
    match platform.system():
        case 'Windows':
            return "C:\\Program Files"
        case 'Darwin':  # MacOs
            return "/Applications"
        case 'Linux':  # These folders may be different based on versions and releases. Probably best to open a file explorer to as generic path
            return "/bin"  # Alternatively /sbin
        case _:
            return None  # Platform not supported


def __get_startup_folder():
    match platform.system():
        case 'Windows':  # Only supporting 10
            return "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        case 'Darwin':  # MacOs
            return "~/Library/Preferences folder"  # (Untested)
        case 'Linux':  # These folders may be different based on versions and releases. Probably best to open a file explorer to as generic path
            return "/bin"  # (Untested). Alternatively, directory might be /sbin
        case _:
            return None  # Platform not supported (i.e Java)


def __copy(source: str):
    destination = __get_startup_folder()

    if destination is not None:
        shutil.copy(source, destination)
    else:
        print("Encountered an error when trying to retrieve the startup folder location")


def __delete(filepath: str):
    pass


if __name__ == '__main__':
    if len(sys.argv) == 0 or sys.argv[0].lower() == 'add':  # Assume add if no args provided
        source_location = filedialog.askopenfilename(initialdir=__get_apps_folder(), title="Select a File", filetypes=(("Application", "*.exe*"), ("All Files", "*.*")))
        if source_location is not None:
            __copy(source_location)
        else:
            print("This platform is not supported!")
    elif sys.argv[0].lower() == 'remove':
        pass  # TODO


