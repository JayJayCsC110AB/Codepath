"""
At a cultural festival, multiple performances are scheduled on a single stage. 
However, due to last-minute changes, some performances need to be rescheduled or canceled. 
The festival organizers use a stack to manage these changes efficiently.

You are given a list changes of strings where each string represents a change action. The actions can be:

"Schedule X": Schedule a performance with ID X on the stage.
"Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
"Reschedule": Reschedule the most recently canceled performance to be the next on stage.
Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

def manage_stage_changes(changes):
    pass
Example Usage:

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
Example Output:

["A", "C", "B", "D"]
[]
["Z"]
"""

"""
Understand: We can schedule using append and cancel using pop usinga  stack, and str = .pop() 
I - the list itself
O- returning a appended list
C- We have to use a stack, 
E -  make sure things are not being popped while empty

Plan: Loop through the lists, since cancel takes from the end we loop through we schedule, if its cancel we take off the end of the current 

"""

def manage_stage_changes(changes):
    schedule = []
    removed = []
    if len(changes) == 0:
        return []

    for i in range(len(changes)):
        if changes[i] == "Cancel" and schedule:
            removed.append(schedule.pop())
        if changes[i] == "Reschedule" and removed:
            schedule.append(removed.pop(0))
        if changes[i][0:8] == "Schedule":
            schedule.append(changes[i][-1])
    return schedule

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 