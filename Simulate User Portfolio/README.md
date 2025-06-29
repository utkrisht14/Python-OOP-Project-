# Personal Investment Portfolio Tracker

A Python-based Object-Oriented Programming (OOP) project that simulates a personal investment portfolio tracker. This project uses composition to manage investment accounts, track various types of assets (stocks, mutual funds, cryptocurrencies), and generate reports.

---

## Features
- Create and manage multiple investment accounts.
- Add and remove different types of assets:
  - **StockAsset**
  - **MutualFundAsset**
  - **CryptoAsset**
- Track total account value.
- Print detailed asset breakdown.
- Generate summary and detailed reports using a report generator.

---

## Class Overview

### `PortfolioManager`
- Manages multiple `InvestmentAccount` instances.
- Methods:
  - `add_account(account)`
  - `remove_account(account_id)`
  - `get_total_portfolio_value()`
  - `generate_portfolio_report()`

### `InvestmentAccount`
- Represents a single investment account with a list of assets.
- Methods:
  - `add_asset(asset)`
  - `remove_asset(asset_id)`
  - `calculate_account_value()`
  - `get_asset_allocation_breakdown()`

### `Asset` (Base Class)
- Common attributes: `asset_id`, `name`, `quantity`, `current_price`
- Subclasses:
  - `StockAsset`
  - `MutualFundAsset`
  - `CryptoAsset`

### `Transaction`
- Represents a buy/sell event of an asset.

### `ReportGenerator`
- Generates account reports.

---

## Sample Usage
```python
portfolio_manager = PortfolioManager()

account = InvestmentAccount(account_name="My Investment Account")
account.add_asset(StockAsset("AST001", "Apple Inc.", 10, 190.00, "AAPL", "NASDAQ"))
account.add_asset(MutualFundAsset("AST002", "Vanguard 500", 5, 420.50, "Vanguard", 0.04))
account.add_asset(CryptoAsset("AST003", "Ethereum", 2.5, 3400.00, "ETH", "0xWallet"))

portfolio_manager.add_account(account)
portfolio_manager.generate_portfolio_report()
