import logging
import os
from random import choice


def random_headers():
    # Get randomized user agent, set default accept and request English page
    # This is done to prevent 403 errors.
    return {
        'User-Agent': choice(config.headers),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US'
    }


def contains_amp_url(string_to_check):
    # If the string contains an AMP link, return True
    if "/amp" in string_to_check or "amp/" in string_to_check or ".amp" in string_to_check or "amp." in string_to_check or "?amp" in string_to_check or "amp?" in string_to_check or "=amp" in string_to_check or "amp=" in string_to_check and "https://" in string_to_check:
        string_contains_amp_url = True
        return string_contains_amp_url

    # If no AMP link was found in the string, return False
    string_contains_amp_url = False
    return string_contains_amp_url


# Get list of subreddits where the bot is allowed
def get_allowed_subreddits():
    if not os.path.isfile("allowed_subreddits.txt"):
        allowed_subreddits = []
        logging.warning("allowed_subreddits.txt could not be found.\n")

    else:
        with open("allowed_subreddits.txt", "r") as f:
            allowed_subreddits = f.read()
            allowed_subreddits = allowed_subreddits.split(",")
            logging.info("allowed_subreddits.txt was found.")

    return allowed_subreddits
