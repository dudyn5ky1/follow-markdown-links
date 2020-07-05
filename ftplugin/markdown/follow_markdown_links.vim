function s:isCursorOnMarkdownLink()
  let line = getline('.')
  let pos = getpos(".")[2]
  let regex = '\v\[([^\[]+)\](\(.*\))'
  let isLink = matchstrpos(line, regex)
  if isLink[0] != ''
    if pos >= isLink[1]
      if  pos <= isLink[2]
        return 1
      endif
    endif
  endif
  return 0
endfunction

if exists("*FollowLink")
    finish
endif

" --------------------------------
" Add plugin to the path
" --------------------------------
if has('python3')
    python3 import sys
    python3 import vim
    python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

    function! FollowLink()
      if &buftype ==# 'quickfix'
        execute "normal! \<CR>"
      else
        if s:isCursorOnMarkdownLink()
          python3 << endOfPython

from follow_markdown_links import follow_link
follow_link()

endOfPython
        endif
      endif
    endfunction
else " python2
    python import sys
    python import vim
    python sys.path.append(vim.eval('expand("<sfile>:h")'))

    function! FollowLink()
      if s:isCursorOnMarkdownLink()
    python << endOfPython

from follow_markdown_links import follow_link
follow_link()

endOfPython
      endif
    endfunction
endif

command! FollowLink call FollowLink()
autocmd FileType markdown nnoremap <script> <CR> :FollowLink<CR>
autocmd FileType markdown nnoremap <script> <BS> :e#<CR>
