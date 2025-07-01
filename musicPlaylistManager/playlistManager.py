def add_song(playlist, song):
    """Add a song (string) to the playlist"""
    playlist.append(song)
    print(f"Added: {song}")

def remove_song(playlist, song):
    """Remove a song by name (first occurrence)."""
    try:
        playlist.remove(song)
        print(f"Removed: {song}")
    except ValueError:
        print(f"Song not found: {song}")

def list_songs(playlist):
    """Print all songs with their index."""
    if not playlist:
        print("Playlist is empty.")
        return
    for idx, song in enumerate(playlist, start=1):
        print(f"{idx}. {song}")

def main():
    playlist = []
    print("🎵 Simple Playlist Manager")
    while True:
        cmd = input("Enter command (add/remove/list/exit): ").strip()
        if cmd.startswith("add "):
            _, song = cmd.split(" ", 1)
            add_song(playlist, song)

        elif cmd.startswith("remove "):
            _, song = cmd.split(" ", 1)
            remove_song(playlist, song)

        elif cmd == "list":
            list_songs(playlist)

        elif cmd == "exit":
            print("Goodbye!")
            break

        else:
            print("Commands: add <song>, remove <song>, list, exit")

if __name__ == "__main__":
    main()
