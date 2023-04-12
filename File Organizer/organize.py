import os
import shutil

dir = "/home/sanju/"

file_types = {
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx",],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma",],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip",],
    "Disc": [".bin", ".dmg", ".iso", ".toast", ".vcd",],
    "Data": [".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml", ".json",],
    "Executables": [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".wsf",],
    "Fonts": [".fnt", ".fon", ".otf", ".ttf",]    
}

def organize():
    for file_type in file_types:
        os.makedirs(os.path.join(dir, file_type), exist_ok=True)

    # loop through each file in the directory
    for filename in os.listdir(dir):
        extension = os.path.splitext(filename)[1][1:].lower()

        for file_type, extensions in file_type.items():
            if extension in extensions:
                counter = 1
                new_filename = f"{file_type} - {counter}.{extension}"
                while os.path.exists(os.path.join(dir, new_filename)):
                    counter += 1
                    new_filename = f"{file_type} - {counter}.{extension}"

                shutil.move(os.path.join(dir, filename), os.path.join(dir, new_filename))
                break

if __name__ == "__main__":
    organize()


