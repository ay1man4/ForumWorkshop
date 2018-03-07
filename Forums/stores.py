class MemberStore:
    members = []

    def get_all(self):
      return MemberStore.members

    def add(self, member):
      MemberStore.members.append(member)

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
    posts = []

    def get_all(self):
      return PostStore.posts

    def add(self, post):
      PostStore.posts.append(post)

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
