# Quick Start Guide - AoE4 AI Analysis System

## What You Have

Your Airtable base is now populated with:

✅ **22 Civilizations** - All AoE4 civs with complete data  
✅ **100 Units** - Core units with stats, costs, and abilities  
✅ **80+ Buildings** - Production and defensive structures  
✅ **100+ Technologies** - Research upgrades and effects  
✅ **8 AI Build Orders** - Ready-to-use strategies  
✅ **5 AI Strategy Analyses** - Matchup breakdowns  

## Access Your Database

**Airtable Base**: Age of Empires 4 - Game Data & AI Analysis  
**Base ID**: `appKeqSFMnexidZfd`

Open Airtable and navigate to this base to view all tables.

## Key Tables to Explore

### 1. Build Orders
View AI-generated build orders for different strategies:
- **English Dark Age Man-at-Arms Rush** - Aggressive early pressure
- **French Royal Knight Rush** - Fast cavalry timing
- **Chinese Boom into Song Dynasty** - Economic powerhouse
- And 5 more strategies!

Each build order includes:
- Step-by-step instructions with timings
- Villager count targets
- AI analysis of strengths/weaknesses

### 2. Strategy Analysis
Check out matchup analyses:
- **English vs French (Open maps)** - How to play this matchup
- **Mongols vs Chinese** - Mobile vs defensive strategies
- **Abbasid vs Rus (Closed maps)** - Economic competition
- And 2 more matchups!

Each analysis provides:
- Early, mid, and late game strategies
- Key units to build
- Important technologies to research
- AI confidence score

### 3. Units, Buildings, Technologies
Browse the complete game database:
- Filter by civilization
- Sort by cost or age
- Search for specific items
- View detailed stats

## Generate More AI Content

### Create New Build Orders

Want a build order for a different civ or strategy? Run:

```bash
cd /home/ubuntu
python3.11 generate_build_orders.py
```

Edit the script to add your desired civilizations and strategies in the `civs_to_process` list.

### Create New Strategy Analyses

Want analysis for different matchups? Run:

```bash
cd /home/ubuntu
python3.11 generate_strategy_analysis.py
```

Edit the `matchups` list to add your desired civ vs civ scenarios.

## Query the Database

### Using MCP CLI

```bash
# List all build orders
manus-mcp-cli tool call list_records --server airtable \
  --input '{"baseId": "appKeqSFMnexidZfd", "tableId": "Build Orders"}'

# Search for English units
manus-mcp-cli tool call search_records --server airtable \
  --input '{"baseId": "appKeqSFMnexidZfd", "tableId": "Units", "searchTerm": "english"}'

# Get all civilizations
manus-mcp-cli tool call list_records --server airtable \
  --input '{"baseId": "appKeqSFMnexidZfd", "tableId": "Civilizations"}'
```

## Use Cases

### 1. Learning New Civilizations
1. Open the **Civilizations** table
2. Read the civilization overview
3. Check the **Build Orders** table for that civ
4. Review **Strategy Analysis** for matchup tips

### 2. Preparing for Ranked Games
1. Identify your opponent's likely civilization
2. Check **Strategy Analysis** for your matchup
3. Review recommended **Units** and **Technologies**
4. Follow a **Build Order** that counters their strategy

### 3. Creating Content
1. Use **Build Orders** as video/stream content
2. Reference **Strategy Analysis** for educational material
3. Query **Units** table for stat comparisons
4. Generate new AI analyses for trending matchups

### 4. Tournament Preparation
1. Analyze meta civilizations in **Civilizations** table
2. Study multiple **Build Orders** for flexibility
3. Review **Strategy Analysis** for key matchups
4. Create custom analyses for specific opponents

## Next Steps

### Expand the Database

Import more data:
```bash
cd /home/ubuntu/data
python3.11 import_technologies.py  # Import more techs
```

### Customize AI Prompts

Edit the generation scripts to:
- Focus on specific playstyles
- Target certain map types
- Emphasize different ages
- Create specialized strategies

### Build Integrations

Use the Airtable API to:
- Create a Discord bot for strategy queries
- Build a web dashboard
- Connect to streaming overlays
- Integrate with replay analysis tools

## Tips for Best Results

### For Build Orders
- AI generates realistic timings based on game data
- Adapt steps based on opponent scouting
- Practice the build order in-game to refine
- Use as a framework, not rigid instructions

### For Strategy Analysis
- AI confidence scores indicate reliability
- Cross-reference with multiple analyses
- Consider your personal playstyle
- Adapt to specific map features

### For Database Queries
- Use filters to narrow results
- Sort by cost for economic planning
- Group by age for tech tree visualization
- Link records for relationship mapping

## Common Questions

**Q: Can I add my own build orders?**  
A: Yes! Use the Airtable interface to create new records in the Build Orders table.

**Q: How accurate is the AI analysis?**  
A: The AI uses actual game data and is trained on strategic concepts. Confidence scores indicate reliability. Always validate in practice.

**Q: Can I import more units/buildings?**  
A: Yes! The import scripts can process all 215 units. Edit the `max_import` variable to import more.

**Q: How do I update for new game patches?**  
A: Pull the latest data from the GitHub repository and re-run the import scripts.

**Q: Can I share this database?**  
A: You can share the Airtable base with others. Note that the original game data is subject to Microsoft's Game Content Usage Rules.

## Resources

- **Full Documentation**: See `AoE4_Airtable_Documentation.md`
- **GitHub Data Source**: https://github.com/aoe4world/data
- **All Scripts**: Located in `/home/ubuntu/` and `/home/ubuntu/data/`

## Get Started Now!

1. Open your Airtable base
2. Browse the **Build Orders** table
3. Try a build order in-game
4. Generate more AI content as needed

Enjoy your AI-powered Age of Empires 4 strategy system! 🎮🤖
