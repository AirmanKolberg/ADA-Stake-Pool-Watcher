import requests
from bs4 import BeautifulSoup


def get_pool_active_stake(url):

    # No cookies required!
    cookies = dict()

    # Parse the HTML data
    soup = BeautifulSoup(requests.get(url, cookies=cookies).content, "html.parser")

    # Grab the string
    results = soup.select_one(".row").get_text(strip=True, separator=" ")

    # Separate the results by ADA
    results_sections = results.split('₳')

    # Select the Active Stake section of the results_sections list
    active_stake = results_sections[1]

    # Remove all data except the Active Stake int()
    active_stake = active_stake.replace(' Active Stake ', '')
    active_stake = active_stake.replace(' ', '')
    active_stake = active_stake.lower()

    # Determine multiplier (thousand or million)
    def determine_multiplier(multiplier, active_stake):

        # Remove 'M' or 'k'
        total_stake = float(active_stake.replace(multiplier[0], ''))

        # Multiply by the multiplier
        total_stake *= multiplier[1]

        return total_stake

    if 'm' in active_stake:
        multiplier = ('m', 1000000)
    elif 'k' in active_stake:
        multiplier = ('k', 1000)

    total_stake = int(determine_multiplier(multiplier, active_stake))

    return total_stake


if __name__ == '__main__':
    pass
