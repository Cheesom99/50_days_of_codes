# link = "https://www.youtube.com/watch?v=RRW2aUSw5vU"
link = "https://youtu.be/RRW2aUSw5vU"

if "www" in link:
    print(link[link.index("=")+1:])
else:
    print(link[link.index("/", 9)+1:])

