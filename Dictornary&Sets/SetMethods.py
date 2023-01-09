
b=set()
print(type(b))

b.add(13)
b.add(14)
b.add(12)
# b.add([12,34,45]) we cannot add list in set beacuse list hashable nhi h hm list ke content ko baad me change bhi kr skte ho
b.add((12,34,45)) #but we can add tuples in set
print(len(b)) #length of set
print(b.remove(12))
print(b.pop())
print(b)
c=(1,2,4,6,7,8)
d=(23,2,4,6,123,54)

