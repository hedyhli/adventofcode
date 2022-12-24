" answers.md
let puzzlefile = expand("%:p")
let dir = strtrans(substitute(system('dirname '.puzzlefile), '\n\+$', '', ''))
exec 'e '.dir.'/answers.md'
" set ma
set buftype=
exec 'r '.puzzlefile

v/answer was/d
%s/.*answer was `\(.*\)`.*/\1
w
bd

" puzzle.md
g/answer was/d
g/this puzzle are complete!/normal dGdd
%s/\n\n```\n\n/\r```\r\r/g
