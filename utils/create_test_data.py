import yaml


def create_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        test_data = yaml.safe_load(f)
        for key in test_data:
            data.append((test_data[key]["test_name"],
                         {"email": test_data[key]["email"], "password": test_data[key]["password"]}))
        print(data)
    return data

# create_data("../test/register_user/data/data_correct_email.yaml")
