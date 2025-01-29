def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_file_contents = file_contents.lower()
        counts = {}
        for char in lowered_file_contents:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
    for key,value in counts.items():
        if key.isalpha() == True:
            print(f"the '{key}' character was found {value} times")

        

main()