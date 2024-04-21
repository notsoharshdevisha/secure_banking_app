import os


def destroy_test_db() -> None:
    test_db_path: str = "./test_bank.db"
    if os.path.exists(test_db_path):
        os.remove(test_db_path)


if __name__ == "__main__":
    destroy_test_db()
