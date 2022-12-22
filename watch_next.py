import spacy


nlp = spacy.load("en_core_web_md")

hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"


def watch_next(description):

    # Read the file and store the data in a dictionary

    movies_dict = {}
    with open("movies.txt", "r") as f:
        for line in f:
            title, desc = line.strip().split(" :")
            movies_dict[title] = desc
        # print(movies_dict)

    # Set the description of the previously watched movie

    hulk_desc = nlp(hulk_description)

    # Empty dictionary to store the similarity scores for each movie

    similarity_scores = {}

    # Calculate the similarity score for each movie

    for title, desc in movies_dict.items():

        # Process the movie description with the spacy library

        movie_description = nlp(desc)

        # Calculate the similarity score using the spacy library's similarity method

        similarity_score = hulk_desc.similarity(movie_description)

        # Add the similarity score for this movie to the dictionary

        similarity_scores[title] = similarity_score

    # Find the movie with the highest similarity score

    suggested_film = max(similarity_scores, key=similarity_scores.get)

    # Return the title of the movie with the highest similarity score

    return suggested_film


print(watch_next(hulk_description))
