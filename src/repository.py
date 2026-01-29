from abc import ABC, abstractmethod
class AccountsRepository(ABC):
    @abstractmethod
    def dave_all(self, account): # pragma: no cover
        pass
    @abstractmethod
    def load_all(self): # pragma: no cover
        pass