import sys
import os
from pages.notewriter_page import NoteWriterPage
from TestCase.base_test import BaseTest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class TestDate(BaseTest):

    def test_1(self):
        pagenotewriter = NoteWriterPage(self.driver)
        pagenotewriter.test_date()

# python3 -m unittest TestCase.test_1
