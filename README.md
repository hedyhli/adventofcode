# Advent of Code \o/

**is this some leaderboarder's highly-optimized, highly-readable solutions?**

nope.

I try to optimize some when I have free time, golf solutions aren't even the best.
do you like code-golfing? check out [this
repo](https://github.com/Starwort/advent-of-golf-2022)!

long, modular solutions are always documented, but rarely (if not at all) unit-tested

**does this have solutions in your favorite programming language?**

take a look at the language usage breakdown, if the git forge you're reading
this from supports it.

if it doesn't support it, then there's a good chance that you're a shell
literate! cook up a oneliner to analyze my file types here...

```sh
find 20?? ! -name '*.md' ! -name '*.txt' -type f | sed 's/.*\.//' | sort | uniq -c | sort -bnr
```

😉

I'm sure you'll find ways to improve mine

the .jpg files are probably screenshots of Apple Shortcuts solutions (mostly
2021), so they are in fact valid file types of solutions.

**do I have a neat setup for input and submitting?**

yeah, but not exactly neat

- fetching puzzle description - https://github.com/scarvalhojr/aoc-cli
- fetching input and submitting (for python) - https://pypi.org/project/advent-of-code-data/

**do I have a neat script or templates which I use to create new directory structures?**

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

**am I going to (eventually) do all the previous puzzles I had missed?**

perhaps.

<details>
<summary>the plan (in addition to 2022+ daily)</summary>

- [x] 2020 (python) days 1-5
- [ ] 2020 (python) days 6-10
- [ ] 2020 (python) days 11-15
- [ ] 2021 (python) days 1-5
- [ ] 2020 (golang) days 1-5
- [ ] 2020 (golang) days 6-10
- [ ] 2020 (golang) days 11-15
- [ ] 2021 (golang) days 1-5
- [ ] 2021 (shell) days 1-5
- [ ] 2020 (java) days 1-5
- [ ] 2021 (python) days 6-10
- [ ] 2021 (python) days 11-15
- [ ] 2021 (golang) days 6-10
- [ ] 2021 (golang) days 11-15
- [ ] 2020 (shell) days 1-5
- [ ] 2020 (lua) days 1-5
- [ ] 2021 (lua) days 1-5

- [ ] 2020 (python) days 16-20
- [ ] 2020 (golang) days 16-20
- [ ] 2020 (python) days 20-25
- [ ] 2020 (java) days 16-20
- [ ] 2020 (golang) days 20-25


wow, you're still reading?

</details>
