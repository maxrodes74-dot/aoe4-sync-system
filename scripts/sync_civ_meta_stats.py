#!/usr/bin/env python3.11
"""
Sync Civilization Meta Stats from AoE4 World API to Airtable
Pulls live win rates, pick rates, and game statistics
"""
import json
import subprocess
import requests
from datetime import datetime

BASE_ID = "appKeqSFMnexidZfd"
TABLE_ID = "Civilization Meta Stats"
API_BASE = "https://aoe4world.com/api/v0"

def create_record(fields):
    """Create a record in Airtable using manus-mcp-cli"""
    input_data = {
        "baseId": BASE_ID,
        "tableId": TABLE_ID,
        "fields": fields
    }
    
    cmd = [
        "manus-mcp-cli", "tool", "call", "create_record",
        "--server", "airtable",
        "--input", json.dumps(input_data)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout

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

# Civilization name mapping (API uses underscores, we want readable names)
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
        
        result = create_record(record)
        if result:
            count += 1
    
    print(f"\n✓ Synced {count}/{len(stats_list)} civilizations")

if __name__ == "__main__":
    print("="*60)
    print("AoE4 World API → Airtable Sync")
    print("Civilization Meta Statistics")
    print("="*60)
    
    # Sync overall stats for ranked solo
    sync_stats("rm_solo", None)
    
    # Optionally sync for specific rank levels
    # Uncomment to sync rank-specific data:
    # sync_stats("rm_solo", "conqueror")
    # sync_stats("rm_solo", "diamond")
    # sync_stats("rm_solo", "platinum")
    
    print("\n" + "="*60)
    print("Sync complete!")
    print("="*60)
