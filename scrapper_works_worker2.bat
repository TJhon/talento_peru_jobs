@echo off
python works.py --n_reg 12 13 14 16 17 18 19 20 21 22 23 24 25
set today=%date%
git add -A
git commit -m "Data worker 2 %today%"
git push 