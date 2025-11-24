#!/usr/bin/env python3
"""
Generate AI-powered meta analysis using live data from AoE4 World API
STANDALONE VERSION - Uses Airtable API directly (no MCP dependency)
"""
import json
import os
import requests
from openai import OpenAI

# Configuration
BASE_ID = "appKeqSFMnexidZfd"
TABLE_NAME = "Strategy Analysis"
API_BASE = "https://aoe4world.com/api/v0"
AIRTABLE_API = "https://api.airtable.com/v0"

# Get tokens from environment
AIRTABLE_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
if not AIRTABLE_TOKEN:
    raise ValueError("AIRTABLE_ACCESS_TOKEN environment variable not set")

# Initialize OpenAI client
client = OpenAI()

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

def fetch_civ_stats(leaderboard="rm_solo"):
    """Fetch current civilization statistics"""
    url = f"{API_BASE}/stats/{leaderboard}/civilizations"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return None

def generate_meta_report(stats_data):
    """Use AI to analyze the current meta based on live statistics"""
    civs = stats_data.get('data', [])
    top_5 = civs[:5]
    bottom_5 = civs[-5:]
    
    top_civs_text = "\n".join([
        f"- {c['civilization'].replace('_', ' ').title()}: {c['win_rate']:.2f}% WR, {c['pick_rate']:.2f}% PR, {c['games_count']} games"
        for c in top_5
    ])
    
    bottom_civs_text = "\n".join([
        f"- {c['civilization'].replace('_', ' ').title()}: {c['win_rate']:.2f}% WR, {c['pick_rate']:.2f}% PR, {c['games_count']} games"
        for c in bottom_5
    ])
    
    prompt = f"""You are an expert Age of Empires 4 meta analyst. Analyze the current competitive meta based on live statistics from ranked 1v1 games.

**Top 5 Performing Civilizations:**
{top_civs_text}

**Bottom 5 Performing Civilizations:**
{bottom_civs_text}

**Patch:** {stats_data.get('patch', 'Unknown')}

Provide a comprehensive meta analysis including:
1. Why the top civilizations are dominating
2. What strategies they enable
3. How to counter the meta picks
4. Which underperforming civs might be sleeper picks
5. Predictions for meta shifts

Format as JSON:
{{
  "early_game": "Early game meta analysis",
  "mid_game": "Mid game meta trends",
  "late_game": "Late game considerations",
  "key_units": "Most important units in current meta",
  "key_technologies": "Critical technologies",
  "confidence": 90,
  "reasoning": "Detailed reasoning for the analysis"
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an expert Age of Empires 4 competitive analyst who provides data-driven meta analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"Error generating analysis: {e}")
        return None

def generate_civ_specific_guide(civ_name, civ_stats, all_stats):
    """Generate a guide for playing a specific civilization in the current meta"""
    rank = next((i+1 for i, c in enumerate(all_stats) if c['civilization'] == civ_stats['civilization']), 0)
    total_civs = len(all_stats)
    
    prompt = f"""You are an expert Age of Empires 4 coach. Create a guide for playing {civ_name} in the current competitive meta.

**{civ_name} Statistics:**
- Win Rate: {civ_stats['win_rate']:.2f}%
- Pick Rate: {civ_stats['pick_rate']:.2f}%
- Meta Ranking: #{rank} out of {total_civs}
- Average Game Duration: {civ_stats.get('duration_average', 0):.0f} seconds

Provide practical advice for:
1. Early game priorities (first 10 minutes)
2. Mid game power spikes and strategies
3. Late game compositions
4. Key matchups to be aware of
5. Why this civ is performing at this level

Format as JSON:
{{
  "early_game": "Early game strategy",
  "mid_game": "Mid game approach",
  "late_game": "Late game plan",
  "key_units": "Units to prioritize",
  "key_technologies": "Technologies to research",
  "confidence": 85,
  "reasoning": "Why this approach works"
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an expert Age of Empires 4 coach who provides practical, data-driven advice."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"Error generating guide: {e}")
        return None

if __name__ == "__main__":
    print("="*60)
    print("AI Meta Analysis Generator (Standalone)")
    print("Using Live AoE4 World Data")
    print("="*60)
    
    print("\nFetching live statistics...")
    stats_data = fetch_civ_stats("rm_solo")
    
    if not stats_data:
        print("Failed to fetch statistics")
        exit(1)
    
    civs = stats_data.get('data', [])
    patch = stats_data.get('patch', 'Unknown')
    
    print(f"Loaded data for {len(civs)} civilizations")
    print(f"Patch: {patch}")
    
    # Generate overall meta report
    print("\n" + "="*60)
    print("Generating Overall Meta Report...")
    print("="*60)
    
    meta_analysis = generate_meta_report(stats_data)
    if meta_analysis:
        record = {
            "title": f"Current Meta Analysis - Patch {patch}",
            "civilization": "All",
            "matchup_vs": "Meta Overview",
            "map_type": "Open",
            "early_game": meta_analysis.get('early_game', ''),
            "mid_game": meta_analysis.get('mid_game', ''),
            "late_game": meta_analysis.get('late_game', ''),
            "key_units": meta_analysis.get('key_units', ''),
            "key_technologies": meta_analysis.get('key_technologies', ''),
            "ai_confidence": meta_analysis.get('confidence', 80),
            "ai_reasoning": meta_analysis.get('reasoning', '')
        }
        
        result = create_airtable_record(record)
        if result:
            print("✓ Created meta analysis report")
    
    # Generate guides for top 3 civs
    print("\n" + "="*60)
    print("Generating Top Tier Guides...")
    print("="*60)
    
    for i, civ_stats in enumerate(civs[:3]):
        civ_name = civ_stats['civilization'].replace('_', ' ').title()
        print(f"\nGenerating guide for #{i+1}: {civ_name}...")
        
        guide = generate_civ_specific_guide(civ_name, civ_stats, civs)
        if guide:
            record = {
                "title": f"{civ_name} - Current Meta Guide (Top Tier)",
                "civilization": civ_name,
                "matchup_vs": "Current Meta",
                "map_type": "Open",
                "early_game": guide.get('early_game', ''),
                "mid_game": guide.get('mid_game', ''),
                "late_game": guide.get('late_game', ''),
                "key_units": guide.get('key_units', ''),
                "key_technologies": guide.get('key_technologies', ''),
                "ai_confidence": guide.get('confidence', 80),
                "ai_reasoning": guide.get('reasoning', '')
            }
            
            result = create_airtable_record(record)
            if result:
                print(f"  ✓ Created guide for {civ_name}")
    
    print("\n" + "="*60)
    print("Meta Analysis Complete!")
    print("="*60)
