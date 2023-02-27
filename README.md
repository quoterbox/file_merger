# Merger for XLSX or CSV files to one CSV file

## Description

1. Put your **XLSX** or **CSV** files in a separate directory, for example `files_csv/` or `files_xlsx/`.
2. Start `pipenv run python main.py`
3. The main script has some options for example:


    from fmerger.fmerger import FMerger

    file_merger = FMerger({
        "sources_options": {
            "source_dir": "files_xlsx",
            "source_encoding": "",
            "source_delimiter": ";",
            "source_newline": "",
        },
        "target_file_options": {
            "target_file": "merged_files.csv",
            "target_encoding": "",
            "target_delimiter": ";",
            "target_newline": "",
        }
    })

    file_merger.merge()

## Setup

### How to start python script in shell

1. Install python 3.7+ https://www.python.org/downloads/windows/ (or version for you OS)
2. Install pipenv `pip install --user pipenv`. Docs are here: https://github.com/pypa/pipenv
3. To install all required packages run this command: `pipenv install`
4. To start python script: `pipenv run py main.py` or `pipenv run python main.py`

### License
[MIT License](./LICENSE.md)

### Author
[JQ/Quoterbox](https://github.com/quoterbox)
