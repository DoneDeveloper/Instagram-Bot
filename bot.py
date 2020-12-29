from instapy import InstaPy


# Inside those two variable you will put your credentials. I left it blank
session = InstaPy(username = "", password="",headless_browser=True)
session.login()

session.set_relationship_bounds(enabled=True, max_followers=100)
session.set_do_follow(True, percentage=50)
session.like_by_tags(['webdeveloper','python','html','css'],amount=3)



session.end()