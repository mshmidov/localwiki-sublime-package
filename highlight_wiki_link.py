import os

import sublime
import sublime_plugin

from .view import is_in_project
from .linkfinder import find_selected_link_text
from .wikilink import WikiLink

REGION_SCOPE = "wikilink"
REGION_ID = "localwiki.wikilink"

EXISTING_LINK = sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE | sublime.DRAW_SOLID_UNDERLINE
MISSING_LINK = sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE | sublime.DRAW_STIPPLED_UNDERLINE


class HighlightWikiLinkCommand(sublime_plugin.EventListener):
    def on_selection_modified_async(self, view):

        if is_in_project(view) and view.file_name() is not None:

            view.erase_regions(REGION_ID)

            selection = view.sel()[0]

            link = WikiLink.from_text_and_region(find_selected_link_text(view, selection))

            if link:
                view.add_regions(REGION_ID,
                                 [link.region()],
                                 REGION_SCOPE,
                                 "",
                                 EXISTING_LINK if os.path.exists(link.reference().resolve(view)) else MISSING_LINK)