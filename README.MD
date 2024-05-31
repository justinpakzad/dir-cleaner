# DirCleaner

Dir cleaner is a simple Python script that helps you clean directories efficiently. There is a few options such as cleaning  directories by file types, dates, and sizes. The script also allows for the option to back up any directories beforehand, as-well as the option for a deep or shallow cleansing of folders. A shallow cleanse will only apply the cleaning to the top-level directory while our deep cleanse will recursively iterate through all nested directories in that folder and perform the cleaning.

## Configuration
The `categories.py` file serves as the main file for defining which file types the cleaning script recognizes and processes when cleaning by suffix. It comes pre-configured with categories for various file types, including audio, video, images, documents, and more. Feel free to modify the entries in `categories.py` to match the specific file types you frequently handle. Simply add or remove file extensions from the existing categories, or even create new categories as needed. All directory paths specified in command options are interpreted relative to the user's home directory. Make sure to provide paths accordingly.


## Installation

Clone the repository:
```
git clone https://github.com/justinpakzad/DirCleaner
```


## Usage

#### 1. `clean_by_suffix`
Cleans directory based on file suffixes.
- **Options**:
  - `--source_dir`: Specifies the source directory to clean *(required)*.
  - `--backup`: Enables a backup of the directory before cleaning *(optional)*.
  - `--backup_dir`: Specifies where backups are stored *(optional)*.
  - `--shallow`: Limits the cleaning to the top-level directory only *(optional)*.

#### 2. `clean_by_date`
Organizes files in the directory by the year and month of their creation.
- **Options**:
  - `--source_dir`: Specifies the source directory to clean *(required)*.
  - `--year_only`: Organizes files by year only, skipping month categorization *(optional)*.
  - `--backup`: Enables a backup of the directory before cleaning *(optional)*.
  - `--backup_dir`: Specifies where backups are stored *(optional)*.
  - `--shallow`: Limits the cleaning to the top-level directory only *(optional)*.

#### 3. `clean_by_size`
Sorts and cleans files in the directory based on their size into predefined size groups.
- **Options**:
  - `--source_dir`: Specifies the source directory to clean *(required)*.
  - `--backup`: Enables a backup of the directory before cleaning *(optional)*.
  - `--backup_dir`: Specifies where backups are stored *(optional)*.
  - `--shallow`: Limits the cleaning to the top-level directory only *(optional)*.

#### 4. `delete_files`
Deletes files that are older than a specified number of days.
- **Options**:
  - `--source_dir`: Specifies the source directory to clean *(required)*.
  - `--n_days`: The minimum age (in days) of files to be deleted. Files older than this threshold will be deleted *(required)*.
  - `--backup`: Enables a backup of the directory before cleaning *(optional)*.
  - `--backup_dir`: Specifies where backups are stored *(optional)*.

## Examples
### Clean Directory by File Suffix
```bash
python main.py clean_by_suffix --source_dir <source_directory> --backup --backup_dir <backup_directory>
```
### Clean Directory by Date
```bash
python main.py clean_by_date --source_dir <source_directory>
```
### Clean Directory by File Size
```bash
python main.py clean_by_size --source_dir <source_directory>
```
### Deletes files that are older than a specified number of days.
```bash
python main.py delet_files --source_dir <source_directory> --n_days <number of days old>
```

## Contributing

Any contributions are welcomed. For major changes, please open an issue first to discuss what you would like to change.
