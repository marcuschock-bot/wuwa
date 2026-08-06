#Error handling
def validate_age(age):
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        return age
        if age > 120:
            raise ValueError("Age seems unrealistic.")
        return true 

try:
     validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
  