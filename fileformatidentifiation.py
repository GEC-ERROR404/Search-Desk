import fleep
def FileTypeIdentification(path):
    with open(path, "rb") as file:
        info = fleep.get(file.read(128))
    print(info.mime[0])

    import fleep

    with open("D:\\images\\aurebesh.jpg", "rb") as file:
        info = fleep.get(file.read(128))
    print(info.mime[0])

    FileTypeIdentification("D:\\images\\aurebesh.jpg")