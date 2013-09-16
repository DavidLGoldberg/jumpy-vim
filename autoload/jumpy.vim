" NOTE: You must have python support enabled for vim.
if !has('python')
    finish
endif

function! Label()
    pyfile label.py
endfunction

command! JumpyLabel call Label()
