#!/usr/bin/env python3
"""
SRE Incident & Error Budget Burn Rate Simulator
Author: Anil Kumar
"""
import time
import sys

def simulate_burn_rate():
    print("==================================================")
    print("🚨 SRE OBSERVABILITY INCIDENT SIMULATOR")
    print("==================================================")
    print("[*] Target Service: payment-engine (Production)")
    print("[*] Simulating sudden error spike (500 Internal Server Error)...")
    
    total_requests = 10000
    error_rate = 0.05 # 5% error rate (Burns 100% of 99.9% SLO budget rapidly)
    
    for i in range(1, 6):
        print(f"  • Interval {i}/5: Transmitting telemetry -> Error Rate: {error_rate*100}% | P95 Latency: 420ms")
        time.sleep(1)
        
    print("\n[!] Prometheus Alert Triggered: 'ErrorBudgetBurnRateFast'")
    print("[!] Routing alert to PagerDuty On-Call & Microsoft Teams Incident Channel...")
    print("[✔] Automated SRE Diagnostic Playbook Triggered: Captured thread dumps & CPU profiles.")
    print("==================================================")

if __name__ == "__main__":
    simulate_burn_rate()
