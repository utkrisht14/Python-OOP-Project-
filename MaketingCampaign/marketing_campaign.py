import random

class MarketingManager:
    def __init__(self):
        self.campaigns = {}

    def add_campaign(self, campaign):
        while True:
            new_camp = f"CAMP{random.randint(1000,9999)}"
            if new_camp not in self.campaigns:
                campaign.campaign_id = new_camp
                self.campaigns[new_camp] = campaign
                return new_camp

    def remove_campaign(self, campaign_id):
        if campaign_id in self.campaigns:
            del self.campaigns[campaign_id]

    def generate_performance_report(self):
        for campaign_id, campaign in self.campaigns.items():
            print(f"\nCampaign ID: {campaign_id}")
            metrics = campaign.calculate_total_metrics()
            print(
                f"Impressions: {metrics['impressions']}, Clicks: {metrics['clicks']}, "
                f"Conversions: {metrics['conversions']}, Cost: {metrics['cost']:.2f}"
            )

    def compare_campaigns_by_roi(self, revenue_map):
        roi_list = []
        for campaign_id, campaign in self.campaigns.items():
            revenue = revenue_map.get(campaign_id, 0)
            roi = campaign.calculate_roi(revenue)
            roi_list.append((campaign_id, roi))
        roi_list.sort(key=lambda x: x[1], reverse=True)
        print("\nCampaigns ranked by ROI:")
        for cid, roi in roi_list:
            print(f"{cid}: ROI = {roi:.2f}")


class Campaign:
    def __init__(self, campaign_id=None, name="", budget=0, assets=None):
        self.campaign_id = campaign_id
        self.name = name
        self.budget = budget
        self.assets = assets if assets else []

    def add_asset(self, asset):
        self.assets.append(asset)

    def remove_asset(self, asset_id):
        self.assets = [asset for asset in self.assets if asset.asset_id != asset_id]

    def calculate_total_metrics(self):
        total_impressions = sum(asset.impressions for asset in self.assets)
        total_clicks = sum(asset.clicks for asset in self.assets)
        total_conversions = sum(asset.conversions for asset in self.assets)
        total_cost = sum(asset.cost for asset in self.assets)
        return {
            "impressions": total_impressions,
            "clicks": total_clicks,
            "conversions": total_conversions,
            "cost": total_cost
        }

    def calculate_roi(self, revenue):
        total_cost = sum(asset.cost for asset in self.assets)
        if total_cost == 0:
            return float("inf")
        return (revenue - total_cost) / total_cost


class ContentAsset:
    def __init__(self, asset_id, title, impressions, clicks, conversions, cost):
        self.asset_id = asset_id
        self.title = title
        self.impressions = impressions
        self.clicks = clicks
        self.conversions = conversions
        self.cost = cost

    def get_ctr(self):
        return (self.clicks / self.impressions) * 100 if self.impressions else 0.0

    def get_conversion_rate(self):
        return (self.conversions / self.impressions) * 100 if self.impressions else 0.0


class EmailCampaign(ContentAsset):
    def __init__(self, asset_id, title, impressions, clicks, conversions, cost, open_rate):
        super().__init__(asset_id, title, impressions, clicks, conversions, cost)
        self.open_rate = open_rate


class SocialMediaCampaign(ContentAsset):
    def __init__(self, asset_id, title, impressions, clicks, conversions, cost, platform):
        super().__init__(asset_id, title, impressions, clicks, conversions, cost)
        self.platform = platform


class AdCampaign(ContentAsset):
    def __init__(self, asset_id, title, impressions, clicks, conversions, cost, ad_network):
        super().__init__(asset_id, title, impressions, clicks, conversions, cost)
        self.ad_network = ad_network


# Example Usage
manager = MarketingManager()

campaign1 = Campaign(name="New Product Launch", budget=10000)
campaign1.add_asset(SocialMediaCampaign("AST001", "Instagram Teaser", 10000, 500, 50, 1500, "Instagram"))
campaign1.add_asset(EmailCampaign("AST002", "Launch Email", 5000, 300, 45, 500, 40.5))

campaign_id = manager.add_campaign(campaign1)
manager.generate_performance_report()
manager.compare_campaigns_by_roi({campaign_id: 8000})
