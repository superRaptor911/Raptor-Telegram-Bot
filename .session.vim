let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/program/python/telegram-bots/bot1
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +7 main.py
badd +45 State.py
badd +32 botHelpMenu.py
badd +15 games/GameMenu.py
badd +142 games/StonePaperScissors.py
badd +59 raptorTrading/coins.py
badd +1 utility.py
badd +1 games/guessTheWord.py
badd +10 setup.sh
badd +4 botConfig.py
argglobal
%argdel
$argadd main.py
edit main.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '2resize ' . ((&lines * 3 + 22) / 45)
exe 'vert 2resize ' . ((&columns * 1 + 87) / 174)
exe '3resize ' . ((&lines * 3 + 22) / 45)
exe 'vert 3resize ' . ((&columns * 76 + 87) / 174)
argglobal
let s:l = 7 - ((6 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
7
normal! 016|
wincmd w
argglobal
enew
wincmd w
argglobal
enew
wincmd w
exe '2resize ' . ((&lines * 3 + 22) / 45)
exe 'vert 2resize ' . ((&columns * 1 + 87) / 174)
exe '3resize ' . ((&lines * 3 + 22) / 45)
exe 'vert 3resize ' . ((&columns * 76 + 87) / 174)
tabnext 1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOFc
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
