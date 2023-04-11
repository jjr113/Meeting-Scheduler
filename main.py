import pandas as pd
import tkinter as tk
import tkinter.filedialog

def schedule_meetings():
    # Read in the data
    df = pd.read_excel(file_entry.get())

    # Initialize the meetings dictionary
    meetings = {}

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
                
            # Iterate over each desired person
            for person2 in desired:
                # If the person is not already in the meetings dictionary, add them
                if person2 not in meetings:
                    meetings[person2] = []
                    
                # Add the current person to the list of people they want to meet with
                if name not in meetings[person2]:
                    meetings[person2].append(name)
                    
                # Add the current person to the list of people they have already met with
                if name not in meetings:
                    meetings[name] = []
                meetings[name].append(person2)

    # Display the scheduled meetings in the GUI
    results_text.delete(1.0, tk.END)
    for person1 in meetings:
        if person1 in df['What is your name?'].values:
            results_text.insert(tk.END, f"{person1} is scheduled to meet with:\n")
            for person2 in meetings[person1]:
                results_text.insert(tk.END, f"  {person2}\n")
            results_text.insert(tk.END, "\n")

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
