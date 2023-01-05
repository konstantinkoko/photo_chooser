import os.path
from os import listdir

import sqlite3
import tkinter.filedialog as tk


way_to_catalog_info = f'{os.getcwd()}\way_to_catalog.txt'

def get_way_to_catalog() -> str:

    way_to_catalog = f'{os.getcwd()}'

    if os.path.exists(way_to_catalog_info):

        try:
            with open(way_to_catalog_info, "r") as inf:
                for line in inf:
                    way_to_catalog = line
        except FileNotFoundError:
            pass
        
    else:

        with open(way_to_catalog_info, 'w') as inf:
            inf.write(way_to_catalog)
    
    return way_to_catalog


def get_way_to_raw() -> str:
    return f'{os.getcwd()}'


def change_way_to_dir(title): #ytpe?
    return tk.askdirectory(title=title)

def change_way_to_file(title): #ytpe?
    return tk.askopenfilename(title=title)
    

def refresh_way_to_catalog_info(way_to_catalog) -> None:
    with open(way_to_catalog_info, 'w') as inf:
            inf.write(way_to_catalog)


def get_list_from_text(text: str) -> list:
    """Формирует список имён из текста с именами выбранных изображений"""
    names = []
    for elem in text.split():
        names += [name for name in elem.strip().split(",")]
    return names


def get_list_of_raw_files(way_do_dir: str) -> list:
    """Формирует список имён raw-файлов в заданной директории"""
    files = listdir(way_do_dir)
    raw_files = []
    for file in files:
        if _check_raw(file):
            raw_files.append(file)
    if len(raw_files) == 0:
        raise FileNotFoundError
    return raw_files


def get_files_to_update(raw_files, changed_photos: str) -> list:
    """Формирует список имён выбранных файлов"""
    changed_files_numbers = [_get_number_from_name(file_name) for file_name in changed_photos]
    files_to_change = []
    for file in raw_files:
        if _get_number_from_name(file) in changed_files_numbers:
            files_to_change.append(file)
    return tuple(files_to_change)


def update_rating_in_catalog(way_to_catalog, way_to_dir: str, update_list: tuple) -> None:
    """Устанавливает рейтинг, изменяя каталог lightroom"""

    try:
        connection = sqlite3.connect(way_to_catalog)
        cursor = connection.cursor()
    
        cursor.execute('''
            SELECT absolutePath FROM AgLibraryRootFolder
                        ''')
        
        data = cursor.fetchall()
        
        pathFolders = [k[0] for k in data]
        pathFolder = ''
        for folder in pathFolders:
            if folder in way_to_dir and len(folder) > len(pathFolder):
                pathFolder = folder
        
        rootFolder = way_to_dir.split(pathFolder)[1] + '/'

        cursor.execute(f'''
            SELECT Adobe_images.id_local FROM AgLibraryRootFolder
            LEFT JOIN AgLibraryFolder ON AgLibraryRootFolder.id_local = AgLibraryFolder.rootFolder
            LEFT JOIN AgLibraryFile ON AgLibraryFolder.id_local = AgLibraryFile.folder
            LEFT JOIN Adobe_images ON AgLibraryFile.id_local = Adobe_images.rootFile
            WHERE AgLibraryRootFolder.absolutePath = ?
            AND AgLibraryFolder.pathFromRoot = ?
            AND AgLibraryFile.originalFilename in {update_list}
                ''', (pathFolder, rootFolder))

        data = cursor.fetchall()
        
        local_id_list_to_update = tuple([k[0] for k in data])

        cursor.execute(f'''
            SELECT * FROM Adobe_images
            WHERE Adobe_images.id_local in {local_id_list_to_update}
                ''')
        
        data = cursor.fetchall()

        cursor.execute(f'''
            UPDATE Adobe_images SET rating=4
            WHERE Adobe_images.id_local in {local_id_list_to_update}
                ''')

        connection.commit()
        connection.close()

    except sqlite3.DatabaseError:
        raise
    except ValueError:
        raise


def _check_raw(file_name: str) -> bool:
    """Проверяет по расширению, является ли файл raw-файлом"""
    raw = ("raf", "cr2", "cr3", "crw", "nef", "nrw", "ari", "dpx", "arw", "srf", "sr2", "bay", "dcr", "kdc",
           "erf", "3fr", "mef", "mrw", "orf", "ptx", "pef", "raw", "rwl", "rw2", "r3d", "srw", "x3f")
    status = False
    for suffix in raw:
        if file_name.lower().endswith(suffix):
            status = True
            break
    return status


def _get_number_from_name(file_name: str) -> str:
    """Возвращает цифры из имени файла: 'IMG_1243' -> '1243'"""
    number = ''.join([i for i in file_name if i.isdigit()])
    return number