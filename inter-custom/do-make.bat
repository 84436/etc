@ECHO OFF
SETLOCAL

SET FONT_FEATURES_DEFAULT=liga,kern,calt,ccmp
SET FONT_FEATURES_ADDITIONAL=case,cpsp,ss01,ss03,ss04
SET FONT_FEATURES=%FONT_FEATURES_DEFAULT%,%FONT_FEATURES_ADDITIONAL%

(
    CD "input"
    FOR %%i IN (*) DO (
        ECHO %%i
        CALL pdm run pyftfeatfreeze -f %FONT_FEATURES% "%%i" "..\output\%%i"
    )
)

ENDLOCAL
