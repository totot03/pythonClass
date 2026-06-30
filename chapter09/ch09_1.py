# 클래스 설계 (스타크래프트)
# 클래스명은 Unit, 멤버변수: 이름 name , 체력 hp, 공격력 damage, 스피드 speed)

class Unit:
  #생성자
  def __init__(self, name, hp, damage, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print("유닛이름: {0} 체력:{1} 이동속도:{2} 생성완료 ".format(self.name, self.hp, self.damage, self.speed))

# 공격유닛생성 
# 클래스명은 AttackUnit, 멤버변수: name, hp, damage, speed
class AttackUnit:
  #생성자
  def __init__(self, name, hp, damage, speed):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.speed = speed
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

# 보병
soldier1 = AttackUnit("보병1", 40, 5, 10)
soldier2 = AttackUnit("보병2", 40, 5, 10)
soldier3 = AttackUnit("보병3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 130, 35, 20)
tank2 = AttackUnit("탱크2", 130, 35, 20)

# 보병1 공격(10시 방향)
# soldier1.attack(10)
# soldier1.attack(10)
# soldier1.attack(10)
# tank1.attack(10)
# tank2.attack(10)

# 배열관리
attack_list = []
attack_list.append(soldier1)
attack_list.append(soldier2)
attack_list.append(soldier3)
attack_list.append(tank1)
attack_list.append(tank2)

for unit in attack_list:
  unit.attack(10)

# 공격받음 => 반복문을 활용하여 공격받음
# soldier1.damaged(5)
# soldier2.damaged(5)
# soldier3.damaged(5)
# tank1.damaged(10)
# tank2.damaged(10)

for unit in attack_list:
  unit.damaged(10)

# 날아다니면서 공격하는 유닛
# 사용되는 객체가 자신만의 멤버변수를 추가하면, 자기자신에만 해당이 된다.
# 같은 클래스 다른 유닛에는 멤버변수가 추가 되지 않는다.
airunit1 = AttackUnit("전투기", 200, 30, 10)
soldier4 = AttackUnit("보병4", 40, 5, 10)
# 날아다니는 기능(멤버변수로 추가가능)
airunit1.fly = True

if airunit1.fly == True :
  print(f"{airunit1.name} {airunit1.hp} {airunit1.damage} {airunit1.speed} 궁중유닛: {airunit1.fly}")

# if soldier4.fly == True :
#   print(f"{soldier4.name} {soldier4.hp} {soldier4.damage} {soldier4.speed} 궁중유닛: {soldier4.fly}")
# else:
#   print(f"{soldier4.name} {soldier4.hp} {soldier4.damage} {soldier4.speed}")

