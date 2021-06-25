from url_maker import create_url
from file_reader import read_file
from twilio_functions import call_me, text_me
from webscrape_data import get_pool_active_stake


if __name__ == '__main__':

    # 64 million, the max ADA you'd want in a pool
    max_pool = 64000000

    # Read pool data from file
    ada_pool = read_file('ada_pool.txt')
    url = create_url(ada_pool)

    active_stake = get_pool_active_stake(url)

    # Use a comma in numbers > 1,000 for humans to read
    readable_active_stake = f'{active_stake:,}'

    # Display the current result on the screen
    print(f'Active Stake:  {readable_active_stake}')

    if active_stake > max_pool:
        text_me(f'ALERT:\nActive Stake: {active_stake:,} > 64 million')
        call_me()
