# AoE4 World API Integration Guide

## Overview

Your Airtable database now includes **live data integration** with the AoE4 World API! This provides real-time competitive statistics, player rankings, and meta analysis to enhance your strategic insights.

## What's New

### New Tables

#### 1. Civilization Meta Stats
Real-time win rates, pick rates, and performance metrics for all civilizations.

**Data Includes:**
- Win rate percentage (current patch)
- Pick rate percentage (how often played)
- Total games played
- Average game duration
- Patch version
- Rank-specific data (optional)

**Use Cases:**
- Identify strongest civilizations in current meta
- Track meta shifts across patches
- Compare performance at different rank levels
- Inform civilization selection for ranked games

#### 2. Leaderboard Players
Top 50 players from the ranked solo leaderboard.

**Data Includes:**
- Player name and profile ID
- Current rank and rating (ELO)
- Win rate and total games
- Rank level (Conqueror, Diamond, etc.)
- Country
- Last game timestamp

**Use Cases:**
- Study top player preferences
- Analyze high-level strategies
- Track rising stars
- Identify coaching opportunities

### Enhanced AI Analysis

#### 3. Meta Analysis Reports (in Strategy Analysis table)
AI-generated insights using live competitive data.

**New Analysis Types:**
- **Overall Meta Report** - Current patch meta overview
- **Top Tier Guides** - How to play the strongest civs
- **Underdog Guides** - How to win with weaker civs

**What Makes This Special:**
- Uses REAL competitive data, not just theory
- Updates based on actual win rates and pick rates
- Identifies current power picks and counters
- Provides rank-specific insights

## API Endpoints Available

The AoE4 World API provides extensive data. Here are the key endpoints:

### Civilization Statistics
```
GET https://aoe4world.com/api/v0/stats/rm_solo/civilizations
GET https://aoe4world.com/api/v0/stats/rm_team/civilizations
```
Parameters:
- `rank_level`: bronze, silver, gold, platinum, diamond, conqueror
- `patch`: specific patch version

### Leaderboards
```
GET https://aoe4world.com/api/v0/leaderboards/rm_solo
GET https://aoe4world.com/api/v0/leaderboards/rm_team
```
Parameters:
- `page`: pagination
- `query`: search player names
- `country`: filter by country code
- `profile_id`: specific player(s)

### Player Data
```
GET https://aoe4world.com/api/v0/players/:profile_id
GET https://aoe4world.com/api/v0/players/:profile_id/games
```
Get detailed player stats and match history.

### Map Statistics
```
GET https://aoe4world.com/api/v0/stats/rm_solo/maps
```
Win rates and performance by map.

### Full API Documentation
Visit: https://aoe4world.com/api

## Sync Scripts

### 1. Sync Civilization Meta Stats
```bash
python3.11 /home/ubuntu/sync_civ_meta_stats.py
```

**What it does:**
- Fetches current win rates and pick rates
- Updates Civilization Meta Stats table
- Includes patch version and timestamp

**Customization:**
Edit the script to sync rank-specific data:
```python
sync_stats("rm_solo", "conqueror")  # Conqueror rank only
sync_stats("rm_solo", "diamond")     # Diamond rank
sync_stats("rm_team", None)          # Team games
```

### 2. Sync Leaderboard Players
```bash
python3.11 /home/ubuntu/sync_leaderboard.py
```

**What it does:**
- Fetches top 50 players from ranked solo
- Updates Leaderboard Players table
- Includes ratings, win rates, and last game info

**Customization:**
```python
sync_leaderboard("rm_solo", top_n=100)  # Top 100 players
sync_leaderboard("rm_team", top_n=50)   # Team leaderboard
```

### 3. Generate AI Meta Analysis
```bash
python3.11 /home/ubuntu/generate_meta_analysis.py
```

**What it does:**
- Fetches live competitive statistics
- Uses AI to analyze current meta
- Creates guides for top and bottom performing civs
- Adds reports to Strategy Analysis table

**Output:**
- 1 overall meta report
- 3 top-tier civilization guides
- 2 underdog civilization guides

## Automation Options

### Option 1: Manual Updates
Run the sync scripts whenever you want fresh data:
```bash
cd /home/ubuntu
python3.11 sync_civ_meta_stats.py
python3.11 sync_leaderboard.py
python3.11 generate_meta_analysis.py
```

### Option 2: Scheduled Updates
Set up automatic syncing using cron jobs or scheduled tasks.

**Daily sync example:**
```bash
# Add to crontab to run daily at 6 AM
0 6 * * * cd /home/ubuntu && python3.11 sync_civ_meta_stats.py
0 6 * * * cd /home/ubuntu && python3.11 sync_leaderboard.py
```

**Weekly meta analysis:**
```bash
# Run every Sunday at 8 AM
0 8 * * 0 cd /home/ubuntu && python3.11 generate_meta_analysis.py
```

### Option 3: On-Demand via Airtable Automations
Create Airtable automations that trigger the sync scripts via webhooks or external services.

## Current Data Snapshot

### Civilization Meta (as of sync)
**Top 5 Performing:**
1. **Golden Horde** - 54.58% WR, 7.98% PR
2. **Knights Templar** - 52.76% WR, 5.18% PR
3. **Japanese** - 52.76% WR, 6.84% PR
4. **Order of the Dragon** - 52.71% WR, 3.95% PR
5. **Ayyubids** - 52.17% WR, 1.72% PR

**Bottom 5 Performing:**
1. **Rus** - 43.88% WR, 2.52% PR
2. **Chinese** - 44.97% WR, 3.51% PR
3. **Holy Roman Empire** - 45.69% WR, 4.33% PR
4. **Abbasid Dynasty** - 46.45% WR, 1.86% PR
5. **Sengoku Daimyo** - 46.95% WR, 6.70% PR

### Leaderboard Top 5
1. **VortiX** - 2315 ELO
2. **酷不酷** - 2288 ELO
3. **El Sensei** - 2272 ELO
4. **David Kim** - 2195 ELO
5. **ORANGUTAN** - 2177 ELO

## Advanced Use Cases

### 1. Meta Tracking Dashboard
Create Airtable views to:
- Sort civs by win rate
- Filter by rank level
- Track changes over time
- Identify emerging trends

### 2. Player Analysis
- Study top player civilization preferences
- Analyze win rates by rank
- Identify coaching opportunities
- Track your own progress vs leaderboard

### 3. Content Creation
- Generate meta reports for videos/streams
- Create tier lists based on real data
- Analyze patch impact
- Predict tournament picks

### 4. Competitive Preparation
- Identify strongest meta picks
- Study counter strategies
- Analyze opponent preferences
- Prepare rank-specific builds

### 5. AI-Enhanced Strategy
Combine static game data with live stats:
- AI generates builds for current meta
- Matchup analysis using win rate data
- Rank-specific strategy recommendations
- Counter-meta strategies

## Data Freshness

### Update Frequency Recommendations

**Civilization Meta Stats:**
- Update: Daily or after patches
- Reason: Meta shifts quickly after balance changes
- Critical for: Ranked play, content creation

**Leaderboard Players:**
- Update: Weekly
- Reason: Rankings change gradually
- Critical for: Studying top play, coaching

**AI Meta Analysis:**
- Update: Weekly or after patches
- Reason: Requires processing time, meta needs to stabilize
- Critical for: Strategic planning, content

## API Rate Limits

The AoE4 World API is public and doesn't require authentication for most endpoints. However:

- Be respectful with request frequency
- Add delays between bulk requests (scripts include 0.3s delays)
- Cache data when possible
- Don't hammer the API

## Extending the Integration

### Additional Endpoints to Consider

**Map Statistics:**
```python
# Get win rates by map
url = "https://aoe4world.com/api/v0/stats/rm_solo/maps"
```

**Player Match History:**
```python
# Get recent games for a player
url = f"https://aoe4world.com/api/v0/players/{profile_id}/games"
```

**Civilization Matchup Matrix:**
```python
# Get civ vs civ win rates
url = f"https://aoe4world.com/api/v0/stats/rm_solo/matchups"
```

**Esports Tournament Data:**
```python
# Get tournament leaderboard
url = "https://aoe4world.com/api/v0/esports/leaderboards/1"
```

### Creating New Tables

Want to add more API data? Create new tables:

```bash
# Example: Map Statistics table
manus-mcp-cli tool call create_table --server airtable --input '{
  "baseId": "appKeqSFMnexidZfd",
  "name": "Map Statistics",
  "description": "Win rates and statistics by map",
  "fields": [
    {"name": "map_name", "type": "singleLineText"},
    {"name": "win_rate", "type": "number", "options": {"precision": 2}},
    {"name": "games_count", "type": "number", "options": {"precision": 0}}
  ]
}'
```

Then create a sync script following the pattern in `sync_civ_meta_stats.py`.

## Troubleshooting

### API Connection Issues
```python
# Test API connectivity
curl https://aoe4world.com/api/v0/stats/rm_solo/civilizations
```

### Airtable Sync Errors
- Check base ID is correct: `appKeqSFMnexidZfd`
- Verify table names match exactly
- Ensure MCP integration is active

### Missing Data
- API may be temporarily unavailable
- Patch changes can affect data structure
- Check script output for specific errors

## Best Practices

1. **Regular Updates**: Sync data regularly for accurate insights
2. **Backup Data**: Export Airtable data before major updates
3. **Version Control**: Keep scripts in version control
4. **Monitor Changes**: Track when meta shifts occur
5. **Validate Data**: Cross-check with in-game experience

## Integration Architecture

```
AoE4 World API
      ↓
Python Sync Scripts
      ↓
Airtable Database
      ↓
AI Analysis (OpenAI)
      ↓
Strategic Insights
```

## Next Steps

### Immediate Actions
1. ✅ Run sync scripts to get latest data
2. ✅ Review meta analysis reports in Airtable
3. ✅ Explore leaderboard players table
4. ✅ Check civilization meta stats

### Future Enhancements
1. **Automated Scheduling** - Set up cron jobs for regular syncs
2. **Map Statistics** - Add map-specific win rates
3. **Matchup Matrix** - Create civ vs civ win rate table
4. **Player Tracking** - Follow specific players over time
5. **Tournament Data** - Integrate esports statistics
6. **Web Dashboard** - Build a visual interface
7. **Discord Bot** - Query data via Discord commands

## Resources

- **AoE4 World Website**: https://aoe4world.com
- **API Documentation**: https://aoe4world.com/api
- **GitHub Data Repository**: https://github.com/aoe4world/data
- **Your Airtable Base**: Age of Empires 4 - Game Data & AI Analysis

## Support

For API-related questions:
- Check AoE4 World API documentation
- Visit AoE4 World Discord/community

For Airtable integration:
- Review script comments
- Check Airtable MCP documentation
- Test with smaller datasets first

---

**Your database is now powered by live competitive data!** 🚀

Use these insights to dominate the ladder, create compelling content, and stay ahead of the meta.
