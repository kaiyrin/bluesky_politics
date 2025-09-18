from data_prep import get_political_accounts
from data_prep import get_political_posts

def main():
    max_account = 3
    keyword_limit = 100
    sleep = 0.25 # seconds pase per request
    posts_per_account = 3
    political_accounts = get_political_accounts(max_accounts=max_account, sleep_time=sleep, limit=keyword_limit)
    print("Political accounts found:", political_accounts)
    posts = get_political_posts(account_input_list=political_accounts, posts_per_account=posts_per_account)
    print(posts)


if __name__ == "__main__":
    main()