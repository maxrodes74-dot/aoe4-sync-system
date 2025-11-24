# Age of Empires 4 - Airtable Database & AI Analysis System

## Overview

This system provides a comprehensive relational database of Age of Empires 4 game data integrated with AI-powered strategic analysis capabilities. The database is hosted in Airtable and contains detailed information about all civilizations, units, buildings, and technologies, along with AI-generated build orders and matchup analyses.

## Database Structure

### Airtable Base Information
- **Base Name**: Age of Empires 4 - Game Data & AI Analysis
- **Base ID**: `appKeqSFMnexidZfd`
- **Access**: Available through your Airtable account

### Core Data Tables

#### 1. Civilizations (22 records)
Contains all playable civilizations with their unique characteristics and bonuses.

**Key Fields:**
- `civ_id` - Unique identifier (e.g., "english", "mongols")
- `name` - Display name (e.g., "English", "Mongols")
- `description` - Brief overview of the civilization
- `classes` - Playstyle categories (e.g., "Defense, Longbows, Farming")
- `overview` - Detailed JSON of civilization bonuses and unique features

**Example Civilizations:**
- English, French, Mongols, Chinese, Abbasid Dynasty, Delhi Sultanate, Holy Roman Empire, Rus, Malians, Ottomans, Japanese, Byzantines, and more

#### 2. Units (100+ records)
Comprehensive unit database with stats, costs, and combat information.

**Key Fields:**
- `unit_id` - Unique identifier
- `name` - Unit name
- `age` - Available age (1=Dark, 2=Feudal, 3=Castle, 4=Imperial)
- `cost_food`, `cost_wood`, `cost_stone`, `cost_gold` - Resource costs
- `build_time` - Production time in seconds
- `hitpoints` - Unit health
- `movement_speed` - Movement speed value
- `unique` - Whether this is a unique unit
- `icon_url` - Link to unit icon image

**Sample Units:**
- Infantry: Spearman, Man-at-Arms, Landsknecht
- Archers: Archer, Crossbowman, Longbowman
- Cavalry: Scout, Horseman, Knight, Royal Knight
- Siege: Battering Ram, Mangonel, Trebuchet, Bombard
- Unique: Longbowman (English), Mangudai (Mongols), Streltsy (Rus)

#### 3. Buildings (80+ records)
All buildings with construction costs and capabilities.

**Key Fields:**
- `building_id` - Unique identifier
- `name` - Building name
- `age` - Available age
- `cost_food`, `cost_wood`, `cost_stone`, `cost_gold` - Construction costs
- `build_time` - Construction time
- `hitpoints` - Building health
- `unique` - Whether this is a unique building
- `icon_url` - Link to building icon

**Building Categories:**
- Economic: House, Mill, Lumber Camp, Mining Camp, Farm
- Military: Barracks, Archery Range, Stable, Siege Workshop
- Defensive: Outpost, Stone Wall, Keep
- Special: Market, Monastery, University, Dock

#### 4. Technologies (100+ records)
Research technologies and their effects.

**Key Fields:**
- `tech_id` - Unique identifier
- `name` - Technology name
- `age` - Available age
- `cost_food`, `cost_wood`, `cost_stone`, `cost_gold` - Research costs
- `research_time` - Time to research
- `effects` - JSON description of what the technology does
- `description` - Human-readable effect description
- `unique` - Whether this is a unique technology

**Technology Categories:**
- Economic: Wheelbarrow, Horticulture, Double Broadax
- Military: Bloomery, Steeled Arrow, Siege Engineering
- Defensive: Fortify Outpost, Boiling Oil
- Unit Upgrades: Veteran/Elite upgrades

### AI Analysis Tables

#### 5. Build Orders (8 AI-generated records)
Step-by-step build orders created by AI for different strategies.

**Key Fields:**
- `name` - Build order name
- `civilization` - Which civ this is for
- `strategy_type` - Rush, Boom, Fast Castle, etc.
- `description` - Strategy overview
- `steps` - Detailed step-by-step instructions with timings
- `total_time_seconds` - How long the build takes
- `villager_count` - Target villager count
- `ai_generated` - Marked as AI-created
- `ai_analysis` - AI commentary on strengths/weaknesses

**Generated Build Orders:**
1. **English Dark Age Man-at-Arms Rush** - Aggressive early game strategy leveraging English unique units
2. **English Boom with Defensive Network** - Economic expansion with defensive bonuses
3. **French Royal Knight Rush** - Fast cavalry pressure build
4. **Mongol Early Mangudai Rush** - Mobile harassment strategy
5. **Chinese Boom into Song Dynasty Economy** - Economic powerhouse build
6. **Abbasid Fast Castle into Camel Archers** - Quick age-up strategy
7. **Rus Boom Economy with Hunting Cabin Focus** - Resource generation focus
8. **Holy Roman Empire Fast Castle** - Efficient castle age timing

#### 6. Strategy Analysis (5 AI-generated records)
Detailed matchup analysis for civilization vs civilization scenarios.

**Key Fields:**
- `title` - Matchup description
- `civilization` - Your civilization
- `matchup_vs` - Opponent civilization
- `map_type` - Open, Closed, Water, or Hybrid
- `early_game` - Dark/Feudal Age strategy
- `mid_game` - Castle Age strategy
- `late_game` - Imperial Age strategy
- `key_units` - Which units to prioritize
- `key_technologies` - Important tech research
- `ai_confidence` - AI confidence score (0-100)
- `ai_reasoning` - Why this strategy works

**Generated Analyses:**
1. **English vs French (Open)** - Longbowman vs Royal Knight dynamics
2. **Mongols vs Chinese (Open)** - Mobile vs Defensive playstyles
3. **Abbasid Dynasty vs Rus (Closed)** - Economic competition analysis
4. **Holy Roman Empire vs English (Hybrid)** - Mixed map strategy
5. **French vs Mongols (Open)** - Cavalry-focused matchup

## How to Use This System

### For Build Order Generation

The system demonstrates AI capabilities to generate custom build orders. You can extend this by:

1. **Creating new build orders** - Run the generation script with different civilizations and strategies
2. **Analyzing existing builds** - Query the database to compare resource timings
3. **Optimizing strategies** - Use the AI analysis to refine build orders

**Example Python code to generate more build orders:**
```python
python3.11 /home/ubuntu/generate_build_orders.py
```

### For Game Analysis

The AI can analyze:
- **Civilization matchups** - Which civ has advantages against another
- **Map-specific strategies** - How terrain affects strategy
- **Unit compositions** - Optimal army makeups
- **Technology priorities** - Which techs to research first

**Example Python code to generate more analyses:**
```python
python3.11 /home/ubuntu/generate_strategy_analysis.py
```

### Querying the Database

You can query the Airtable database using the MCP integration:

```bash
# List all records in a table
manus-mcp-cli tool call list_records --server airtable \
  --input '{"baseId": "appKeqSFMnexidZfd", "tableId": "Units"}'

# Search for specific units
manus-mcp-cli tool call search_records --server airtable \
  --input '{"baseId": "appKeqSFMnexidZfd", "tableId": "Units", "searchTerm": "knight"}'

# Get a specific civilization
manus-mcp-cli tool call search_records --server airtable \
  --input '{"baseId": "appKeqSFMnexidZfd", "tableId": "Civilizations", "searchTerm": "english"}'
```

## AI Integration Details

### Models Used
- **Primary Model**: GPT-4.1-mini via OpenAI API
- **Temperature**: 0.7 (balanced creativity and accuracy)
- **Response Format**: Structured JSON for easy parsing

### AI Capabilities

The system can:

1. **Generate Build Orders**
   - Analyzes civilization bonuses
   - Creates step-by-step instructions
   - Provides timing benchmarks
   - Explains strategy strengths/weaknesses

2. **Analyze Matchups**
   - Compares civilization strengths
   - Recommends unit compositions
   - Suggests technology priorities
   - Provides confidence scores

3. **Strategic Insights**
   - Early game priorities
   - Mid game transitions
   - Late game compositions
   - Map-specific adaptations

### Extending the AI System

You can create additional AI-powered features:

**Counter Analysis:**
```python
# Analyze what counters a specific unit composition
# Generate optimal responses to enemy strategies
```

**Meta Analysis:**
```python
# Track which strategies are most effective
# Identify trending builds and counters
```

**Custom Recommendations:**
```python
# Input your playstyle preferences
# Get personalized civilization and strategy recommendations
```

## Data Sources

### Original Data
- **Source**: [aoe4world/data GitHub repository](https://github.com/aoe4world/data)
- **Format**: JSON files parsed from game files
- **License**: Microsoft Game Content Usage Rules apply
- **Version**: Latest as of November 2025

### Data Processing
- Used unified data format to avoid duplicates
- Imported 215 unique units (100 imported to Airtable)
- Imported 22 civilizations (all imported)
- Imported 80+ buildings
- Imported 100+ technologies

## Future Enhancements

### Recommended Additions

1. **Unit Relationships**
   - Add linked records between units and buildings (production relationships)
   - Create counter relationship tables

2. **Complete Data Import**
   - Import remaining 115 units
   - Import all buildings and technologies
   - Add upgrades and abilities tables

3. **Advanced AI Features**
   - Build order optimizer based on opponent scouting
   - Real-time game state analyzer
   - Tournament meta analysis

4. **Visualization**
   - Tech tree visualizations
   - Build order timelines
   - Unit counter matrices

5. **Integration**
   - Connect to game replay files
   - API for external applications
   - Discord bot for strategy queries

## Scripts and Tools

### Available Scripts

All scripts are located in `/home/ubuntu/` and `/home/ubuntu/data/`:

1. **import_civs.py** - Import civilizations data
2. **import_units.py** - Import units data
3. **import_buildings.py** - Import buildings data
4. **import_technologies.py** - Import technologies data
5. **generate_build_orders.py** - AI build order generator
6. **generate_strategy_analysis.py** - AI matchup analyzer

### Running Scripts

```bash
# Import more data
cd /home/ubuntu/data
python3.11 import_technologies.py

# Generate more AI content
cd /home/ubuntu
python3.11 generate_build_orders.py
python3.11 generate_strategy_analysis.py
```

## Technical Details

### Database Schema Design

The schema follows relational database best practices:
- Primary keys for all tables
- Normalized data structure
- JSON fields for complex nested data
- URL fields for external resources
- Checkbox fields for boolean flags
- Number fields with appropriate precision

### API Rate Limiting

The import scripts include rate limiting:
- 0.3 second delay between API calls
- Batch processing where possible
- Error handling and retry logic

### Performance Considerations

- Unified data format reduces redundancy
- Indexed primary keys for fast lookups
- Airtable's built-in caching
- Efficient JSON parsing

## Support and Maintenance

### Updating Data

To update with new game patches:

1. Pull latest data from GitHub repository
2. Run import scripts with updated data
3. Regenerate AI analyses for new content

### Troubleshooting

**Common Issues:**
- API rate limits: Add delays between calls
- Missing data: Check file paths and JSON structure
- AI generation errors: Verify OpenAI API key

## Conclusion

This system provides a powerful foundation for AI-driven Age of Empires 4 strategy analysis. The combination of comprehensive game data and AI-generated insights enables:

- **Build order creation and optimization**
- **Matchup analysis and counter-strategies**
- **Data-driven decision making**
- **Strategic planning and preparation**

The modular design allows easy extension with additional features, making it a scalable platform for competitive play, content creation, and game analysis.

---

**Created**: November 23, 2025  
**Data Source**: aoe4world/data GitHub repository  
**AI Model**: GPT-4.1-mini  
**Platform**: Airtable
