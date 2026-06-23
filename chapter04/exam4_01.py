# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com 
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 (nav) (5) 
# (1) (!)
# 예) 생성된 비밀번호 : nav51!

# pw = "http://naver.com"
# pw2 = (pw.replace("http://", ""))
# print(pw2)
# print(pw2[0:5])
# pw3 = pw2[0:5]
# pw4 = ((pw2[0:3]) + (pw2.count("pw3"))  )

url = "http://google.com"
url1 = url.replace("http://", "")  # naver.com
find = url1.find(".")              # 5
url2 = (url1[:find])               # naver
password = url2[:3]+str(len(url2)) + str(url2.count("e")) + "!" 
print(f"생성된 비밀번호는 : {password}")