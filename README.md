# Python File Handling CLI

A command-line tool built in Python that lets you **create, read, update, and delete** files — implemented using the `pathlib` module and standard file I/O operations.

## Features

- **Create File** – Create a new file and write custom content to it (checks if the file already exists before creating).
- **Read File** – Read and display the content of any existing file.
- **Update File** – Update an existing file in three ways:
  - Rename the file
  - Overwrite the file with new content
  - Append new content to the existing file
- **Delete File** – Delete a file after confirming it exists.
- **Directory Listing** – Before every operation, the tool lists all files and folders in the current directory so you can pick the correct file name.
- **Error Handling** – All operations are wrapped in try-except blocks to handle invalid inputs and unexpected errors gracefully.

## Tech Stack / Concepts Used

- Python 3
- `pathlib` module (`Path`, `.exists()`, `.is_file()`, `.rename()`)
- `os` module (`os.remove()`)
- File I/O (`open()`, read/write/append modes)
- Exception handling (`try-except`)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ayyanchiplunkar/python-file-handling.git
   cd python-file-handling
   ```

2. Run the script:
   ```bash
   python MAIN.PY
   ```

3. Follow the on-screen menu:
   ```
   press 1 for creating a new file
   press 2 for read the file
   press 3 for updating the file
   press 4 for deleting a file
   ```

## Example Usage

```
please tell your choice: 1
please enter the file name: notes.txt
what you want to write in this file: Hello, this is my first file!
file created successfully
```

## Future Improvements

- Add input validation for invalid menu choices
- Support for reading/writing binary files
- Add unit tests using `unittest` or `pytest`
- Convert to a GUI or web-based version using Tkinter/Flask

## Author

**Ayyan Chiplunkar**
Aspiring Data Analyst | Python & SQL Enthusiast
[GitHub](https://github.com/ayyanchiplunkar)
