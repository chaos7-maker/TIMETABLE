import random
from exceptions import PeriodOverlapError

class RosterEngine:
    def __init__(self, classes, subject_teacher, subject_periods):
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.periods = ["P1", "P2", "P3", "P4", "Lunch", "P5", "P6", "P7"]
        self.classes = classes
        self.subject_teacher = subject_teacher
        self.subject_periods = subject_periods
        self.timetable = self._init_timetable()

    def _init_timetable(self):
        return {c: {d: {p: ("LUNCH" if p == "Lunch" else None) 
                for p in self.periods} for d in self.days} for c in self.classes}

    def generate(self):
        for c in self.classes:
            for sub, count in self.subject_periods.items():
                left = count
                while left > 0:
                    d, p = random.choice(self.days), random.choice(self.periods)
                    if p != "Lunch" and self.timetable[c][d][p] is None:
                        self.timetable[c][d][p] = sub
                        left -= 1

    def cancel_period(self, cls, day, period):
        self.timetable[cls][day][period] = None
        print(f"Period {period} on {day} for {cls} is now FREE.")

    def reassign_period(self, cls, day, period, new_sub):
        current = self.timetable[cls][day][period]
        if current is not None and current != "LUNCH":
            raise PeriodOverlapError(day, period, current)
        self.timetable[cls][day][period] = new_sub
        print(f"Successfully assigned {new_sub} to {day} {period}.")