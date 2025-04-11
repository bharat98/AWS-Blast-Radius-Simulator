# simulate.py - version 1

import argparse
import json
import re
from pathlib import Path

def load_policy(file_path):
    """Load and return IAM policy JSON from file"""
    try:
        with open(file_path, 'r') as f:
            policy = json.load(f)
        return policy
    except Exception as e:
        print(f"[ERROR] Failed to load policy: {e}")
        return None

def extract_permissions(policy):
    """Extract all allowed actions from the policy"""
    permissions = []

    statements = policy.get("Statement", [])
    if not isinstance(statements, list):
        statements = [statements]  # Support single-object policies

    for stmt in statements:
        if stmt.get("Effect", "").lower() != "allow":
            continue

        actions = stmt.get("Action", [])
        resources = stmt.get("Resource", "*")
        sid = stmt.get("Sid", "None")

        # Normalize single string to list
        if isinstance(actions, str):
            actions = [actions]

        if isinstance(resources, str):
            resources = [resources]

        permissions.append({
            "Sid": sid,
            "Actions": actions,
            "Resources": resources
        })

    return permissions

def load_aws_action_db():                           # Loads all the AWS actions from JSON file 
    path = "./aws_actions.json"
    with open(path, "r") as f:
        return(json.load(f))

    

def main():
    parser = argparse.ArgumentParser(description="Simulate IAM policy blast radius.")
    parser.add_argument("policy", type=str, help="Path to IAM policy JSON file")
    args = parser.parse_args()

    policy = load_policy(args.policy)
    if policy is None:
        return

    permissions = extract_permissions(policy)

    print("\n[+] Parsed Permissions:")
    for p in permissions:
        print(f"  SID: {p['Sid']}")
        for action in p['Actions']:
            print(f"    Action: {action}")
        for resource in p['Resources']:
            print(f"    Resource: {resource}")

if __name__ == "__main__":
    main()
