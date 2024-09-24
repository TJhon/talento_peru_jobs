@echo off
python works.py --n_reg 15
set today=%date%
git add -A
git commit -m "Data worker 3 - Lima %today%"
git push -u origin testing_page