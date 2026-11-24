import os

TEXT = "My Monday earned one star: the Wi-Fi died mid-standup, the inbox hit 400 unread, and the only thing on time was the meeting about being late."


def main():
    assert 1 <= len(TEXT) <= 200, "gate: entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
