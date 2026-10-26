import os

os.makedirs("data", exist_ok=True)

# 1
def save_scores(path: str, scores: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        for name, score in scores.items():
            file.write("{}:{}\n".format(name, score))

# 2
def add_score(path: str, name: str, score: int) -> None:
    with open(path, "a", encoding="utf-8") as file:
        file.write("{}:{}\n".format(name, score))

# 3
def read_scores(path: str) -> dict[str, int]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            scores: dict[str, int] = {}
            for line in file:
                if not line.strip():
                    continue
                name, score = line.strip().split(":")
                scores[name] = int(score)
            return scores
    except FileNotFoundError:
        print("⚠ ფაილი ვერ მოიძებნა")
        return{}




save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
add_score("data/scores.txt", "დათო", 64)
add_score("data/scores.txt", "მარიამი", 97)

with open("data/scores.txt", encoding="utf-8") as file:
    print(file.read(), end="")

scores = read_scores("data/scores.txt")
print(scores)

# 4

print(f"სტუდენტები: {len(scores.keys())}")
print(f"საშუალო ქულა: {round(sum(scores.values())/len(scores.keys()), 1)}")
high_score = max(scores.values())
print(f"საუკეთესო: {max(scores, key=scores.get)} {high_score}")
with open("data/passed.txt", "w", encoding="utf-8") as file:
    for name, score in scores.items():
        if score >= 80:
            file.write("{}\n".format(name))
names = []
with open("data/passed.txt", "r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        names.append(name)
print(names)