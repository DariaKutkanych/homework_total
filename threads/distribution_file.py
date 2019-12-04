import argparse
import glob
import os
from datetime import date
from threading import Thread


file_type = None


def replace():
    files = glob.glob(f".\current_directory\*.{file_type}")[0]
    file_name = files.split("\\")[-1]
    mod_date = date.fromtimestamp(int(os.path.getmtime(files)))
    directory_name = f'{mod_date.day}_{mod_date.month}'
    if not os.path.exists(directory_name):
        os.makedirs(f'./{directory_name}')
    os.replace(files, f'./{directory_name}/{file_name}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-t',
                        '--type',
                        type=str,
                        default=None)
    args = parser.parse_args()

    file_type = f'{args.type}'

    while True:
        if glob.glob(f".\current_directory\*.{file_type}"):
            t1 = Thread(target=replace)
            t1.start()
            t1.join()
