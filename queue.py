class Queue:
		DEFAULT CAPACITY = 10

		def init (self):
			self._data = [None] ArrayQueue.DEFAULT CAPACITY
			self._size = 0
			self._front = 0

		def len (self):
			return self._size

		def is_empty(self):
			return self._size == 0

		def first_element(self):
			if not self.is_empty():
				return self._data[self._front]

		def dequeue(self):
			if self.is_empty( ):
				print(" Queue is empty" )
			else:
				answer = self._data[self._front]
				self._data[self._front] = None
				self._front = (self._front + 1) % len(self._data)
				self._size −=1
				return answer

		def enqueue(self, e):
			if self._size == len(self._data):
				self.resize(2 len(self._data))
			avail = (self._front + self._size) % len(self._data)
			self._data[avail] = e
			self._size += 1

		def resize(self, cap):
			old = self._data
			self._data = [None]*cap
			walk = self._front
			for k in range(self. size):
				self. data[k] = old[walk]
				walk = (1 + walk) % len(old)
			self. front = 0