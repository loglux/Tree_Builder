# Tree Builder

Tree Builder is a Python script that generates a text-based visualisation of your directory structure and represents it in a tree format. It scans the directory of your choice and prints a tree structure, representing your files and directories. This tool can be handy for Windows users, since the built-in tree command does not allow exclusions.

## Features

- Scans and presents a directory structure in a clear tree format.
- Option to ignore certain directories.
- Option to include files in the tree structure or to only display directories.

## Usage

First, define a list of directories you want to ignore. These could be directories that are unrelated to your project's structure.
```python
ignore = ['__pycache__', '.git', '.idea', '.venv']
```
Next, create a new instance of the `DirectoryTree` class. Pass in the directory you want to start from as well as the list of directories to ignore.
```python
start_path = '.' # The directory to start from
```
Folders only
```python
tree.display()
```
Folders and files
```python
tree.display(True)
```
Example:
```bash
python tree_builder.py
```

