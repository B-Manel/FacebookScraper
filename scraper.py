from facebook_scraper import get_posts
from typing import List, Dict, Any
import sqlite3

connexion = sqlite3.connect('Facebook.db')
# the cursor allows access to db to make changes
cursor = connexion.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS pages(id TEXT, text TEXT, time TEXT, likes INT, comments INT, shares INT, url TEXT, 
    username TEXT)''')


class Scraper:

    @staticmethod
    def data_scraper(page_name: str, nb_pages: int = 1) -> List[Dict[str, Any]]:
        """
        This function scrapes data from a public Facebook page.

        :param page_name: Public Facebook page name
        :param nb_pages:  Number of pages to be scraped
        :return: list of scraped posts data
        """
        posts_list = []
        for post in get_posts(page_name, pages=nb_pages):
            posts_list.append(post)

            # different categories of scraped data
            post_id = post['post_id']
            text = post['post_id']
            time = post['time']
            likes = post['likes']
            comments = post['comments']
            shares = post['shares']
            post_url = post['post_url']
            username = post['username']

            cursor.execute(
                '''INSERT INTO pages VALUES (?,?,?,?,?,?,?,?)''',
                (post_id, text, time, likes, comments, shares, post_url, username))

        return posts_list

    # saving scraped data to DB
    data_scraper.__func__(page_name='nike')
    connexion.commit()

    # closing connexion
    connexion.close()
