import csv
import random

# Load verbs and their conjugations from CSV file
def load_verbs(file_path='verbs.csv'):
    verbs = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Store verbs as a dictionary with conjugations and stative status
            verbs[row['base']] = {
                'base': row['base'],
                'third_person': row['third_person'],
                'gerund': row['gerund'],
                'past': row['past'],
                'stative': row['stative'] == 'yes'  # Convert stative column to boolean
            }
    return verbs

# Generate the correct sentence for each tense and form
def generate_correct_sentence(verb, conjugations, subject, tense, form):
    base = conjugations['base']
    third_person = conjugations['third_person']
    gerund = conjugations['gerund']
    past = conjugations['past']
    is_stative = conjugations['stative']
    
    # Ensure that the subject "I" is always capitalized
    if subject == 'i':
        subject = 'I'
    
    # If the verb is stative, continuous forms are "n/a"
    if is_stative and tense in ['present continuous', 'past continuous']:
        return "n/a"
    
    if tense == 'present simple':
        if form == 'positive':
            if subject in ['he', 'she', 'it']:
                return f"{subject} {third_person}"
            else:
                return f"{subject} {base}"
        elif form == 'negative':
            if subject in ['he', 'she', 'it']:
                return f"{subject} doesn't {base}"
            else:
                return f"{subject} don't {base}"
        elif form == 'question':
            if subject in ['he', 'she', 'it']:
                return f"Does {subject} {base}"
            else:
                return f"Do {subject} {base}"
        elif form == 'negative question':
            if subject in ['he', 'she', 'it']:
                return f"Doesn't {subject} {base}"
            else:
                return f"Don't {subject} {base}"
    
    elif tense == 'present continuous':
        if form == 'positive':
            if subject == 'I':
                return f"{subject} am {gerund}"
            elif subject in ['he', 'she', 'it']:
                return f"{subject} is {gerund}"
            else:
                return f"{subject} are {gerund}"
        elif form == 'negative':
            if subject == 'I':
                return f"{subject} am not {gerund}"
            elif subject in ['he', 'she', 'it']:
                return f"{subject} isn't {gerund}"
            else:
                return f"{subject} aren't {gerund}"
        elif form == 'question':
            if subject == 'I':
                return f"Am {subject} {gerund}"
            elif subject in ['he', 'she', 'it']:
                return f"Is {subject} {gerund}"
            else:
                return f"Are {subject} {gerund}"
        elif form == 'negative question':
            if subject == 'I':
                return f"Aren't I {gerund}"  # "Aren't I" is used instead of "Amn't I"
            elif subject in ['he', 'she', 'it']:
                return f"Isn't {subject} {gerund}"
            else:
                return f"Aren't {subject} {gerund}"
    
    elif tense == 'past simple':
        if form == 'positive':
            return f"{subject} {past}"
        elif form == 'negative':
            return f"{subject} didn't {base}"
        elif form == 'question':
            return f"Did {subject} {base}"
        elif form == 'negative question':
            return f"Didn't {subject} {base}"
    
    elif tense == 'past continuous':
        if form == 'positive':
            if subject in ['I', 'he', 'she', 'it']:
                return f"{subject} was {gerund}"
            else:
                return f"{subject} were {gerund}"
        elif form == 'negative':
            if subject in ['I', 'he', 'she', 'it']:
                return f"{subject} wasn't {gerund}"
            else:
                return f"{subject} weren't {gerund}"
        elif form == 'question':
            if subject in ['I', 'he', 'she', 'it']:
                return f"Was {subject} {gerund}"
            else:
                return f"Were {subject} {gerund}"
        elif form == 'negative question':
            if subject in ['I', 'he', 'she', 'it']:
                return f"Wasn't {subject} {gerund}"
            else:
                return f"Weren't {subject} {gerund}"
    
    elif tense == 'future simple':
        if form == 'positive':
            return f"{subject} will {base}"
        elif form == 'negative':
            return f"{subject} won't {base}"
        elif form == 'question':
            return f"Will {subject} {base}"
        elif form == 'negative question':
            return f"Won't {subject} {base}"
    
    return ""

# Function to practice conjugation for a single verb
def conjugation_practice(verbs):
    subject_group1 = ['I', 'you', 'we', 'they']
    subject_group2 = ['he', 'she', 'it']
    tenses = ['present simple', 'present continuous', 'past simple', 'past continuous', 'future simple']
    forms = ['positive', 'negative', 'question', 'negative question']

    # Randomly choose a verb
    chosen_verb = random.choice(list(verbs.keys()))
    conjugations = verbs[chosen_verb]
    print(f"Verb: {chosen_verb}")

    # For each tense and form, randomly select one subject from each group
    for tense in tenses:
        # Handle stative verbs for present and past continuous, prompt once
        if conjugations['stative'] and tense in ['present continuous', 'past continuous']:
            # Randomly select one form and one subject
            form = random.choice(forms)
            subject = random.choice(subject_group1 + subject_group2)
            print(f"\n{subject}, {tense}, {form}:")
            user_input = input()
            if user_input.strip().lower() == 'n/a':  # Compare case-insensitively
                print("Correct!")
            else:
                print("Incorrect. The correct answer is: n/a")
            continue  # Skip other forms for stative verbs in continuous tenses

        for form in forms:
            # Randomly select one subject from each group
            subject1 = random.choice(subject_group1)
            subject2 = random.choice(subject_group2)

            for subject in [subject1, subject2]:
                while True:
                    # Simplified prompt for user
                    print(f"\n{subject}, {tense}, {form}:")
                    user_sentence = input()

                    # Generate the correct sentence
                    correct_sentence = generate_correct_sentence(chosen_verb, conjugations, subject.lower(), tense, form)

                    # Compare user input to the correct sentence (ignoring case)
                    if user_sentence.strip().lower() == correct_sentence.strip().lower():
                        print("Correct!")
                        break  # Move to the next one if correct
                    else:
                        print(f"Incorrect. The correct sentence is: {correct_sentence}")
                        print("Please try again.")

# Main function to loop through verbs indefinitely
def main():
    verbs = load_verbs()  # Load verbs from CSV
    while True:
        conjugation_practice(verbs)

if __name__ == "__main__":
    main()
