# utilizes Spotipy, developed by Plamere, available at https://github.com/plamere/spotipy
# to install, type in command-line: pip install spotipy
import spotipy

# ids: int or string list (?)
# output: dict

def crawler(ids):
    for userid in ids:
        