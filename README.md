# genpark-order-delivery-estimator-skill

> **GenPark AI Agent Skill** -- Shipping delivery timeline estimator.

## Quick Start

```python
from client import OrderDeliveryEstimatorClient
client = OrderDeliveryEstimatorClient()
res = client.estimate_timeline(2, "UPS")
print(res["min_days"])
```
