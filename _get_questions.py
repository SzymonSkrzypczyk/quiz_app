from typing import List
from dataclasses import dataclass
import requests


@dataclass
class Question:
    category: str
    correct: str
    incorrect: List
    question: str
    tags: List
    difficulty: str


def get_questions(limit: int = 5):
    if limit > 20:
        limit = 20
    r = requests.get(f'https://the-trivia-api.com/api/questions?limit={limit}')
    data = []
    for i in r.json():
        data.append(Question(
            i['category'],
            i['correctAnswer'],
            i['incorrectAnswers'],
            i['question'],
            i['tags'],
            i['difficulty']
        ))
    return data


if __name__ == '__main__':
    print(get_questions(5))
