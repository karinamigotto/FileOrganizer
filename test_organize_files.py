import os
import pytest
from file_organizer import organize_files, load_config

def test_organize_files(tmpdir):
    source_folder = tmpdir.mkdir("source")
    destination_folder = tmpdir.mkdir("destination")

    source_folder.join("test1.txt").write("test")
    source_folder.join("test2.jpg").write("test")
    source_folder.join("test3.pdf").write("test")

    organize_files(str(source_folder), str(destination_folder))

    assert os.path.exists(os.path.join(destination_folder, "Text_Files", "test1.txt"))
    assert os.path.exists(os.path.join(destination_folder, "Images", "test2.jpg"))
    assert os.path.exists(os.path.join(destination_folder, "Documents", "test3.pdf"))

def test_load_config():
    config = load_config()
    assert "source_folder" in config
    assert "destination_folder" in config
    assert "email" in config
