# Advent of Code \o/

**is this some leaderboarder's highly-optimized, highly-readable solutions?**

nope.

I try to optimize some when I have free time, golf solutions aren't even the best.
do you like code-golfing? check out [this
repo](https://github.com/Starwort/advent-of-golf-2022)!

long, modular solutions are always documented, but rarely (if not at all) unit-tested

**principles**

- no custom library imports (only stdlib)
- each puzzle is **standalone**. they can be run using the standard compiler/interpreter
- standard I/O is used for input and output

**does this have solutions in my favorite programming language?**

take a look at the language usage breakdown, if the git forge you're reading
this from supports it.

if it doesn't support it, then there's a good chance that you're a shell
literate! cook up a oneliner to analyze my file types here...

```sh
find 20?? ! -name '*.md' ! -name '*.txt' -type f | sed 's/.*\.//' | sort | uniq -c | sort -bnr
```

the .jpg files are screenshots of Apple Shortcuts solutions (mostly
2021), so they are in fact valid file types of solutions.

as of writing:
```
  53 py
  15 jpg
  14 fnl
   8 cpp
   7 lua
   2 moon
   2 go
   1 elm
```

**do you have a neat setup for input and submitting?**

yeah, but not exactly neat

- fetching puzzle description - https://github.com/scarvalhojr/aoc-cli
- fetching input and submitting (for python) - https://pypi.org/project/advent-of-code-data/

**do you have a neat script or templates which you use to create new directory structures?**

yup!

check out [bin/new](bin/new)

templates at [skel/](skel/)

**pretend this is actual installable software and document how a user should set it up**

prereqs
- python
- cargo
- any other language you wish to run

install 'dependencies' (lol)
- https://github.com/scarvalhojr/aoc-cli
- set up direnv
  - set `$AOCROOT` to the path to this git repo in the `.envrc` **of the parent dir of the repo**
  - check envs using `bin/new --help`
- create virtualenv
- activate virtualenv
- install from `requirements.txt`
- start solving new puzzles as they come, using `bin/new`

**are you going to (eventually) do all the previous puzzles?**

perhaps.

