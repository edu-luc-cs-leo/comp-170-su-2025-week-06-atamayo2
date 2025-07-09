# Question 1---- 
def load_to_list(filepath: str) -> list[float]:
    data = []
    with open(filepath, "r") as file:
        for line in file:
            data.append(float(line.strip()))
    return data 
# This code reads the file data that contains the temperature and returns flot values that
# represent those temperature 

# Question 2
def descriptive_statistics(source_data: list[float]) -> None:
    total = len(source_data)
    avg = round(sum(source_data) / total, 2)
    smallest = min(source_data)
    largest = max(source_data)   
    print(f"There are {total} values in the data source.")
    print(f"The average value is {avg}")
    print(f"The highest value is {largest} and the smallest value is {smallest}.")
# This code gives us the total number of values, averages, and
# the minimum and maximum temperature numbers.
# Then code prints it out

#Question 3
def apply_markup(filepath: str) -> None:
    with open(filepath, "r") as file:
        for line in file:
            new_line = []
            for word in line.strip().split():
                if word.startswith("."):
                    new_line.append(word[1:].upper())
                elif word.startswith("_"):
                    new_line.append(" ".join(word[1:]))
                else:
                    new_line.append(word)
            print(" ".join(new_line))



# This final code just reads the text files and adds the necessary markups by 
# going line to line and doing what the code is asking for. For example, if the code has "blank"
# print out "Blank" and so on. which then prints it out line by line.
#----------------------------------------------------------------------------
# Reflection for week 5 assignment

# When I looked at my Week 5 submission next to the other answers that had been posted, I saw that 
# while my code worked fine in most situations, it was missing specific tests for edge cases like 
# empty strings or None inputs.  The posted answers had better logic with flags and more thorough 
# comments, which made the code easier to read and understand.  Also, I learned I need to use type 
# hints and comments more often and include more information about how I came to my conclusions. I
# feel like i do use some comments but i think i need to add more. I just feel so stuck and last minute
# when i do these assignments that its hard to take time to sit back and think before i submit/ask questions
# When I'm stuck, I sometimes have trouble asking for help. But looking over these answers makes 
# me want to get better at testing and debugging and participate more in class.  
# Basically, this comparison taught me how to write code that is cleaner and more consistent.
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Manually calling my functions to see that they work!

# Question 1- load temperatures and print

temps = load_to_list("data/temperatures.txt")
print ("Loaded temperatures:",temps)

# Question 2- show descriptive statistics for temp
descriptive_statistics(temps)

# Question 3- apply markup formatting to text file
print("\nFormatted markup.txt:\n")
apply_markup("data/markup.txt")

