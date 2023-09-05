import instaloader

L = instaloader.Instaloader()
L.load_session_from_file("USERNAME")


def download_and_print_stories(username):
    profile = instaloader.Profile.from_username(L.context, username)
    user_id = profile.userid
    # Завантаження історій
    L.download_stories(userids=[user_id])

def download_storyitem(username):
    profile = instaloader.Profile.from_username(L.context, username)

    for highlight in L.get_highlights(profile):
        # highlight is a Highlight object
        for item in highlight.get_items():
            # item is a StoryItem object
            L.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))

def download_posts(username):
    profile = instaloader.Profile.from_username(L.context, username)

    for post in profile.get_posts():
        L.download_post(post, target=f"{username}/{post.date_utc}")

if __name__ == '__main__':
    username = input("Введіть ім'я користувача Instagram: ")

    story = input("Хочете скачати історії: Y/N ")
    if story == "Y" or story == "y":
        download_and_print_stories(username)

    post = input("Хочете скачати пост: Y/N ")
    if post == "Y" or post == "y":
        download_posts(username)

    highlight = input("Хочете скачати хіджити: Y/N ")
    if highlight == "Y" or highlight == "y":
        download_storyitem(username)
