class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s, %d years" % (self.name, self.age)

class Post:
    def __init__(self, member, title, content):
        self. member = member
        self.title = title
        self.content = content

    def __str__(self):
        return "%s: [%s] -> [%s]" % (self.member.name, self.title, self.content)
