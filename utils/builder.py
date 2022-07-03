import faker

fake = faker.Faker()


class Builder:

    @staticmethod
    def fake_name() -> str:
        return fake.name().split(' ')[0]

    @staticmethod
    def fake_username() -> str:
        return fake.profile(fields=['username'])['username']

    @staticmethod
    def fake_email() -> str:
        return fake.email()

    @staticmethod
    def fake_phone_number() -> str:
        return f'{fake.msisdn()[0:3]}'