# python-firewall
This is my solution to Illumio's Coding Challenge for the Policy Team for the Back-end Software Engineering Intern, Policy, Summer 2020 Role.

### a. how you tested your solution
I didn't have enough time to generate large datasets of 500K-1M items, so I tested on the sample rules given by the spec of the coding assignment.
### b. any interesting coding, design, or algorithmic choices you’d like to point out
The following is the more important bits in my thought process:

Before doing any coding in the given 2 hours, I did a lot of thinking and designing. Knowing that "tradeoffs between space and time complexity is a core component of this coding assignment" and that it is expected that the code "work 'reasonably quickly' (i.e. not appear unresponsive) for large datasets", I resolved to the one data structure I know is used extensively to save time - the hashtable, which I thought would be especially useful in this case, since we're searching for a match or search for the input in any of the given rules. Since the hashtable is the only data structure, on https://www.bigocheatsheet.com/ at least, whose "Search" time complexity is θ(1) on average, I wanted the accept_packet function to call a search in the dictionary to decrease runtime. I wanted to spend less time on syntax, so I went for the language I knew the best, Python, whose hashtable is implemented by the built-in data type dictionary.

Then, I chose to have a tuple of (direction, protocol, number) be the key and a tuple of (port, ip_address) be the value because I saw from the sample rules that it is possible for 2 rules to have the same direction, protocol, and port, which led me into thinking about having (direction, protocol, port) as the key. However, that didn't seem intuitively "balanced" enough and practically, can cause extremely slow runtime if there are many rules with the same direction, protocol, and port. So I decided to split the 4 components of a rule evenly betwee the key and the value. The number, which is different for every key's tuple, is to allow for entries from rules with the same direction and protocol but different port and ip address.
### c. any refinements or optimizations that you would’ve implemented if you had more time
I would've implemented ways to handle duplicates, which is a common edge case I've come across. If there were many duplicates, it would waste a lot of time.
### d. anything else you’d like the reviewer to know
I trust that interns are put into the team that Illumio believes best suits their skillset, but since I'm also a Data Science major who plans to take a database course and otherwise work with data more, I have a particular interest in the Data team. However, I would be happy to be placed in whichever team.
