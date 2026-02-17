#!/usr/bin/env python3
"""
Extract UI requirements from PRD or brief files.

Analyzes product documents to identify:
- UI components needed
- User interactions
- Data requirements
- Key features

Usage:
    python extract_requirements.py <path-to-prd.md>
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Set


def extract_user_stories(content: str) -> List[str]:
    """Extract user stories from content."""
    user_stories = []

    # Pattern: "As a [role], I want [feature] so that [benefit]"
    pattern = r"As a .+?, I (?:want|need|can).+?(?:so that|because).+?[.!]"
    matches = re.finditer(pattern, content, re.IGNORECASE)

    for match in matches:
        user_stories.append(match.group(0))

    return user_stories


def identify_ui_components(content: str) -> Set[str]:
    """Identify potential Shadcn components from content."""
    components = set()

    # Common UI patterns mapped to Shadcn components
    patterns = {
        'button': r'\b(button|click|submit|action|cta)\b',
        'form': r'\b(form|input|field|enter|fill out)\b',
        'input': r'\b(input|text field|search|filter)\b',
        'card': r'\b(card|tile|panel|container)\b',
        'dialog': r'\b(modal|dialog|popup|overlay)\b',
        'dropdown': r'\b(dropdown|select|menu|picker)\b',
        'table': r'\b(table|list|grid|row|column)\b',
        'tabs': r'\b(tab|tabbed|navigation)\b',
        'toast': r'\b(notification|toast|alert|message)\b',
        'checkbox': r'\b(checkbox|check|toggle|enable)\b',
        'radio': r'\b(radio|option|choice|select one)\b',
        'slider': r'\b(slider|range|adjust|scale)\b',
        'badge': r'\b(badge|tag|label|status)\b',
        'avatar': r'\b(avatar|profile picture|user image)\b',
        'accordion': r'\b(accordion|collapse|expand|section)\b',
        'calendar': r'\b(calendar|date|picker|schedule)\b',
        'progress': r'\b(progress|loading|status bar)\b',
        'textarea': r'\b(textarea|text area|multi-line|comment)\b',
    }

    content_lower = content.lower()
    for component, pattern in patterns.items():
        if re.search(pattern, content_lower):
            components.add(component)

    return components


def identify_interactions(content: str) -> List[str]:
    """Identify user interactions from content."""
    interactions = []

    # Action verbs indicating interactions
    action_patterns = [
        r'user (?:can |will |should )?(\w+(?:\s+\w+){0,3})',
        r'(?:click|tap|press|select|choose|enter|submit|upload|download|search|filter|sort|view|edit|delete|create|add|remove)',
    ]

    for pattern in action_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            text = match.group(0).strip()
            if len(text) > 5:  # Filter out very short matches
                interactions.append(text)

    # Deduplicate while preserving order
    seen = set()
    unique_interactions = []
    for item in interactions[:20]:  # Limit to top 20
        if item.lower() not in seen:
            seen.add(item.lower())
            unique_interactions.append(item)

    return unique_interactions


def identify_data_requirements(content: str) -> List[str]:
    """Identify data fields and requirements."""
    data_fields = []

    # Look for common field patterns
    field_patterns = [
        r'(?:user |customer |product |order )?(\w+)\s+(?:field|input|data|information)',
        r'(?:name|email|password|phone|address|city|state|zip|country)',
        r'(?:title|description|price|quantity|date|time|status|category)',
    ]

    content_lower = content.lower()
    for pattern in field_patterns:
        matches = re.finditer(pattern, content_lower)
        for match in matches:
            field = match.group(0).strip()
            if field and len(field) < 50:
                data_fields.append(field)

    # Deduplicate
    return list(set(data_fields[:15]))  # Limit to 15 most relevant


def extract_features(content: str) -> List[str]:
    """Extract key features from content."""
    features = []

    # Look for feature sections
    feature_section_pattern = r'##?\s*(?:Features?|Functionality|Capabilities?|Requirements?)\s*\n(.*?)(?=\n##|\Z)'
    matches = re.finditer(feature_section_pattern, content, re.DOTALL | re.IGNORECASE)

    for match in matches:
        section_content = match.group(1)
        # Extract bullet points
        bullets = re.findall(r'[-*+]\s+(.+)', section_content)
        features.extend(bullets[:10])  # Limit features

    return features


def analyze_prd(file_path: Path) -> Dict:
    """Analyze a PRD file and extract requirements."""
    if not file_path.exists():
        print(f"❌ Error: File not found: {file_path}")
        sys.exit(1)

    content = file_path.read_text()

    print(f"📄 Analyzing: {file_path.name}\n")

    analysis = {
        'user_stories': extract_user_stories(content),
        'ui_components': identify_ui_components(content),
        'interactions': identify_interactions(content),
        'data_requirements': identify_data_requirements(content),
        'features': extract_features(content),
    }

    return analysis


def print_analysis(analysis: Dict) -> None:
    """Print analysis results in a readable format."""
    print("=" * 60)
    print("REQUIREMENTS ANALYSIS")
    print("=" * 60)

    print("\n📦 SHADCN COMPONENTS TO INSTALL:")
    if analysis['ui_components']:
        for component in sorted(analysis['ui_components']):
            print(f"  • {component}")
        print(f"\n💡 Install command:")
        components_str = ' '.join(sorted(analysis['ui_components']))
        print(f"  npx shadcn@latest add {components_str}")
    else:
        print("  None identified")

    print("\n🎯 KEY FEATURES:")
    if analysis['features']:
        for feature in analysis['features'][:10]:
            print(f"  • {feature}")
    else:
        print("  None identified")

    print("\n👤 USER STORIES:")
    if analysis['user_stories']:
        for story in analysis['user_stories'][:5]:
            print(f"  • {story}")
    else:
        print("  None identified")

    print("\n🖱️  USER INTERACTIONS:")
    if analysis['interactions']:
        for interaction in analysis['interactions'][:10]:
            print(f"  • {interaction}")
    else:
        print("  None identified")

    print("\n📊 DATA REQUIREMENTS:")
    if analysis['data_requirements']:
        for data in analysis['data_requirements']:
            print(f"  • {data}")
    else:
        print("  None identified")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Extract UI requirements from PRD or brief files"
    )
    parser.add_argument(
        "file_path",
        type=Path,
        help="Path to the PRD or brief markdown file"
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )

    args = parser.parse_args()

    analysis = analyze_prd(args.file_path)

    if args.format == "json":
        import json
        # Convert set to list for JSON serialization
        analysis['ui_components'] = list(analysis['ui_components'])
        print(json.dumps(analysis, indent=2))
    else:
        print_analysis(analysis)


if __name__ == "__main__":
    main()
