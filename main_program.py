import file_handling
import display
import music_reports


def main():
    option = None
    while option != '0':
        menu()
        try:
            option = user_input("\nType an option: ")
            options(option)
        except KeyError:
            print_massege("\nThere is no such option!")
        except ValueError:
            print_massege("\nInvalid input!")
    print_massege("\nGood-bye!")

    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
def menu():
    commands_list = "Exit", "Get the artist by genre", "Get the longest album", "Get the last oldest album", "Get total length of all albums", "Get genre stats", "Get oldest in genre", "Delete by artist and album name" 
    display.print_program_menu(commands_list)

def options(option):
    if option == "1":
        get_genre_list()
    
    elif option == "2":
        get_longest()
    
    elif option == "3":
        get_oldest()

    elif option == "4":
        total_albums_length()

    elif option == "5":
        get_genre_stats()
    
    elif option == "6":
        get_oldest_genre()

    elif option == "7":
        albums = music_reports.import_music_list()
        artist = user_input("Type an artist you want to delete: ")
        album_name = user_input("Type an album you want to delete: ")
        delete_album_by_artist_and_album_name(albums, artist, album_name)

    elif option == "0":
        return 0

    else:
        raise KeyError()


def delete_album_by_artist_and_album_name(albums, artist, album_name):
    for a in albums:
        if artist == a[0] and album_name == a[1]:
            albums.remove(a)
            display.print_albums_list(albums)
            file_handling.export_data(albums, 'albums_data.txt', 'w')


def get_genre_list():
    albums = music_reports.import_music_list()
    genre = user_input("Type a genre: ")
    genre_albums = music_reports.get_albums_by_genre(albums, genre)
    if isinstance(genre_albums, list):
        display.print_albums_list(genre_albums)
    else:
        print_massege(genre_albums)


def get_oldest():

    albums = music_reports.import_music_list()
    oldest_album = music_reports.get_last_oldest(albums)
    display.print_album_info(oldest_album)



def total_albums_length():

    albums = music_reports.import_music_list()
    total_length = music_reports.get_total_albums_length(albums)
    total = str(total_length)
    display.print_command_result(total)


def get_longest():

    albums = music_reports.import_music_list()
    longest_album = music_reports.get_longest_album(albums)
    display.print_album_info(longest_album)


def get_oldest_genre():
    albums = music_reports.import_music_list()
    genre = user_input("Type a genre: ")

    oldest_album = music_reports.get_last_oldest_of_genre(albums, genre)

    display.print_album_info(oldest_album)

def get_genre_stats():

    albums = music_reports.import_music_list()
    albums_by_genre = music_reports.get_genre_stats(albums)
    print_dict_info(albums_by_genre)


def user_input(massege):
    user_answer = input(massege)
    return user_answer


def print_massege(massege):
    print(massege)


def print_dict_info(albums):
    print("\n")
    for key, value in albums.items():
        print (f"{key}: {value}")
    print("\n")

if __name__ == '__main__':
    main()
