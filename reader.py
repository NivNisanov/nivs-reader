"""nivs-reader: personal, read-only Reddit reader (u/N1troVex)."""
import argparse
import os

import praw

USER_AGENT = "script:nivs-reader:v0.1.0 (by /u/N1troVex)"
ALLOWED = {"iosapps", "SideProject", "HomeMaintenance", "iOSGaming"}


def client() -> praw.Reddit:
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        username=os.environ["REDDIT_USERNAME"],
        password=os.environ["REDDIT_PASSWORD"],
        user_agent=USER_AGENT,
    )
    reddit.read_only = True
    return reddit


def main() -> None:
    p = argparse.ArgumentParser(description="Read recent public posts in a subreddit.")
    p.add_argument("subreddit")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--comments", action="store_true", help="also print top comments")
    a = p.parse_args()
    if a.subreddit not in ALLOWED:
        raise SystemExit(f"Not in allowed list: {sorted(ALLOWED)}")
    for post in client().subreddit(a.subreddit).new(limit=min(a.limit, 25)):
        print(f"{post.title}\n  https://www.reddit.com{post.permalink}  ({post.num_comments} comments)")
        if a.comments:
            post.comments.replace_more(limit=0)
            for c in post.comments[:3]:
                print("    -", c.body[:200].replace("\n", " "))


if __name__ == "__main__":
    main()
