import json
import numpy as np
from algorithm.establishment import Establishment
from algorithm.user import User


class Dataset:

    def __init__(self):
        with open('/Users/aaronabraham/Desktop/stonks_data/customer_profiles.txt') as account_file:
            accounts = json.load(account_file)['result']['customers']
        accounts_by_user_id = {}
        for account in accounts:
            user_id = account['id']
            if user_id not in accounts_by_user_id:
                accounts_by_user_id[user_id] = account

        with open('/Users/aaronabraham/Desktop/stonks_data/new_customer_transactions.txt') as transaction_file:
            transactions_nested = json.load(transaction_file)
        transactions = []
        for subdict in transactions_nested:
            transactions.extend(subdict['result'])

        transactions_by_user = {}
        transactions_by_establishment = {}
        self.establishment_indices_by_tag = {}
        for transaction in transactions:
            user_id = transaction['customerId']
            if user_id not in transactions_by_user:
                transactions_by_user[user_id] = []
            transactions_by_user[user_id].append(transaction)
            establishment_id = transaction['description']
            if establishment_id not in transactions_by_establishment:
                transactions_by_establishment[establishment_id] = []
            transactions_by_establishment[establishment_id].append(transaction)

        self.establishments = []
        for establishment_id in transactions_by_establishment:
            transaction = transactions_by_establishment[establishment_id][0]
            try:
                name = transaction['merchantName']
            except KeyError:
                name = transaction['description']
            try:
                coords = [transaction['locationLatitude'], transaction['locationLongitude']]
            except KeyError:
                continue
            self.establishments.append(Establishment(establishment_id, coords, transaction['categoryTags'][0], transactions_by_establishment[establishment_id], name))

        self.establishment_ids = [establishment.establishment_id for establishment in self.establishments]
        self.users = [User(transactions_by_user[key], self.establishment_ids, accounts_by_user_id[key]) for key in transactions_by_user]
        self.combined_attribute_values = np.stack([user.attribute_values for user in self.users if None not in user.attribute_values])
        self.norm_mean = np.mean(self.combined_attribute_values, axis=0)
        self.norm_std_dev = np.std(self.combined_attribute_values, axis=0)
        if (self.norm_std_dev == 0.0).any():
            self.norm_std_dev = 1.0
        for user in self.users:
            try:
                user.norm_attribute_values = (user.attribute_values - self.norm_mean) / self.norm_std_dev
            except TypeError:
                user.norm_attribute_values = None
        self.main_user = self.users[0]
        self.users = self.users[1:]

    def get_recommendations(self, user_coords, tag, sliders, income):
        sliders = np.array(sliders, dtype=float)
        sliders /= np.sum(sliders)
        self.main_user.attribute_values = np.concatenate([sliders, [income]])
        self.main_user.norm_attribute_values = (self.main_user.attribute_values - self.norm_mean) / self.norm_std_dev
        establishment_visits = self.weighted_establishments(self.main_user)
        for i in range(len(self.establishments)):
            if self.establishments[i].distance_km(user_coords) > 5:
                establishment_visits[i] = -1
            if self.establishments[i].tag != tag:
                establishment_visits[i] = -1
        indices = np.flip(np.argsort(establishment_visits))
        best_establishments = []
        for i in indices[:5]:
            establishment = self.establishments[i]
            best_establishments.append([establishment.coords[0], establishment.coords[1], establishment.name])
        return best_establishments

    def weighted_establishments(self, user):
        weighted_establishment_visits = np.zeros(user.establishment_visits.shape)
        for other_user in self.users:
            if other_user.norm_attribute_values is None or other_user.establishment_visits is None:
                continue
            distance = user.distance(other_user)
            weight = 1 / (distance + 0.1)
            weighted_establishment_visits += weight * other_user.establishment_visits
        weighted_establishment_visits /= np.sum(weighted_establishment_visits)
        return weighted_establishment_visits
