class ComicDatabase:
    def __init__(self):
        self.comics = []

    def add_comic(self, title, author, genre, year):
        comic = {
            "title": title,
            "author": author,
            "genre": genre,
            "year": year
        }
        self.comics.append(comic)

    def search_comics(self, keyword):
        found_comics = []
        for comic in self.comics:
            if keyword.lower() in comic["title"].lower() or \
               keyword.lower() in comic["author"].lower():
                found_comics.append(comic)
        return found_comics
    