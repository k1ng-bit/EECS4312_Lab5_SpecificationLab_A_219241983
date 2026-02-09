## Student Name: Daksh Dave
## Student ID: 219241983

"""
Stub file for the meeting slot suggestion exercise.

Implement the function `suggest_slots` to return a list of valid meeting start times
on a given day, taking into account working hours, and possible specific constraints. See the lab handout
for full requirements.
"""
from typing import List, Dict


# Helper Functions needed for the final suggest_slots() function
def toMin(hhmm: str) -> int:
    #split the hhmm string to hours and mins
    hours, minutes = hhmm.split(":")    # split by : char
    return int(hours) * 60 + int(minutes)

def toHHMM(mins: int) -> str:
    hours = mins // 60 
    minutes = mins % 60
    return f"{hours:02d}:{minutes:02d}"

def isFri(day:str)->bool:
    d = day.strip().lower

    if d.startsWith("fri"):
        return true
    try:
        y, m, dd = day.split("-")
        return date(int(y), int(m), int(dd)).weekday() == 4  # Fri
    except Exception:
        return False



def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    
    """implementing variables for the function"""
    
    work_hour_start = toMin("9:00")
    work_hour_end = toMin("17:00")
    lunch_start = toMin("12:00")
    lunch_end = toMin("13:00")
    Fri_end = toMin("15:00")
    friday = isFri(day)
    
    increment = 15      # time slots increment by 15 minutes. 
    buffer = 15         # buffer time after an event is completed

    blocked = []        # list containing time slots that cannot be assigned
    blocked.append((lunch_start, lunch_end)) #cannot assign lunch times for meeting


    if meeting_duration<=0:     #if no meeting, then no need for available time slots
        return []
    
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
    
    for ev in events:

        event_start = toMin(ev["start"])
        event_end = toMin(ev["end"])
        
        if event_end <= event_start:
            continue
        
        if event_end <= work_hour_start or event_start >= work_hour_end:
            continue

        event_start = max(event_start, work_hour_start)
        event_end = min(event_end, work_hour_end)
        
        event_end = min(event_end + buffer, work_hour_end)

        blocked.append((event_start, event_end))
    
    blocked.sort()
    
    merged = []     #merged to get rid of any overlaps

    for s, e in blocked:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    def overlaps_any(s: int, e: int) -> bool:
        for bs, be in merged:
            if s < be and e > bs:
                return True
        return False

    latest_start = work_hour_end - meeting_duration
    if latest_start < work_hour_start:
        return []

    available_times = []

    t = work_hour_start
    while t <= latest_start:
        # Lunch rule: block STARTS during lunch (not overlaps)
        if not (lunch_start <= t < lunch_end):
            end = t + meeting_duration
            if not overlaps_any(t, end):
                available_times.append(toHHMM(t))
        t += increment

        if friday and t>= Fri_end:
            t+= increment
            continue

    return available_times

    #raise NotImplementedError("suggest_slots function has not been implemented yet")