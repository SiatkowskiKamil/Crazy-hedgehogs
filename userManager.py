class UserLoginClass:

    current_username = None
    log = False

    username_mapping = {
        "Bob": (0, "Bob", "password"),
        "Rolf": (1, "Rolf", "long4assword"),
        "Jose": (2, "Jose", "bob123"),
        "username": (3, "username", "password"),
        "Kamil": (4, "Kamil", "qwe123")
    }

    def __init__(self):
        self.username_input = None
        self.password_input = None

    def login(self, username_input, password_input):
        self.username_input = username_input
        self.password_input = password_input

        try:
            _, username, password = self.username_mapping[self.username_input]

            if self.password_input == password:
                self.log = True
                self.current_username = username
                return f"{self.current_username} log in!",
            else:
                return "Login failure"
        except KeyError:
            return "Username not found."
