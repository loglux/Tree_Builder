import os

class DirectoryTree:
    def __init__(self, start_path, ignored_folders=None):
        self.start_path = start_path
        self.ignored_folders = ignored_folders if ignored_folders else []

    def dir_tree(self, dir_path, file_output=False, indentation=""):
        if os.path.basename(dir_path) in self.ignored_folders:
            return

        if os.path.isdir(dir_path):
            print(indentation + "|-- " + os.path.basename(dir_path))
            for item in os.listdir(dir_path):
                self.dir_tree(os.path.join(dir_path, item), file_output, indentation + "   ")
        elif file_output:
            print(indentation + "|-- " + os.path.basename(dir_path))

    def display(self, file_output=False):
        print(self.start_path)
        for item in os.listdir(self.start_path):
            self.dir_tree(os.path.join(self.start_path, item), file_output)


# Usage
if __name__ == '__main__':
    ignored_folders = ['.venv', '__pycache__', '.git', '.idea']
    start_path = '.'
    tree = DirectoryTree(start_path, ignored_folders)
    # Folders only
    tree.display()

    # Folders and files
    # tree.display(True)
