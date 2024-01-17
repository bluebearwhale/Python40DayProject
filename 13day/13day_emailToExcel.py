import re

test_string="""
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""
#정규표현식 사용
results=re.findall(r'[\w\.-]+@[\w\.-]+',test_string)
print(results)
#중복 내용 제거 코드
results=list(set(results))
print(results)
