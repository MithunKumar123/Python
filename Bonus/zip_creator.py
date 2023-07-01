import zipfile, pathlib


def make_archive(filepath, dest_dir):
    dest_path = pathlib.Path(dest_dir, "Compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for file in filepath:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)
