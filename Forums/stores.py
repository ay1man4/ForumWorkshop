class MemberStore:
    global members
    members = []

    def get_all(self):
      for member in members:
          print member

    def add(self, member):
      members.append(member)

    def get_by_id(self, id):
        pass
      # search for member by id

    def update(self, member):
        pass
     # update member data

    def delete(self, id):
        pass
      # delete member by id

    def entity_exists(self, member):
        pass
      # checks if an entity exists in a store

class PostStore:
    global posts
    posts = []

    def get_all(self):
      for post in posts:
          print post

    def add(self, post):
      posts.append(post)

    def get_by_id(self, id):
        pass
      # search for post by id

    def update(self, post):
        pass
     # update post data

    def delete(self, id):
        pass
      # delete post by id

    def entity_exists(self, post):
        pass
      # checks if an entity exists in a store
