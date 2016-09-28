; -- Example1.iss --
; Demonstrates copying 3 files and creating an icon.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=A 1D Game
AppVersion=1.0
DefaultDirName={pf}\1DGame
Compression=lzma2
SolidCompression=yes
OutputDir=Output

[Files]
Source: "dist\*"; DestDir:"{app}"; Excludes: "*.exe"; Flags: recursesubdirs
Source: "dist\GameChar.exe"; DestDir:"{app}"
Source: "dist\vcredist_x86.exe"; DestDir:"{app}"; AfterInstall: RunOtherInstaller


[Code]
procedure RunOtherInstaller;
var
  ResultCode: Integer;
begin
  if not Exec(ExpandConstant('{app}\vcredist_x86.exe'),'','',SW_SHOWNORMAL, ewWaitUntilTerminated, ResultCode)
  then
    MsgBox('Other installer failed to run!'+#13#10+SysErrorMessage(ResultCode),mbError,MB_OK);
  end;