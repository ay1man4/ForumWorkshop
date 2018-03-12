import models
import stores

member1 = models.Member("Ayman", 34)
member2 = models.Member("Azhar", 19)
member3 = models.Member("Yososf", 38)

post1 = models.Post(member1, "Title 1", "Content 1 Content 1 Content 1")
post2 = models.Post(member1, "Title 2", "Content 2 Content 2 Content 2")
post3 = models.Post(member2, "Title 3", "Content 3 Content 3 Content 3")

print member1
print member2
print member3

print post1
print post2
print post3

store1 = stores.MemberStore()
store1.add(member1)
store1.add(member2)
store1.add(member3)

member_store1 = store1.get_all()
for m in member_store1:
    print m

print store1.get_by_id(1)
print store1.entity_exists(member3)

store1.delete(2)
print store1.get_by_id(2)
print store1.entity_exists(member2)
