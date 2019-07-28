https://git-scm.com/download/win

에서 git을 다운로드 받고 설치를 한다.

next만 계속 누르면 설치됨.

-----------------------------------------

http://www.github.com 에 가입한다.

새로운 저장소(Repository)를 만든다.
new Repository -> myPy

------------------------------------------------------

cmd[enter] - console 

cd c:\Users\esther\Desktop\myPy
cd : (change directory - 디렉토리(폴더)를 바꾼다.)
\ : 역슬래시

dir :해당디렉토리에 있는 파일 목록을 본다.

----------------------------------------
git을 설치한 후 한번 명령하면 된다.

git config --global user.name "esther Kim"
git config --global user.email esther4185@gmail.com

---------------------------------------
저장소에서 처음 만들었을때만 아래와 같이 실행
콘솔에서 C:\Users\esther\Desktop\myPy
디렉토리로 이동한 후 아래와 같이 명령을 실행한다.

git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/esther1104/myPy.git
git push -u origin master

---------------------------------------------
myPy디렉토리의 내용이 변경되었을 때 실행
콘솔에서 C:\Users\esther\Desktop\myPy
로 이동

git add .
git commit -m "fix codes"
git push



