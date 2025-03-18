from datetime import date


class IUser():
    pass


class Admin(IUser):
    pass


class Moderator(IUser):
    pass


class User(IUser):
    pass


class IHasVote():
    pass


class Tag():
    pass


class Post():
    def __init__(self, author: IUser, date: date, content: str):
        self.author = author
        self.date = date
        self.content = content


class Comment():
    def __init__(self, author: IUser, date: date, content: str):
        self.author = author
        self.date = date
        self.content = content


class ForumDescription():
    pass


class Forum():
    def __init__(self, name: str, mods: list[Moderator]):
        self.name = name
        self.posts: list[Post] = []
        self.mods = mods


class Chat():
    pass


class Notification():
    """
    Joindre et suivre
    """
    pass
