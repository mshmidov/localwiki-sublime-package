import sublime

from .common import LINK_REGEX


def find_selected_link_text(view, selection):
    if selection is not None:

        region = view.find(LINK_REGEX, find_link_start(view, selection.a))

        if region and region.intersects(selection):
            text = view.substr(region)
            return text, region


def find_link_start(view, cursor):
    position = cursor

    while (position > 0
           and not view.substr(position - 1) == '['
           and view.classify(position) & sublime.CLASS_LINE_START == 0):
        position -= 1

    return position - 1
