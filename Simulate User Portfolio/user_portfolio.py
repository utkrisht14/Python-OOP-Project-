import random

class PortfolioManager:
    def __init__(self):
        self.accounts = {}

    def add_account(self, investment_account):
        while True:
            new_acc_id = f"ACC{random.randint(100000, 999999)}"
            if new_acc_id not in self.accounts:
                investment_account.account_id = new_acc_id
                self.accounts[new_acc_id] = investment_account
                return new_acc_id

    def remove_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]

    def get_total_portfolio_value(self):
        total_value = sum(account.calculate_account_value() for account in self.accounts.values())
        return total_value

    def generate_portfolio_report(self):
        for account_id, account in self.accounts.items():
            print(f"\nReport for Account: {account_id} - {account.account_name}")
            account.get_asset_allocation_breakdown()
            print(f"Total Account Value: {account.calculate_account_value()}")


class InvestmentAccount:
    def __init__(self, account_id=None, account_name="", assets=None):
        self.account_id = account_id
        self.account_name = account_name
        self.assets = assets if assets else []

    def add_asset(self, asset):
        self.assets.append(asset)

    def remove_asset(self, asset_id):
        self.assets = [asset for asset in self.assets if asset.asset_id != asset_id]

    def calculate_account_value(self):
        return sum(asset.get_value() for asset in self.assets)

    def get_asset_allocation_breakdown(self):
        for asset in self.assets:
            print(f"{asset.name} ({asset.__class__.__name__}): {asset.get_value()}")


class Asset:
    def __init__(self, asset_id, name, quantity, current_price):
        self.asset_id = asset_id
        self.name = name
        self.quantity = quantity
        self.current_price = current_price

    def get_value(self):
        return self.quantity * self.current_price

    def get_details(self):
        return f"{self.name}: {self.quantity} units @ {self.current_price} each = {self.get_value()}"


class StockAsset(Asset):
    def __init__(self, asset_id, name, quantity, current_price, ticker_symbol, exchange):
        super().__init__(asset_id, name, quantity, current_price)
        self.ticker_symbol = ticker_symbol
        self.exchange = exchange


class MutualFundAsset(Asset):
    def __init__(self, asset_id, name, quantity, current_price, fund_manager, expense_ratio):
        super().__init__(asset_id, name, quantity, current_price)
        self.fund_manager = fund_manager
        self.expense_ratio = expense_ratio


class CryptoAsset(Asset):
    def __init__(self, asset_id, name, quantity, current_price, coin_type, wallet_address):
        super().__init__(asset_id, name, quantity, current_price)
        self.coin_type = coin_type
        self.wallet_address = wallet_address


class Transaction:
    def __init__(self, transaction_id, txn_type, asset_id, quantity, price, date):
        self.transaction_id = transaction_id
        self.txn_type = txn_type
        self.asset_id = asset_id
        self.quantity = quantity
        self.price = price
        self.date = date

    def get_transaction_summary(self):
        return f"{self.txn_type.title()} {self.quantity} of {self.asset_id} at {self.price} on {self.date}"


class ReportGenerator:
    def generate_summary_report(self, account):
        print(f"Summary for {account.account_name}:")
        print(f"Total Value: {account.calculate_account_value()}")

    def generate_detailed_asset_report(self, account):
        print(f"Detailed Asset Report for {account.account_name}:")
        for asset in account.assets:
            print(asset.get_details())


# Example usage
portfolio_manager = PortfolioManager()

account = InvestmentAccount(account_name="My Investment Account")
account.add_asset(StockAsset("AST001", "Apple Inc.", 10, 190.00, "AAPL", "NASDAQ"))
account.add_asset(MutualFundAsset("AST002", "Vanguard 500", 5, 420.50, "Vanguard", 0.04))
account.add_asset(CryptoAsset("AST003", "Ethereum", 2.5, 3400.00, "ETH", "0xWallet"))

portfolio_manager.add_account(account)
portfolio_manager.generate_portfolio_report()
