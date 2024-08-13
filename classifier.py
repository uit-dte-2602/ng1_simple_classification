# Add more imports as/if needed...
from data import class_type, data_train, features

# Allowed imports: Modules included in Python (see https://docs.python.org/3.10/py-modindex.html),
# and external libraries listed in requirements.txt


# Helper function for showing data (not part of assignment)
def print_data():
    """ Print animal name and feature names and values """
    for animal_name, animal_features in data_train.items():
        feature_string = ', '.join([f'{feature_name} = {feature_value}'
                                    for feature_name, feature_value in zip(features, animal_features)])
        print(f'{animal_name}: ' + feature_string)


# Modify the code below to return "sensible" classes based on input features.
# Feel free to add and remove code, the silly if statements below are only
# meant to show how features can be used and combined.
# The code returns the placeholder integer 0 in every case. The final classifier
# must return integers in the range 1-7 (corresponding to 7 animal classes)
def classify_animal(hair, feathers, eggs, milk, airborne, aquatic, predator, toothed,
                    backbone, breathes, venomous, fins, legs, tail, domestic, catsize):
    """ Classifies animal based on 16 features 

    Arguments:
    ----------
    hair, feathers, ... : int
        Features descibing an animal

    Returns:
    ---------
    class_int: int
        Integer in range 1-7 corresponding to 7 classes of animal

    """
    pass


def run_classifier():
    """ Run classifier for every animal (row) in training dataset """
    n_correct_classifications = 0
    for data_row in data_train.values():
        class_int = data_row[-1]
        animal_features = data_row[:-1]
        if classify_animal(*animal_features) == class_int:
            n_correct_classifications += 1
    print('Number of correct classifications: ' +
          f'{n_correct_classifications} / {len(data_train)}')


if __name__ == "__main__":
    # print_data()
    run_classifier()
