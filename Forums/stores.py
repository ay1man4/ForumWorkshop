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
        return self.get_by_id(member.id) is not None


class PostStore:
    posts = []

    def get_all(self):
        return PostStore.posts


    def add(self, post):
        PostStore.posts.append(post)


    def get_by_id(self, id):
        for post in PostStore.posts:
            if post.id == id:
                return post
        return None


    def update(self, post):
        pass
        # update post data

    def delete(self, id):
        post = self.get_by_id(id)
        if post is not None:
            PostStore.posts.remove(post)


    def entity_exists(self, post):
        if self.get_by_id(post.id) is not None
