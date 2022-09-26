import os
from _collections_abc import Iterable


def gen_files_path(folder: str, path=None) -> Iterable[str]:
    if path is None:
        path = os.path.abspath(os.path.join(os.path.sep))
    for i_elem in os.listdir(path):
        temp = os.path.abspath(os.path.join(path, i_elem))
        if os.path.isdir(temp) and i_elem != folder:
            gen_files_path(folder, temp)
        yield temp
        if i_elem == folder:
            return

# зачет!
