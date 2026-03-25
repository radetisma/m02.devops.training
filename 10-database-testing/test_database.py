import unittest
import database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        database.init_database()
        database.delete_all_users()

    def tearDown(self):
        database.delete_all_users()

    def test_create_user(self):
        user_id = database.create_user("John", "john@test.com", 30)
        self.assertIsNotNone(user_id)

    def test_create_duplicate_user(self):
        database.create_user("John", "john@test.com", 30)

        with self.assertRaises(ValueError):
            database.create_user("Jane", "john@test.com", 25)

    def test_get_user_by_id(self):
        user_id = database.create_user("John", "john@test.com", 30)
        user = database.get_user_by_id(user_id)

        self.assertEqual(user["name"], "John")

    def test_get_user_by_email(self):
        database.create_user("John", "john@test.com", 30)
        user = database.get_user_by_email("john@test.com")

        self.assertEqual(user["name"], "John")

    def test_get_all_users(self):
        database.create_user("A", "a@test.com")
        database.create_user("B", "b@test.com")

        users = database.get_all_users()
        self.assertEqual(len(users), 2)

    def test_update_user(self):
        user_id = database.create_user("John", "john@test.com", 30)

        success = database.update_user(user_id, name="Johnny")
        self.assertTrue(success)

        user = database.get_user_by_id(user_id)
        self.assertEqual(user["name"], "Johnny")

    def test_update_nonexistent(self):
        success = database.update_user(999, name="Ghost")
        self.assertFalse(success)

    def test_delete_user(self):
        user_id = database.create_user("John", "john@test.com", 30)

        success = database.delete_user(user_id)
        self.assertTrue(success)

    def test_delete_nonexistent(self):
        success = database.delete_user(999)
        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()