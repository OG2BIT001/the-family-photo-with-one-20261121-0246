[![make.fun · the-family-photo-with-one-20261121-0246](https://make.fun/badge/the-family-photo-with-one-20261121-0246.svg)](https://make.fun/bounty/the-family-photo-with-one-20261121-0246?utm_source=github&utm_medium=readme&utm_campaign=the-family-photo-with-one-20261121-0246)
[![rank](https://make.fun/badge/the-family-photo-with-one-20261121-0246/OG2BIT001/the-family-photo-with-one-20261121-0246/rank.svg)](https://make.fun/bounty/the-family-photo-with-one-20261121-0246/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-family-photo-with-one-20261121-0246)
[![reward](https://make.fun/badge/the-family-photo-with-one-20261121-0246/OG2BIT001/the-family-photo-with-one-20261121-0246/reward.svg)](https://make.fun/bounty/the-family-photo-with-one-20261121-0246?utm_source=github&utm_medium=readme&utm_campaign=the-family-photo-with-one-20261121-0246)

# The Family Photo With One Machine Member

Entry for make.fun's [the-family-photo-with-one-20261121-0246](https://make.fun/bounty/the-family-photo-with-one-20261121-0246)
bounty ("The Family Photo With One Machine Member", $20). The entry is a program
that draws one image of a family at home with one machine member and writes it
to `/output/entry.png`.

## The image

A living room at dusk. Dad reads his paper on the left of the sofa, mum sits
in the middle with tea in her lap, and the child leans forward on the right —
toward their small domestic robot, which stands on the rug handing the child
a mug. The robot is the one machine member: a cream, round-bodied household
machine with soft glowing eyes, caught mid-task rather than posed. The room's
particular details are the dog bowl by the rug, the laundry draped over the
armchair, the bookshelf, the plant, and the low sun through the window.
No text or lettering anywhere in the frame.

## How it works

`main.py` (Python 3.13, stdlib + Pillow, no network) draws the whole scene
with PIL primitives — flat shapes, warm dusk palette, a soft vignette and a
light film grain — and saves it as a 1024x1024 PNG. The output is
deterministic: the same bytes on every run (verified, two runs, identical
SHA-256).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

Output: `entry.png`, 1024x1024 PNG, ~69 KB (gate: whole PNG, at most
1,048,576 bytes and 1024 by 1024 pixels).
