# Author : tarlansoltanov
# Name : Dubstep
# ID : 551dc350bf4e526099000ae5
# Link : https://www.codewars.com/kata/551dc350bf4e526099000ae5
# Level : 6 KYU
# Language : Python

def song_decoder(song):
    ans = song.split("WUB")

    for i in range(0,ans.count('')):
        ans.remove('')

    return(' '.join(e for e in ans))