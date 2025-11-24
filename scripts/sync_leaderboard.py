#!/usr/bin/env python3.11
"""
Sync Top Players from AoE4 World Leaderboards to Airtable
"""
import json
import subprocess
import requests
from datetime import datetime

BASE_ID = "appKeqSFMnexidZfd"
TABLE_ID = "Leaderboard Players"
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
    
    # Limit to top N
    players = players[:top_n]
    
    print(f"Found {len(players)} players")
    
    count = 0
    for player in players:
        # Calculate win rate
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
        
        result = create_record(record)
        if result:
            count += 1
    
    print(f"\n✓ Synced {count}/{len(players)} players")

if __name__ == "__main__":
    print("="*60)
    print("AoE4 World API → Airtable Sync")
    print("Leaderboard Players")
    print("="*60)
    
    # Sync top 50 players from ranked solo
    sync_leaderboard("rm_solo", top_n=50)
    
    # Optionally sync team leaderboard
    # sync_leaderboard("rm_team", top_n=50)
    
    print("\n" + "="*60)
    print("Sync complete!")
    print("="*60)
