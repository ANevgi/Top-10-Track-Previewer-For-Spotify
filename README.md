# Top-10-Track-Previewer-For-Spotify
Gets 30-second previews and cover art from an artist's top 10 songs on Spotify.

# How to Use
You will first need to create a Spotify (Developer) App (tutorial for that is at https://developer.spotify.com/documentation/general/guides/app-settings/).

Because of the way that the Spotify API works, you need to have a user access token for any request made now so I used the spotify-token module, but there are other ways if you wish to change the code. Add your Spotify username and password in the relevant variables.

Add the artist's URI, which can be found via the artist's Spotify page.

After you hit run, you'll be met with a big list of song names, song previews and song cover arts. The links can then be used to access the data.

# To-do
- [ ] Add function of stating the name of an artist and URI is automatically found, so everything can be done via the program.
- [ ] Show a metric for the popularity of the song (at the time) e.g. plays, downloads etc.

# Example
![alt-text](https://raw.githubusercontent.com/ANevgi/Top-10-Track-Previewer-For-Spotify/master/Top%2010%20Track%20Previewer%20Result.PNG)

First Song (so you can click the links):
Song Name: You Need To Calm Down

Song Preview: https://p.scdn.co/mp3-preview/ddafac48971e46afddb31643680bfe2f6c44e1dc?cid=d8a5ed958d274c2e8ee717e6a4b0971d

Song Cover Art: https://i.scdn.co/image/6441b3a54e720b0fab3646c89ef35869d559414d
