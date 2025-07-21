import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.docx','.doc', '.rtf', '.csv'],
    "AUDIOS": ['.mp3','.m4a','.m4b'],
    "VIDEOS": ['.mp4','.mov','.avi'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"

print(pickDirectory('.mp3'))

def organiseDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organiseDirectory()
