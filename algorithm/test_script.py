from algorithm.dataset import Dataset

dataset = Dataset()
user_coords = [43.75, -79.45]
recommendations = dataset.get_recommendations(user_coords, 'Food and Dining', [0.2, 0.2, 0.2, 0.2, 0.1, 0.1], 30000)
for e in recommendations:
    print(e)
