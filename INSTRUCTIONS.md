# set-up and execution instructions:

set-up:
1. pip install spotipy
2. enter exported environment variables into the terminal to authenticate 
   the account through the Spotify API

execution:
1. python crawler.py [username] [number]
2. python graphmaker.py playlists.pyfile
3. python fasterpathfinder.py graph.pyfile
4. python centrality.py dist.pyfile path.pyfile songlist.pyfile [int between 0 and 3]
5. python generatepath.py path.pyfile songlist.pyfile 'song_1' 'song_2' 
6. python neighborfinder.py songlist.pyfile dist.pyfile 'song' [number]
7. python playlistneighborfinder.py path.pyfile songlist.pyfile
8. python triangles.py graph.pyfile 'song'