import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class VoiceOfTheCustomerVocScore(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VOICE_OF_THE_CUSTOMER_VOC_SCORE",
            name_="Voice of the Customer (VoC) Score",
            description_="A measure of customer feedback about their experiences with and expectations for a company's products or services.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product'],
            formula_="Sum of All Customer Feedback Scores / Number of Feedback Instances",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )
