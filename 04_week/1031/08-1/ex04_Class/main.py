import csv
from member import Member

def load_members_from_csv(filename):
    members = []
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            member = Member(row['id'], row['name'], int(row['age']))
            members.append(member)
    return members

if __name__ == "__main__":
    members = load_members_from_csv("D:\\c402_LJH\\python\\04_week\\1031\\08-1\\ex04_Class\\member-info.csv")

    print(members)
    print(type(members))

    for member in members:
        print(f"ID: {member.get_id()}")
        print(f"Name: {member.get_name()}")
        print(f"Age: {member.get_age()}")
        print("-" * 30)
