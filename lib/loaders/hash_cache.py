import dbm

from lib.loaders.loader_utils import md5

db = dbm.open('file_name_hashes', 'c')


def check_path(path):
    if path not in db:
        return True
    file_hash = md5(path)
    return db[path] != file_hash


def update_file_hash(path):
    db[path] = md5(path)
