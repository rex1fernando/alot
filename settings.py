editor_cmd = "/usr/bin/vim -f -c 'set filetype=mail' %s"
pager_cmd = "/usr/bin/view -f -c 'set filetype=mail' %s"
terminal_cmd = 'urxvt -T notmuch -e %s'
spawn_editor = True
spawn_pager = True

# colour palette.
# id, fg16, bg16, mono, fg256, bg256
# see http://excess.org/urwid/reference.html#AttrSpec
# http://excess.org/urwid/wiki/DisplayAttributes
# interactive test-palette: http://excess.org/urwid/browser/palette_test.py
palette = [
    ('header', 'white', 'dark blue', 'bold', 'white', 'dark blue'),
    ('footer', 'white', 'dark blue', 'bold,standout', 'white', '#006'),
    ('prompt', 'light gray', 'black', 'standout', 'light gray', ''),
    ('threadline', '', '', '', '', ''),
    ('threadline_date', 'light gray', '', '', 'g58', ''),
    ('threadline_mailcount', 'light gray', '', '', 'light gray', ''),
    ('threadline_tags', 'brown', '', '', '#a86', ''),
    ('threadline_authors', 'dark green', '', '', '#6d6', ''),
    ('threadline_subject', 'light gray', '', '', 'g58', ''),
    ('threadline_content', 'dark gray', '', '', '#866', ''),
    ('threadline_focus', 'white', 'dark gray', 'standout', 'white', 'g11'),
    ('threadline_date_linefocus', 'light gray', 'dark gray', 'standout', 'g58', 'g11'),
    ('threadline_mailcount_linefocus', 'light gray', 'dark gray', 'standout', 'light gray', 'g11'),
    ('threadline_tags_linefocus', 'yellow,bold', 'dark gray', 'standout', '#ff8', 'g11'),
    ('threadline_authors_linefocus', 'dark green,bold', 'dark gray', 'standout','#8d6', 'g11'),
    ('threadline_subject_linefocus', 'light gray', 'dark gray', 'standout','g58', 'g11'),

    ('messagesummary_even', 'white', 'light blue', 'standout', 'white', '#068'),
    ('messagesummary_odd', 'white', 'dark blue', 'standout', 'white', '#006'),
    ('messagesummary_focus', 'white', 'dark green', 'standout,bold', '#ff8', 'g58'),
    ('message_header', 'white', 'dark gray', '', 'white', 'dark gray'),
    ('message_body', 'light gray', 'black', '', 'light gray', ''),

    ('bufferlist_results_even', 'light gray', 'black', '', '', 'g3'),
    ('bufferlist_results_odd', 'light gray', 'black', '', '', ''),
    ('bufferlist_focus', 'white', 'dark gray', '', '#ffa', 'g38'),

    ('taglist_tag', 'light gray', 'black', '', '', ''),
    ('taglist_focus', 'white', 'dark gray', '', '#ffa', 'g38'),
]
displayed_headers = [
    'From',
    'To',
    'Cc',
    'Bcc',
    'Subject',
]

authors_maxlength = 30


hooks = {
        'pre-shutdown': lambda ui: ui.logger.info('goodbye!'),
        }
