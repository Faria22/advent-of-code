current_molecules = [''.join(initial_state)]

steps = 0

while 'e' not in current_molecules:
    steps += 1

    new_molecules = {
        molecule.replace(start, end, 1)
        for molecule in current_molecules
        for start, end in reverse_rules_items
        if start in molecule
    }

    current_molecules = sorted(new_molecules, key=len)[:1000]

print(steps)
