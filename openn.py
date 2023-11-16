import webbrowser

def open_youtube(search):
    youtube_url = f"https://www.youtube.com/results?search_query={search.replace(' ' , '+')}"
    webbrowser.open(youtube_url)

