from jikanpy import Jikan
import os.path
import urllib.request
jikan = Jikan()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(ROOT_DIR, "data")


def get_image(data):
    return data['images']['jpg']['image_url']


def get_genres(data):
    return list(map(lambda d: d['name'], data['genres']))


def write_genre_to_file(genres, id):
    file = open(os.path.join(save_path, id)+".txt", "w")
    print(genres)
    file.write(",".join(genres))
    file.close()

def save_image(url,id):
    urllib.request.urlretrieve(url,os.path.join(save_path, id)+".jpg")


def get_top(page):
    result = jikan.top(type='anime', page=page)  # 25 per page
    topList = result['data']
    for anime in topList:
        id = str(anime['mal_id'])
        print("Getting Anime " + id)
        write_genre_to_file(get_genres(anime), id)
        save_image(get_image(anime), id)

# Getting 250 examples of genre list and images
if __name__ == '__main__':
    for i in range(1,10):
        print("Page "+str(i)+" ===============")
        get_top(i)


