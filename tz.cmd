set f=%1
echo %f%
pause
set t=%date:~1,8%
echo %t%

set g="GitHub\my\sim\game\设计思路\txt"
For /f "tokens=5,55 delims=\" %i in (%g%) do echo %i
For /f "tokens=7,55 delims=\" %i in (%g%) do echo %i
For /f "tokens=8,55 delims=\" %i in (%g%) do echo %i
For /f "tokens=11,55 delims=\" %i in (%g%) do echo %i
For /f "tokens=5,6,7 delims=\" %i in (%g%) do echo %i %j %k
For /f %i in (%g%) do echo %i

For /f "delims=\" %i in (%g%) do (
set v=%i
echo %v%  )

For /f "tokens=5 delims=\" %i in (%g%) do echo %i
pause