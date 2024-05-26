# FolderCleanser

Folder cleanser is a simple Python script that helps you clean directories efficiently. We offer a few options such as cleaning  directories by file types, dates, and sizes. We also allow for the option of backing up any directories beforehand, as-well as the option for a deep or shallow cleansing of folders. A shallow cleanse will only apply the cleaning to the top-level directory while our deep cleanse will recursively iterate through all nested directories in that folder and perform the cleaning. Feel free to change the categories.py file to cater folder names to your needs.

## Installation

Clone the repository:
```
git clone https://github.com/justinpakzad/FolderCleanser
```

## Usage
#### Clean Directory by File Suffix

To clean files by their file suffixes, with an optional backup:

```bash
python main.py clean_by_suffix <source_directory> --backup --backup_dir <backup_directory>
```
To perform a shallow clean (does not traverse subdirectories):
```bash
python main.py clean_by_suffix <source_directory> --shallow
```

#### Clean Directory by Date

To clean files in a directory grouped by month and year (optional back up available):
```bash
python main.py clean_by_date <source_directory>
```
To clean files in a directory grouped by year only:
```bash
python main.py clean_by_date <source_directory> --year_only
```
#### Clean Directory by File Size
To clean files in a directory grouped by file size (optional back up available):
```bash
python main.py clean_by_size <source_directory>
```

