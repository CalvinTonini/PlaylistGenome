# set-up and execution instructions:

1. pip install spotipy
2. enter exported environment variables into the terminal to authenticate 
   the account through the Spotify API
3. python crawler.py [username] [number]
4. python graphmaker.py playlists.pyfile
5. python fasterpathfinder.py graph.pyfile
6. python centrality.py dist.pyfile path.pyfile songlist.pyfile
7. python generatepath.py path.pyfile songlist.pyfile 'song_1' 'song_2' 
8. python neighborfinder.py songlist.pyfile dist.pyfile 'song' [number]
9. python playlistneighborfinder.py path.pyfile songlist.pyfile
9. python triangles.py graph.pyfile 'song'
