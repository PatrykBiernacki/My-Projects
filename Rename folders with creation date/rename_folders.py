"""This program organizes folders chronologically by modifying their name to contain creation date in format 'YYYYMMDD-originalname'"""

from datetime import datetime
import os

import log_activity

class AddDateToName:

    list_of_folders = []


    @classmethod
    def list_dir(cls):
        """Creates list of directories from file."""
        try:
            with open('list_dir.txt','r') as file:
                for line in file:
                    line = line.strip('\n')
                    if line[0] == '*':  # Recognizes relative directories by first symbol '*'
                        line = os.path.join(os.getcwd(), line.strip('*\\'))
                        
                    if cls.check_dir_valid(line):
                        cls.list_of_folders.append(line)
                    else:
                        print(f'{line} is not a valid directory.')
        except Exception as e:
            print('EXCEPTION RAISED AS:', e) 


    @classmethod
    def check_dir_valid(cls, folder_dir:str) -> bool:
        """Acept directory string. Return True if directory exists and contains folders inside. Returns False otherwise."""
        if not os.path.isdir(folder_dir):
            print('Provided directory does not exist.')
            return(False)
        if not any(os.path.isdir(os.path.join(folder_dir, item)) for item in os.listdir(folder_dir)):
            print('This directory does not contain folders.')
            return(False)
        else:
            print(f'{folder_dir} <- directory is valid.')
            return(True)


    @classmethod
    def rename_folders_in_locations(cls) -> list:
        """Adds creation time to folders name in defined directories. Names in 'YYMMDD-originalname' format."""
        for directory in cls.list_of_folders:
            folder_name_generator = cls.gen_folders_in_directory(directory) #generator of folder names in directory.
            for folder_name in folder_name_generator:
                print(f'Reviewing folder {folder_name}')
                folder_creation_date = datetime.fromtimestamp(os.path.getctime(os.path.join(directory, folder_name)))
                if not folder_name.split('-')[0] == folder_creation_date.strftime('%Y%m%d'):
                    new_folder_name = '{0}-{1}'.format(folder_creation_date.strftime('%Y%m%d'), folder_name)
                    os.rename(os.path.join(directory, folder_name), os.path.join(directory, new_folder_name))
                    print(f'Folder {folder_name} renamed as {new_folder_name}.')
                else:
                    print(f'Folder {folder_name} already named correctly.')
                    continue
        return cls.list_of_folders  


    @staticmethod
    def gen_folders_in_directory(folder_dir:str) -> iter:
        """Accepts directory and returns generator of folder names in that dir."""
        return (folder_name for folder_name in os.listdir(folder_dir) if os.path.isdir(os.path.join(folder_dir, folder_name)))


@log_activity.LogActivity
def rename_folders_in_locations_with_log():
    return AddDateToName.rename_folders_in_locations()


if __name__ == '__main__':
    AddDateToName.list_dir()
    rename_folders_in_locations_with_log()