class UserLoginClass:

    username_mapping = {
        "Bob": (0, "Bob", "password"),
        "Rolf": (1, "Rolf", "long4assword"),
        "Jose": (2, "Jose", "bob123"),
        "username": (3, "username", "password")
    }

    def __init__(self) -> None:
        pass

    def login(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input

        try:
            _, username, password = self.username_mapping[self.username_input]

            if self.password_input == password:
                return f"Hello {username}! Your log in!"
            else:
                return "Incorrect password!"
        except KeyError:
            return "Username not found."
