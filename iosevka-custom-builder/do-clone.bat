@ECHO OFF
SETLOCAL

SET ROOT_FOLDER=%~DP0
SET REPO_FOLDER_NAME=repo

CD /D "%ROOT_FOLDER%"
IF EXIST "%REPO_FOLDER_NAME%" (
    ECHO Previous repo clone exists; removing...
    RMDIR /S /Q "%REPO_FOLDER_NAME%"
)

CALL git clone --branch=main --depth=1 "https://github.com/be5invis/Iosevka" "%REPO_FOLDER_NAME%"
COPY private-build-plans.toml "%REPO_FOLDER_NAME%\"
CD "%REPO_FOLDER_NAME%"
CALL git describe --tags

ENDLOCAL
