from dashboard import show_dashboard
from search import search

def main():
    while True:
        print("\n1 - View Dashboard")
        print("2 - Search Alerts")
        print("3 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_dashboard()

        elif choice == "2":
            keyword = input("Search keyword: ")
            results = search(keyword)

            print(f"\nFound {len(results)} results:\n")
            for r in results:
                print(r)

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
