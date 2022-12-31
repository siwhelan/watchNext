# watchNext

Welcome to watchNext - the Movie Recommendation System! This program allows you to get movie recommendations based on the similarity of their descriptions. Simply enter the description of a movie you have recently watched, and the program will use the spacy library to process the descriptions of a list of movies stored in a text file and calculate the similarity scores between the entered movie and each of the other movies. The movie with the highest similarity score will then be recommended to you as the next film to watch.

## Installation

To use the Movie Recommendation System, you will need to have the following dependencies installed:

    spacy

You can install these dependencies using pip:

  pip install spacy

## Usage

To use the program, simply run it and enter the description of the movie you have recently watched when prompted. The program will then output the title of the recommended movie for you to watch next.

  python watch_next.py

## Error Handling

In the event that there are any issues with reading or processing the data from the text file, the program includes error handling to ensure that it does not crash.

## Feedback

If you have any feedback, please reach out to me at simon@swhelan.dev
