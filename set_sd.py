morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

# possible_courses = morning ^ afternoon
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)