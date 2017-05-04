class LimitedStack:
		stack_capacity=10
		
		def __init__(self):
			self._data=[None]*LimitedStack.stack_capacity
			self._count=0
		
		def stack_length(self):
			return self._count

		def stack_empty(self):
			return self._count==0

		def stack_full(self):
			return self._count==LimitedStack.stack_capacity

		def stack_push(self,key):
			if not self.stack_full():
				self._data.append(key)
				self._count+=1

		def stack_pop(self):
			if not self.stack_empty():
				self._count-=1
				return self._data.pop()

		def stack_peek(self):
			if not self.stack_empty():
				return self._data[-1]


from stack import lt.stack
def test_empty_stack():
	s1=ltstack.LimitedStack()
	assert(s1.stack_length()==0)
	assert(s1.stack_empty())
test_empty_stack()