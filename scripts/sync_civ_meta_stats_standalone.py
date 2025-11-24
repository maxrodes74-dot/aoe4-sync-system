#!/usr/bin/env python3
"""
Sync Civilization Meta Stats from AoE4 World API to Airtable
STANDALONE VERSION - Uses Airtable API directly (no MCP dependency)
"""
import json
import os
import requests
from datetime import datetime

# Configuration
BASE_ID = "appKeqSFMnexidZfd"
TABLE_NAME = "Civilization Meta Stats"
API_BASE = "https://aoe4world.com/api/v0"
AIRTABLE_API = "https://api.airtable.com/v0"

# Get Airtable token from environment
AIRTABLE_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
if not AIRTABLE_TOKEN:
    raise ValueError("AIRTABLE_ACCESS_TOKEN environment variable not set")

# Civilization name mapping
CIV_NAME_MAP = {
    "golden_horde": "Golden Horde",
    "knights_templar": "Knights Templar",
    "japanese": "Japanese",
    "order_of_the_dragon": "Order of the Dragon",
    "ayyubids": "Ayyubids",
    "macedonian_dynasty": "Macedonian Dynasty",
    "mongols": "Mongols",
    "tughlaq_dynasty": "Tughlaq Dynasty",
    "malians": "Malians",
    "chinese": "Chinese",
    "french": "French",
    "english": "English",
    "rus": "Rus",
    "abbasid_dynasty": "Abbasid Dynasty",
    "delhi_sultanate": "Delhi Sultanate",
    "holy_roman_empire": "Holy Roman Empire",
    "ottomans": "Ottomans",
    "byzantines": "Byzantines",
    "sengoku_daimyo": "Sengoku Daimyo",
    "zhu_xis_legacy": "Zhu Xi's Legacy",
    "house_of_lancaster": "House of Lancaster",
    "jeanne_darc": "Jeanne d'Arc"
}

def create_airtable_record(fields):
    """Create a record in Airtable using REST API"""
    url = f"{AIRTABLE_API}/{BASE_ID}/{TABLE_NAME}"
    headers = {
        'Authorization': f'Bearer {AIRTABLE_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {'fields': fields}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error creating record: {e}")
        return None

def fetch_civ_stats(leaderboard="rm_solo", rank_level=None):
    """Fetch civilization statistics from AoE4 World API"""
    url = f"{API_BASE}/stats/{leaderboard}/civilizations"
    params = {}
    if rank_level:
        params['rank_level'] = rank_level
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def sync_stats(leaderboard="rm_solo", rank_level=None):
    """Sync civilization stats to Airtable"""
    print(f"\n{'='*60}")
    print(f"Syncing {leaderboard} stats" + (f" for {rank_level}" if rank_level else " (All Ranks)"))
    print(f"{'='*60}")
    
    data = fetch_civ_stats(leaderboard, rank_level)
    if not data:
        print("Failed to fetch data")
        return
    
    stats_list = data.get('data', [])
    patch = data.get('patch', 'unknown')
    timestamp = datetime.now().isoformat()
    
    print(f"Found {len(stats_list)} civilizations")
    print(f"Patch: {patch}")
    
    count = 0
    for stat in stats_list:
        civ_id = stat.get('civilization', '')
        civ_name = CIV_NAME_MAP.get(civ_id, civ_id.replace('_', ' ').title())
        
        record = {
            "civilization": civ_name,
            "leaderboard": leaderboard,
            "rank_level": rank_level if rank_level else "All Ranks",
            "win_rate": round(stat.get('win_rate', 0), 2),
            "pick_rate": round(stat.get('pick_rate', 0), 2),
            "games_count": stat.get('games_count', 0),
            "avg_game_duration": int(stat.get('duration_average', 0)),
            "patch": patch,
            "last_updated": timestamp
        }
        
        print(f"  {civ_name}: {record['win_rate']}% WR, {record['pick_rate']}% PR")
        
        result = create_airtable_record(record)
        if result:
            count += 1
    
    print(f"\n✓ Synced {count}/{len(stats_list)} civilizations")

if __name__ == "__main__":
    print("="*60)
    print("AoE4 World API → Airtable Sync (Standalone)")
    print("Civilization Meta Statistics")
    print("="*60)
    
    # Sync overall stats for ranked solo
    sync_stats("rm_solo", None)
    
    print("\n" + "="*60)
    print("Sync complete!")
    print("="*60)
