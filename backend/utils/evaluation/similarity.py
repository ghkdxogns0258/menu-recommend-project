import numpy as np

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def recommend_similar_menus(menu, menu_data, threshold=0.8):
    liked_features = menu['features']
    similar_menus = []

    for candidate in menu_data:
        similarity = cosine_similarity(liked_features, candidate['features'])
        if similarity >= threshold:
            similar_menus.append(candidate)
            
    return similar_menus
