from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'themotivationalquotesinspire'
insta_password = 'tdp@2003'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True)

session.unfollow_users(amount=50, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=60,
                           sleep_delay=601)                                  