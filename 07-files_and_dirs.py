"""
Files and Directories
====================
"""

from pathlib import Path

Path.cwd()  # Get the current working directory
# - `Path`: Represents a filesystem path.
# - `Path.cwd()`: Returns the current working directory as a Path object.
# - `Path.home()`: Returns the user's home directory as a Path object.
Path.home()  # Get the user's home directory
# - `Path.exists()`: Checks if a path exists.
Path('example.txt').exists()  # Check if 'example.txt' exists in the current directory

# - `Path.is_file()`: Checks if a path is a file.
Path('example.txt').is_file()  # Check if 'example.txt' is a file

# - `Path.is_dir()`: Checks if a path is a directory.
Path('example_dir').is_dir()  # Check if 'example_dir' is a directory

# - `Path.mkdir()`: Creates a new directory.
Path('new_directory').mkdir(exist_ok=True)  # Create 'new_directory', do not raise error if it 

# - `Path.rmdir()`: Removes an empty directory.
Path('empty_directory').rmdir()  # Remove 'empty_directory', must be empty

# - `Path.unlink()`: Deletes a file.
Path('file_to_delete.txt').unlink()  # Delete 'file_to_delete.txt'

# - `Path.rename()`: Renames a file or directory.   
Path('old_name.txt').rename('new_name.txt')  # Rename 'old_name.txt' to 'new_name.txt'

# - `Path.iterdir()`: Iterates over the contents of a directory.
for item in Path('.').iterdir():
    print(item)  # Print each item in the current directory

# - `Path.glob()`: Finds all files matching a pattern.
for txt_file in Path('.').glob('*.txt'):
    print(txt_file)  # Print all .txt files in the current directory

# - `Path.read_text()`: Reads the contents of a file as text.
content = Path('example.txt').read_text()  # Read text from 'example.txt'

# - `Path.write_text()`: Writes text to a file.
Path('output.txt').write_text("Hello, World!")  # Write text to 'output.txt'

# - `Path.read_bytes()`: Reads the contents of a file as bytes.
bytes_content = Path('example.bin').read_bytes()  # Read bytes from 'example.bin

# - `Path.write_bytes()`: Writes bytes to a file.
Path('output.bin').write_bytes(b'\x00\x01\x02')  # Write bytes to 'output.bin'

# - `Path.stat()`: Returns file or directory statistics.
stats = Path('example.txt').stat()  # Get statistics for 'example.txt'

# - `Path.resolve()`: Returns the absolute path of a file or directory.
absolute_path = Path('example.txt').resolve()  # Get the absolute path of 'example.txt'

# - `Path.relative_to()`: Returns a relative path to another path.
relative_path = Path('example.txt').relative_to(Path.cwd())  # Get relative path from current directory

# - `Path.joinpath()`: Joins paths together.
joined_path = Path('example_dir').joinpath('file.txt')  # Join 'example_dir' with 'file.txt'

# - `Path.parts`: Returns the components of the path as a tuple.
path_parts = Path('example_dir/file.txt').parts  # Get the parts of the path

# - `Path.suffix`: Returns the file extension of the path.
file_suffix = Path('example.txt').suffix  # Get the file extension of 'example.txt  '

# - `Path.suffixes`: Returns a list of all file extensions.
file_suffixes = Path('archive.tar.gz').suffixes  # Get all file extensions of 'archive.tar.gz'

# - `Path.with_suffix()`: Changes the file extension of the path.
new_path = Path('example.txt').with_suffix('.md')  # Change 'example.txt' to 'example.md'

# - `Path.with_name()`: Changes the file name while keeping the same directory.
new_name_path = Path('example.txt').with_name('new_example.txt')  # Change 'example.txt' to 'new_example.txt'

# - `Path.with_stem()`: Changes the stem (base name without suffix) of the path.
new_stem_path = Path('example.txt').with_stem('new_example')  # Change 'example.txt' to 'new_example.txt'

# - `Path.expanduser()`: Expands the `~` to the user's home directory.
expanded_path = Path('~/example.txt').expanduser()  # Expand '~' to the user's home directory

# - `Path.resolve(strict=True)`: Resolves the path and raises an error if it does not exist.
try:
    resolved_path = Path('non_existent.txt').resolve(strict=True)  # Will raise an error if 'non_existent.txt' does not exist
except FileNotFoundError:
    print("File does not exist.")

# - `Path.touch()`: Creates a new file or updates the timestamp of an existing file.
Path('new_file.txt').touch()  # Create 'new_file.txt' if it does not exist, or update its timestamp if it does

# - `Path.chmod()`: Changes the permissions of a file or directory. 
Path('example.txt').chmod(0o644)  # Change permissions of 'example.txt' to read/write for owner, read for group and others

# - `Path.symlink_to()`: Creates a symbolic link to a file or directory.
Path('link_to_example.txt').symlink_to('example.txt')  # Create a symbolic link 'link_to_example.txt' pointing to 'example.txt' 

# - `Path.resolve()`: Returns the absolute path of the file or directory.
resolved_path = Path('example.txt').resolve()  # Get the absolute path of 'example.txt'