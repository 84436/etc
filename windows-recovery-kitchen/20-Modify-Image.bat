@ECHO OFF
SETLOCAL

SET WORKSPACE_DRIVE=Z:

CD %~DP0

:: Install LaunchBar as the shell
XCOPY /S /E /I LaunchBar %WORKSPACE_DRIVE%\LaunchBar
COPY winpeshl.ini %WORKSPACE_DRIVE%\Windows\System32\winpeshl.ini

:: Copy apps
XCOPY /S /E "Program Files" "%WORKSPACE_DRIVE%\Program Files"

ENDLOCAL
