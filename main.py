from pathlib import Path
from categories import file_cats
import shutil
from datetime import datetime
import calendar
from collections import defaultdict
import argparse


def backup_dir(source_dir: str, backup_dir: str, create_backup_dir: bool = False):
    home_path = Path.home()
    source_path = home_path.joinpath(source_dir)
    backup_path = home_path.joinpath(backup_dir)
    try:
        if create_backup_dir:
            if source_path.is_dir() and not backup_path.exists():
                shutil.copytree(source_path, backup_path)
            else:
                print(
                    "Source path is not a directory or a backup directory already exists"
                )
        else:
            if source_path.is_dir() and backup_path.is_dir():
                for item in source_path.iterdir():
                    d = backup_path / item.name
                    if item.resolve() == backup_path.resolve():
                        continue
                    elif item.is_dir():
                        shutil.copytree(item, d, dirs_exist_ok=True)
                    else:
                        shutil.copy(item, d)
        print(f"Backup of {source_path} created successfully at {backup_path}")
    except Exception as e:
        print(f"Error backing up directory: {e}")


def check_empty(source_path: str):
    return all(item.name == ".DS_Store" for item in source_path.iterdir()) or not any(
        source_path.iterdir()
    )


def delete_empty_dirs(source_path: str):
    directories = [d for d in source_path.rglob("*") if d.is_dir()]
    directories.sort(key=lambda x: len(x.parts), reverse=True)
    for item in directories:
        if check_empty(item):
            shutil.rmtree(item)


def get_source_path(home_path: str, source_dir: str):
    return home_path.joinpath(source_dir)


def clean_dir_by_suffix(source_dir: str, shallow: bool = False):
    source_path = get_source_path(Path.home(), source_dir)
    files_by_suffix_dict = defaultdict(list)
    if shallow:
        files = source_path.glob("*")
    else:
        files = source_path.rglob("*")
    for item in files:
        if item.is_file():
            file_suffix = item.suffix[1:].lower()
            for folder, suffixes in file_cats.items():
                if file_suffix in suffixes:
                    files_by_suffix_dict[folder].append(item)
    return files_by_suffix_dict


def clean_dir_by_date(source_dir: str, year_only: bool = False, shallow: bool = False):
    source_path = get_source_path(Path.home(), source_dir)
    files_by_date_dict = defaultdict(list)
    if shallow:
        files = source_path.glob("*")
    else:
        files = source_path.rglob("*")
    for item in files:
        if item.is_file():
            creation_date = datetime.fromtimestamp(item.stat().st_birthtime)
            if year_only:
                year = creation_date.year
                files_by_date_dict[str(year)].append(item)
            else:
                year_month = (
                    f"{calendar.month_name[creation_date.month]}_{creation_date.year}"
                )
                files_by_date_dict[year_month].append(item)

    return files_by_date_dict


def clean_dir_by_size(source_dir: str, shallow: bool = False):
    source_path = get_source_path(Path.home(), source_dir)
    files_by_size_dict = defaultdict(list)
    if shallow:
        files = source_path.glob("*")
    else:
        files = source_path.rglob("*")
    for item in files:
        if item.is_file():
            mb = round((item.stat().st_size) / 1000000, 2)
            if mb < 1:
                files_by_size_dict["small_files"].append(item)
            elif mb >= 1 and mb < 100:
                files_by_size_dict["medium_files"].append(item)
            else:
                files_by_size_dict["large_files"].append(item)
    return files_by_size_dict


def move_files_to_dir(source_dir: str, files_dict: dict[list]):
    source_path = get_source_path(Path.home(), source_dir)
    for date, items in files_dict.items():
        for item in items:
            if item.is_file():
                destination_folder = source_path / date
                destination_folder.mkdir(exist_ok=True)
                shutil.move(item, destination_folder / item.name)
    delete_empty_dirs(source_path)


def delete_files_n_days_old(source_dir, n_days=10):
    source_path = get_source_path(Path.home(), source_dir)
    files = source_path.rglob("*")
    for item in files:
        if item.is_file():
            creation_date = datetime.fromtimestamp(item.stat().st_birthtime)
            time_diff = datetime.now() - creation_date
            if time_diff.days >= n_days:
                item.unlink()
    delete_empty_dirs(source_path)


def main():
    parser = argparse.ArgumentParser(description="Folder cleanser")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    suffix_parser = subparsers.add_parser("clean_by_suffix")
    suffix_parser.add_argument("source_dir", help="The directory to clean")
    suffix_parser.add_argument(
        "--shallow",
        help="Perform a shallow clean (do not traverse subdirectories)",
        action="store_true",
    )
    suffix_parser.add_argument(
        "--backup", action="store_true", help="Create a backup before making changes"
    )
    suffix_parser.add_argument(
        "--backup_dir",
        help="The directory where the backup will be stored (in the home directory of said user)",
    )

    date_parser = subparsers.add_parser("clean_by_date")
    date_parser.add_argument("source_dir", help="The directory to clean")
    date_parser.add_argument(
        "--year_only",
        help="Clean directory by year only rather than the default month and year",
        action="store_true",
    )
    date_parser.add_argument(
        "--shallow",
        help="Perform a shallow clean (do not traverse subdirectories)",
        action="store_true",
    )
    date_parser.add_argument(
        "--backup", action="store_true", help="Create a backup before making changes"
    )
    date_parser.add_argument(
        "--backup_dir",
        help="The directory where the backup will be stored (in the home directory of said user)",
    )

    size_parser = subparsers.add_parser("clean_by_size")
    size_parser.add_argument("source_dir", help="The directory to clean")
    size_parser.add_argument(
        "--shallow",
        help="Perform a shallow clean (do not traverse subdirectories)",
        action="store_true",
    )
    date_parser.add_argument(
        "--backup", action="store_true", help="Create a backup before making changes"
    )
    date_parser.add_argument(
        "--backup_dir",
        help="The directory where the backup will be stored (in the home directory of said user)",
    )
    args = parser.parse_args()

    if args.backup and args.backup_dir:
        backup_dir(args.source_dir, args.backup_dir, args.create_backup_dir)

    if args.command == "clean_by_suffix":
        clean_dir_by_suffix(args.source_dir, args.shallow)
    elif args.command == "clean_by_date":
        clean_dir_by_date(args.source_dir, args.year_only, args.shallow)
    elif args.command == "clean_by_size":
        clean_dir_by_size(args.source_dir, args.shallow)
    else:
        parser.print_help()


if __name__ == "__main__":
    # backup_dir("Downloads", "backup_test", create_backup_dir=True)
    # d = clean_dir_by_suffix("Downloads", shallow=False)
    # files_dict = clean_dir_by_date("Desktop/books_test1")
    # move_files_to_dir("Downloads", d)
    # delete_files_n_days_old('Desktop/')
    # files_by_size_dict = clean_dir_by_size("Desktop/books_test")
    # move_files_to_dir("Desktop/books_test1", files_dict)
    # delete_files_n_days_old("Desktop/books_delete")
    main()
