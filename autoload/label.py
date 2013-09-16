import vim

def label_line(line):
    return line + "Yo!"

#vim.command('setlocal modifiable')
# stuff
#vim.command('setlocal nomodifiable')

vim.current.buffer[:] = [label_line(line) for line in vim.current.buffer]

vim.command('highlight Labels ctermbg=green guibg=green')
vim.command('let m = matchadd("Labels", "\\\w\\\{2,}")')
