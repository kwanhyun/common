val = "01012341234" # 11자리
# val = "0111231234" 10자리

import re
pattern =r"^01[016789][1-9]\d{6,7}$" #r (raw) escape의 약자
if re.match(pattern,val): #[1-9] = \d 와 동일
    print('matched')
else:
    print('invalid')


"""app 추가시
1. settings.py 에서 app 추가
2. app 하위에 urls.py 생성 후 patterns 코드적용
3. protejct의 urls에 include까지
""
