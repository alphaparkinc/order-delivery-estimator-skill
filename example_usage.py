"""
example_usage.py -- Demonstrates OrderDeliveryEstimatorClient
"""
from client import OrderDeliveryEstimatorClient

def main():
    client = OrderDeliveryEstimatorClient()
    result = client.estimate_timeline(shipping_zone=4, courier="FedEx", processing_days=2)
    print("[Delivery Estimator Result]")
    print(f"Arrival Estimate: {result['min_days']} to {result['max_days']} business days.")

if __name__ == "__main__":
    main()
