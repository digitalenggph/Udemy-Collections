class User:  # PascalCase - all start letters capitalized
    def __init__(self, user_id, username):  # special method
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Karen")


user_1.follow(user_2)

print(f"{user_1.username} following: {user_1.following}")
print(f"{user_2.username} follower: {user_2.followers}")

