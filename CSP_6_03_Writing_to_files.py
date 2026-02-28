import random


def writeFile(inputList, fileName):
    # Creates a file of the given name and adds each value from the list
    # to said file with each line being an index from the list.
    with open(fileName, "w") as file:
        for item in inputList:
            file.write(str(item) + "\n")


def sortNames(fileName, targetFile):
    # Takes in source file and a target file.
    # Sort all of the values from the source file and write them to the target file.

    try:
        with open(fileName, "r") as file:
            names = file.readlines()

        names = [name.strip() for name in names]

        names.sort()

        with open(targetFile, "w") as file:
            for name in names:
                file.write(name + "\n")

    except FileNotFoundError:
        print(f"{fileName} not found.")


sortNames("names.txt", "namesNew.txt")


def highScore(newScore: int):
    # Adds a new score to the file scores.txt
    # Then returns the average score from all of the scores in scores.txt

    fileName = "scores.txt"

    with open(fileName, "a") as file:
        file.write(str(newScore) + "\n")

    with open(fileName, "r") as file:
        scores = file.readlines()

    scores = [int(score.strip()) for score in scores]
    average = sum(scores) / len(scores)

    return average


print("New Average:", highScore(random.randint(1, 100)))

