import file_handling
import re
import datetime



def get_albums_by_genre(albums, genre):

    genre_albums = []
    for album in albums:
        if album[3] == genre:
            genre_albums.append(album)
        
    if len(genre_albums) < 1:
        raise ValueError("Wrong genre")
        
      
    if len(genre_albums) == 0:
        return "\nThere is no such genre.\n"
    else:
        return genre_albums


def get_genre_stats(albums):

    dict_of_albums = {}

    for album in albums:
        if album[3] not in dict_of_albums.keys():
            dict_of_albums[album[3]] = 1
        elif album[3] in dict_of_albums.keys():
            dict_of_albums[album[3]] += 1

    return dict_of_albums
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """


def get_longest_album(albums):
    long = 0.0
    for album in albums:
        length = album[4].replace(":", ".")
        length = float(length)
        if length > long:
            long = length

    longest_album = str(long).replace(".", ":")
    for album in albums:
        if album[4] == longest_album:
            return album
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """


def get_last_oldest(albums):
    old = 2020
    for album in albums:
        year = int(album[2])
        if year < old:
            old = year

    oldest_album = str(old)
    for album in albums:
        if album[2] == oldest_album:
            last_oldest = album

    return last_oldest
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """

def get_last_oldest_of_genre(albums, genre):
    genre_albums = get_albums_by_genre(albums, genre)
    oldest_album = get_last_oldest(genre_albums)
    return oldest_album
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """


# def to_time(str):
#     """
#     converts time in format "minutes:seconds" (string) to seconds (int)
#     """
#     SEC_IN_MIN = 60
#     min_sec = str.split(':')
#     return int(min_sec[0])*SEC_IN_MIN + int(min_sec[1])

def get_total_albums_length(albums):

    res = datetime.datetime(100,1,1,0,0,0)
    total_length = []
    new_list_seconds = []
    
    for album in albums:
        total_length.append(album[4].replace(":",","))    

    for l in total_length:
        time = l.split(",")
        minute = int(time[0])
        second = int (time[1])
        res += datetime.timedelta(minutes=minute, seconds=second)


    result_time = res.strftime("%H:%M:%S").split(":")
    new_minutes = int(result_time[0])*60
    new_seconds = int(result_time[2])
    result_minutes = int(result_time[1]) + new_minutes
    total_total = (result_minutes * 60 + new_seconds) / 60

    return float("%.2f" % total_total)
  

def import_music_list():

    music_list = file_handling.import_data("albums_data.txt")
    return music_list