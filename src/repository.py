from abc import ABC, abstractmethod
class AccountsRepository(ABC):
    @abstractmethod
    def dave_all(self, account):
        pass
    @abstractmethod
    def load_all(self):
        pass