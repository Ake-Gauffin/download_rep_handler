# download_rep_handler

Automatically organize files in your downloads folder on macOS using Python's `pathlib`.

## Usage

Run from your downloads folder:

```bash
python3 sort_downloads.py
```

Or specify a different directory:

```bash
python3 sort_downloads.py /path/to/directory
```

## Features

- Automatically categorizes files by type (video, audio, images, documents, archives, programming)
- Creates directory structure automatically
- Prevents file overwriting
- Detailed logging of operations
- Error handling for permission issues

## Customization

Edit the `CATEGORIES` dictionary in `sort_downloads.py` to customize file types and directory paths. 