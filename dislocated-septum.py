#!/usr/bin/env python3
import random

# Updated word banks with less concrete nouns, more concrete actions, and slightly vague adverbs
subjects = ["idea", "thought", "emotion", "concept", "dream", "memory", "vision", "illusion", "feeling", "imagination", "belief", "hope", "perception", "notion"]
actions = ["is", "takes", "to", "get to", "after that", "before again", "an then", "if it", "was", "seems like", "goes to", "comes with", "happens", "moves", "stops", "looks at", "feels"]
descriptions = ["unbelievable", "without it", "if long then", "before", "not so", "without nothing", "believable", "incomplete", "if so", "necessary", "confusing", "expected", "unheard", "beautiful", "strange"]
adverbs = ["occasionally", "sometimes", "seldom", "nearly", "partially", "somewhat", "hardly", "barely", "mostly", "generally", "regularly", "usually"]
determiners = ["the", "a", "my"]

# Function to generate a random sentence with specific conditions
def generate_complex_sentence():
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
        additional_sentence = generate_complex_sentence().rstrip('.')
        # 25% chance to make one of them a fragment (2 term)
        if random.random() < 0.25:
            additional_sentence = f"{random.choice(subjects)} {random.choice(actions)}"
        sentence = f"{sentence} {additional_sentence}."

    # 15% chance to include quotes on some term
    if random.random() < 0.15:
        quote_term = random.choice([subject1, action1, description1])
        sentence = sentence.replace(quote_term, f'"{quote_term}"', 1)

    return sentence

# Generate and collect 20 random sentences with specific conditions
random_sentences_complex = [generate_complex_sentence() for _ in range(20)]

for sentence in random_sentences_complex:
    print(sentence)

exit(0)
