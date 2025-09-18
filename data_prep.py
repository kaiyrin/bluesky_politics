from ast import keyword
from atproto import Client
import os
import time


client = Client()

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')
handle = os.getenv('BSKY_HANDLE')


client.login(handle, password)
politics_keywords = ["politics", "election", "government", "policy", "vote", 
                    "democracy", "senate", "congress", "president", "campaign", 
                    "legislation","freedom", "free_speech", "free speech", "justice"]

def contains_politics(text):
    if not text:
        return False
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in politics_keywords)



def get_political_accounts(max_accounts, sleep_time,limit, client = client):
    found_accounts = set()
    full_politics = []
    for key in politics_keywords:
        accounts = client.app.bsky.actor.search_actors(params={"q": key, "limit": limit})
        for account in accounts.actors:
            display = account.display_name or ''
            bio = account.description or ''
            actor_username = account.handle

        if contains_politics(display) or contains_politics(bio) or contains_politics(actor_username):
            found_accounts.add(actor_username)
            full_politics.append({
                'bsk_handle': actor_username,
                'display': display,
                'bio': bio
            })
            if len(found_accounts) >= max_accounts:
                return list(found_accounts)
        time.sleep(sleep_time)  #p.s. ai suggestion

def get_political_posts(account_input_list,posts_per_account, client=client):
    all_posts = {}
    for account in account_input_list:
        try:
            response = client.app.bsky.feed.get_author_feed(params={"actor": account, "limit": posts_per_account})
            all_posts[account] = [
                post.post.record.text
                for post in response.feed
                if hasattr(post.post.record, 'text')
            ]
        except Exception as e:
            print(f"Error fetching posts for {account}: {e}")
    return all_posts
