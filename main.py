from fmerger.fmerger import FMerger


if __name__ == "__main__":
    file_merger = FMerger({
        "sources_options": {
            "source_dir": "files_csv",
            # "source_encoding": "utf-8",
            "source_delimiter": ";",
            "source_newline": "",
        },
        "target_file_options": {
            "target_file": "merged_files.csv",
            # "target_encoding": "",
            "target_delimiter": ";",
            "target_newline": "",
        }
    })

    file_merger.merge()
