@ECHO OFF
SETLOCAL

SET WORKSPACE_DRIVE=Z:

CD %~DP0

:: Install LaunchBar as the shell
XCOPY /S /E /Y /I LaunchBar %WORKSPACE_DRIVE%\LaunchBar
COPY winpeshl.ini %WORKSPACE_DRIVE%\Windows\System32\winpeshl.ini

:: Copy apps
MKDIR "%WORKSPACE_DRIVE%\Apps"
XCOPY /S /E /Y "Apps" "%WORKSPACE_DRIVE%\Apps"

:: Copy System32 stuff
XCOPY /S /E /Y "System32" "%WORKSPACE_DRIVE%\Windows\System32"

ENDLOCAL
