"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temp = [31, 30, 29, 32, 30, 31, 28]
    return temps

def analyze_temps(temp_list):
    average = sum(temp_list) / 7
    high = max(temp_list)
    low = min(temp_list)
    return(average, high, low)

def display_analysis(avg, high, low):
    print("Temprature Analysis for the Week:")
    print(f"Average: %.1f C" % avg)
    print("Highest:", high, "C")
    print("Lowest:" + low + "C")   

input = get_temperatures()
result = analyze_temps(input)
display_anlysis(result[0], result[1], result[2])

   