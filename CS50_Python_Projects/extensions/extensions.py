def main():
    extension_input = input("File name: ")
    extension_input = extension_input.lower().strip()
    extensions(extension_input)

def extensions(ext_answer):
    if ext_answer.endswith(".gif"):
        print("image/gif")

    elif ext_answer.endswith(".jpeg") or ext_answer.endswith(".jpg"):
        print("image/jpeg")

    elif ext_answer.endswith(".png"):
        print("image/png")

    elif ext_answer.endswith(".pdf"):
        print("application/pdf")

    elif ext_answer.endswith(".txt"):
        print("text/plain")

    elif ext_answer.endswith(".zip"):
        print("application/zip")

    else: print("application/octet-stream")

main()
