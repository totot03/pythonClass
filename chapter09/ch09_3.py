# 다중상속 진행한다. (모호성을 해결하는 방법을 구현한다.)
class Unit:
  #생성자
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    # print("유닛이름: {0} 체력:{1} 이동속도:{2} 생성완료 ".format(self.name, self.hp, self.damage, self.speed))
  def move(self,  location):
    print("[지상 유닛 이동]")
    print(f"{self.name}유닛이 체력:{self.hp}, {location} 방향으로 이동중")

  def move(self, location):
    print(f"{self.name} 지상유닛이 {location} 방향으로 가고 있습니다.")


    # 공격유닛생성 
# 클래스명은 AttackUnit, 멤버변수: name, hp, damage, speed
class AttackUnit(Unit):
  #생성자
  def __init__(self, name, hp, speed, damage ):
    # 부모생성자를 책임을 진다.
    Unit.__init__(self, name, hp, speed)
    self.damage = damage
    print(f"{self.name} 유닛이 체력:{self.hp}, 공격력:{self.damage}, 이동속도:{self.speed} 유닛이 생성됨")

  # 멤버함수(공격함수)
  def attack(self,location):
    print(f"{self.name}가 {location} 시 방향으로 공격력{self.damage} 으로 공격하고 있습니다.")

   # 멤버함수(공격을 당하는 함수)
  def damaged(self, damage):
    print(f"{self.name} 상대방으로 부터 공격력{damage}으로 공격을 받고 있습니다.")
    self.hp = self.hp - damage
    print(f"{self.name} 공격을 받아서 남아있는 체력{self.hp}입니다.")
    if self.hp <= 0:
      print(f"{self.name} 유닛은 파괴되었습니다.")

# 공중 유무 유닛
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

  # 멤버함수
  def fly(self, name, location):
    print(f"{name} 유닛이 {self.flying_speed}로 {location} 방향으로 날아가고 있습니다.")

# 다중상속 (지상공격유닛, 공중유무 유닛)
class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, speed, damage, flying_speed):
    AttackUnit.__init__(self, name, hp, speed, damage)
    Flyable.__init__(self, flying_speed)
  
  # 오버라이딩
  def move(self, location):
    print(f"{self.name} 공격유닛이 {location} 방향으로 {self.flying_speed}속도로 날아가고 있습니다.")

# 공격기능을 가진 interceptor 객체생성

intercepter = FlyableAttackUnit("요격기", 300, 0, 80, 200)
# intercepter.attack("2시방향")
# intercepter.damaged(60)
# intercepter.fly(intercepter.name, "4시")
intercepter.move("3시")