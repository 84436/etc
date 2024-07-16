@ECHO OFF
SETLOCAL

SET WORKSPACE_DRIVE=Z:

WIM capture %WORKSPACE_DRIVE% WindowsRecoveryMod.wim ^
    "Microsoft Windows Recovery Environment (amd64)" ^
    "Microsoft Windows Recovery Environment (amd64)" ^
    --boot ^
    --compress=lzx:100

ENDLOCAL
