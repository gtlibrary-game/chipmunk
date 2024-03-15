import argparse
import glob
import os
import sys

def gather_files(search_pattern, root_directory):
    """
    Recursively gather files matching the search pattern within the root directory.
    """
    full_path_pattern = os.path.join(root_directory, search_pattern)
    return glob.glob(full_path_pattern, recursive=True)

def write_to_stdout(files):
    """
    Write the contents of the gathered files to stdout, separating them with a newline.
    """
    for file_path in files:
        # Ensure it's a file, not a directory
        if os.path.isfile(file_path):
            sys.stdout.write(f"// Start of {file_path}\n")
            with open(file_path) as f:
                sys.stdout.write(f.read() + "\n\n// End of {file_path}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prepare a database of files for GPT ingestion.')
    parser.add_argument('-p', '--pattern', required=True, help='Search pattern for files to include, e.g., "**/*.py" for all Python files or "**/*" for all files')
    parser.add_argument('-r', '--root_directory', default='.', help='Root directory to search for files')
    args = parser.parse_args()

    files = gather_files(args.pattern, args.root_directory)
    write_to_stdout(files)
