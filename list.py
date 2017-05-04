class slist:
	class _node:

		def __init__(self,info):
			self._data=info
			self._next=None

	def __init__(self):
		self._head=None
		self._tail=None
		self._length=0

	def is_empty(self):
		return self._length==0

	def count(self):
		return self._length

	def get_first(self):
		if not self.is_empty():
			return self._head._data

	def add_to_head(self,ele):
		new_node=self._node(ele)
		if not self.is_empty():
			new_node._next=self._head
			self._head=new_node
		else:
			self._head=self._tail=new_node
		self-_length+=1

	def get_last(self):
		if not self.is_empty():
			return self._tail._data

	def add_to_tail(self,ele):
		new_node=self._node(ele)
		if not self.is_empty():
			self._tail._next=new_node
			self._tail=new_node
		else:
			self._head=self._tail=new_node
		self-_length+=1
