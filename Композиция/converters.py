from processor import Processor
class Upper(Processor):
	def converter(self,data):
		return data.upper()
if __name__=='__main__':
	import sys
	obj=Upper(sys.stdin,sys.stdout)
	obj.process()
# class HTMLize:
# 	def write(self,line):
# 		print('<PRE>%s<PRE>') % (line.rstrip())

# if __name__=='__main__':
# 	Upper(open('some.txt'),HTMLize()).process()