# pylint: disable=R0903
'''Hash Table module'''

class HashTableIterator:
    '''Hash Table iterator class'''
    def __init__(self, table):
        self._table = table
        self._prev_h = 0
        self._prev_c = -1

    def __next__(self):
        while self._prev_h < len(self._table):
            for i in range(self._prev_c + 1, len(self._table.table()[self._prev_h])):
                self._prev_c = i
                return self._table.table()[self._prev_h][i]
            self._prev_h += 1
            self._prev_c = -1
        raise StopIteration

class HashTable:
    '''Hash Table iterator class'''
    def __init__(self, array, mod=10 ** 5 + 1303):
        self._mod = mod
        self._table = [[] for i in range(mod)]
        for i in array:
            self.add(i)

    def add(self, val):
        '''Add'''
        if val in self:
            return
        hash_val = hash(val) % self._mod
        self._table[hash_val].append(val)

    def delete(self, val):
        '''Delete'''
        hash_val = hash(val) % self._mod
        try:
            self._table[hash_val].remove(val)
        except:
            raise Exception("Delete non-existing value")

    def __contains__(self, val):
        hash_val = hash(val) % self._mod
        return val in self._table[hash_val]

    def __len__(self):
        return self._mod

    def table(self):
        '''Table'''
        return self._table

    def __iter__(self):
        return HashTableIterator(self)
