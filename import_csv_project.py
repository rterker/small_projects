import csv
import pathlib
import time
import re
import pysftp
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List
# import shutil

# @dataclass
# class File(ABC):
#     path: pathlib.Path
#     source_name: str
#     file_date: int
#     file_type: str

#     @abstractmethod
#     get file_date(self) -> int:
#     """Get the file date to search for."""

#     @abstractmethod
#     get_source_system(self) -> str:
#     """Get the source system."""

#     @abstractmethod
#     set_file_format(self) -> str:
#     """Set file format."""

#     @abstractmethod
#     get_file_type(self) -> str:
#     """Get file type."""

# class Electra_file(File):
#     get file_date(self) -> int:
#     """Set the file date to search for."""


#     get_source_system(self) -> str:
#     """Set the source system."""

#     set_file_format(self) -> str:
#     """Set file format."""
        


def get_file_date() -> int:
    file_date_to_work_with: str = input('Enter file date to work with in format "YYMMDD": ')
    try:
        file_date_to_work_with: int = int(file_date_to_work_with)
    except ValueError: 
        print('Please enter an integer for the date in the format "YYMMDD".')
        get_file_date()
    file_date_to_work_with = int(file_date_to_work_with)
    if (file_date_to_work_with < 10000000) or (file_date_to_work_with > 99999999):
        print('Please enter an integer for the date in the format "YYMMDD".')
        get_file_date()
    return file_date_to_work_with

# def get_file_names_to_match(file_date_to_work_with: int, prefixes: list) -> list:
#     file_names: list = []
#     file_date_to_work_with: str = str(file_date_to_work_with)
#     for prefix in prefixes:
#         file_name: str = prefix + file_date_to_work_with
#         file_names.append(file_name)
#     return file_names

def get_files(working_dir: pathlib.Path, prefixes: list, file_date_to_work_with: int, file_type: str) -> list:
    files = []
    directory_contents: list = pathlib.Path.iterdir(working_dir)
    for file in directory_contents:    
        for file_name_prefix in prefixes:
            # if re.search(f'^{file_name_prefix}{file_date_to_work_with}.*$', file.name):
            if re.search(f'^{file_date_to_work_with}_{file_name_prefix}_[0-9][0-9]_XXX.{file_type}', file.name):
                files.append(file)
    return files

def get_column_headers(csv_file: pathlib.Path) -> list:
    with open(csv_file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            return row

def create_output_file(file_paths: list, working_dir: pathlib.Path, column_headers: list, file_date_to_work_with: int):
    destination_file_content = []
    # destination_file_content.append(column_headers)
    for file in file_paths:
        if re.search('.XXX', file.suffix, flags=re.IGNORECASE):
            with open(file, mode='r') as file:
                csv_reader = csv.reader(file, delimiter=',')
                for row in csv_reader:
                    destination_file_content.append(row)        
    with open(pathlib.Path.home().joinpath('XXXXXXX').joinpath('Temp').joinpath(f'{file_date_to_work_with}_new_file_XXX.csv'), mode='w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')
        for row in destination_file_content:
            csv_writer.writerow(row)
        return new_file

def main():
    ## Parameters
    working_dir: pathlib.Path = pathlib.Path('/Users/rterker/desktop/test_folder')
    # file_type = 'XX'
    file_type = 'XXX'
    # prefixes: list = [f'XXXX{file_type}', f'XXXXX{file_type}', f'XXXXX{file_type}', f'XXXXX{file_type}']
    prefixes: list = ['XXX', 'XXX', 'XXX', 'XXX', 'XXX']

    file_date_to_work_with_main: int = get_file_date()
    # file_names_to_match: list = get_file_names_to_match(file_date_to_work_with_main, prefixes)
    file_paths: list = get_files(working_dir, prefixes, file_date_to_work_with=file_date_to_work_with_main, file_type=file_type) ## Experimenting with keyword arguments.
    try:
        column_headers = get_column_headers(file_paths[0])
        new_file = create_output_file(file_paths, working_dir, column_headers, file_date_to_work_with_main)
    except IndexError:
        print('We are not finding any headers.')

if __name__ == '__main__':
    main()


# with pysftp.Connection('hostname', username='me', password='secret') as sftp:
#     with sftp.cd('XXXXX'):
#         sftp.chdir('XXX')
#         sftp.get('file', preserve_mtime=True)
#         ## Where is the file copied to locally?
     