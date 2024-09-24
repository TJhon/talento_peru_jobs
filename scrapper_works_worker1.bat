@echo off
python works.py --n_reg 1 2 3 4 5 6 7 8 9 10 11 12
set today=%date%
git add -A
git commit -m "Data worker 1 %today%"
git push -u origin testing_page