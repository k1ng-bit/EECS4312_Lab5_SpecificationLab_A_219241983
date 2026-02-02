## Student Name: Daksh Dave
## Student ID: 219241983

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict

def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    
    """implementing variables for the function"""

    work_start = 9 * 60
    work_end = 17*60
    lunch_start = 12 * 60
    lunch_end = 13 * 60
    slot_step = 15

    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Three-letter day abbreviation (e.g., "Mon", "Tue", ... "Fri")

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """
    # TODO: Implement this function
    

    raise NotImplementedError("suggest_slots function has not been implemented yet")
