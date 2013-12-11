import os

from .common import safe_file_name, LINK_PATTERN
from .view import get_project_folder, get_current_folder


class WikiLink:
    def __init__(self, text, title, reference, region):
        self._text = text
        self._title = title
        self._reference = LinkReference(reference)
        self._region = region

    def text(self):
        return self._text

    def title(self):
        return self._title

    def reference(self):
        return self._reference

    def region(self):
        return self._region

    @staticmethod
    def from_text_and_region(text_and_region):

        if text_and_region:

            text, region = text_and_region

            match = LINK_PATTERN.match(text)

            if match:
                title = match.group(1)
                reference = match.group(2)

                return WikiLink(text, title, reference or safe_file_name(title), region)


class LinkReference:
    def __init__(self, reference):
        self._is_abs = os.path.isabs(reference)
        self._reference = reference
        self._joinable_reference = reference[1:] if self._is_abs else reference

    def resolve(self, view):
        root = get_project_folder(view) if self._is_abs else get_current_folder(view)

        return os.path.realpath(os.path.join(root, self._joinable_reference))
