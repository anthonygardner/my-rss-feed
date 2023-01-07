#!/usr/bin/env python3

from bs4 import BeautifulSoup

import pandas as pd
import requests


def main():
    # Set website url
    url = "https://www.lesswrong.com/users/eliezer_yudkowsky"

    # Make an http request to the website
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    r = requests.get(url, headers=header)

    # Determine the response
    status = r.status_code
    if status == 200:
        print("Received a response")
    elif status == 403:
        print("Website is blocking a response")
    elif status == 404:
        print("Website not found")
    elif status == 500:
        print("There's an internal server error")

    # Get all of the html code
    s = BeautifulSoup(r.content, "html.parser")
    
    # Extract the raw html for posts section
    posts_raw_html = []
    for line in s.find_all("div", {"class": "PostsList2-posts"}):
        posts_raw_html.append(line)

    # Extract the titles of each post
    post_titles = []
    post_dates = []
    for title, date in zip(
        s.find_all("span", {"class": "PostsTitle-root"}),
        s.find_all("span", {
        "class": "Typography-root Typography-body2 PostsItem2MetaInfo-metaInfo PostsItemDate-postedAt"}),
        ):
        post_titles.append(title.get_text())
        post_dates.append(date.get_text())
    
    df = pd.DataFrame({
        "Title": post_titles,
        "Date": post_dates,
    })
    print(df)
    

if __name__ == '__main__':
    main()
