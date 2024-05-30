# DirCleaner

Dir cleaner is a simple Python script that helps you clean directories efficiently. There is a few options such as cleaning  directories by file types, dates, and sizes. The script also allows for the option to back up any directories beforehand, as-well as the option for a deep or shallow cleansing of folders. A shallow cleanse will only apply the cleaning to the top-level directory while our deep cleanse will recursively iterate through all nested directories in that folder and perform the cleaning.

## Configuration
The `categories.py` file serves as the main file for defining which file types the cleaning script recognizes and processes when cleaning by suffix. It comes pre-configured with categories for various file types, including audio, video, images, documents, and more. Feel free to modify the entries in `categories.py` to match the specific file types you frequently handle. Simply add or remove file extensions from the existing categories, or even create new categories as needed.


## Installation

Clone the repository:
```
git clone https://github.com/justinpakzad/DirCleaner
```
## Usage

### Command Line Options
- `clean_by_suffix`: Cleans directory based on file suffixes.
- `clean_by_date`: Cleans directory by organizing files according to the year and month of creation.
- `clean_by_size`: Cleans directory by the size of files, sorting them into three groups.
- `--source_dir`: Specifies the source directory to clean *(required)*.
- `--backup`: Adds a flag to backup the directory before cleaning *(optional)*.
- `--backup_dir`: Specifies the directory where the backup will be stored *(optional)*.
- `--shallow`: Adds a flag to perform a shallow clean that does not traverse subdirectories *(optional)*.
- `--year_only`: Adds a flag to organize files only by year, applicable only when using `clean_by_date` *(optional)*.


### Clean Directory by File Suffix

To clean files by their file suffixes, with an optional backup:

```bash
python main.py clean_by_suffix --source_dir <source_directory> --backup --backup_dir <backup_directory>
```
### Clean Directory by Date

To clean files in a directory grouped by month and year (optional back up available):
```bash
python main.py clean_by_date --source_dir <source_directory>
```
### Clean Directory by File Size
To clean files in a directory grouped by file size (optional back up available):
```bash
python main.py clean_by_size --source_dir <source_directory>
```
## Contributing

Any contributions are welcomed. For major changes, please open an issue first to discuss what you would like to change.
