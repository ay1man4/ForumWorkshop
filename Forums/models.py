class Member:
    last_id = 0
    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age

    def __str__(self):
        return "[%d]: %s, %d years" % (self.id, self.name, self.age)

class Post:
    def __init__(self, member, title, content):
        self. member = member
        self.title = title
        self.content = content

    def __str__(self):
        return "%s: [%s] -> [%s]" % (self.member.name, self.title, self.content)
