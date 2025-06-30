#!/usr/bin/env python3

"""
update_readme_devices.py

This script updates the `README.md` file in the Dasharo Issues repository by generating
a section that lists supported devices and links each one to its open issues on GitHub.

It should be executed each time we add a new device (or drop existing one), to make sure
the list is up to date.

It:
- Loads the `.github/advanced-issue-labeler.yml` policy file.
- Extracts all device labels and their associated keys.
- Generates a Markdown list of device names linking to GitHub issue searches.
- Replaces the content between `<!-- BEGIN DEVICE ISSUES -->` and `<!-- END DEVICE ISSUES -->`
  in `README.md` with this list.

Usage:
    Run this script from the root of the repository:
        python3 update_readme_devices.py
"""

import yaml
import urllib.parse
import re

REPO = "dasharo/dasharo-issues"
YAML_PATH = ".github/advanced-issue-labeler.yml"
README_PATH = "README.md"
START_MARKER = "<!-- BEGIN DEVICE ISSUES -->"
END_MARKER = "<!-- END DEVICE ISSUES -->"

def load_policy_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def extract_device_entries(policy):
    entries = []
    for section in policy.get("policy", []):
        for sec in section.get("section", []):
            if sec.get("id") == ["device"] and "other" in sec.get("block-list", []):
                for item in sec.get("label", []):
                    label_name = item["name"]
                    for key in item.get("keys", []):
                        entries.append((key, label_name))
    return entries

def generate_issue_search_url(repo, label_name):
    quoted = urllib.parse.quote(f'"{label_name}"')
    return f"https://github.com/{repo}/issues?q=is%3Aissue+state%3Aopen+label%3A{quoted}"

def generate_readme_section(entries):
    lines = ["## Issues per device", "\nBelow is a list of open issues affecting specific devices:"]
    for device_name, label_name in sorted(entries, key=lambda x: x[0].lower()):
        url = generate_issue_search_url(REPO, label_name)
        lines.append(f"- [{device_name}]({url})")
    return "\n".join(lines)

def update_readme(readme_path, new_section):
    with open(readme_path, "r") as f:
        content = f.read()

    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    replacement = f"{START_MARKER}\n{new_section}\n{END_MARKER}"

    if pattern.search(content):
        updated = pattern.sub(replacement, content)
    else:
        updated = content.strip() + "\n\n" + replacement

    with open(readme_path, "w") as f:
        f.write(updated)

if __name__ == "__main__":
    policy = load_policy_yaml(YAML_PATH)
    entries = extract_device_entries(policy)
    section = generate_readme_section(entries)
    update_readme(README_PATH, section)
    print("README.md updated with flat device issue links.")
