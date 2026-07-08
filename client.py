"""
order-delivery-estimator-skill: Client SDK
Estimates delivery arrival intervals based on zone multipliers.
"""
from __future__ import annotations
from typing import Optional


class OrderDeliveryEstimatorClient:
    """
    SDK for shipment arrival estimations.
    """

    def estimate_timeline(
        self,
        shipping_zone: int,
        courier: str,
        processing_days: int = 1,
    ) -> dict:
        c = courier.upper()
        
        # Base transit calculation
        if c == "DHL":
            base_transit = 1
        elif c == "FEDEX" or c == "UPS":
            base_transit = 2
        else:
            base_transit = 4  # Default slow post USPS

        zone_delay = int(shipping_zone * 0.5)
        
        min_est = processing_days + base_transit + zone_delay
        max_est = min_est + 2

        return {
            "min_days": min_est,
            "max_days": max_est,
            "carrier_assigned": c
        }
