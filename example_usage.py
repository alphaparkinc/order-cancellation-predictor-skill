"""
example_usage.py -- Demonstrates OrderCancellationPredictorClient
"""
from client import OrderCancellationPredictorClient

def main():
    client = OrderCancellationPredictorClient()
    result = client.predict_risk(
        payment_status="pending",
        days_since_first_order=0,
        total_item_qty=25
    )
    print("[Cancellation Risk Result]")
    print(f"Probability: {result['cancellation_probability']}")
    print(f"Risk Tier: {result['risk_tier']}")
    print(f"Review Flag: {result['review_recommended']}")

if __name__ == "__main__":
    main()
