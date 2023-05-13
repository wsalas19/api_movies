from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer



model_data = [];
cv = CountVectorizer(stop_words='english')
cv_matrix = cv.fit_transform(model_data['text'])
cosine_sim = cosine_similarity(cv_matrix,cv_matrix)

def recomendaciones(titulo, cosine_sim = cosine_sim):
    # Getting the index of the movie that matches the title
    idx = model_data[model_data['title'] == str(titulo).lower()].index[0]
    # Getting the similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    #Sorting the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Getting the top 5 recommendations
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    recommendations=list(model_data['title'].iloc[movie_indices].str.title())
    return {'lista recomendada': recommendations} 