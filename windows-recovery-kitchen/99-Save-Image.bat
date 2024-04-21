@ECHO OFF
SETLOCAL

SET WORKSPACE_DRIVE=Z:

WIM capture %WORKSPACE_DRIVE% WindowsRecovery.wim ^
    "Microsoft Windows Recovery Environment (amd64)" ^
    "Microsoft Windows Recovery Environment (amd64)" ^
    --boot ^
    --compress=lzx:100

ENDLOCAL
