import os
from os import listdir
from os.path import isfile, join
import shutil
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", type=str)
    parser.add_argument("--output_folder", type=str, default="dist")
    args = parser.parse_args()

    try:
        input_folder = os.path.abspath(args.input_folder)
        output_folder = os.path.abspath(args.output_folder)

        if not os.path.exists(input_folder):
            raise FileNotFoundError(f"Вказана папка '{input_folder}' не існує.")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        copy(input_folder, output_folder)

    except FileNotFoundError as e:
        print(f"Помилка: {e}")
    except PermissionError as e:
        print(f"Помилка доступу: {e}")
    except OSError as e:
        print(f"Системна помилка: {e}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")


def copy(input_folder, output_folder):
    for el in listdir(input_folder):
        input_path = join(input_folder, el)
        if isfile(input_path):
            file_name, file_extension = os.path.splitext(el)
            folder_name = file_extension.lstrip(".").upper() or "NO_EXTENSION"
            type_folder = join(output_folder, folder_name)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            shutil.copy(input_path, join(type_folder, el))
        elif os.path.isdir(input_path):
            copy(input_path, output_folder)


if __name__ == "__main__":
    main()