@ECHO OFF
SETLOCAL

SET IMAGE_NAME=Windows IoT Enterprise
SET VERSION_BASE=22631.2428
SET VERSION_TARGET=
SET VERSION_KB=
SET WORKSPACE_DRIVE=Z:

TITLE * Extract Image to Workspace Drive
WIM apply %VERSION_BASE%.wim 2 %WORKSPACE_DRIVE%
:: 1 = Enterprise, 2 = IoT Enterprise
:: Double-check with "wim info" first

TITLE * Add Latest Cumulative Update (%VERSION_KB%)
DISM /Image:%WORKSPACE_DRIVE% /Add-Package ^
    /PackagePath:"%VERSION_KB%-%VERSION_TARGET%.msu"

TITLE * Clean Component Store
DISM /Image:%WORKSPACE_DRIVE% /Cleanup-Image /StartComponentCleanup /ResetBase

TITLE * Capture Workspace Drive as New Image
WIM capture %WORKSPACE_DRIVE% %VERSION_TARGET%.wim ^
    "%IMAGE_NAME% (%VERSION_TARGET%)" ^
    "%IMAGE_NAME% (%VERSION_TARGET%)" ^
    --compress=lzx:100 ^
    --include-integrity
:: Even though LZMS exists, we prefer to use the same compression algorithm
:: for both the image and CompactOS.

TITLE
ENDLOCAL
