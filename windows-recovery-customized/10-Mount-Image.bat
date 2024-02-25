@ECHO OFF
SETLOCAL

DISM /Mount-Wim ^
    /WimFile:WindowsRecovery.original.wim ^
    /Index:1 ^
    /MountDir:Mount

ENDLOCAL