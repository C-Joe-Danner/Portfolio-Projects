import praw
import random
import time

reddit = praw.Reddit(
    client_id="1FQC1v7CP_vwdbjpy-dqbg",
    client_secret="0ETl1T6AyygxPxek4wLNAlFiTFzC-g",
    user_agent="<console:CountDonut:1.0>",
    username="count-donut-bot",
    password="DonutDraculaPW1!",
    check_for_async=False
)

subreddit = reddit.subreddit("mbmbam")

fun_fact = ["You have summoned ~~Donut Dracula~~ Count Donut! Count Donut is immune to all Earthly pathogens but he still wears a facemask",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut has Internal Blood Syndrome 'IBS' meaning that he can only consume and digest blood.",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut lives in a castle in Donutvania but considers himself a citizen of nowhere.",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut used to employ a servant named Renfield but Count Donut murdered him in cold blood at the request of the Travis",
            "You have summoned ~~Donut Dracula~~ Count Donut! Long before Count Donut appeared on the podcast, Justin impersonated him in Episode 1 of the Seeso TV show",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut glistens in sunlight.",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut and Richard Stink both live inside of Justin and when they emerge Justin is sent to hell until they stop controlling his body",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut has a son Count Rick Donut Jr",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut appreciates donuts aesthetically and could eat them but prefers not to because of his gluten intolerance",
            "You have summoned ~~Donut Dracula~~ Count Donut! Count Donut does need to drink blood to survive, however, he only steals the blood types nobody wants such as D."]

for submission in subreddit.hot(limit=100):
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " donut " in comment_lower:
                print("-----")
                print(comment.body)
                random_index = random.randint(0, len(fun_fact) - 1)
                comment.reply(fun_fact[random_index])
                time.sleep(660)