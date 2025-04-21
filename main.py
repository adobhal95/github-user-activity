import sys
from dotenv import load_dotenv
from services import get_user_events


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <username>")
        print("Example: python main.py octocat")
        sys.exit(1)
    load_dotenv()
    user_id: str = sys.argv[1]
    events = get_user_events(user_id)


if __name__ == "__main__":
    main()
