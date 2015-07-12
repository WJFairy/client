ntsd -c q -pn run.exe
del 新客户端测试系统.exe /F /S /Q

cd C:\workspace\web

xcopy action dist\action /E /Y /F /I
xcopy template dist\template /E /Y /F /I
xcopy static dist\static /E /Y /F /I
xcopy utest dist\utest /E /Y /F /I
xcopy mvc dist\mvc /I /T /Y
copy mvc\settings.py dist\mvc\settings.py /Y
copy settings.py dist\settings.py
python setup.py py2exe

xcopy C:\workspace\web\dist C:\pack\client\lib_w  /E /Y /F /I

pause
