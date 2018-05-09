#人
class Human():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100
	def shot(self,maga,bullet):
		maga.addBullet(bullet)

	def sunandsteel(self,gun,maga):
		gun.addMaga(maga)

	def takeGun(self,gun):
		self.gun = gun

	def openGun(self,diren):
		if diren.hp > 0:
			zidn = self.gun.popGunBullet()
			if zidan:
				zidan.kill(diren)
			else:
				print("没子弹了")

#枪
class Gun():
	def __init__(self,name):
		self.name = name
		self.maga = None

	def addMaga(self,maga):
		self.maga = maga

	def popGunBullet(self):
		return self.maga.popBullet()

#弹夹
class Maga():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []

	def addBullet(self,bullet):
		self.bullet_list.append(bullet)

	def popBullet(self):
		if self.bullet_list:

			return self.bullet_list.pop()
		else:
			return None

#子弹
class Bullet():
	def __init__(self):
		self.weili = 50
	
	def kill(self,diren):
		diren.hp -= self.weili
		if drien.hp <=0:
			diren.hp = 0
			print("%s死了，剩余血量为%d"%(diren.name,diren.hp))
		else:
			print("%s剩余血量为%d"%(diren.name,diren.hp))

laowang = Human("老王")
AWM = Gun("Awm")
maga = Maga(5)
for i in range(5):
	bullet = Bullet()
	laowang.shot(maga,bullet)
laowang.sunandsteel(AWM,maga)
laosong = Human("老宋")
laowang.takeGun(AWM)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
