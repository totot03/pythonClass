# 상속

# 일반유닛
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

nurse1 = Unit("간호사1", 40, 5)
nurse2 = Unit("간호사1", 40, 5)

    # 공격유닛생성 
# 클래스명은 AttackUnit, 멤버변수: name, hp, damage, speed
class AttackUnit(Unit):
  #생성자
  def __init__(self, name, hp, damage, speed):
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
  
  # 오버라이딩
  def move(self, location):
    print("[지상 유닛 이동]")
    print(f"{self.name}유닛이 체력:{self.hp}, 공격력:{self.damage}, {location} 방향으로 이동중")

# 보병, 탱크 유닛을 생성
soldier1 = AttackUnit("보병1", 40, 5, 10)
soldier2 = AttackUnit("보병2", 40, 5, 10)
soldier3 = AttackUnit("보병3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 130, 35, 20)
tank2 = AttackUnit("탱크2", 130, 35, 20)

attack_unit = []
attack_unit.append(soldier1)
attack_unit.append(soldier2)
attack_unit.append(soldier3)
attack_unit.append(tank1)
attack_unit.append(tank2)

# 5개 유닛을 반복문을 이용해서 공격처리
for unit in attack_unit:
  unit.attack(2)
  unit.move(10)

# 5개 유닛을 반복문을 이용해서 공격받기 처리
# for unit in attack_unit:
#   unit.damaged(10)

# 상속(오버라이딩과 다형성구현 이 가장 중요한 개념이다.)