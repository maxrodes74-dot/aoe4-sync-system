# Age of Empires 4 - Airtable Database Schema

## Overview
This database is designed to support AI-powered build order generation and game analysis for Age of Empires 4.

## Core Data Tables

### 1. Civilizations
**Purpose**: Store all civilization data with their unique characteristics
**Fields**:
- `civ_id` (Primary Key, Single Line Text)
- `name` (Single Line Text)
- `description` (Long Text)
- `classes` (Single Line Text) - e.g., "Defense, Longbows, Farming"
- `overview` (Long Text) - JSON formatted civilization bonuses and features
- `techtree` (Long Text) - JSON formatted tech tree structure

### 2. Units
**Purpose**: Store all unit data with stats and relationships
**Fields**:
- `unit_id` (Primary Key, Single Line Text)
- `base_id` (Single Line Text)
- `name` (Single Line Text)
- `age` (Number) - 1-4 representing Dark Age to Imperial Age
- `civilizations` (Multiple Select or Link to Civilizations)
- `description` (Long Text)
- `classes` (Long Text) - JSON array of unit classes
- `display_classes` (Single Line Text)
- `unique` (Checkbox) - Is this a unique unit?
- `cost_food` (Number)
- `cost_wood` (Number)
- `cost_stone` (Number)
- `cost_gold` (Number)
- `cost_total` (Number)
- `cost_popcap` (Number)
- `build_time` (Number)
- `produced_by` (Link to Buildings) - Multiple links
- `hitpoints` (Number)
- `weapons` (Long Text) - JSON array
- `armor` (Long Text) - JSON array
- `movement_speed` (Number)
- `sight_line` (Number)
- `icon_url` (URL)

### 3. Buildings
**Purpose**: Store all building data
**Fields**:
- `building_id` (Primary Key, Single Line Text)
- `base_id` (Single Line Text)
- `name` (Single Line Text)
- `age` (Number)
- `civilizations` (Multiple Select or Link to Civilizations)
- `description` (Long Text)
- `classes` (Long Text) - JSON array
- `display_classes` (Single Line Text)
- `unique` (Checkbox)
- `cost_food` (Number)
- `cost_wood` (Number)
- `cost_stone` (Number)
- `cost_gold` (Number)
- `cost_total` (Number)
- `build_time` (Number)
- `produced_by` (Link to Units) - Usually villager
- `hitpoints` (Number)
- `armor` (Long Text) - JSON array
- `icon_url` (URL)
- `produces_units` (Link to Units) - Multiple links
- `produces_technologies` (Link to Technologies) - Multiple links

### 4. Technologies
**Purpose**: Store all technology/upgrade data
**Fields**:
- `tech_id` (Primary Key, Single Line Text)
- `base_id` (Single Line Text)
- `name` (Single Line Text)
- `age` (Number)
- `civilizations` (Multiple Select or Link to Civilizations)
- `description` (Long Text)
- `classes` (Long Text) - JSON array
- `display_classes` (Single Line Text)
- `unique` (Checkbox)
- `cost_food` (Number)
- `cost_wood` (Number)
- `cost_stone` (Number)
- `cost_gold` (Number)
- `cost_total` (Number)
- `research_time` (Number)
- `produced_by` (Link to Buildings)
- `effects` (Long Text) - JSON array describing what the tech does
- `icon_url` (URL)

### 5. Upgrades
**Purpose**: Store unit upgrade paths (e.g., Veteran to Elite)
**Fields**:
- `upgrade_id` (Primary Key, Single Line Text)
- `base_id` (Single Line Text)
- `name` (Single Line Text)
- `age` (Number)
- `civilizations` (Multiple Select or Link to Civilizations)
- `description` (Long Text)
- `cost_food` (Number)
- `cost_wood` (Number)
- `cost_stone` (Number)
- `cost_gold` (Number)
- `cost_total` (Number)
- `research_time` (Number)
- `produced_by` (Link to Buildings)
- `affects_units` (Link to Units) - Multiple links
- `icon_url` (URL)

### 6. Abilities
**Purpose**: Store special abilities units and buildings can use
**Fields**:
- `ability_id` (Primary Key, Single Line Text)
- `base_id` (Single Line Text)
- `name` (Single Line Text)
- `age` (Number)
- `civilizations` (Multiple Select or Link to Civilizations)
- `description` (Long Text)
- `classes` (Long Text) - JSON array
- `icon_url` (URL)

## AI Analysis Tables

### 7. Build Orders
**Purpose**: Store AI-generated and community build orders
**Fields**:
- `build_order_id` (Auto Number, Primary Key)
- `name` (Single Line Text)
- `civilization` (Link to Civilizations)
- `strategy_type` (Single Select) - e.g., "Rush", "Boom", "Turtle", "All-in"
- `target_age` (Single Select) - "Dark Age", "Feudal Age", "Castle Age", "Imperial Age"
- `description` (Long Text)
- `steps` (Long Text) - JSON array of build order steps with timing
- `total_time` (Number) - Estimated time to complete in seconds
- `villager_count` (Number) - Final villager count
- `resources_needed` (Long Text) - JSON object with resource requirements
- `counters` (Multiple Select) - What strategies this counters
- `countered_by` (Multiple Select) - What strategies counter this
- `ai_generated` (Checkbox)
- `ai_analysis` (Long Text) - AI commentary on strengths/weaknesses
- `win_rate` (Number) - If available from game data
- `created_date` (Created Time)
- `updated_date` (Last Modified Time)

### 8. Unit Compositions
**Purpose**: Store effective unit combinations for different scenarios
**Fields**:
- `composition_id` (Auto Number, Primary Key)
- `name` (Single Line Text)
- `civilization` (Link to Civilizations)
- `age` (Single Select)
- `units` (Link to Units) - Multiple links
- `unit_ratios` (Long Text) - JSON object describing ideal ratios
- `total_cost` (Number) - Total resource cost
- `purpose` (Single Select) - "Anti-Infantry", "Anti-Cavalry", "Anti-Siege", "Mixed", etc.
- `effectiveness_score` (Number) - AI-calculated effectiveness
- `counters` (Link to Unit Compositions)
- `countered_by` (Link to Unit Compositions)
- `ai_analysis` (Long Text)
- `created_date` (Created Time)

### 9. Strategy Analysis
**Purpose**: Store AI-generated strategic insights
**Fields**:
- `analysis_id` (Auto Number, Primary Key)
- `civilization` (Link to Civilizations)
- `matchup_vs` (Link to Civilizations) - Opponent civilization
- `map_type` (Single Select) - "Open", "Closed", "Water", "Hybrid"
- `recommended_strategy` (Single Select)
- `early_game_focus` (Long Text)
- `mid_game_focus` (Long Text)
- `late_game_focus` (Long Text)
- `key_units` (Link to Units) - Multiple links
- `key_technologies` (Link to Technologies) - Multiple links
- `key_buildings` (Link to Buildings) - Multiple links
- `timing_attacks` (Long Text) - JSON array of timing windows
- `economic_priorities` (Long Text)
- `ai_confidence_score` (Number) - 0-100
- `ai_reasoning` (Long Text)
- `created_date` (Created Time)
- `updated_date` (Last Modified Time)

### 10. Counter Relationships
**Purpose**: Track what units/buildings counter what
**Fields**:
- `counter_id` (Auto Number, Primary Key)
- `unit_or_building` (Single Line Text) - ID reference
- `counters` (Long Text) - JSON array of what this counters
- `countered_by` (Long Text) - JSON array of what counters this
- `effectiveness_rating` (Number) - 1-10 scale
- `ai_notes` (Long Text)

## Relationships

### Key Relationships:
1. **Civilizations → Units**: One-to-Many (A civ has many units)
2. **Civilizations → Buildings**: One-to-Many
3. **Civilizations → Technologies**: One-to-Many
4. **Buildings → Units**: Many-to-Many (Buildings produce units)
5. **Buildings → Technologies**: Many-to-Many (Buildings enable technologies)
6. **Technologies → Units**: Many-to-Many (Technologies affect units)
7. **Build Orders → Civilizations**: Many-to-One
8. **Build Orders → Units**: Many-to-Many (Build orders use specific units)
9. **Unit Compositions → Units**: Many-to-Many
10. **Strategy Analysis → All Core Tables**: Many-to-Many

## Data Import Strategy

### Phase 1: Core Data (Use unified data to avoid duplicates)
1. Import 22 Civilizations
2. Import unique Units (from all-unified.json)
3. Import unique Buildings (from all-unified.json)
4. Import unique Technologies (from all-unified.json)
5. Import unique Upgrades (from all-unified.json)
6. Import unique Abilities (from all-unified.json)

### Phase 2: Relationships
1. Link units to civilizations
2. Link buildings to civilizations
3. Link production relationships (buildings → units, buildings → technologies)

### Phase 3: AI Analysis
1. Generate sample build orders using AI
2. Create unit composition recommendations
3. Generate strategy analysis for key matchups

## AI Integration Points

### For Build Order Generation:
- Input: Civilization, Strategy Type, Target Age
- Process: Analyze unit costs, build times, tech requirements
- Output: Step-by-step build order with timings

### For Game Analysis:
- Input: Civilization matchup, map type
- Process: Analyze unit counters, tech advantages, timing windows
- Output: Strategic recommendations with confidence scores

### For Unit Composition:
- Input: Civilization, Age, Purpose (what to counter)
- Process: Calculate cost-effectiveness, counter relationships
- Output: Optimal unit ratios and compositions
