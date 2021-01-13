import numpy as np

ATTRIBUTE_WEIGHTS = np.array([1, 1, 1, 1, 1, 1, 6])

TAGS = ['Auto and Transport', 'Entertainment', 'Food and Dining', 'Health and Fitness', 'Home', 'Shopping']


class User:

    def __init__(self, transactions, establishment_ids, account):
        self.establishment_visits = np.zeros(len(establishment_ids))
        total_expenditure = sum(transaction['currencyAmount'] for transaction in transactions)
        expenditure_by_tag = {}
        for transaction in transactions:
            establishment_id = transaction['description']
            try:
                index = establishment_ids.index(establishment_id)
            except ValueError:
                continue
            self.establishment_visits[index] += 1

            tag = transaction['categoryTags'][0]
            if tag not in expenditure_by_tag:
                expenditure_by_tag[tag] = 0
            expenditure_by_tag[tag] += transaction['currencyAmount']

        values_in_order = []
        for tag in TAGS:
            if tag in expenditure_by_tag:
                values_in_order.append(expenditure_by_tag[tag])
            else:
                values_in_order.append(0.0)
        normalized_values = [value / total_expenditure for value in values_in_order]
        try:
            self.income = account['totalIncome']
        except KeyError:
            self.income = None
        self.attribute_values = np.array(normalized_values + [self.income])

        if np.sum(self.establishment_visits) > 0.001:
            self.establishment_visits /= np.sum(self.establishment_visits)
        else:
            self.establishment_visits = None
        self.norm_attribute_values = None

    def distance(self, other_user):
        return np.sum(ATTRIBUTE_WEIGHTS * np.square(self.norm_attribute_values - other_user.norm_attribute_values))
