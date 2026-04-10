class PeriodOverlapError(Exception):
    """Exception raised when attempting to assign a subject to a non-empty slot."""
    def __init__(self, day, period, current_val):
        self.message = f"Conflict: Slot {day} {period} is already occupied by {current_val}."
        super().__init__(self.message)