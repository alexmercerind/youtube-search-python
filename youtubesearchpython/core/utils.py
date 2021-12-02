def playlist_from_channel_id(channel_id: str) -> str:
    list_id = "UU" + channel_id[2:]
    return f"https://www.youtube.com/playlist?list={list_id}"
