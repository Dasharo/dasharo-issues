#!/usr/bin/env python3
"""
Script to update the README.md with current device issue links.
Also includes EC testability interface documentation.
"""

import re
a section that lists supported devices and links each one to its open issues on GitHub.

# List of devices to track - can be extended
DEVICES = [
    ("novacustom_nv4x_tgl", "NovaCustom NV4x 11th Gen"),
    ("novacustom_ns5x/7x_tgl", "NovaCustom NS5x/NS7x 11th Gen"),
    ("novacustom_ns5x/7x_adl", "NovaCustom NS5x/NS7x 12th Gen"),
    ("novacustom_nv4x_adl", "NovaCustom NV4x 12th Gen"),
- Extracts all device labels and their associated keys.
    ("novacustom_v54_mtl", "NovaCustom V54 14th Gen"),
    ("novacustom_v56_mtl", "NovaCustom V56 14th Gen"),
    ("asus_kgpe-d16", "Asus KGPE-D16"),
    ("novacustom_nv4x_tgl", "NovaCustom NV4x 11th Gen"),
    ("novacustom_ns5x/7x_tgl", "NovaCustom NS5x 11th Gen"),
    ("dell_optiplex_7010", "Dell OptiPlex 7010"),
    ("dell_optiplex_9010", "Dell OptiPlex 9010"),
    ("hardkernel_odroid_h4", "Hardkernel Odroid H4"),
        python3 update_readme_devices.py
    ("MSI PRO Z790-P boards", "MSI Pro Z790-P"),
]


def generate_device_section():
    """Generate the device issues section."""
    lines = ["## Issues per device", ""]
REPO = "dasharo/dasharo-issues"
YAML_PATH = ".github/advanced-issue-labeler.yml"
README_PATH = "README.md"
START_MARKER = "<!-- BEGIN DEVICE ISSUES -->"
        lines.append(f"- [{display_name}]({url})")
    return "\n".join(lines) + "\n"


def update_readme():
    """Update the README.md file with current device links."""
    readme_path = Path("README.md")
def extract_device_entries(policy):
    entries = []
    for section in policy.get("policy", []):
        for sec in section.get("section", []):
            if sec.get("id") == ["device"] and "other" in sec.get("block-list", []):
    
    # Find the device issues section
    start_marker = "## Issues per device"
    end_marker = "<!-- END DEVICE ISSUES -->"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
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
    with open(readme_path, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    update_readme()
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
