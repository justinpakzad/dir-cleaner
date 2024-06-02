# DirCleaner

Dir cleaner is a simple Python script that helps you clean directories efficiently. There is a few options such as cleaning  directories by file types, dates, and sizes. The script also allows for the option to back up any directories beforehand, as-well as the option for a deep or shallow cleansing of folders. A shallow cleanse will only apply the cleaning to the top-level directory while our deep cleanse will recursively iterate through all nested directories in that folder and perform the cleaning.

## Configuration
The `categories.py` file serves as the main file for defining which file types the cleaning script recognizes and processes when cleaning by suffix. It comes pre-configured with categories for various file types, including audio, video, images, documents, and more. Feel free to modify the entries in `categories.py` to match the specific file types you frequently handle. Simply add or remove file extensions from the existing categories, or even create new categories as needed. All directory paths specified in command options are interpreted relative to the user's home directory. Make sure to provide paths accordingly.


## Installation

Clone the repository:
```
git clone https://github.com/justinpakzad/DirCleaner
```


## Command Line Options

#### 1. `clean`
Cleans directory based on file suffixes.
- **Options**:
  - `--source_dir`: Specifies the source directory to clean *(required)*.
  - `--method`: The method of cleaning. Options include suffix,date, and size.
  - `--backup`: Enables a backup of the directory before cleaning *(optional)*.
  - `--backup_dir`: Specifies where backups are stored. If a backup directory does not exist, one will be created automatically.*(optional)*.
  - `--shallow`: Limits the cleaning to the top-level directory only *(optional)*.
  - `--year_only`: Organizes files by year only, skipping month categorization *(only applicable for date method)*.

**Example**:
```bash
python main.py organize --source_dir <source_directory> --method <method_of_cleaning> --backup -b-backup_dir <backup_directory>
```

#### 2. `delete_files`
Deletes files that are older than a specified number of days.
- **Options**:
  - `--source_dir`: Specifies the source directory to clean *(required)*.
  - `--n_days`: The minimum age (in days) of files to be deleted. Files older than this threshold will be deleted.
  - `--n_months`: The minimum age (in months) of files to be deleted.
  - `--n_years`: The minimum age (in years) of files to be deleted.
  - `--backup`: Enables a backup of the directory before cleaning *(optional)*.
  - `--backup_dir`: Specifies where backups are stored *(optional)*.
  - **Note**: Only one of `--n_days`, `--n_months`, or `--n_years` can be used for a single command execution. They are mutually exclusive options.

**Example**
```bash
python main.py delete_files --source_dir <source_directory> --n_days <number of days old>
```


## Contributing

Any contributions are welcomed. For major changes, please open an issue first to discuss what you would like to change.
