"""
Utility module for demonstrating various Python data structures
"""

def create_user_profile(name: str, age: int, skills: list) -> dict:
    """Creates a user profile using different data structures"""
    return {
        "name": name,
        "age": age,
        "skills": skills,
        "profile_tuple": (name, age),  # Immutable data
        "skill_count": len(skills)
    }

def process_user_data(users: list) -> tuple:
    """Process user data and return statistics"""
    ages = [user["age"] for user in users]
    avg_age = sum(ages) / len(ages) if ages else 0
    all_skills = set()
    
    for user in users:
        all_skills.update(user["skills"])
    
    return (avg_age, len(all_skills), list(all_skills))


# Create sample user data using various data structures
users = [
    create_user_profile("Alice", 25, ["Python", "JavaScript"]),
    create_user_profile("Bob", 30, ["Python", "Java"]),
    create_user_profile("Charlie", 35, ["C++", "Rust"])
]

# Process user data
avg_age, unique_skills_count, all_skills = process_user_data(users)
print(f"Average age: {avg_age}")
print(f"Unique skills: {all_skills}")
