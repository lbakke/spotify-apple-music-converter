#!/usr/bin/env python3

import spotipy

link = input("paste the spotify link here\n")

pieces = link.split("/")
apireference = pieces[4]
apipieces = apireference.split("?")
songid = apipieces[0]

urn = 'spotify:track:' + songid
sp = spotipy.Spotify(auth='BQBaPnFd-b6GJjXJIYQK5bE7_kJjV03JNOIVme2Z6z5m6r3gYEzd4dl1kDikYFe0qkisgtk-GQQYY6MJ5mLnfqgfTRX9jkJ1jlVSPbZtYS0JprdaKOtDzNwfWBnV-FPwHjSEOQrE6nvPSbO4zEP0D1r4')

track = sp.track(urn)
print(track['name'])
print(track['artists'][0]['name'])
