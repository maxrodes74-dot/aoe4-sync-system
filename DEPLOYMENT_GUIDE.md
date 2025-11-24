# Deployment Guide - AoE4 Sync System

## Your Repository

🎉 **GitHub Repository Created:**  
**https://github.com/maxrodes74-dot/aoe4-sync-system**

All your scripts are now in version control and ready for deployment!

## Deployment Options

### Option 1: GitHub Actions (Recommended - FREE)

GitHub Actions provides free automated scheduling. Perfect for this use case.

#### Setup Steps:

1. **Add GitHub Secrets**
   - Go to: https://github.com/maxrodes74-dot/aoe4-sync-system/settings/secrets/actions
   - Click "New repository secret"
   - Add these secrets:
     - `OPENAI_API_KEY`: Your OpenAI API key
     - `AIRTABLE_ACCESS_TOKEN`: Your Airtable personal access token

2. **Create Workflow Files**
   
   You'll need to manually create the workflow files in GitHub (the CLI couldn't push them due to permissions).
   
   Go to your repo → Actions → "set up a workflow yourself"
   
   **File 1: `.github/workflows/daily-sync.yml`**
   ```yaml
   name: Daily Data Sync
   
   on:
     schedule:
       - cron: '0 6 * * *'  # 6 AM UTC daily
     workflow_dispatch:  # Manual trigger
   
   jobs:
     sync:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: pip install -r requirements.txt
         
         - name: Sync Meta Stats
           env:
             OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
           run: python scripts/sync_civ_meta_stats.py
         
         - name: Sync Leaderboard
           env:
             OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
           run: python scripts/sync_leaderboard.py
   ```
   
   **File 2: `.github/workflows/weekly-analysis.yml`**
   ```yaml
   name: Weekly AI Analysis
   
   on:
     schedule:
       - cron: '0 8 * * 0'  # 8 AM UTC on Sundays
     workflow_dispatch:
   
   jobs:
     analyze:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         
         - name: Install dependencies
           run: pip install -r requirements.txt
         
         - name: Generate AI Analysis
           env:
             OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
           run: python scripts/generate_meta_analysis.py
   ```

3. **Enable Actions**
   - Go to: https://github.com/maxrodes74-dot/aoe4-sync-system/actions
   - Enable workflows if prompted

4. **Test It**
   - Go to Actions tab
   - Select "Daily Data Sync"
   - Click "Run workflow" → "Run workflow"
   - Watch it run!

**Cost:** FREE (2,000 minutes/month on free tier)

---

### Option 2: Vercel Cron Jobs (Easiest Setup)

Vercel provides simple serverless function deployment with cron scheduling.

#### Setup Steps:

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Clone Your Repo**
   ```bash
   git clone https://github.com/maxrodes74-dot/aoe4-sync-system.git
   cd aoe4-sync-system
   ```

3. **Create `vercel.json`**
   ```json
   {
     "crons": [
       {
         "path": "/api/sync-meta",
         "schedule": "0 6 * * *"
       },
       {
         "path": "/api/sync-leaderboard",
         "schedule": "0 6 * * *"
       },
       {
         "path": "/api/generate-analysis",
         "schedule": "0 8 * * 0"
       }
     ]
   }
   ```

4. **Create API endpoints** in `api/` directory

5. **Deploy**
   ```bash
   vercel deploy --prod
   ```

6. **Add Environment Variables** in Vercel dashboard

**Cost:** FREE on Hobby plan

---

### Option 3: Railway (Simplest)

Railway provides easy deployment with cron jobs.

#### Setup Steps:

1. **Go to Railway:** https://railway.app
2. **New Project** → **Deploy from GitHub repo**
3. **Select:** `maxrodes74-dot/aoe4-sync-system`
4. **Add Environment Variables:**
   - `OPENAI_API_KEY`
5. **Add Cron Service** in Railway dashboard

**Cost:** $5/month (includes generous free tier)

---

### Option 4: Local Server/VPS

Run on your own computer or VPS with cron jobs.

#### Setup Steps:

1. **Clone Repository**
   ```bash
   git clone https://github.com/maxrodes74-dot/aoe4-sync-system.git
   cd aoe4-sync-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

4. **Set Up Cron Jobs**
   ```bash
   crontab -e
   ```
   
   Add:
   ```cron
   # Daily sync at 6 AM
   0 6 * * * cd /path/to/aoe4-sync-system && python scripts/sync_civ_meta_stats.py
   0 6 * * * cd /path/to/aoe4-sync-system && python scripts/sync_leaderboard.py
   
   # Weekly AI analysis on Sundays at 8 AM
   0 8 * * 0 cd /path/to/aoe4-sync-system && python scripts/generate_meta_analysis.py
   ```

**Cost:** FREE (if you have a server) or $5-10/month for VPS

---

## Important: Airtable MCP Setup

**Note:** The scripts currently use `manus-mcp-cli` which is specific to the Manus environment.

### For Standalone Deployment, You Need To:

**Option A: Use Airtable API Directly**

Modify the scripts to use Airtable's REST API instead of MCP:

```python
import requests

AIRTABLE_TOKEN = os.getenv('AIRTABLE_ACCESS_TOKEN')
BASE_ID = 'appKeqSFMnexidZfd'
TABLE_NAME = 'Civilization Meta Stats'

headers = {
    'Authorization': f'Bearer {AIRTABLE_TOKEN}',
    'Content-Type': 'application/json'
}

url = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'
response = requests.post(url, headers=headers, json={'fields': record})
```

**Option B: Use Airtable Python SDK**

```bash
pip install pyairtable
```

```python
from pyairtable import Api

api = Api(os.getenv('AIRTABLE_ACCESS_TOKEN'))
table = api.table('appKeqSFMnexidZfd', 'Civilization Meta Stats')
table.create(record)
```

I can modify the scripts to use either approach if you'd like!

---

## Recommended Setup

**For easiest 24/7 operation:**

1. **GitHub Actions** for scheduling (free)
2. **Modify scripts** to use Airtable API directly
3. **Set up secrets** in GitHub
4. **Enable workflows**
5. **Done!** Runs automatically forever

---

## Getting Your API Keys

### OpenAI API Key
1. Go to: https://platform.openai.com/api-keys
2. Create new secret key
3. Copy and save it (you won't see it again)

### Airtable Personal Access Token
1. Go to: https://airtable.com/create/tokens
2. Create token with:
   - Scopes: `data.records:read`, `data.records:write`
   - Access: Your base `appKeqSFMnexidZfd`
3. Copy the token

---

## Next Steps

1. **Choose your deployment method** (I recommend GitHub Actions)
2. **Get your API keys** (OpenAI + Airtable)
3. **Set up secrets/environment variables**
4. **Test the deployment**
5. **Verify data syncs to Airtable**

Let me know which option you want to use and I can help you set it up!

---

## Monitoring

### Check if it's working:

**GitHub Actions:**
- Go to Actions tab in your repo
- See workflow runs and logs

**Airtable:**
- Check your tables for new records
- Look at `last_updated` timestamps

### Troubleshooting:

**Sync fails:**
- Check API keys are correct
- Verify Airtable token has write permissions
- Check workflow logs for errors

**No data appearing:**
- Verify base ID is correct
- Check table names match exactly
- Ensure scripts have proper permissions

---

## Cost Summary

| Method | Setup Time | Monthly Cost | Reliability |
|--------|-----------|--------------|-------------|
| GitHub Actions | 15 min | $0 | ⭐⭐⭐⭐⭐ |
| Vercel | 20 min | $0 | ⭐⭐⭐⭐⭐ |
| Railway | 10 min | $5 | ⭐⭐⭐⭐⭐ |
| Local Cron | 30 min | $0-10 | ⭐⭐⭐ |

**Recommendation:** GitHub Actions (free, reliable, easy)

---

Ready to deploy? Let me know which method you want and I'll help you get it running! 🚀
