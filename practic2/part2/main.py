class Dictionary(object):
    def __init__(self, SZ, hashf=0):
        self.hashTable = [[]] * SZ
        self.SZ = SZ
        self.hashf = hashf

    def size(self):
        size = 0
        for i in range(self.SZ):
            if self.hashTable[i] != []:
                size += 1
        return size

    def hashF1(self, key):  # метод деления
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.SZ

    def set(self, key, value):
        if (self.hashf == 0):
            id = self.hashF1(key)
        else:
            id = self.hashf(self.SZ, key)

        if (self.hashTable[id] != []):
            if self.hashTable[id][0] != key:
                for i in range(self.SZ):
                    if self.hashTable[i] == []:
                        id = i
                        break
                    else:
                        if self.hashTable[i][0] == key:
                            id = i
                            break

        self.hashTable[id] = [key, value]

    def get(self, key):
        if (self.hashf == 0):
            id = self.hashF1(key)
        else:
            id = self.hashf(self.SZ, key)

        if self.hashTable[id] == []:
            return ''
        if (self.hashTable[id][0] != key):
            for i in range(self.SZ):
                if self.hashTable[i] != []:
                    if self.hashTable[i][0] == key:
                        id = i
                        break

        return self.hashTable[id][1]
