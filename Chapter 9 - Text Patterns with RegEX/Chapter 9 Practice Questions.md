1. re.compile()
2. to avoid using escape characters
3. the first instance of the matching regex
4. use the .search() method on a match object
5. group 0 covers the entire object, group 1 covers the area code, group 3 covers the number after the dash.
6. use an escape character i.e. \. or \( or \)
7. findall() returns a list of strings if no groups are used in the regex, it will return a list of tuples if groups are used.
8. this is the pipe character, it funstions as a logical or. option A | option B | option C is like saying Option A or option B or option C
9. ? matches zero or one instance of something. It can also be used to signify greedy or non-greedy matching {n,m}? or *? or +?
10. * matches zero or more instances of the preceding qualifier, + matches one or more
11. {3} means three instances, {3,5} means three to five instances
12. \d - a single whole number, \w - single word, \s - single space
13. \D \W \S - signify anything except the above things
14. .* means anything, .*? means anything but optional. So .* would mean, anything in this section counts as a match, .*? would mean the same thing but the match would be an optional condition
15. [a-z0-9]
16. use the second argument re.I. i.e. re.compile(r'[a-z]', re.I)
17. . matches any character except for new lines. re.DOTALL matches any character including new lines
18. X drummers, X pipers, five rings, X hens
19. re.VERBOSE allows you to make multiline regexes with # comments to increase readability.