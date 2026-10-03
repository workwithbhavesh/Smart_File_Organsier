from pathlib import Path

folder_path = input("Enter the path: ")

folder = Path(folder_path)

for file in folder.iterdir():

  print(file.name)

  suff = file.suffix.lower()
    # Images
  if (suff == ".png" or suff == ".jpg" or suff == ".jpeg" or
        suff == ".gif" or suff == ".webp" or suff == ".bmp" or
        suff == ".svg" or suff == ".tiff"):
        print("It is an image")
        image_folder = folder/"Images"
        image_folder.mkdir(exist_ok=True)
        
        file.rename(image_folder/file.name)
        print("folder created")
  
        

    # Documents
  elif (suff == ".pdf" or suff == ".docx" or suff == ".doc" or
          suff == ".txt" or suff == ".rtf" or suff == ".odt"):
        print("This is a document")
        document_folder = folder/"Documents"
        document_folder.mkdir(exist_ok=True)
        file.rename(document_folder/file.name)

    # Spreadsheets
  elif (suff == ".xlsx" or suff == ".xls" or suff == ".csv" or
          suff == ".ods"):
        print("This is a spreadsheet")
        sheets_folder = folder/"Sheets"
        sheets_folder.mkdir(exist_ok=True)
        file.rename(sheets_folder/file.name)
        

    # Presentations
  elif (suff == ".pptx" or suff == ".ppt" or suff == ".odp"):
        print("This is a presentation")
        Presentation_folder = folder/"Presentation"
        Presentation_folder.mkdir(exist_ok=True)
        file.rename(Presentation_folder/file.name)

    # Music
  elif (suff == ".mp3" or suff == ".wav" or suff == ".flac" or
          suff == ".aac" or suff == ".m4a" or suff == ".ogg"):
        print("This is music")
        music_folder = folder/"music"
        music_folder.mkdir(exist_ok=True)
        file.rename(music_folder/file.name)

    # Videos
  elif (suff == ".mp4" or suff == ".mkv" or suff == ".avi" or
          suff == ".mov" or suff == ".wmv" or suff == ".webm"):
        print("This is a video")
        video_folder = folder/"video"
        video_folder.mkdir(exist_ok=True)
        file.rename(video_folder/file.name)

    # Subtitles
  elif (suff == ".srt" or suff == ".ass" or suff == ".vtt"):
        print("This is a subtitle")
        subtitle_folder = folder/"subtitle"
        subtitle_folder.mkdir(exist_ok=True)
        file.rename(subtitle_folder/file.name)

    # Programs
  elif (suff == ".exe" or suff == ".msi"):
        print("This is an installer/program")
        setup_folder = folder/"setup"
        setup_folder.mkdir(exist_ok=True)
        file.rename(setup_folder/file.name)

    # Code
  elif (suff == ".py" or suff == ".java" or suff == ".c" or
          suff == ".cpp" or suff == ".js" or suff == ".html" or
          suff == ".css" or suff ==".ipynb"):
        print("This is code")
        code_folder = folder/"code"
        code_folder.mkdir(exist_ok=True)
        file.rename(code_folder/file.name)

    # Archives
  elif (suff == ".zip" or suff == ".rar" or suff == ".7z" or
          suff == ".tar" or suff == ".gz"):
        print("This is an archive")
        zip_folder = folder/"archives"
        zip_folder.mkdir(exist_ok=True)
        file.rename(zip_folder/file.name)
  

  else:
        print("Unknown file type")
    
  
