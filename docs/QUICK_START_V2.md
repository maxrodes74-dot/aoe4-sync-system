# Quick Start Guide v2 - AoE4 AI Analysis System with Live API Data

## What's New in V2

🎉 **Live API Integration!** Your database now pulls real-time data from AoE4 World:

✅ **Live Civilization Meta Stats** - Current win rates and pick rates  
✅ **Top 50 Leaderboard Players** - Real rankings and ratings  
✅ **AI Meta Analysis** - Insights using live competitive data  

## Your Complete Database

### Static Game Data
✅ 22 Civilizations with bonuses  
✅ 100+ Units with stats  
✅ 80+ Buildings  
✅ 100+ Technologies  
✅ 8 AI Build Orders  

### Live API Data (NEW!)
✅ 22 Civilization Meta Stats (current patch)  
✅ 50 Top Players from leaderboard  
✅ 6 AI Meta Analysis reports (using live data)  

## Access Your Database

**Airtable Base**: Age of Empires 4 - Game Data & AI Analysis  
**Base ID**: `appKeqSFMnexidZfd`

## Quick Actions

### View Current Meta
1. Open **Civilization Meta Stats** table
2. Sort by `win_rate` (descending)
3. See which civs are dominating right now!

**Current Top 3:**
- Golden Horde: 54.58% WR
- Knights Templar: 52.76% WR  
- Japanese: 52.76% WR

### Check Top Players
1. Open **Leaderboard Players** table
2. See current #1: VortiX at 2315 ELO
3. Study their preferred strategies

### Read AI Meta Analysis
1. Open **Strategy Analysis** table
2. Find "Current Meta Analysis - Patch" entry
3. Read AI insights on why certain civs dominate
4. Check guides for top-tier and underdog civs

## Update Live Data

### Get Latest Stats
```bash
cd /home/ubuntu
python3.11 sync_civ_meta_stats.py
```
Updates civilization win rates and pick rates.

### Refresh Leaderboard
```bash
cd /home/ubuntu
python3.11 sync_leaderboard.py
```
Gets current top 50 players.

### Generate New Meta Analysis
```bash
cd /home/ubuntu
python3.11 generate_meta_analysis.py
```
Creates AI reports using latest competitive data.

## Use Cases

### 1. Ranked Preparation
**Before your session:**
1. Check **Civilization Meta Stats** for strongest picks
2. Read **AI Meta Analysis** for current strategies
3. Review **Build Orders** for your chosen civ
4. Study **Strategy Analysis** for key matchups

### 2. Content Creation
**For videos/streams:**
1. Pull latest meta stats for tier lists
2. Use AI analysis for talking points
3. Reference top player data
4. Create data-driven content

### 3. Learning & Improvement
**To get better:**
1. Study **Leaderboard Players** preferences
2. Compare your stats to meta averages
3. Follow AI recommendations
4. Practice builds for meta civs

### 4. Meta Tracking
**Stay ahead of changes:**
1. Sync data after patches
2. Compare win rates over time
3. Identify emerging strategies
4. Predict tournament picks

## Key Tables Explained

### Civilization Meta Stats (NEW!)
**What it shows:** Real competitive performance  
**Updated:** Run sync script anytime  
**Use for:** Picking strongest civs, tracking meta

**Key Fields:**
- `win_rate`: How often this civ wins
- `pick_rate`: How often it's played
- `games_count`: Sample size
- `patch`: Current game version

### Leaderboard Players (NEW!)
**What it shows:** Top 50 ranked players  
**Updated:** Run sync script anytime  
**Use for:** Studying high-level play

**Key Fields:**
- `rank`: Current leaderboard position
- `rating`: ELO rating
- `win_rate`: Player's win percentage
- `country`: Player's country

### Strategy Analysis (Enhanced!)
**What it shows:** AI strategic insights  
**Now includes:** Live data-based analysis  
**Use for:** Learning matchups and strategies

**New Analysis Types:**
- Overall meta reports
- Top-tier civilization guides
- Underdog "how to win" guides

## Sample Workflow

### Morning Routine (5 minutes)
```bash
# Update all live data
cd /home/ubuntu
python3.11 sync_civ_meta_stats.py
python3.11 sync_leaderboard.py
```

Then in Airtable:
1. Check meta stats for changes
2. Review top player movements
3. Adjust your civ pool accordingly

### Weekly Deep Dive (30 minutes)
```bash
# Generate fresh AI analysis
cd /home/ubuntu
python3.11 generate_meta_analysis.py
```

Then:
1. Read new meta analysis report
2. Study top-tier civ guides
3. Practice recommended builds
4. Update your strategy notes

### Pre-Tournament (1 hour)
1. Sync all latest data
2. Generate meta analysis
3. Study opponent preferences (if known)
4. Prepare counter-strategies
5. Practice key matchups

## Pro Tips

### For Competitive Players
- Sync data daily during active patches
- Focus on Conqueror/Diamond rank stats
- Study top player civilization choices
- Use AI analysis to identify counters

### For Content Creators
- Generate meta reports weekly
- Create tier lists from real data
- Reference top player stats
- Use AI insights for video scripts

### For Learners
- Compare your performance to meta averages
- Study underdog guides for off-meta picks
- Follow build orders for meta civs
- Track your improvement over time

## Automation Ideas

### Daily Auto-Sync
Set up a cron job to sync data automatically:
```bash
# Add to crontab
0 6 * * * cd /home/ubuntu && python3.11 sync_civ_meta_stats.py
```

### Weekly Reports
Generate meta analysis every Sunday:
```bash
0 8 * * 0 cd /home/ubuntu && python3.11 generate_meta_analysis.py
```

### Discord Notifications
Integrate with Discord to get meta updates automatically.

## Understanding the Meta

### Win Rate vs Pick Rate
- **High WR, Low PR**: Sleeper pick, underutilized
- **High WR, High PR**: Meta dominant, expect nerfs
- **Low WR, High PR**: Popular but weak, avoid
- **Low WR, Low PR**: Needs buffs or better understanding

### Current Meta Insights
Based on latest sync:

**Overperforming:** Golden Horde, Knights Templar, Japanese  
**Meta Staples:** French, English (high pick rate)  
**Underperforming:** Rus, Chinese, HRE  
**Sleeper Picks:** Ayyubids (52% WR, 1.7% PR)

## Common Questions

**Q: How often should I sync data?**  
A: Daily for active players, weekly for casual. Always after patches.

**Q: Is the API data accurate?**  
A: Yes! It's from actual ranked games on AoE4 World.

**Q: Can I track specific players?**  
A: Yes! Use the player API endpoints (see API Integration Guide).

**Q: What if a civilization isn't in the meta stats?**  
A: All 22 civs are included. Check the sync script output.

**Q: How does AI use live data?**  
A: It analyzes win rates, pick rates, and game counts to generate insights.

## Next Steps

### Immediate (Do Now)
1. ✅ Open Airtable and explore new tables
2. ✅ Run sync scripts to get latest data
3. ✅ Read the current meta analysis
4. ✅ Pick a top-tier civ to practice

### Short Term (This Week)
1. Set up daily data syncing
2. Study top player preferences
3. Practice meta builds
4. Track your win rate vs meta average

### Long Term (This Month)
1. Build automation for data updates
2. Create custom views in Airtable
3. Develop your meta-specific strategies
4. Share insights with your community

## Resources

- **Full API Guide**: See `API_INTEGRATION_GUIDE.md`
- **Original Documentation**: See `AoE4_Airtable_Documentation.md`
- **AoE4 World**: https://aoe4world.com
- **API Docs**: https://aoe4world.com/api

## Get Started Now!

1. Open Airtable → **Civilization Meta Stats**
2. Sort by win rate
3. Pick a top-tier civ
4. Check **Build Orders** for that civ
5. Read **Strategy Analysis** for matchups
6. Go dominate! 🎮🏆

---

**Your AI-powered, live-data-enhanced AoE4 strategy system is ready!**

Stay ahead of the meta. Make data-driven decisions. Climb the ladder. 🚀
