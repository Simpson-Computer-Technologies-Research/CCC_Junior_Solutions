# // Get the sequence input
sequence: str = input()

# // Handle a sequence section
def handle_seq_section(res: str):
    # // Split the sequence section by + if tighten
    if "+" in res:
        res_split: list[str] = res.split('+')
        print(f"{res_split[0]} tighten {res_split[1]}")

    # // Or Split the sequence section by - if loosen
    elif "-" in res:
        res_split: list[str] = res.split('-')
        print(f"{res_split[0]} loosen {res_split[1]}")


# // Define Sequence Section Start
start: int = 0

# // Iterate over the characters in the sequence
for i in range(len(sequence)):
    isdigit: bool = sequence[i].isdigit()

    # // If the end of a sequence section
    if isdigit and (sequence[i] != "+" or sequence[i] != "-"):
        res: str = sequence[start:i+1]

        # // Handle the sequence section
        handle_seq_section(res)
        
        # // Reset the start variable
        start = i+1
