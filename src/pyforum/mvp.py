from datetime import date

### Écrire une REPL ###


class IUser():
    pass


# class Moderator(IUser):
#     pass


class User(IUser):
    pass


# class IHasVote():
#     pass


# class Tag():
#     pass


class Post():
    def __init__(self, author: IUser, date: date, content: str):
        self.author = author
        self.date = date
        self.content = content

    def to_dict(self):
        return {
            "author": self.author,
            "date": self.date,
            "content": self.content
        }


class BD():
    def enregister_utilisateur(self, user: IUser):
        pass

    def enregister_post(self, post: Post):
        pass

    def enregister_comment(self, comment: Comment):
        pass


class Comment():
    def __init__(self, author: IUser, date: date, content: str):
        self.author = author
        self.date = date
        self.content = content


# class ForumDescription():
#     pass


class Forum():
    def __init__(self, name: str, mods: list[Moderator]):
        self.name = name
        self.posts: list[Post] = []
        self.mods = mods

    def ajouter_post(self, *posts_info) -> Post:
        pass

    def supprimer_post(self, post_id) -> None:
        pass


# class Chat():
#     pass


# class Notification():
#     """
#     Joindre et suivre
#     """
#     pass
