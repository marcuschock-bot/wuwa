import re  # import java.util.regex.Pattern;

# Quick cheat sheet / notes
# def = creates a function (like a Java method)
# dict = dictionary / map (stores key-value pairs)
# import re = loads regex tools for working with text
# return = sends a value back from a function
# print() = shows output on screen
# f-string = formats text with variable values

single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a multi-line string
    that can span multiple lines."""

# Exercise 1
text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike.
"""


def analyze_text(text: str) -> dict:  # def = public static void
    """Return word, character, and sentence counts for text."""
    words = re.findall(r"\b[\w']+\b", text)
    sentences = re.findall(r"[.!?]+", text)
    characters = len(text)
    return {
        "words": len(words),
        "characters": characters,
        "sentences": len(sentences),
    }


if __name__ == "__main__":
    result = analyze_text(text)
    print("Text analyzer results:")
    print(f"Words: {result['words']}")  # f-string formatting
    print(f"Characters: {result['characters']}")
    print(f"Sentences: {result['sentences']}")

name = "Alice"
age = 30
message_1 = f"My name is {name} and I am {age} years old." #example for f-string formatting
print(message_1)

# Exercise 1 done by marcus
text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike.
"""
print("Word Count : ", len(text.split())) #count the number of words in the text
print ("Character Count : ", len(text)) #count the number of characters in the text
print ("Sentence Count : ", len(re.findall(r"[.!?]+", text))) #count the number of sentences in the text
