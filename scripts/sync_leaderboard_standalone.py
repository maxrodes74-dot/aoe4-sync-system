#!/usr/bin/env python3
"""
Sync Top Players from AoE4 World Leaderboards to Airtable
STANDALONE VERSION - Uses Airtable API directly (no MCP dependency)
"""
import json
import os
import requests

# Configuration
BASE_ID = "appKeqSFMnexidZfd"
TABLE_NAME = "Leaderboard Players"
API_BASE = "https://aoe4world.com/api/v0"
AIRTABLE_API = "https://api.airtable.com/v0"

# Get Airtable token from environment
AIRTABLE_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
if not AIRTABLE_TOKEN:
    raise ValueError("AIRTABLE_ACCESS_TOKEN environment variable not set")

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

def fetch_leaderboard(leaderboard="rm_solo", page=1):
    """Fetch leaderboard from AoE4 World API"""
    url = f"{API_BASE}/leaderboards/{leaderboard}"
    params = {"page": page}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching leaderboard: {e}")
        return None

def sync_leaderboard(leaderboard="rm_solo", top_n=50):
    """Sync top N players from leaderboard to Airtable"""
    print(f"\n{'='*60}")
    print(f"Syncing Top {top_n} Players from {leaderboard}")
    print(f"{'='*60}")
    
    data = fetch_leaderboard(leaderboard, page=1)
    if not data:
        print("Failed to fetch leaderboard")
        return
    
    players = data.get('players', [])
    players = players[:top_n]
    
    print(f"Found {len(players)} players")
    
    count = 0
    for player in players:
        wins = player.get('wins', 0)
        losses = player.get('losses', 0)
        total_games = wins + losses
        win_rate = (wins / total_games * 100) if total_games > 0 else 0
        
        record = {
            "player_name": player.get('name', 'Unknown'),
            "profile_id": player.get('profile_id', 0),
            "rank": player.get('rank', 0),
            "rating": player.get('rating', 0),
            "rank_level": player.get('rank_level', 'Unknown'),
            "win_rate": round(win_rate, 2),
            "games_count": total_games,
            "leaderboard": leaderboard,
            "country": player.get('country', ''),
            "last_game": player.get('last_game_at', '')
        }
        
        print(f"  #{record['rank']}: {record['player_name']} - {record['rating']} ELO ({record['win_rate']}% WR)")
        
        result = create_airtable_record(record)
        if result:
            count += 1
    
    print(f"\n✓ Synced {count}/{len(players)} players")

if __name__ == "__main__":
    print("="*60)
    print("AoE4 World API → Airtable Sync (Standalone)")
    print("Leaderboard Players")
    print("="*60)
    
    sync_leaderboard("rm_solo", top_n=50)
    
    print("\n" + "="*60)
    print("Sync complete!")
    print("="*60)
