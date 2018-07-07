from matchtv.api import Api


def main():
    matches = Api.get_matches()
    for match in matches:
        print("Found: " + str(match))
        streams = match.get_streams()
        for stream in streams:
            print("Stream:" + str(stream))


if __name__ == "__main__":
    main()
