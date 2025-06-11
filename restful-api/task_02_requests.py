#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""

import requests
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder."""

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder."""

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code == 200:
        posts = r.json()

        fieldnames = ["id", "title", "body"]
        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for post in posts:
                filtered_posts = {key: post[key] for key in fieldnames}
                writer.writerow(filtered_posts)

        print("Données sauvegardées dans posts.csv")
    else:
        print("Erreur lors de la requête : {r.status_code}")
