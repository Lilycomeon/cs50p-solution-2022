import os

file = input("File name: ")
file = file.lower().strip()

file_name, file_extension = os.path.splitext(file)

match file_extension:
    case ".jpg" | ".jpeg":
        print ("image/jpeg")
    case ".pdf":
        print ("application/pdf")
    case ".gif":
        print ("image/gif")
    case ".png":
        print ("image/png")
    case ".txt":
        print ("text/plain")
    case ".zip":
        print ("application/zip")
    case _:
        print("application/octet-stream")
