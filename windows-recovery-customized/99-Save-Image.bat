@ECHO OFF
SETLOCAL

DISM /Capture-Image ^
    /ImageFile:WindowsRecovery.wim ^
    /CaptureDir:Mount ^
    /Name:"Microsoft Windows Recovery Environment (amd64)" ^
    /Description:"Microsoft Windows Recovery Environment (amd64)" ^
    /Compress:max ^
    /Bootable ^
    /CheckIntegrity /Verify

ENDLOCAL