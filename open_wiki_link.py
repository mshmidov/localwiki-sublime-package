import os

import sublime
import sublime_plugin

from .common import make_sure_path_exists
from .view import is_in_project
from .linkfinder import find_selected_link_text
from .wikilink import WikiLink


class OpenWikiLinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        view = self.view

        if is_in_project(view) and view.file_name() is not None:

            selection = view.sel()[0]

            link = WikiLink.from_text_and_region(find_selected_link_text(view, selection))

            if link:
                target_file = link.reference().resolve(view)

                if not os.path.exists(target_file):
                    make_sure_path_exists(os.path.dirname(target_file))

                    with open(target_file, 'a') as new_file:
                        new_file.write('# ' + link.title())

                existing_view = view.window().find_open_file(target_file)

                if existing_view:
                    view.window().focus_view(existing_view)
                else:
                    view.window().focus_view(view.window().open_file(target_file, sublime.TRANSIENT))