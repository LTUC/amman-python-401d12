import requests
from bs4 import BeautifulSoup
import json

url = "https://news.ycombinator.com/"

page = requests.get(url)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

all_posts = soup.find_all('tr',class_='athing')

# print(all_posts)

#########################################################################################

# all_posts_arr = []
# for post in all_posts:

#     title_tag = post.find('span', class_="titleline").find('a')
#     title = title_tag.text.strip() if title_tag else 'No title'
#     # print(title)

#     link = title_tag['href'] if title_tag else 'No link'
#     # print(link)

#     subtext = post.find_next_sibling('tr').find('td', class_="subtext")

#     score_tag = subtext.find('span', class_="score")
#     score = score_tag.text.strip() if score_tag else '0 points'
#     # print(score)

#     comments_tag = subtext.find_all('a')[-1] if subtext else None  # return last ancor element from subtext
#     comments = comments_tag.text.strip() if comments_tag else '0 comments'
#     # print(comments)

#     single_post = {
#         'title' : title,
#         'link' : link,
#         'score' : score,
#         'comments' : comments
#     }

#     all_posts_arr.append(single_post)

#########################################################################################

def cleaner(post):
        
    title_tag = post.find('span', class_="titleline").find('a')
    title = title_tag.text.strip() if title_tag else 'No title'
    # print(title)

    link = title_tag['href'] if title_tag else 'No link'
    # print(link)

    subtext = post.find_next_sibling('tr').find('td', class_="subtext")

    score_tag = subtext.find('span', class_="score")
    score = score_tag.text.strip() if score_tag else '0 points'
    # print(score)

    comments_tag = subtext.find_all('a')[-1] if subtext else None  # return last ancor element from subtext
    comments = comments_tag.text.strip() if comments_tag else '0 comments'
    # print(comments)

    return {
        'title' : title,
        'link' : link,
        'score' : score,
        'comments' : comments
    }

cleaned_posts_arr = [cleaner(post) for post in all_posts]



json_data = json.dumps(cleaned_posts_arr, indent=2)

with open('hacker_news.json', 'w') as file:
    file.write(json_data)



