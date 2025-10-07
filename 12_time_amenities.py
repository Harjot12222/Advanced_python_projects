import time
import threading

def clock():
    """Displays the current date and time."""
    current_time = time.strftime("%d/%m/%Y, %H:%M:%S")
    print(f"🕒 Current time: {current_time}")

def timer():
    """Counts down from a user-defined number of seconds."""
    try:
        t = int(input("Enter the timer in seconds: "))
        if t <= 0:
            print("❌ Timer must be greater than 0!")
            return
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    print(f"⏳ Timer started for {t} seconds.")
    for i in range(t, 0, -1):
        print(i)
        time.sleep(1)
    print("⏰ Time is up!")

def stopwatch():
    """Counts up in seconds until user input stops it."""
    count = 0
    stop_flag = False

    def get_input():
        nonlocal stop_flag
        input("Press Enter to stop the stopwatch...\n")
        stop_flag = True

    threading.Thread(target=get_input, daemon=True).start()

    print("⏱️ Stopwatch started. Press Enter to stop.")
    while not stop_flag:
        count += 1
        print(count)
        time.sleep(1)
    print(f"✅ Stopwatch stopped at {count} seconds.")

def main():
    while True:
        print("\n__Basic Clock & Timer Utility__")
        print("1. Timer")
        print("2. Clock")
        print("3. Stopwatch")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            timer()
        elif choice == "2":
            clock()
        elif choice == "3":
            stopwatch()
        elif choice == "4":
            print("Thanks for using the utility. Have a great day! ❤️")
            break
        else:
            print("❌ Invalid input. Please enter 1-4.")

if __name__ == "__main__":
    main()
