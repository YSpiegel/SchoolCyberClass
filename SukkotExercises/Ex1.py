import datetime


def date_data(date):
    """
      Returns age and checks for a birthday
      :param date:
      :return: [age, has_bd]
      """
    today = date.today()
    has_bd = today.day == date.day and today.month == date.month
    age = today.year - date.year
    if today.month < date.month or (date.month == today.month and date.day < today.day):
        age -= 1
    return [age, has_bd]


birthdate = input("Enter your birthdate: ")  # received as DD/MM/YYYY
birthdate = birthdate.split("/")
birthdate = datetime.date(int(birthdate[2]), int(birthdate[1]), int(birthdate[0]))
data = date_data(birthdate)
print(f"You are {data[0]} years old and you {'have' if data[1] else 'do not have'} a birthday")
