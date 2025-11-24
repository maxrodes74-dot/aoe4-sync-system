# AoE4 World API → Airtable Sync System

Autonomous data synchronization system for Age of Empires 4 competitive statistics.

## What This Does

Automatically syncs live competitive data from AoE4 World API to your Airtable database:
- **Civilization meta statistics** (win rates, pick rates)
- **Top player leaderboards** (rankings, ratings)
- **AI-generated meta analysis** (strategic insights)

## Quick Start

### Prerequisites
- Python 3.11+
- OpenAI API key
- Airtable MCP integration configured

### Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

3. **Install MCP CLI:**
```bash
# The manus-mcp-cli tool is required for Airtable integration
# Follow Manus documentation to set up MCP integration
```

### Running Scripts

**Update civilization meta stats:**
```bash
python scripts/sync_civ_meta_stats.py
```

**Update leaderboard players:**
```bash
python scripts/sync_leaderboard.py
```

**Generate AI meta analysis:**
```bash
python scripts/generate_meta_analysis.py
```

**Update everything:**
```bash
python scripts/sync_civ_meta_stats.py && \
python scripts/sync_leaderboard.py && \
python scripts/generate_meta_analysis.py
```

## Deployment Options

### Option 1: GitHub Actions (Recommended)

Free automated scheduling using GitHub Actions.

**Setup:**
1. Push this repo to GitHub
2. Add secrets in repo settings:
   - `OPENAI_API_KEY`
   - `AIRTABLE_ACCESS_TOKEN`
3. Enable GitHub Actions
4. Scripts run automatically on schedule

See `.github/workflows/sync.yml` for configuration.

### Option 2: Vercel Cron Jobs

Deploy to Vercel with scheduled functions.

**Setup:**
1. Install Vercel CLI: `npm i -g vercel`
2. Deploy: `vercel deploy`
3. Configure cron in `vercel.json`

### Option 3: AWS Lambda

Serverless execution on AWS.

**Setup:**
1. Package scripts with dependencies
2. Create Lambda functions
3. Set up EventBridge schedules
4. Configure environment variables

### Option 4: Local Cron Jobs

Run on your own server/computer.

**Setup:**
```bash
# Edit crontab
crontab -e

# Add daily sync at 6 AM
0 6 * * * cd /path/to/aoe4-sync-deployment && python scripts/sync_civ_meta_stats.py
0 6 * * * cd /path/to/aoe4-sync-deployment && python scripts/sync_leaderboard.py

# Add weekly AI analysis on Sundays at 8 AM
0 8 * * 0 cd /path/to/aoe4-sync-deployment && python scripts/generate_meta_analysis.py
```

## Configuration

### Airtable Setup

**Base ID:** `appKeqSFMnexidZfd`

**Required Tables:**
- Civilization Meta Stats
- Leaderboard Players
- Strategy Analysis

### Sync Frequency Recommendations

- **Meta Stats:** Daily (or after patches)
- **Leaderboards:** Weekly
- **AI Analysis:** Weekly (or after patches)

### Customization

Edit scripts to customize:
- Number of top players to sync
- Rank-specific data filtering
- Leaderboard types (solo/team)
- AI analysis parameters

## Scripts Overview

### sync_civ_meta_stats.py
Fetches civilization statistics from AoE4 World API and updates Airtable.

**What it syncs:**
- Win rates
- Pick rates
- Games count
- Average game duration
- Current patch version

**Customization:**
```python
# Sync rank-specific data
sync_stats("rm_solo", "conqueror")
sync_stats("rm_solo", "diamond")

# Sync team games
sync_stats("rm_team", None)
```

### sync_leaderboard.py
Fetches top players from leaderboards and updates Airtable.

**What it syncs:**
- Player names
- Rankings and ratings
- Win rates
- Game counts
- Countries

**Customization:**
```python
# Sync top 100 players
sync_leaderboard("rm_solo", top_n=100)

# Sync team leaderboard
sync_leaderboard("rm_team", top_n=50)
```

### generate_meta_analysis.py
Uses AI to analyze current meta and generate strategic guides.

**What it generates:**
- Overall meta report
- Top-tier civilization guides
- Underdog civilization guides

**Requires:** OpenAI API key

## Monitoring

### Check Sync Status

Scripts output detailed logs:
```bash
python scripts/sync_civ_meta_stats.py
# Output shows success/failure for each record
```

### Error Handling

- API connection errors: Retries automatically
- Airtable errors: Logged with details
- Missing data: Skipped with warning

## Troubleshooting

### "Module not found" errors
```bash
pip install -r requirements.txt
```

### "API connection failed"
- Check internet connection
- Verify AoE4 World API is accessible
- Check for rate limiting

### "Airtable sync failed"
- Verify MCP integration is configured
- Check base ID and table names
- Ensure Airtable access token is valid

### "OpenAI API error"
- Verify API key is set in environment
- Check OpenAI account has credits
- Ensure API key has proper permissions

## API Rate Limits

- AoE4 World API: No authentication required, be respectful
- OpenAI API: Depends on your plan
- Airtable API: 5 requests/second per base

Scripts include delays to respect rate limits.

## Cost Estimates

### Free Tier (GitHub Actions)
- 2,000 minutes/month free
- Syncs cost ~1 minute each
- **Cost:** $0/month

### OpenAI API
- GPT-4.1-mini: ~$0.15 per 1M tokens
- Meta analysis: ~10K tokens per run
- **Cost:** ~$0.001 per analysis (~$0.05/month weekly)

### Airtable
- Free plan: 1,200 records per base
- Pro plan: $20/month for unlimited
- **Cost:** $0-20/month depending on data volume

## Security

### Secrets Management
- Never commit `.env` file
- Use environment variables in production
- Rotate API keys regularly

### Access Control
- Limit Airtable access token permissions
- Use read-only API keys where possible
- Monitor usage logs

## Documentation

Full documentation in `docs/` directory:
- `API_INTEGRATION_GUIDE.md` - Complete API reference
- `QUICK_START_V2.md` - User guide
- `AoE4_Airtable_Documentation.md` - System overview

## Support

### Issues
- Check script output for error messages
- Review documentation
- Verify API connectivity

### Updates
- Pull latest changes from repo
- Review changelog for breaking changes
- Test in development before production

## License

Scripts use AoE4 World public API and are subject to Microsoft's Game Content Usage Rules.

## Contributing

Improvements welcome:
- Additional API endpoints
- New sync strategies
- Enhanced error handling
- Performance optimizations

---

**Autonomous, 24/7 competitive data syncing for Age of Empires 4** 🚀
