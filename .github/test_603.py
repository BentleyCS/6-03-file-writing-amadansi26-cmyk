from your_file_name import writeFile, sortNames, highScore
import os


def test_writeFile():
    test_list = ["Charlie", "Alice", "Bob"]
    writeFile(test_list, "test_names.txt")
    
    with open("test_names.txt", "r") as f:
        contents = f.readlines()
    
    assert contents == ["Charlie\n", "Alice\n", "Bob\n"]


def test_sortNames():
    # Create unsorted file first
    writeFile(["Charlie", "Alice", "Bob"], "test_names.txt")
    
    sortNames("test_names.txt", "sorted_test_names.txt")
    
    with open("sorted_test_names.txt", "r") as f:
        contents = f.readlines()
    
    assert contents == ["Alice\n", "Bob\n", "Charlie\n"]


def test_highScore():
    # Reset scores file for clean test
    with open("scores.txt", "w") as f:
        f.write("10\n20\n30\n")
    
    average = highScore(40)
    
    # Expected average: (10 + 20 + 30 + 40) / 4 = 25
    assert average == 25
