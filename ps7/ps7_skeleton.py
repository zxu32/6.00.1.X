import random as rand
import string
import operator

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location

    def get_number_of_species(self, animal):
        return self.species_types.get(animal, 0)

    def get_location(self):
        x = self.location[0]
        y = self.location[1]
        return (float(x), float(y))

    def get_species_count(self):
        return self.species_types.copy()#, len(self.species_types)

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        if species in self.species_types:
            self.species_types[species] -= 1
            if self.species_types[species] <= 1:
                del self.species_types[species]


class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        score = 1 * AdoptionCenter.get_number_of_species(adoption_center, self.desired_species)
        return float(score)


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        score = Adopter.get_score(self, adoption_center) + 0.3*sum(AdoptionCenter.get_number_of_species(adoption_center, i) for i in self.considered_species)
        return round(score, 15)



class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        score = max(0.0, Adopter.get_score(self, adoption_center) - 0.3 *AdoptionCenter.get_number_of_species(adoption_center, self.feared_species))
        return round(score, 15)


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        if any(i in AdoptionCenter.get_species_count(adoption_center) for i in self.allergic_species):
            score = 0.0
        else:
            score = Adopter.get_score(self, adoption_center)
        return round(score, 15)



class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness


    def get_score(self, adoption_center):
        if any(i in AdoptionCenter.get_species_count(adoption_center) for i in self.allergic_species):
            allergicList = set.intersection(set(self.allergic_species), set(AdoptionCenter.get_species_count(adoption_center)))
            score = Adopter.get_score(self, adoption_center) * min(self.medicine_effectiveness[i] for i in allergicList)
        else:
            score = Adopter.get_score(self, adoption_center)
        return round(score, 15)

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will assign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    def get_linear_distance(self, to_location):
        distance = ((self.location[0] - to_location[0])**2 + (self.location[1] - to_location[1])**2)**0.5
        return distance
    def get_score(self, adoption_center):
        distance = self.get_linear_distance(adoption_center.get_location())
        score = 0
        if distance < 1:
            score = Adopter.get_score(self, adoption_center)
        if 1 <= distance < 3:
            score = rand.uniform(.7, .9) * Adopter.get_score(self, adoption_center)
        if 3 <= distance <= 5:
            score = rand.uniform(.5, .7) * Adopter.get_score(self, adoption_center)
        if 5 <= distance:
            score = rand.uniform(.1, .5) * Adopter.get_score(self, adoption_center)
        return round(score, 15)


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    scoreList = []
    for i in list_of_adoption_centers:
        item = [i, adopter.get_score(i)]
        scoreList.append(item)
    scoreList.sort(key=lambda score: score[1], reverse=True)
    return [item[0] for item in scoreList]


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    scoreList = []
    for i in list_of_adopters:
        item = [i, i.get_score(adoption_center)]
        print(item[1])
        scoreList.append(item)
    scoreList.sort(key=lambda score: score[1], reverse=True)

    top_n_list = [item[0] for item in scoreList]
    return top_n_list
