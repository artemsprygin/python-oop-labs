class Super:
	def method(self): 
		pass
class Tool:
	def __method(self): # Получит имя _Tool__method
		pass
def other(self): # Используется внутренний метод
	self.__method()
class Sub1(Tool, Super): 
	pass
	def actions(self): 
		self.method() # Вызовет метод Super.method
class Sub2(Tool):
	def __init__(self): 
		self.method = 99 # Не уничтожит метод Tool.__method