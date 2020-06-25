import vlc
import time

vlc = vlc.Instance()
player = vlc.media_player_new()
media = vlc.media_new('./test.mp4')
player.set_media(media)
player.play()
time.sleep(25)
print("dobre tam")