" answers.md
let puzzlefile = expand("%:p")
let dir = strtrans(substitute(system('dirname '.puzzlefile), '\n\+$', '', ''))
exec 'e '.dir.'/answers.md'
normal ggdG
" set ma
set buftype=
exec 'r '.puzzlefile

v/^Your puzzle answer was/d
normal ggdt`xjdt`x$xxk$xx
w
bd

" puzzle.md
g/^Your puzzle answer was/d

g/^Both parts of this puzzle/normal! dG

%s/\n\n```/\r```/g

%s/`\*\(.\{-}\)\*`/*`\1`*/
%s/\*\(.\{-}\)\*/**\1**/g
