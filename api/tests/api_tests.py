import pytest
from jsonschema import validate
import api.stuff.schemas.schemas

from api.tests.base import BaseApi


class TestStatus(BaseApi):
    def test_status(self):
        answer = self.api_client.get_status()
        assert answer.status_code == 404


class TestPet(BaseApi):

    # POST
    @pytest.mark.parametrize('name', [123, "Tihon"],
                             ids=['integer_name', 'string_name'])
    def test_create_pet(self, name):
        new_pet = self.api_client.create_pet(name=name)
        assert new_pet.status_code == 200
        new_pet = new_pet.json()
        validate(instance=new_pet, schema=api.stuff.schemas.schemas.schema_pet_create)

    # PUT
    def test_update_pet(self):
        new_pet = self.api_client.create_pet()
        assert new_pet.status_code == 200
        new_pet = new_pet.json()
        id_new_pet = new_pet['id']
        res = self.api_client.update_existing_pet(id_new_pet)
        assert res.status_code == 200
        validate(instance=res.json(), schema=api.stuff.schemas.schemas.schema_pet_update)

    # DELETE
    def test_delete_pet(self):
        new_pet = self.api_client.create_pet().json()
        id_new_pet = new_pet['id']
        result = self.api_client.delete_pet(id_new_pet)
        assert result.status_code == 200
        result = result.json()
        assert result['message'] == str(id_new_pet)
        validate(instance=result, schema=api.stuff.schemas.schemas.schema_pet_delete)
        result = self.api_client.delete_pet(id_new_pet)
        assert result.status_code == 404

    #GET
    def test_find_pet_by_id(self):
        new_pet = self.api_client.create_pet().json()
        id_new_pet = new_pet['id']
        result = self.api_client.find_pet_by_id(id_new_pet)
        assert result.status_code == 200
        result = result.json()
        validate(instance=result, schema=api.stuff.schemas.schemas.schema_pet_get)


class TestUser(BaseApi):

    #CREATE
    def test_create_user(self):
        new_user = self.api_client.create_user()
        assert new_user.status_code == 200
        validate(instance=new_user.json(), schema=api.stuff.schemas.schemas.schema_user_get)



