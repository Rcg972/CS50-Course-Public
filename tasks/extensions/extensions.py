def main():
    extensions(input("File Name : "))



def extensions(promt):
    promt = promt.strip().lower()

    if "." in promt:
        extension = promt.rsplit(".", 1)[1]
        if promt.endswith((".gif", ".jpg", ".jpeg", ".png")):
            if promt.endswith(".jpg"):
                print("image/jpeg")
            else:
                print(f"image/{extension}")
        elif promt.endswith((".pdf", ".zip")):
            print(f"application/{extension}")
        elif promt.endswith(".txt"):
            print("text/plain")
        else:
            print("application/octet-stream")
    else:
        print("application/octet-stream")



main()
