import os
import re
import webbrowser
import subprocess

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import vim

DEFAULT_EXTENSION = 'md'
MAX_LINE_LEN = 1024

def _extract_link_under_cursor():
    _, col = vim.current.window.cursor
    line = vim.current.line

    # skip long lines to stop hogging CPU in vim
    if len(line) >= MAX_LINE_LEN:
        return

    # find the markdown link substring from line
    start_pos = line.rfind("(")
    if start_pos < 0: return

    end_pos = line.rfind(")")
    if end_pos < 0: return

    start_pos += 1

    link = line[start_pos:end_pos]
    return link

def _is_local_link(link):
    link = urlparse(link)
    return not link.netloc

def _resolve_link(link):
    buf_path = os.path.dirname(vim.current.buffer.name)
    return os.path.join(buf_path, link)

def _ensure_extension(link):
    filename, extension = os.path.splitext(link)
    if extension == '':
        return link + '.' + DEFAULT_EXTENSION
    return link

def _transform_spaces(link):
    return link.replace('%20', ' ')

def follow_link():
    link = _extract_link_under_cursor()
    if not link: return

    # extract link text and link url
    # link = re.findall(r'^\[([^]]*)\]\(([^)]*)\)$', link)
    # if not link: return

    # if not local link then stop
    # text, link = link[0]
    if not _is_local_link(link):
        webbrowser.open_new_tab(link)
        return

    original_link = link
    # Support [Text]() cases; Assume Text as link
    # Also assume default extension
    # if not link: link = text
    link = _ensure_extension(link)

    # Resolve link (if relative) with relation
    # to current file in buffer
    link = _resolve_link(link)

    # Transform %20 to spaces
    link = _transform_spaces(link)

    # Use open for file links
    filename, extension = os.path.splitext(link)
    if extension != '.md':
        subprocess.call(['open', link])
        return

    # Go to header if contains #
    if '#' in link:
        return vim.command('call mkdx#JumpToHeader()')
    # Open if exists
    if os.path.exists(link):
        return vim.command('e %s' % link)

    # Directory path does not exist. Ask user to create it.
    dirpath = os.path.dirname(link)
    if not os.path.exists(dirpath):
        msg = '"%s" does not exist. create? ' % dirpath
        vim.command('let result = input(\'%s\', \'Yes\')' % msg)
        result = vim.eval('result')
        if result != 'Yes': return
        os.makedirs(dirpath)

    # TODO add the markdown link name as title
    # Open as new file
    return vim.command('e %s' % link)
