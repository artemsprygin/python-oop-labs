class wrapper:
	def __init__(self, object):
		self.wrapped = object 
	def __getattr__(self, attrname):
		print('Trace:', attrname) 
		return getattr(self.wrapped, attrname)

# x=wrapper([1,2,3])
# x.append(4)
# print(x.wrapped)
# # x=wrapper()
# xy=wrapper({'a':0,'b':1})
# xy.keys()