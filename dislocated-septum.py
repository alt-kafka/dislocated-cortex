#!/usr/bin/env python3
import json
import random
import argparse
import os

# Function to generate a random sentence with specific conditions
def generate_sentence(library):
    subjects = library["subjects"]
    actions = library["actions"]
    descriptions = library["descriptions"]
    adverbs = library["adverbs"]
    determiners = library["determiners"]

    subject1 = random.choice(subjects)
    action1 = random.choice(actions)
    description1 = random.choice(descriptions)
    adverb1 = random.choice(adverbs)

    determiner1 = random.choice(determiners) if random.random() < 0.3 else ""

    # Create parts of the sentence
    part1 = f"{subject1} {action1} {description1} {adverb1}."
    part2 = f"{action1} {description1} {subject1} {adverb1}."
    part3 = f"{description1} {subject1} {action1} {adverb1}."
    part4 = f"{adverb1} {subject1} {action1} {description1}."

    sentence1 = random.choice([part1, part2, part3, part4])

    # 40% chance to create a compound sentence
    if random.random() < 0.4:
        subject2 = random.choice(subjects)
        action2 = random.choice(actions)
        description2 = random.choice(descriptions)
        adverb2 = random.choice(adverbs)

        determiner2 = random.choice(determiners) if random.random() < 0.3 else ""

        part5 = f"{subject2} {action2} {description2} {adverb2}."
        part6 = f"{action2} {description2} {subject2} {adverb2}."
        part7 = f"{description2} {subject2} {action2} {adverb2}."
        part8 = f"{adverb2} {subject2} {action2} {description2}."

        sentence2 = random.choice([part5, part6, part7, part8])
        sentence = f"{sentence1[:-1]} and {sentence2[0].lower()}{sentence2[1:]}"
    else:
        sentence = sentence1

    # 40% chance to create a double sentence
    if random.random() < 0.4:
        additional_sentence = generate_sentence(library).rstrip('.')
        # 25% chance to make one of them a fragment (2 term)
        if random.random() < 0.25:
            additional_sentence = f"{random.choice(subjects)} {random.choice(actions)}"
        sentence = f"{sentence} {additional_sentence}."

    # 15% chance to include quotes on some term
    if random.random() < 0.15:
        quote_term = random.choice([subject1, action1, description1])
        sentence = sentence.replace(quote_term, f'"{quote_term}"', 1)

    return sentence

# CLI logic to select the library
def main():
    parser = argparse.ArgumentParser(description='Generate random philosophical sentences.')
    parser.add_argument('--library', type=str, default=None, help='The library to use for generating sentences')
    parser.add_argument('--dir', type=str, default='.', help='The directory to search for libraries')
    args = parser.parse_args()

    library_name = args.library
    if library_name and not library_name.endswith('.json'):
        library_name += '.json'

    if args.library:
        library_path = os.path.join(args.dir, library_name)
        with open(library_path, 'r') as f:
            library = json.load(f)
    else:
        libraries = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if f.endswith('.json')]
        library_path = random.choice(libraries)
        with open(library_path, 'r') as f:
            library = json.load(f)

    for _ in range(20):
        library_key = list(library.keys())[0]  # Get the first key from the JSON file
        print(generate_sentence(library[library_key]))

if __name__ == "__main__":
    main()
