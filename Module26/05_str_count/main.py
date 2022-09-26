import os
from collections.abc import Iterable


def gen_files_dir(path: str, depth=1) -> Iterable[str]:
    depth -= 1
    with os.scandir(path) as p:
        for entry in p:
            yield entry.path
            if entry.is_dir() and depth > 0:
                yield from gen_files_dir(entry.path, depth)


if __name__ == '__main__':
    directory = 'C:\Python310\lib'
    files = list(gen_files_dir(directory))
    line_count = 0

    for file_dir in files:
        if not os.path.isfile(file_dir):
            continue
        skip_File = True
        for ending in '.py':
            if file_dir.endswith(ending):
                skip_File = False

        if not skip_File:
            try:
                file = open(file_dir, "r")
                local_count = 0
                for line in file.read().split('\n'):
                    if (not line.strip() == '') and (not line.strip().startswith("#")) and (not line.strip().startswith('"')):
                        local_count += 1
                print('{} - {} ст'.format(file_dir, local_count))
                line_count += local_count
                file.close()
            except:
                continue

    print("=====================================")
    print("Всего строк  - ", line_count)

# зачет!
