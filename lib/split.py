def split(msg: str) -> list:
    return [c for c in msg]

if __name__ == "__main__":
    sentence = "A quick brown fox jump over a lazy dog"
    print(split(sentence))