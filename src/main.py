import argparse
import shutil
import calendar
from pathlib import Path
from categories import file_cats
from datetime import datetime
from collections import defaultdict


def check_empty(source_path: Path) -> bool:
    return all(item.name == ".DS_Store" for item in source_path.iterdir()) or not any(
        source_path.iterdir()
    )


def delete_empty_dirs(source_path: Path) -> None:
    directories = [d for d in source_path.rglob("*") if d.is_dir()]
    directories.sort(key=lambda x: len(x.parts), reverse=True)
    for item in directories:
        if check_empty(item):
            shutil.rmtree(item)


def get_source_path(home_path: str, source_dir: str) -> Path:
    return Path(home_path).joinpath(source_dir)


def verify_directory_exists(source_path: str) -> bool:
    if not source_path.is_dir():
        raise FileNotFoundError("The source directory {source_path} does not exist.")
    return True


def compute_file_size_mb(item):
    size_mb = (item.stat().st_size) / 1000000
    return size_mb


def size_validator(file_size: float) -> str:
    if file_size < 1:
        return "small_files"
    elif file_size >= 1 and file_size < 100:
        return "medium files"

    return "large files"


def copy_dir_contents(source_dir: str, backup_dir: str) -> None:
    home_path = Path.home()
    source_path = home_path.joinpath(source_dir)
    backup_path = home_path.joinpath(backup_dir)

    if not source_path.is_dir():
        raise FileNotFoundError("The source directory {source_path} does not exist.")

    if not backup_path.exists():
        backup_path.mkdir(exist_ok=True)
        print(f"Backup of {source_path} created successfully at {backup_path}")

    for item in source_path.iterdir():
        destination = backup_path / item.name
        if item.resolve() == backup_path.resolve():
            continue
        elif item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True)
        else:
            shutil.copy(item, destination)


def backup_dir(source_dir: str, backup_dir: str) -> None:
    home_path = Path.home()
    source_path = home_path.joinpath(source_dir)
    backup_path = home_path.joinpath(backup_dir)
    try:
        copy_dir_contents(source_path, backup_path)
    except Exception as e:
        print(f"Error backing up directory: {e}")


def get_files(source_path: str, shallow: bool = False) -> list:
    return source_path.glob("*") if shallow else source_path.rglob("*")


def organize_files(
    source_dir: str,
    method: str = "suffix",
    shallow: bool = False,
    year_only: bool = False,
) -> dict:
    source_path = get_source_path(Path.home(), source_dir)
    if not verify_directory_exists(source_path):
        return None

    files = get_files(source_path, shallow)
    organized_files = defaultdict(list)
    for item in files:
        if item.is_file():
            if method == "suffix":
                file_suffix = item.suffix[1:].lower()
                for folder, suffixes in file_cats.items():
                    if file_suffix in suffixes:
                        organized_files[folder].append(item)
            elif method == "date":
                creation_date = datetime.fromtimestamp(item.stat().st_birthtime)
                if year_only:
                    year = creation_date.year
                    organized_files[str(year)].append(item)
                else:
                    year_month = f"{calendar.month_name[creation_date.month]}_{creation_date.year}"
                    organized_files[year_month].append(item)
            elif method == "size":
                file_size_mb = compute_file_size_mb(item)
                organized_files[size_validator(file_size_mb)].append(item)

            else:
                print("Invalid method")
    return organized_files


def move_files_to_dir(source_dir: str, files_dict: dict[list]) -> None:
    source_path = get_source_path(Path.home(), source_dir)
    for date, items in files_dict.items():
        for item in items:
            if item.is_file():
                destination_folder = source_path / date
                destination_folder.mkdir(exist_ok=True)
                shutil.move(item, destination_folder / item.name)
    delete_empty_dirs(source_path)


def print_memory_saved(memory_list: list) -> None:
    if not memory_list:
        print("No files were deleted")
    else:
        total_memory = sum(memory_list)
        if total_memory >= 1000:
            print(
                f"{len(memory_list)} files have been deleted and {round(total_memory / 1000,2)} GB have been made available."
            )
        else:
            print(
                f"{len(memory_list)} files have been deleted and {round(total_memory,2)} MB have been made available."
            )


def time_validator(
    creation_date: datetime.date,
    n_days: int = None,
    n_months: int = None,
    n_years: int = None,
) -> bool:
    now = datetime.now()
    time_diff = now - creation_date
    if n_days:
        if time_diff.days >= n_days:
            return True
    if n_months:
        if (time_diff.days / 30) >= n_months:
            return True
    if n_years:
        if (time_diff.days / 365) >= n_years:
            return True

    return False


def delete_files_by_time(
    source_dir: str, n_days: int = None, n_months: int = None, n_years: int = None
) -> None:
    source_path = get_source_path(Path.home(), source_dir)

    if not verify_directory_exists(source_path):
        return None

    files = get_files(source_path)
    memory_saved = []
    for item in files:
        if item.is_file():
            creation_date = datetime.fromtimestamp(item.stat().st_birthtime)
            file_size_mb = compute_file_size_mb(item)
            if time_validator(creation_date, n_days, n_months, n_years):
                item.unlink()
                memory_saved.append(file_size_mb)
            else:
                continue

    print_memory_saved(memory_saved)
    delete_empty_dirs(source_path)


def confirm_cleaning(directory: str) -> bool:
    inp = input(f"Please confirm the cleaning of {directory} (yes/no) ")
    return inp.lower().strip() in ["y", "yes"]


def confirm_backup(directory: str) -> bool:
    inp = input(f"Please confirm the backup of {directory}(yes/no) ")
    return inp.lower() in ["y", "yes"]


def confirm_deletion(directory: str) -> bool:
    inp = input(f"Please confirm the deletion of files from {directory} (yes/no) ")
    return inp.lower().strip() in ["y", "yes"]


def get_args():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--backup",
        action="store_true",
        help="Create a backup before making changes",
        required=False,
    )
    parent_parser.add_argument(
        "--backup_dir",
        help="The directory where the backup will be stored",
        required=False,
    )

    parser = argparse.ArgumentParser(description="Folder cleanser")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    organize_parser = subparsers.add_parser("clean", parents=[parent_parser])
    organize_parser.add_argument(
        "--source_dir", help="The directory you would like to clean."
    )
    organize_parser.add_argument(
        "--method",
        help="The method of cleaning",
        choices=["suffix", "date", "size"],
        required=True,
    )
    organize_parser.add_argument(
        "--shallow",
        help="Perform a shallow clean (do not traverse subdirectories)",
        action="store_true",
        required=False,
    )
    organize_parser.add_argument(
        "--year_only",
        help="Option to sort by year only",
        action="store_true",
        required=False,
    )

    delete_files_parser = subparsers.add_parser("delete_files", parents=[parent_parser])
    delete_files_parser.add_argument(
        "--source_dir",
        help="The directory where the files you would like to delete are located.",
        required=True,
    )
    delete_files_time_group = delete_files_parser.add_mutually_exclusive_group(
        required=True
    )
    delete_files_time_group.add_argument(
        "--n_days",
        type=int,
        help="The age of the files you want to delete in days (i.e., delete everything more than 10 days old)",
    )
    delete_files_time_group.add_argument(
        "--n_months",
        type=int,
        help="The age of the files you want to delete in months",
    )
    delete_files_time_group.add_argument(
        "--n_years",
        type=int,
        help="The age of the files you want to delete in years",
    )
    return parser


def main():
    parser = get_args()
    args = parser.parse_args()
    if args.backup and args.backup_dir:
        if confirm_backup(args.source_dir):
            backup_dir(args.source_dir, args.backup_dir)
    if args.command == "clean":
        if confirm_cleaning(args.source_dir):
            organized_files = organize_files(
                source_dir=args.source_dir,
                method=args.method,
                shallow=args.shallow,
                year_only=args.year_only,
            )

            move_files_to_dir(args.source_dir, organized_files)

    elif args.command == "delete_files":
        if confirm_deletion(args.source_dir):
            if args.n_days:
                delete_files_by_time(args.source_dir, n_days=int(args.n_days))
            elif args.n_months:
                delete_files_by_time(args.source_dir, n_months=int(args.n_months))
            elif args.n_years:
                delete_files_by_time(args.source_dir, n_years=int(args.n_years))
            else:
                print("Invalid time period")

    else:
        print("No valid commands were given for more info please check --help")


if __name__ == "__main__":
    main()
