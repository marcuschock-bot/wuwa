text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike.
"""

word_count = len(text.split())
character_count = len(text)
sentence_count = text.count('.') + text.count('!') + text.count('?')

print("Word Count : ", word_count)
print("Character Count : ", character_count)
print("Sentence Count : ", sentence_count)
