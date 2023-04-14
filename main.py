import pandas as pd
import tkinter as tk
import tkinter.filedialog

def schedule_meetings():
    # Read in the data
    df = pd.read_excel(file_entry.get())

    # Create a dictionary to map affiliations to person names
    affiliation_to_person = {}
    for i in range(len(df)):
        name = df.iloc[i]['What is your name?']
        affiliation = df.iloc[i]['What is your affiliation?']
        if pd.notnull(name) and pd.notnull(affiliation):
            affiliation_to_person[affiliation] = name

    # Create a dictionary to map affiliations to person names
    person_to_affiliate  = {}
    for i in range(len(df)):
        name = df.iloc[i]['What is your name?']
        affiliation = df.iloc[i]['What is your affiliation?']
        if pd.notnull(name) and pd.notnull(affiliation):
            person_to_affiliate [name] = affiliation

    # Initialize the meetings dictionary
    meetings = {}
    matches = []
    # Iterate over each row of the dataframe
    for i in range(len(df)):
        # Get the name of the person
        name = df.iloc[i]['What is your name?']
        
        # Check if the person is in the "What is your name?" column
        if pd.notnull(name):
            # Get the list of people they want to meet with
            desired = df.iloc[i]['Who would you like to meet with? (Check up to 5)\n* indicates Center member']
            
            # Split the string into a list of names
            if isinstance(desired, str):
                desired = desired.split('; ')
            else:
                desired = []

            # Change affiliate to cooresponding name if noticed affiliate name in desired
            x=0
            for person in desired:
                if person in affiliation_to_person:
                    desired[x] = affiliation_to_person[person]
                x+=1

            # Iterate over each desired person
            for person in desired:
                # Add the current person to the list of people they have already met with
                if name not in meetings:
                    meetings[name] = []
                if person not in meetings:
                    meetings[person] = []
                if person not in meetings[name]:
                    # Check if the desired person also wants to meet with the current person
                    if person in meetings:
                        if name in meetings[person]:
                            # Add the match to the list of matches
                            matches.append((name, person))
                    meetings[name].append(person)

    # Display the scheduled meetings in the GUI
    results_text.delete(1.0, tk.END)
    for person1 in meetings:
        if person1 in df['What is your name?'].values:
            results_text.insert(tk.END, f"{person1} is scheduled to meet with:\n")
            for person2 in meetings[person1]:
                results_text.insert(tk.END, f"  {person2}\n")
            results_text.insert(tk.END, "\n")
    
    # Display matches in the GUI
    results_text.insert(tk.END, "\nMatches:\n")
    for match in matches:
        person1, person2 = match
        if person1 in df['What is your name?'].values and person2 in df['What is your name?'].values:
            results_text.insert(tk.END, f"{person1} and {person2} have been matched!\n")



# Create the GUI
root = tk.Tk()
root.title("One-On-One Scheduler")

# Create the file selection button
file_label = tk.Label(root, text="Select the data file:")
file_label.pack()
file_button = tk.Button(root, text="Browse", command=lambda: file_entry.insert(tk.END, tkinter.filedialog.askopenfilename()))
file_button.pack()
file_entry = tk.Entry(root)
file_entry.pack()

# Create the run button
run_button = tk.Button(root, text="Run", command=schedule_meetings)
run_button.pack()

# Create the results text box
results_text = tk.Text(root)
results_text.pack()

root.mainloop()
