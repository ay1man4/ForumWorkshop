class MemberStore:
    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_by_id(self, id):
        for member in MemberStore.members:
            if member.id == id:
                return member
        return None

    def update(self, member):
        pass
        # update member data

    def delete(self, id):
        member = self.get_by_id(id)
        if member is not None:
            MemberStore.members.remove(member)

    def entity_exists(self, member):
        if member is not None:
            return member in MemberStore.members


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
