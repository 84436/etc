@ECHO OFF
SETLOCAL

SET WORKSPACE_DRIVE=Z:

WIM apply WindowsRecovery.original.wim %WORKSPACE_DRIVE%

ENDLOCAL