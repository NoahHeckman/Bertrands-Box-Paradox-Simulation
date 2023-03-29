# Bertrand's Box Paradox
This is a simple Python script that demonstrates the probability of Bertrand's Box Paradox. Bertrand's Box Paradox is a veridical paradox in elementary probability theory. It was first posed by Joseph Bertrand in his 1889 work, Calcul des Probabilités. The problem is presented as follows:

There are three boxes:

1. box containing two gold coins,
2. box containing two silver coins,
3. box containing one gold coin and one silver coin.

The question is to calculate the probability, after choosing a box at random and withdrawing one coin at random, if that happens to be a gold coin, of the next coin drawn from the same box also being a gold coin.

The solution to this problem is counterintuitive. After pulling out a gold coin first, the probability of pulling out a second gold coin is 66.66%. The goal of this script is to test that probability through a simulation of the problem. It generates random selections from the boxes and calculates the probabilities of pulling out gold and silver coins.

## Installation
To run this script, you will need Python 3 installed on your machine. You can download Python 3 from the official website: https://www.python.org/downloads/

## Usage
To run the script, simply navigate to the directory containing the "two_coins_three_jars.py" file and execute the following command in your terminal:

`python two_coins_three_jars.py`

The script will generate 100,000 random attempts to pick two coins from the three boxes and will calculate the probability of pulling out a gold coin first and the probability of pulling out a second gold coin after pulling out a first.

## Results
The actual results will vary with each simulation run, they should return something similar to this:

```
Total Number of Attempts: 100000
First coin gold: 49998
First coin silver: 50002
Expected chance of first coin being Gold: 50%
Actual chance of first coin being Gold: 50.0%

After first coin Gold:
Second coin Gold: 33332
Second coin Silver: 16666
Expected chance of second coin being Gold: 66.66%
Actual chance of second coin being Gold: 66.66%
```

The results show that the probability of pulling out a gold coin first is roughly 50%, as expected. After pulling out a gold coin first, the probability of pulling out a second gold coin is roughly 66.66%, also as expected.

## Why I Built This
I built this project because I am passionate about coding and I love math. I am an entry-level software engineer with skills in full-stack development and data science. This project allowed me to practice my Python skills and apply my knowledge of probability and statistics to a real-world problem.

## Future Improvements
There are a few ways this project could be improved in the future:

* Increase the number of attempts to get more accurate results.
* Add visualization to help users better understand the probabilities.
* Improve system of random selection.

## License
This project is licensed under the MIT License. Feel free to use and modify the code as you see fit.
