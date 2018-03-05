import models

member1 = models.Member("Ayman", 34)
member2 = models.Member("Azhar", 19)

post1 = models.Post(member1, "Title 1", "Content 1 Content 1 Content 1")
post2 = models.Post(member1, "Title 2", "Content 2 Content 2 Content 2")
post3 = models.Post(member2, "Title 3", "Content 3 Content 3 Content 3")

print member1.name
print member2.name

print post1.member.name + ": [" + post1.title + "] " + post1.content
print post2.member.name + ": [" + post2.title + "] " + post2.content
print post3.member.name + ": [" + post3.title + "] " + post3.content
