from pathlib import Path
import yaml


def change_data_positive_email():
    def modify_email(email):
        local, domain = email.split('@')
        return f"{local}@{domain}z"

    path = Path("./")

    yaml_files = list(path.rglob("*.yaml"))

    for file_path in yaml_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        print(data)
        for key, value in data.items():
            if 'email' in value:
                value['email'] = modify_email(value['email'])
        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

