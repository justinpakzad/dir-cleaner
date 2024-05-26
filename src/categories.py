file_cats = {
    "audio": ["mp3", "wav", "raw", "wma", "mid", "midi"],
    "video": ["mp4", "mpg", "mpeg", "avi", "mov", "flv", "mkv", "mwv", "m4v", "h264"],
    "images": [
        "png",
        "jpg",
        "jpeg",
        "gif",
        "svg",
        "bmp",
        "psd",
        "svg",
        "tiff",
        "tif",
        "heic",
    ],
    "compressed": ["zip", "z", "7z", "rar", "tar", "gz", "rpm", "pkg", "deb"],
    "installation": ["dmg", "exe", "iso"],
    "csvs":["csv"],
    "docs": [
        "txt",
        "ods",
        "doc",
        "docx",
        "html",
        "odt",
        "tex",
        "ppt",
        "pptx",
        "log",
    ],
    "pdfs": ["pdf"],
    "excel_files":["xls","xlsx"],
    "sql":['sql','sqlite'],
    "markdown":["md"],
    "python": ["py", "ipynb"],
    "ableton": ["als"],
}


def confirmation_prompt_clean():
    inp = input("Please confirm to cleanse this folder y/n")
    if str(inp) == "n":
        return False
    return True


def confirmation_prompt_backup():
    inp = input("Would you like to create a backup of this directory?")
    if str(inp) == "n":
        return False
    elif str(inp) == "y":
        return
