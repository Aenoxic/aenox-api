from aenox import AenoXAPI
from datetime import datetime

if __name__ == "__main__":
    api = AenoXAPI(api_key="1b18d866-59f4-4366-8a5a-b55ebc78845c")
    claimed = api.get_guild_stats(1262732535990059009).language
    print(claimed)
    print(f"Type: {type(claimed)}")