# Marketing Campaign Manager

This is a Python-based object-oriented project that allows marketing teams to manage and evaluate multiple digital campaigns. It supports tracking key performance metrics like impressions, clicks, conversions, and return on investment (ROI).

## Features

- Manage multiple marketing campaigns under a single manager
- Add and remove campaign content assets (emails, social media posts, ads)
- Calculate performance metrics per campaign
- Compare campaigns by ROI to evaluate efficiency

## Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP) principles
  - Inheritance
  - Composition

## Class Overview

### MarketingManager
Handles all campaigns and provides utilities to report and compare performance.

**Methods:**
- `add_campaign(campaign)`: Adds a new campaign with a unique ID
- `remove_campaign(campaign_id)`: Removes a campaign by ID
- `generate_performance_report()`: Displays a report of all campaigns
- `compare_campaigns_by_roi(revenue_map)`: Sorts and compares campaigns based on ROI

---

### Campaign
Represents a single campaign and holds a list of associated content assets.

**Attributes:**
- `campaign_id`
- `name`
- `budget`
- `assets` (list of content objects)

**Methods:**
- `add_asset(asset)`: Add a new content asset
- `remove_asset(asset_id)`: Remove asset by ID
- `calculate_total_metrics()`: Aggregates impressions, clicks, conversions, and cost
- `calculate_roi(revenue)`: Calculates campaign ROI based on given revenue

---

### ContentAsset (Base Class)
Represents a piece of marketing content with measurable metrics.

**Attributes:**
- `asset_id`, `title`, `impressions`, `clicks`, `conversions`, `cost`

**Methods:**
- `get_ctr()`: Calculates Click-Through Rate
- `get_conversion_rate()`: Calculates Conversion Rate

---

### Inherited Classes
- **EmailCampaign**: Adds `open_rate`
- **SocialMediaCampaign**: Adds `platform`
- **AdCampaign**: Adds `ad_network`

---

## Example Usage

```python
manager = MarketingManager()

campaign1 = Campaign(name="New Product Launch", budget=10000)
campaign1.add_asset(SocialMediaCampaign("AST001", "Instagram Teaser", 10000, 500, 50, 1500, "Instagram"))
campaign1.add_asset(EmailCampaign("AST002", "Launch Email", 5000, 300, 45, 500, 40.5))

campaign_id = manager.add_campaign(campaign1)
manager.generate_performance_report()
manager.compare_campaigns_by_roi({campaign_id: 8000})
