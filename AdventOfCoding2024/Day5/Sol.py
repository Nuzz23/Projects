from collections import deque, defaultdict
with open('./AdventOfCoding2024/Day5/Data.txt', 'r', encoding='UTF-8') as fp:
    rules, seq = {}, []

    # Parse rules and sequences
    for line in fp:
        if line.strip():
            if '|' in line:
                x, y = map(int, line.strip().split('|'))
                if x not in rules:
                    rules[x] = set()
                rules[x].add(y)
            else:
                seq.append(list(map(int, line.strip().split(','))))

# Function to check if an update is in the correct order
def is_valid_order(update, rules):
    # For each rule, ensure that the left page is before the right page in the update
    for x in rules:
        for y in rules[x]:
            if x in update and y in update:
                # Find the positions of x and y in the update
                if update.index(x) > update.index(y):
                    return False
    return True

# Function to calculate the middle page of a valid update
def calculate_middle(update):
    # Return the middle element of the update (if the length is odd)
    return update[len(update) // 2]

# Variable to store the sum of middle pages for valid updates
somma = 0
invalidIndex = set()


# Iterate through all updates
for i, update in enumerate(seq):
    if is_valid_order(update, rules):
        somma += calculate_middle(update)
    else:
        invalidIndex.add(i)

print(somma)

# Function to check if an update is in the correct order
def is_valid_order(update, rules):
    for x in rules:
        for y in rules[x]:
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    return False
    return True

# Function to perform topological sorting to correct the order of pages
def topological_sort(update, rules):
    # Create an in-degree dictionary only for pages in the current update
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    
    # Build graph and in-degree dictionary
    for x in rules:
        if x in update:  # Only process x if it's in the update
            for y in rules[x]:
                if y in update:  # Only process y if it's in the update
                    graph[x].append(y)
                    in_degree[y] += 1
    
    # Initialize queue with pages that have zero in-degree
    queue = deque([page for page in update if in_degree[page] == 0])
    sorted_pages = []
    
    # Perform the topological sort
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        
        # Decrease the in-degree of neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages


# Variable to store the sum of middle pages of corrected updates
somma = 0
# Process each invalid update and correct its order
for idx in invalidIndex:
    update = seq[idx]
    corrected_order = topological_sort(update, rules)
    middle_page = corrected_order[len(corrected_order) // 2]
    somma += middle_page

print(somma)
