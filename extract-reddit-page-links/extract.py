import praw


# for more methods, see:
# https://github.com/praw-dev/praw/blob/master/praw/objects.py#L1544

def extract_top_youtube_submissions(subreddit, amount):
    r = praw.Reddit(user_agent='extract-reddit-page-links')
    submissions = r.get_subreddit(subreddit).get_top_from_day(limit=amount)
    submission_list = []
    # remove all the links that are not from youtube
    for submission in submissions:
        submission_list.append(submission)
    for submission in submissions:
        # if the URL isn't from youtube
        if not is_from_youtube(submission.url):
            submission_list.remove(submission)
    submission_list.reverse()
    return submission_list


# returns True if passed in link is from youtube, otherwise, False

def is_from_youtube(link):
    if "youtube.com" in link or "youtu.be.com" in link:
        return True
    else:
        return False


# nicely prints submissions

def print_submissions(submissions):
    for submission in submissions:
        print
        print submission.title
        print submission.url
        print

# sample
# print_submissions(extract_top_youtube_submissions("youtubehaiku", 20))
