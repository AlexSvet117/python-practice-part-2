# do not change the method name
def main():
    pass # replace with your code
list_of_songs = []
list_of_songs.append("\"Bohemian Rhapsody\" - Queen")
print(f"Adding: \"Bohemian Rhapsody\" - Queen")
print(f"Current playlist: {list_of_songs}")
list_of_songs.append("\"Hotel California\" - Eagles")
print(f"Adding: \"Hotel California\" - Eagles")
print(f"Current playlist: {list_of_songs}")
list_of_songs.append("\"Sweet Child O'Mine\" - Guns N'Roses")
print(f"Adding: \"Sweet Child O'Mine\" - Guns N'Roses")
print(f"Current playlist: {list_of_songs}")
list_of_songs.append("\"Billie Jean\" - Michael Jackson")
print(f"Adding: \"Billie Jean\" - Michael Jackson")
print(f"Current playlist: {list_of_songs}")
list_of_songs.append("\"Stairway to Heaven\" - Led Zeppelin")
print(f"Adding: \"Stairway to Heaven\" - Led Zeppelin")
print(f"Current playlist: {list_of_songs}")
print(f"Recently added songs (last 3): {list_of_songs[-3:]}")
print(f"First song: {list_of_songs[0]} and Last song: {list_of_songs[-1]}")
list_of_songs.remove('"Hotel California" - Eagles')
top_songs = list_of_songs[:2]
print(f"Top songs list: {top_songs}")



    
# do not change the following lines:
main()
