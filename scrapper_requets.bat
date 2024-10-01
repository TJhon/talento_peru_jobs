@echo off
python main.py
set today=%date%
git add -A
git commit -m "Data with requets %today%"
git push 