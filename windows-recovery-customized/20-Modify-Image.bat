@ECHO OFF
SETLOCAL

CD %~DP0

:: Install LaunchBar as the shell
XCOPY /S /E /I LaunchBar Mount\LaunchBar
COPY winpeshl.ini Mount\Windows\System32\winpeshl.ini

:: Copy apps
XCOPY /S /E "Program Files" "Mount\Program Files"

ENDLOCAL
