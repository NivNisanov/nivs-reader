# nivs-reader

A small personal, non-commercial, read-only Reddit script for u/N1troVex.

It reads public posts and comments in a few subreddits I take part in (r/iosapps, r/SideProject, r/HomeMaintenance, r/iOSGaming) so I can follow discussions and decide which threads to reply to myself.

## Scope
- Read only (OAuth `read` scope). No posting, voting, messaging or moderation.
- One account, one OAuth client, low volume, well under rate limits.
- No storage beyond temporary viewing, no model training, no resale or redistribution.
- Deleted content is never kept.

## Setup
1. Register a `script` app at https://www.reddit.com/prefs/apps (redirect URI `http://localhost:8080`).
2. Set environment variables: `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET`, `REDDIT_USERNAME`, `REDDIT_PASSWORD`.
3. `pip install -r requirements.txt`
4. `python reader.py SideProject --limit 10`
