import os
import argparse

def replace_spaces_in_paths(root_path: str, replace_char: str = '') -> bool:
    """
    Replace all spaces in folder and file names with a specified character recursively from a given root folder.
    
    Parameters:
    - root_path (str): The root directory from which the renaming process starts.
    - replace_char (str): The character to replace spaces with in folder and file names. Defaults to ''.
    
    Returns:
    - bool: True if any folder or file was renamed, False otherwise.
    """
    any_replacement = False
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        # Rename directories
        for dirname in dirnames:
            old_dir_path = os.path.join(dirpath, dirname)
            new_dirname = dirname.replace(' ', replace_char)
            new_dir_path = os.path.join(dirpath, new_dirname)
            if old_dir_path != new_dir_path:
                os.rename(old_dir_path, new_dir_path)
                any_replacement = True
                print(f'Renamed folder: "{old_dir_path}" to "{new_dir_path}"')

        # Rename files
        for filename in filenames:
            old_file_path = os.path.join(dirpath, filename)
            new_filename = filename.replace(' ', replace_char)
            new_file_path = os.path.join(dirpath, new_filename)
            if old_file_path != new_file_path:
                os.rename(old_file_path, new_file_path)
                any_replacement = True
                print(f'Renamed file: "{old_file_path}" to "{new_file_path}"')

    return any_replacement

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace spaces in folder and file names with a specified character.')
    parser.add_argument('--folder_route', type=str, default='.', help='The root directory from which the renaming process starts.')
    parser.add_argument('--replace_char', type=str, default='', help='The character to replace spaces with in folder and file names. Defaults to an empty string.')

    args = parser.parse_args()
    if not replace_spaces_in_paths(args.folder_route, args.replace_char):
        print(f"There were no spaces inside the {args.folder_route} folders or files.")
