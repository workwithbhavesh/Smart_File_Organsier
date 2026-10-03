from pathlib import Path

folder_path = input("Enter the path: ")
folder = Path(folder_path)

for file in folder.iterdir():
  print(file.name)
  print(file.suffix)