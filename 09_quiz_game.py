import random

def quiz_game():
    score = 0
    questions = [
        {
            "q": "What is the capital of India?",
            "options": ["New York", "Delhi", "Moscow", "Los Angeles"],
            "answer": "Delhi"
        },
        {
            "q": "How many oceans are there in the world?",
            "options": ["1", "2", "4", "5"],
            "answer": "5"
        },
        {
            "q": "Which planet is known as the red planet?",
            "options": ["Mercury", "Venus", "Mars", "Jupiter"],
            "answer": "Mars"
        },
        {
            "q": "What art form is described as decorative handwriting or handwritten lettering?",
            "options": ["Calligraphy", "Astrology", "Callilogy", "Extensive Writing"],
            "answer": "Calligraphy"
        },
        {
            "q": "What is acrophobia a fear of?",
            "options": ["Heights", "Spiders", "Closed spaces", "Water"],
            "answer": "Heights"
        }
    ]

    random.shuffle(questions)

    for q in questions:
        print("\n" + q["q"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        
        ans = input("Enter your answer (number or text): ").strip()
        
        # Accept numeric input as well
        if ans.isdigit():
            ans_idx = int(ans) - 1
            if 0 <= ans_idx < len(q["options"]):
                ans_text = q["options"][ans_idx]
            else:
                print("Invalid number. Skipping question.")
                continue
        else:
            ans_text = ans

        if ans_text.lower() == q["answer"].lower():
            print("Excellent work 👍")
            score += 1
        else:
            print(f"Sorry, the correct answer was {q['answer']}")
        
        print("Current Score:", score)

        confirm = input("Do you want to continue? (y/n): ").lower().strip()
        if confirm == "n":
            break

    print("\nFinal Score:", score)

if __name__ == "__main__":
    quiz_game()
