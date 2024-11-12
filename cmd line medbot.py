import datetime
import pandas as pd

# Load or create the Excel database
def load_database(file_name="patients_data.xlsx"):
    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Age", "Gender", "Problem", "Response"])
        df.to_excel(file_name, index=False)
    return df

def save_database(df, file_name="patients_data.xlsx"):
    df.to_excel(file_name, index=False)

def main():
    database = load_database()

    while True:
        user_input = input("How can I assist you today?\n 1.Health\t 2.Appointment\t 3.Reminder\t 4.Diagnosis\t 5.Exit\n ::")
        if "health" in user_input.lower() or "1" in user_input:
            database = health_inquiry(database)
        elif "appointment" in user_input.lower() or "2" in user_input:
            book_appointment()
        elif "reminder" in user_input.lower() or "3" in user_input:
            prescription_reminder()
        elif "diagnosis" in user_input.lower() or "4" in user_input:
            first_level_diagnosis()
        elif "exit" in user_input.lower() or "5" in user_input:
            save_database(database)
            break
        else:
            print("Sorry, I didn't understand that. Please try again.")

def health_inquiry(database):
    # Collecting the information
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    problem = input("what is the problem you have?:")
    # Placeholder response
    response = "Providing health information..."

    # Save the details to the database
    new_entry = pd.DataFrame({"Name": [name], "Age": [age], "Gender": [gender], "Problem": [problem],"Response": [response]})

    # Use pd.concat instead of append
    database = pd.concat([database, new_entry], ignore_index=True)

    print("Information saved successfully.")
    save_database(database)

def book_appointment():
    doctor = input("Which doctor would you like to book an appointment with? ")
    date = input("Please enter the date for the appointment (YYYY-MM-DD): ")
    try:
        appointment_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        print(f"Appointment booked with Dr. {doctor} on {appointment_date.strftime('%A, %B %d, %Y')}.")
    except ValueError:
        print("Invalid date format. Please try again.")

def prescription_reminder():
    prescription = input("What is the prescription for? ")
    time = input("What time should I remind you? (HH:MM in 24-hour format): ")
    try:
        reminder_time = datetime.datetime.strptime(time, "%H:%M").time()
        print(f"Reminder set for {prescription} at {reminder_time.strftime('%H:%M')}.")
    except ValueError:
        print("Invalid time format. Please try again.")

def first_level_diagnosis():
    symptoms = input("Please describe your symptoms: ").lower()
    # This is a placeholder, typically you'd use an AI model or decision tree

    if "fever" in symptoms:
        print("Assistant: Fever can be a sign of infection. Stay hydrated and rest. If it persists, consider seeing a doctor.")
    elif "cough" in symptoms:
        print("Assistant: Cough can be due to a cold or allergy. Drink warm fluids and avoid irritants. If it’s severe, seek medical advice.")
    elif "headache" in symptoms:
        print("Assistant: Headaches can be caused by stress, dehydration, or lack of sleep. Drink water and rest. If the pain is severe, consult a healthcare provider.")
    elif "sore throat" in symptoms:
        print("Assistant: A sore throat can be a sign of a viral infection. Drink warm fluids and use throat lozenges. If it persists, consider seeing a doctor.")
    elif "stomach ache" in symptoms:
        print("Assistant: Stomach aches can be due to indigestion or stress. Try to relax, and avoid spicy foods. If it’s severe, consult a healthcare provider.")
    elif "dizziness" in symptoms:
        print("Assistant: Dizziness can be caused by dehydration or sudden movements. Sit down, drink water, and if it persists, see a doctor.")
    elif "chest pain" in symptoms:
        print("Assistant: Chest pain can be serious. Rest and avoid physical activity. Seek immediate medical attention if the pain persists or is severe.")
    elif "fatigue" in symptoms:
        print("Assistant: Fatigue can be due to lack of sleep or overexertion.import datetime")
    else:
        print("**please contact your doctor**")

if __name__ == "__main__":
    main()
