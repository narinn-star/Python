#모듈 사용 방법

#mymod.py 모듈이 있고 가정. 이 모튤을 import 해서 사용할 수 있는 방법

#1. sys 모듈 사용
# import sys
# sys.path.append("c:디렉터리 명")
# import mymod

#2. PYTHONPATH 환경 변수 사용
# \Users\home>set PYTHONPATH=c:디렉터리 명
# \Users\home>python
# import mymod

#3. 현재 디렉터리 사용
# \Users\home>cd c:디렉터리 명
# \디렉터리>python
# import mymod