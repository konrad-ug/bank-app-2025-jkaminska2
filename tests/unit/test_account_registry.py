from src.account import Account, AccountRegistry

class TestAccountRegistry:
    def test_accounts(self):
        registry = AccountRegistry()
        acc = Account("John", "Doe", "93857264539", None, 5000)
        registry.add_account(acc)
        assert registry.search_account("93857264539").first_name == "John"
        assert registry.search_account("93857264530") is None
        assert registry.accounts_counter() == 1
        assert registry.accounts_list() == [acc]