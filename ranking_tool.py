import random

def initialize_rankings(names):
    rankings = {name: 0 for name in names}
    return rankings

def compare_names_in_group(group_names, rankings):
    random.shuffle(group_names)
    for i in range(len(group_names)):
        name1 = group_names[i]
        for j in range(i + 1, len(group_names)):
            name2 = group_names[j]
            choice = input(f"Select name 'A' ({name1}) or 'B' ({name2}): ").upper()
            if choice == 'A':
                rankings[name1] += 1
            elif choice == 'B':
                rankings[name2] += 1

def sort_names(rankings):
    return sorted(rankings, key=lambda name: rankings[name])

if __name__ == "__main__":
    # Prompt user for a list of names
    input_names = input("Enter a list of names separated by commas: ")
    names = [name.strip() for name in input_names.split(',')]

    # Check if the list of names is too short
    if len(names) < 10:
        print("Please enter at least 10 names.")
    else:
        # Create groups from the list of names
        groups = [
            names[0:9], names[10:19], names[20:29], names[30:39], names[40:49],
            names[50:59], names[60:69], names[70:79], names[80:]
        ]

        rankings = initialize_rankings(names)

        for group_num, group_names in enumerate(groups, start=1):
            print(f"Ranking names in Group {group_num} (round 1):")
            compare_names_in_group(group_names, rankings)
            print()

"""# Groups"""

sorted_names_in_groups = {}

# Invert the rankings within each group
for group_num, group_names in enumerate(groups, start=1):
    inverted_rankings = {name: max(rankings.values()) - rankings[name] for name in group_names}
    sorted_names_in_groups[group_num] = sort_names(inverted_rankings)

# Print sorted names for each group
for group_num, sorted_names in sorted_names_in_groups.items():
    print(f"Sorted names in Group {group_num} (inverted rankings):")
    for i, name in enumerate(sorted_names, start=1):
        print(f"{i}. {name}")
    print()

# Combine the sorted names from all groups into one list
combined_sorted_names = []
for group_num, sorted_names in sorted_names_in_groups.items():
    combined_sorted_names.extend(sorted_names)

# Print the combined sorted list
print("Combined rankings for all groups (inverted rankings):")
for i, name in enumerate(combined_sorted_names, start=1):
    print(f"{name}")
