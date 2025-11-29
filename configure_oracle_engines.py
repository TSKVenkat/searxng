#!/usr/bin/env python3
"""
Script to configure SearXNG engines for Oracle Research
This enables only the engines needed for academic research and disables the rest
"""

import yaml
import sys
from pathlib import Path

# Engines to ENABLE for Oracle
ENABLED_ENGINES = {
    # General Search
    'google', 'bing', 'brave', 'duckduckgo', 'qwant', 'startpage',
    
    # Academic & Scientific
    'google scholar', 'semantic scholar', 'pubmed', 'arxiv', 'core', 
    'base', 'crossref', 'springer', 'openalex',
    
    # Code & Dev
    'github', 'gitlab', 'stackexchange', 'searchcode code',
    
    # News & Info
    'wikipedia', 'wikidata', 'reddit', 'hackernews',
    
    # Utilities
    'currency',
    
    # Media
    'google images', 'bing images', 'google videos', 'bing videos',
    'bing news'
}

def configure_engines(settings_file='searx/settings.yml'):
    """Configure SearXNG engines for Oracle research"""
    
    settings_path = Path(settings_file)
    if not settings_path.exists():
        print(f"Error: {settings_file} not found!")
        return False
    
    print(f"Loading {settings_file}...")
    with open(settings_path, 'r', encoding='utf-8') as f:
        settings = yaml.safe_load(f)
    
    if 'engines' not in settings:
        print("Error: No engines section found in settings!")
        return False
    
    enabled_count = 0
    disabled_count = 0
    
    print("\nConfiguring engines...")
    for engine in settings['engines']:
        engine_name = engine.get('name', '').lower()
        
        if engine_name in ENABLED_ENGINES:
            # Enable this engine
            engine['disabled'] = False
            if 'inactive' in engine:
                engine['inactive'] = False
            enabled_count += 1
            print(f"  ✓ Enabled: {engine.get('name')}")
        else:
            # Disable this engine
            engine['disabled'] = True
            disabled_count += 1
    
    # Backup original
    backup_path = settings_path.with_suffix('.yml.backup')
    print(f"\nBacking up original to {backup_path}...")
    with open(backup_path, 'w', encoding='utf-8') as f:
        yaml.dump(settings, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    # Save updated settings
    print(f"Saving updated settings to {settings_file}...")
    with open(settings_path, 'w', encoding='utf-8') as f:
        yaml.dump(settings, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"\n✅ Configuration complete!")
    print(f"   - Enabled: {enabled_count} engines")
    print(f"   - Disabled: {disabled_count} engines")
    print(f"   - Backup saved to: {backup_path}")
    
    return True

if __name__ == '__main__':
    success = configure_engines()
    sys.exit(0 if success else 1)
