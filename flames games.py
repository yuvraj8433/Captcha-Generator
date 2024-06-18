def remove_common_chars(name1, name2):
    # Convert names to lists to allow mutable operations
    name1 = list(name1)
    name2 = list(name2)
    
    # Remove common characters
    for char in name1[:]:
        if char in name2:
            name1.remove(char)
            name2.remove(char)
    
    return name1, name2

def get_final_count(name1, name2):
    # Calculate the total length of remaining characters
    return len(name1) + len(name2)

def flames_result(count):
    flames = ["F", "L", "A", "M", "E", "S"]
    
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        
        if index >= 0:
            # If index is positive, remove the element at that index and rearrange list
            flames = flames[index+1:] + flames[:index]
        else:
            # If index is -1, remove the last element
            flames = flames[:index]
    
    return flames[0]

def main():
    # Input player names
    player1 = input("Enter the first name: ").upper().replace(" ", "")
    player2 = input("Enter the second name: ").upper().replace(" ", "")
    
    # Remove common characters
    name1, name2 = remove_common_chars(player1, player2)
    
    # Get the final count of remaining characters
    count = get_final_count(name1, name2)
    
    # Get the FLAMES result
    result = flames_result(count)
    
    # Display the relationship status
    relationships = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affectionate",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    
    print(f"Relationship status: {relationships[result]}")

# Run the main function
if __name__ == "__main__":
    main()
