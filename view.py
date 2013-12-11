import os


def get_project_folder(view):
    if view.file_name():
        folders = [os.path.realpath(folder['path']) for folder in view.window().project_data()['folders']]

        current_folder = get_current_folder(view)

        for folder in folders:
            if os.path.commonprefix([current_folder, folder]) == folder:
                return folder


def get_current_folder(view):
    return os.path.dirname(os.path.realpath(view.file_name()))


def is_in_project(view):
    return view.window().project_data() is not None
