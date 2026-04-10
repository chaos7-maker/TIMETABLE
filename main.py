from data_input import collect_user_data
from creation import RosterEngine
from exceptions import PeriodOverlapError

def main():
    # 1. Setup
    sub_teacher, sub_periods, classes = collect_user_data()
    engine = RosterEngine(classes, sub_teacher, sub_periods)
    engine.generate()

    while True:
        print("\n1. View Roster | 2. Reassign | 3. Cancel | 4. Exit")
        choice = input("Choice: ")

        if choice == "1":
            for c in classes:
                print(f"\n--- {c} ---")
                for d in engine.days:
                    print(f"{d}: {list(engine.timetable[c][d].values())}")
        
        elif choice == "2":
            try:
                cls = input("Class: ")
                day = input("Day (Mon-Fri): ")
                p = input("Period (P1-P7): ")
                sub = input("New Subject: ")
                engine.reassign_period(cls, day, p, sub)
            except PeriodOverlapError as e:
                print(f"\n[ERROR] {e}")
                override = input("Force override? (y/n): ")
                if override.lower() == 'y':
                    engine.timetable[cls][day][p] = sub
        
        elif choice == "3":
            cls = input("Class: ")
            day = input("Day: ")
            p = input("Period: ")
            engine.cancel_period(cls, day, p)

        elif choice == "4":
            break

if __name__ == "__main__":
    main()