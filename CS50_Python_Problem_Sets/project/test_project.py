from Sphynixtest import create_file,delete_file,create_folder,delete_folder


def test_create_file():
    assert create_file("create file named file.txt") == 0

def test_delete_file():
    assert delete_file("delete file named file.txt") == 0

def test_create_folder():
    assert create_folder("create folder named new folder") == 0


def test_delete_folder():
    assert delete_folder("delete folder named new folder") == 0

