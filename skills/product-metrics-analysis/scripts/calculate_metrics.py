#!/usr/bin/env python3
"""
Product Metrics Calculator

Calculates common product metrics from input data.
Supports CSV, JSON, and direct data input.
"""

import sys
import json
import csv
from typing import Dict, List, Union
from datetime import datetime
from collections import defaultdict


def calculate_growth_rate(old_value: float, new_value: float) -> float:
    """Calculate percentage growth rate."""
    if old_value == 0:
        return 0.0
    return ((new_value - old_value) / old_value) * 100


def calculate_conversion_rate(conversions: int, total: int) -> float:
    """Calculate conversion rate as percentage."""
    if total == 0:
        return 0.0
    return (conversions / total) * 100


def calculate_retention_rate(active_users: int, cohort_size: int) -> float:
    """Calculate retention rate as percentage."""
    if cohort_size == 0:
        return 0.0
    return (active_users / cohort_size) * 100


def calculate_churn_rate(churned_users: int, starting_users: int) -> float:
    """Calculate churn rate as percentage."""
    if starting_users == 0:
        return 0.0
    return (churned_users / starting_users) * 100


def calculate_dau_mau_ratio(dau: int, mau: int) -> float:
    """Calculate DAU/MAU ratio (stickiness)."""
    if mau == 0:
        return 0.0
    return (dau / mau) * 100


def calculate_ltv(arpu: float, churn_rate: float) -> float:
    """Calculate customer lifetime value from ARPU and churn rate."""
    if churn_rate == 0:
        return 0.0
    return arpu / (churn_rate / 100)


def calculate_ltv_cac_ratio(ltv: float, cac: float) -> float:
    """Calculate LTV/CAC ratio."""
    if cac == 0:
        return 0.0
    return ltv / cac


def calculate_arpu(total_revenue: float, total_users: int) -> float:
    """Calculate average revenue per user."""
    if total_users == 0:
        return 0.0
    return total_revenue / total_users


def calculate_funnel_conversion(step_counts: List[int]) -> List[Dict[str, Union[int, float]]]:
    """
    Calculate funnel conversion rates.

    Args:
        step_counts: List of user counts at each funnel step

    Returns:
        List of dicts with step number, count, and conversion rate
    """
    if not step_counts or step_counts[0] == 0:
        return []

    results = []
    total_started = step_counts[0]

    for i, count in enumerate(step_counts):
        conversion = (count / total_started) * 100
        drop_off = 0.0

        if i > 0:
            drop_off = ((step_counts[i-1] - count) / step_counts[i-1]) * 100

        results.append({
            "step": i + 1,
            "count": count,
            "conversion_from_start": round(conversion, 2),
            "drop_off_from_previous": round(drop_off, 2)
        })

    return results


def analyze_cohort_retention(cohort_data: Dict[str, List[int]]) -> Dict:
    """
    Analyze cohort retention data.

    Args:
        cohort_data: Dict with cohort names as keys and list of retention counts over time

    Example:
        {
            "Jan 2024": [1000, 800, 600, 500],  # D0, D7, D30, D90
            "Feb 2024": [1200, 950, 700, 550]
        }
    """
    results = {}

    for cohort_name, counts in cohort_data.items():
        if not counts or counts[0] == 0:
            continue

        cohort_size = counts[0]
        retention_rates = [
            round((count / cohort_size) * 100, 2)
            for count in counts
        ]

        results[cohort_name] = {
            "cohort_size": cohort_size,
            "retention_rates": retention_rates,
            "final_retention": retention_rates[-1] if retention_rates else 0
        }

    return results


def calculate_take_rate(revenue: float, tpv: float) -> float:
    """Calculate take rate / monetization rate."""
    if tpv == 0:
        return 0.0
    return (revenue / tpv) * 100


def calculate_payment_acceptance_rate(approved: int, total_attempts: int) -> float:
    """Calculate payment acceptance/authorization rate."""
    if total_attempts == 0:
        return 0.0
    return (approved / total_attempts) * 100


def calculate_chargeback_rate(chargebacks: int, total_transactions: int) -> float:
    """Calculate chargeback rate."""
    if total_transactions == 0:
        return 0.0
    return (chargebacks / total_transactions) * 100


def calculate_atv(tpv: float, num_transactions: int) -> float:
    """Calculate average transaction value."""
    if num_transactions == 0:
        return 0.0
    return tpv / num_transactions


def calculate_fraud_rate(fraudulent: int, total_transactions: int) -> float:
    """Calculate fraud rate."""
    if total_transactions == 0:
        return 0.0
    return (fraudulent / total_transactions) * 100


def calculate_net_revenue(gross_revenue: float, processing_fees: float,
                         chargebacks: float, refunds: float) -> float:
    """Calculate net revenue after all payment costs."""
    return gross_revenue - processing_fees - chargebacks - refunds


def main():
    """CLI interface for metric calculations."""
    if len(sys.argv) < 2:
        print("Usage: python calculate_metrics.py <metric_type> [args...]")
        print("\nAvailable metrics:")
        print("  growth_rate <old_value> <new_value>")
        print("  conversion_rate <conversions> <total>")
        print("  retention_rate <active_users> <cohort_size>")
        print("  churn_rate <churned_users> <starting_users>")
        print("  dau_mau_ratio <dau> <mau>")
        print("  ltv <arpu> <churn_rate>")
        print("  ltv_cac_ratio <ltv> <cac>")
        print("  arpu <total_revenue> <total_users>")
        print("  funnel <step1_count> <step2_count> ... <stepN_count>")
        print("\nFintech/Payments metrics:")
        print("  take_rate <revenue> <tpv>")
        print("  payment_acceptance_rate <approved> <total_attempts>")
        print("  chargeback_rate <chargebacks> <total_transactions>")
        print("  atv <tpv> <num_transactions>")
        print("  fraud_rate <fraudulent> <total_transactions>")
        print("  net_revenue <gross_revenue> <processing_fees> <chargebacks> <refunds>")
        sys.exit(1)

    metric_type = sys.argv[1].lower()

    try:
        if metric_type == "growth_rate":
            old_val, new_val = float(sys.argv[2]), float(sys.argv[3])
            result = calculate_growth_rate(old_val, new_val)
            print(f"Growth Rate: {result:.2f}%")

        elif metric_type == "conversion_rate":
            conversions, total = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_conversion_rate(conversions, total)
            print(f"Conversion Rate: {result:.2f}%")

        elif metric_type == "retention_rate":
            active, cohort = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_retention_rate(active, cohort)
            print(f"Retention Rate: {result:.2f}%")

        elif metric_type == "churn_rate":
            churned, starting = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_churn_rate(churned, starting)
            print(f"Churn Rate: {result:.2f}%")

        elif metric_type == "dau_mau_ratio":
            dau, mau = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_dau_mau_ratio(dau, mau)
            print(f"DAU/MAU Ratio (Stickiness): {result:.2f}%")

        elif metric_type == "ltv":
            arpu, churn = float(sys.argv[2]), float(sys.argv[3])
            result = calculate_ltv(arpu, churn)
            print(f"Customer Lifetime Value: ${result:.2f}")

        elif metric_type == "ltv_cac_ratio":
            ltv, cac = float(sys.argv[2]), float(sys.argv[3])
            result = calculate_ltv_cac_ratio(ltv, cac)
            print(f"LTV/CAC Ratio: {result:.2f}")

        elif metric_type == "arpu":
            revenue, users = float(sys.argv[2]), int(sys.argv[3])
            result = calculate_arpu(revenue, users)
            print(f"Average Revenue Per User: ${result:.2f}")

        elif metric_type == "funnel":
            step_counts = [int(x) for x in sys.argv[2:]]
            results = calculate_funnel_conversion(step_counts)
            print(json.dumps(results, indent=2))

        # Fintech/Payments metrics
        elif metric_type == "take_rate":
            revenue, tpv = float(sys.argv[2]), float(sys.argv[3])
            result = calculate_take_rate(revenue, tpv)
            print(f"Take Rate: {result:.2f}%")

        elif metric_type == "payment_acceptance_rate":
            approved, total = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_payment_acceptance_rate(approved, total)
            print(f"Payment Acceptance Rate: {result:.2f}%")

        elif metric_type == "chargeback_rate":
            chargebacks, total = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_chargeback_rate(chargebacks, total)
            print(f"Chargeback Rate: {result:.2f}%")

        elif metric_type == "atv":
            tpv, num_txns = float(sys.argv[2]), int(sys.argv[3])
            result = calculate_atv(tpv, num_txns)
            print(f"Average Transaction Value: ${result:.2f}")

        elif metric_type == "fraud_rate":
            fraudulent, total = int(sys.argv[2]), int(sys.argv[3])
            result = calculate_fraud_rate(fraudulent, total)
            print(f"Fraud Rate: {result:.2f}%")

        elif metric_type == "net_revenue":
            gross, fees, chargebacks, refunds = (
                float(sys.argv[2]), float(sys.argv[3]),
                float(sys.argv[4]), float(sys.argv[5])
            )
            result = calculate_net_revenue(gross, fees, chargebacks, refunds)
            print(f"Net Revenue: ${result:,.2f}")

        else:
            print(f"Unknown metric type: {metric_type}")
            sys.exit(1)

    except IndexError:
        print(f"Error: Not enough arguments for {metric_type}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid value - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
