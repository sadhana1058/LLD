from abc import ABC, abstractmethod
from typing import List

# Before: Fat interface bundles three unrelated sets of operations
class UserCRUD(ABC):
    @abstractmethod
    def create_user(self, name: str, email: str):
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> str:
        pass

    @abstractmethod
    def update_user(self, user_id: str, new_email: str):
        pass

    @abstractmethod
    def delete_user(self, user_id: str):
        pass
class AdminControls(ABC):
    @abstractmethod
    def ban_user(self, user_id: str, reason: str):
        pass

    @abstractmethod
    def promote_user(self, user_id: str, role: str):
        pass
class AuditLog(ABC):
    @abstractmethod
    def get_login_history(self, user_id: str) -> List[str]:
        pass

    @abstractmethod
    def get_activity_log(self, user_id: str) -> List[str]:
        pass

class BasicUserService(UserCRUD):
    def create_user(self, name, email):
        print(f"BasicUserService -> Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"BasicUserService -> Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"BasicUserService -> Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"BasicUserService -> Deleting user: {user_id}")

class AdminUserService(UserCRUD,AdminControls):
    def create_user(self, name, email):
        print(f"AdminUserService -> Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"AdminUserService -> Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"AdminUserService -> Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"AdminUserService -> Deleting user: {user_id}")
    def ban_user(self, user_id, reason):
        print(f'AdminUserService -> Banning user {user_id}: {reason}')

    def promote_user(self, user_id, role):
        print(f'AdminUserService -> Promoting user {user_id} to admin')

class FullUserService(UserCRUD,AdminControls,AuditLog):
    def create_user(self, name, email):
        print(f"FullUserService -> Creating user: {name} ({email})")

    def get_user(self, user_id):
        print(f"FullUserService -> Fetching user: {user_id}")
        return f"User-{user_id}"

    def update_user(self, user_id, new_email):
        print(f"FullUserService -> Updating user {user_id} email to {new_email}")

    def delete_user(self, user_id):
        print(f"FullUserService -> Deleting user: {user_id}")
    def ban_user(self, user_id, reason):
        print(f'FullUserService -> Banning user {user_id}: {reason}')

    def promote_user(self, user_id, role):
        print(f'FullUserService -> Promoting user {user_id} to {role}')

    def get_login_history(self, user_id):
        activity = self.get_activity_log(user_id)
        print(f'FullUserService -> Login history for {user_id}: {activity}' )
        

    def get_activity_log(self, user_id):
        return '[2024-01-01, 2024-01-05]'
        

if __name__ == "__main__":
    svc = BasicUserService()
    svc.create_user("Alice", "alice@example.com")
    svc.get_user("u123")
    aus = AdminUserService()
    aus.create_user('Bob','bob@example.com')
    aus.ban_user('u456','spam')
    aus.promote_user('u456','admin')
    fus = FullUserService()
    fus.create_user('Carol','carol@example.com')
    fus.ban_user('u789','abuse')
    fus.get_login_history('u789')



# TODO: Create UserCrud, AdminControls, and AuditLog interfaces.
# TODO: Refactor BasicUserService to implement only UserCrud.
# TODO: Create an AdminUserService that implements UserCrud and AdminControls.
# TODO: Create a FullUserService that implements all three interfaces.