# Copyright (C) 2011-2018  Patrick Totzke <patricktotzke@gmail.com>
# This file is released under the GNU GPL, version 3 or a later revision.
# For further details see the COPYING file
import urwid
from notmuch import NotmuchError

from .buffer import Buffer
from ..settings.const import settings
from ..walker import IterableWalker
from ..widgets.search import ThreadlineWidget
import logging


class SearchBuffer(Buffer):
    """shows a result list of threads for a query"""

    modename = 'search'
    threads = []
    _REVERSE = {'oldest_first': 'newest_first',
                'newest_first': 'oldest_first'}

    def __init__(self, ui, initialquery='', sort_order=None):
        self.dbman = ui.dbman
        self.ui = ui
        self.querystring = initialquery
        default_order = settings.get('search_threads_sort_order')
        self.sort_order = sort_order or default_order
        self.result_count = 0
        self.unread_count = 0
        self.isinitialized = False
        self.rebuild()
        Buffer.__init__(self, ui, self.body)

    def __str__(self):
        formatstring = '[search] (%d message%s, %d unread) query: "%s" '
        return formatstring % (self.result_count,
                               's' if self.result_count > 1 else '', self.unread_count, self.querystring)

    def get_info(self):
        info = {}
        info['querystring'] = self.querystring
        info['result_count'] = self.result_count
        info['result_count_positive'] = 's' if self.result_count > 1 else ''
        return info

    def rebuild(self, reverse=False):
        self.isinitialized = True
        self.reversed = reverse

        if reverse:
            order = self._REVERSE[self.sort_order]
        else:
            order = self.sort_order

        exclude_tags = settings.get_notmuch_setting('search', 'exclude_tags')
        if exclude_tags:
            exclude_tags = [t for t in exclude_tags.split(';') if t]

        try:
            self.unread_count = self.dbman.count_messages(self.querystring+' AND tag:unread')
            self.result_count = self.dbman.count_messages(self.querystring)
            threads = self.dbman.get_threads(
                self.querystring, order, exclude_tags)
        except NotmuchError:
            self.ui.notify('malformed query string: %s' % self.querystring,
                           'error')
            self.listbox = urwid.ListBox([])
            self.body = self.listbox
            return

        self.threadlist = IterableWalker(threads, ThreadlineWidget,
                                         dbman=self.dbman,
                                         reverse=reverse)

        self.listbox = urwid.ListBox(self.threadlist)
        self.body = self.listbox

    def get_selected_threadline(self):
        """
        returns curently focussed :class:`alot.widgets.ThreadlineWidget`
        from the result list.
        """
        threadlinewidget, _ = self.threadlist.get_focus()
        return threadlinewidget

    def get_selected_thread(self):
        """returns currently selected :class:`~alot.db.Thread`"""
        threadlinewidget = self.get_selected_threadline()
        thread = None
        if threadlinewidget:
            thread = threadlinewidget.get_thread()
        return thread

    def consume_pipe(self):
        while not self.threadlist.empty:
            self.threadlist._get_next_item()

    def focus_first(self):
        if not self.reversed:
            self.body.set_focus(0)
        else:
            self.rebuild(reverse=False)

    def focus_last(self):
        if self.reversed:
            self.body.set_focus(0)
        elif self.result_count < 200 or self.sort_order not in self._REVERSE:
            self.consume_pipe()
            num_lines = len(self.threadlist.get_lines())
            self.body.set_focus(num_lines - 1)
        else:
            self.rebuild(reverse=True)
