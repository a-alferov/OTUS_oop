import random


def get_score(
    phone: str | int,
    email: str,
    birthday: str | None = None,
    gender: int | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
) -> float:
    score = 0
    if phone:
        score += 1.5
    if email:
        score += 1.5
    if birthday and gender:
        score += 1.5
    if first_name and last_name:
        score += 0.5
    return score


def get_interests():
    interests = [
        "cars",
        "pets",
        "travel",
        "hi-tech",
        "sport",
        "music",
        "books",
        "tv",
        "cinema",
        "geek",
        "otus",
    ]
    return random.sample(interests, 2)
