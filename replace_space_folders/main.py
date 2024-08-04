import os
import argparse

def replace_spaces_in_folders(folder_route: str, replace_char: str = '') -> bool:
    """
    Replace all spaces in folder names with a specified character recursively from a given root folder.
    
    Parameters:
    - folder_route (str): The root directory from which the renaming process starts.
    - replace_char (str): The character to replace spaces with in folder names. Defaults to ''.
    
    Returns:
    - bool
    """
    folder_replace = False
    for dirpath, dirnames, _ in os.walk(folder_route, topdown=False):
        for dirname in dirnames:
            old_path = os.path.join(dirpath, dirname)
            new_dirname = dirname.replace(' ', replace_char)
            new_path = os.path.join(dirpath, new_dirname)
            if old_path != new_path:
                os.rename(old_path, new_path)
                folder_replace = True
                print(f'Renamed: "{old_path}" to "{new_path}"')

    return folder_replace

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace spaces in folder names with a specified character.')
    parser.add_argument('--folder_route', type=str, default='.', help='The root directory from which the renaming process starts')
    parser.add_argument('--replace_char', type=str, default='', help='The character to replace spaces with in folder names. Defaults to an empty string.')

    args = parser.parse_args()
    if not replace_spaces_in_folders(args.folder_route, args.replace_char):
        print(f"There was no space inside the {args.folder_route} folders.")