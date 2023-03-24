class Name:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return f'Name: {self.name}'


class UpdateName(Name):
    def __init__(self, name: str, surname: str, age: int, height: float):
        super().__init__(name)
        self.surname = surname
        self.age = age
        self.height = height

    def get_update(self):
        return (f'Surname: {self.surname}\n'
                f'Age: {self.age}\n'
                f'Height: {self.height}\n-----')


class Job:
    def __init__(self, profession: str):
        self.profession = profession

    def professions(self):
        return f'Profession: {self.profession}'


class JobTitle(Job):
    def __init__(self, profession: str, experience: float):
        super().__init__(profession)
        self.experience = experience

    def get_experiences(self):
        return f'Experience: {self.experience}\n-----'


class HouseLocation:
    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city

    def locations(self):
        return (f'Country: {self.country}; '
                f'City: {self.city}\n----- ')


class RealEstate:
    def __init__(self, real_state: str):
        self.real_state = real_state

    def real_states(self):
        return f'Real state: {self.real_state}'


main = Name('Ivan')
print(main.get_name())
up = UpdateName('Ivan', 'Smith', 18, 170)
print(up.get_update())
job = Job('encoder')
print(job.professions())
title = JobTitle('encoder', 13)
print(title.get_experiences())
house = HouseLocation('Russia', 'Moscow')
print(house.locations())
estate = RealEstate('airplane')
print(estate.real_states())


