# FolderCleanser

Folder cleanser is a simple Python script that helps you clean directories efficiently. We offer a few options such as cleaning  directories by file types, dates, and sizes. We also allow for the option of backing up any directories beforehand, as-well as the option for a deep or shallow cleansing of folders. A shallow cleanse will only apply the cleaning to the top-level directory while our deep cleanse will recursively iterate through all nested directories in that folder and perform the cleaning.

## Configuration
The `categories.py` file serves as the main file for defining which file types the cleaning script recognizes and processes when cleaning by suffix. It comes pre-configured with categories for various file types, including audio, video, images, documents, and more. Feel free to modify the entries in `categories.py` to match the specific file types you frequently handle. Simply add or remove file extensions from the existing categories, or even create new categories as needed.


## Installation

Clone the repository:
```
git clone https://github.com/justinpakzad/FolderCleanser
```
## Usage

##### Command Line Options
- ```--backup```: Flag to backup a directory before cleaning.
- ```--backup_dir```: The directory where the backup will be stored (in the home directory of said user).
- ```--shallow```: Flag to perform a shallow clean (do not traverse subdirectories).
- ```--year_only```: Flag to organize files only by year (only applicable when cleaning by date).


##### Clean Directory by File Suffix

To clean files by their file suffixes, with an optional backup:

```bash
python main.py clean_by_suffix <source_directory> --backup --backup_dir <backup_directory>
```
##### Clean Directory by Date

To clean files in a directory grouped by month and year (optional back up available):
```bash
python main.py clean_by_date <source_directory>
```
##### Clean Directory by File Size
To clean files in a directory grouped by file size (optional back up available):
```bash
python main.py clean_by_size <source_directory>
```
## Contributing

Any contributions are welcomed. For major changes, please open an issue first to discuss what you would like to change.
