@echo off
for %%i in (in_para*.py) do (
  echo | set /p dummy=%%i :
  python %%i
)