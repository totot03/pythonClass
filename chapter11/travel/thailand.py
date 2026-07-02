# 클래스 모듈 생성
class ThailandModule:
  # __init__ 설정하지 않으면 자동으로 디폴트 생성자 만들어짐

  # 멤버함수
  def detail_travel(self):
    print("태국[4박 5일 패키지] 방콕, 파타야, 해변, 야시장, 커피투어, 쌀국수맛집 : 40만원")

# 현재 모듈을 생성를 했는데 테스트해서 잘 진행이 되는지 테스팅
if __name__ == "__main__":
    print("현재 여기가 ThailandModule 모듈 위치야.")
    test_obj = ThailandModule()
    test_obj.detail_travel()
else: # 외부에서 모듈을 불러다 사용하겠다.
    print("당신은 ThailandModule 모듈을 외부에서 호출하고 사용중입니다.")