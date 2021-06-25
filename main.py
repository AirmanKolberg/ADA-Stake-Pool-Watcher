from url_maker import create_url
from file_reader import read_file
from twilio_functions import call_me, text_me
from webscrape_data import get_pool_active_stake
from system_commands import clear_screen
from datetime import datetime
from time import sleep


# Returns int() for 24hr clock
def get_hour_of_the_day():

    now = datetime.now()
    now = now.strftime('%H:%M:%S')
    now = now.split(':')

    hour = int(now[0])

    return hour


if __name__ == '__main__':

    # 64 million, the max ADA you'd want in a pool
    max_pool = 64000000

    # Read pool data from file
    ada_pool = read_file('ada_pool.txt')
    url = create_url(ada_pool)

    # Hours to notify
    notification_hours = [8, 20]

    while True:

        # Clear the Terminal window
        clear_screen()

        hour_now = get_hour_of_the_day()

        # Check if it's 8am or 8pm, and if so, execute commands
        if hour_now in notification_hours:

            active_stake = get_pool_active_stake(url)

            # Use a comma in numbers > 1,000 for humans to read
            readable_active_stake = f'{active_stake:,}'

            # Display the current result on the screen
            print(f'Active Stake:  {readable_active_stake}')

            if active_stake > max_pool:
                text_me(f'ALERT:\nActive Stake: {readable_active_stake} > 64 million')
                call_me()
            else:
                text_me(f'ADA UPDATE:\nActive Stake: {readable_active_stake}/64 million')

        # Check again in an hour
        sleep(3600)
