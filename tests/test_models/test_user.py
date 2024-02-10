#!/usr/bin/python3
"""
Module for testing the functionality of the User class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User as MyUser


class TestMyUserInstantiation(unittest.TestCase):
    """
    Test cases for verifying the instantiation of the MyUser class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(MyUser, type(MyUser()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(MyUser(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(MyUser().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(MyUser().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(MyUser().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(MyUser.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(MyUser.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(MyUser.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(MyUser.last_name))

    def test_two_users_unique_ids(self):
        user1 = MyUser()
        user2 = MyUser()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_users_different_created_at(self):
        user1 = MyUser()
        sleep(0.05)
        user2 = MyUser()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_users_different_updated_at(self):
        user1 = MyUser()
        sleep(0.05)
        user2 = MyUser()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        user1 = MyUser()
        user1.id = "777777"
        user1.created_at = user1.updated_at = my_date
        user1_str = user1.__str__()
        self.assertIn("[User] (777777)", user1_str)
        self.assertIn("'id': '777777'", user1_str)
        self.assertIn("'created_at': " + my_date_repr, user1_str)
        self.assertIn("'updated_at': " + my_date_repr, user1_str)

    def test_args_unused(self):
        user1 = MyUser(None)
        self.assertNotIn(None, user1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        user1 = MyUser(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(user1.id, "777")
        self.assertEqual(user1.created_at, my_date)
        self.assertEqual(user1.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            MyUser(id=None, created_at=None, updated_at=None)


class TestMyUserSave(unittest.TestCase):
    """
    Test cases for validating the save method of the MyUser class.
    """

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp_file.json")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp_file.json", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user = MyUser()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = MyUser()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        user = MyUser()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = MyUser()
        user.save()
        user_id = "User." + user.id
        with open("file.json", "r") as file:
            self.assertIn(user_id, file.read())


class TestMyUserToDict(unittest.TestCase):
    """
    Test cases for ensuring the correctness of the to_dict method of MyUser class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(MyUser().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = MyUser()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = MyUser()
        user.middle_name = "Holberton"
        user.my_number = 98
        self.assertEqual("Holberton", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = MyUser()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["id"]))
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        user = MyUser()
        user.id = "777777"
        user.created_at = user.updated_at = my_date
        tdict = {
            'id': '777777',
            '__class__': 'User',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(user.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        user = MyUser()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        user = MyUser()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()

