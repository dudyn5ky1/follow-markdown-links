# follow-markdown-links

This vim plugin enables browsing through your markdown files by using links
between them (like a personal wiki). You just have to move the cursor to a link
and press ENTER.

This version was tested only using:

- Neovim with python support
- MacOS (open files)

If you are not using neovim or MacOS feel free to open an issue.

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/prashanthellina/follow-markdown-links ~/.vim/bundle/follow-markdown-links`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/prashanthellina/follow-markdown-links'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/prashanthellina/follow-markdown-links'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/prashanthellina/follow-markdown-links'` to .vimrc
  - Run `:PlugInstall`

## Usage

Press ENTER on any part of the link to follow that link

Example of links

- `[Notes](Notes.md)` or `[Notes]()` or `[Notes](Notes)` will open Notes.md
- `[SubNotes](sub/Notes.md)` or `[sub/Notes]()` or `[Notes](sub/Notes)` will open sub/Notes.md (if `sub` directory does not exist, the plugin will prompt for confirmation and create)
- `[Github](https://github.com/izifortune/follow-markdown-links)` will open a new tab on your default browser
- `[Anchor link](#installation)`

You can press BACKSPACE to navigate to previous file (like "e#").

## TODO

- [ ] Make `open` portable outside of MacOS
