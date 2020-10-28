"""This is a file to create class to keep track of connected users."""


class Connected:
    """This is a class that creates a list to keep track of connected users."""

    def __init__(self):
        """Init file to hold create the list."""
        self.connected_list = []

    def add_user(self, user_id, user_name):
        """Add user function to put their id and name in the list."""
        self.connected_list.append({"USER_ID": user_id, "USER_NAME": user_name})

    def delete_user(self, user_id):
        """Delete user this is called when user disconnects."""
        for user_list in range(len(self.connected_list)):
            if self.connected_list[user_list]["USER_ID"] == user_id:
                del self.connected_list[user_list]
                break

    def number_of_users(self):
        """Returns the number of users or people online."""
        return len(self.connected_list)

    def check_for_user(self, user_id):
        """Check to see if the user is in list, if yes returns name,
        if not it returns empty string."""
        for user_list in range(len(self.connected_list)):
            if self.connected_list[user_list]["USER_ID"] == user_id:
                user_name = self.connected_list[user_list]["USER_NAME"]
                return user_name
        return ""
