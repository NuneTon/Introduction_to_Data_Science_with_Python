import pandas as pd

f = open('Other\data.csv', 'r')
lines = f.readlines()
for i in range(0, len(lines)):
    line = lines[i]
    line = line.replace('"', '')
    line = line.replace(',', '')
    line = line.replace('\t', '')
    if line.strip() == '' or line.strip()[0] == '+':
        continue
    if line.strip() == 'Region':
        file_name = "Other\converted_regions.csv"
        this_case = 'reg'
        continue
    elif line.strip() == 'Location':
        file_name = "Other\converted_location.csv"
        this_case = 'loc'
        continue
    elif line.strip() == 'employees.csv':
        file_name = "Other\converted_employees.csv"
        this_case = 'emp'
        continue
    if this_case == 'reg':
        lst = line.split('|')
        dic = {'REGION_ID': [lst[1].strip()], 'REGION_NAME': [lst[2].strip()]}
    elif this_case == 'loc':
        lst = line.split('|')
        dic = {'LOCATION_ID': [lst[1].strip()], 'STREET_ADDRESS': [lst[2].strip()], 'POSTAL_CODE': [lst[3].strip()],
               'CITY': [lst[4].strip()], 'STATE_PROVINCE': [lst[5].strip()], 'COUNTRY_ID': [lst[6].strip()]}
    elif this_case == 'emp':
        lst = line.split('|')
        dic = {'EMPLOYEE_ID': [lst[1].strip()], 'FIRST_NAME': [lst[2].strip()], 'LAST_NAME': [lst[3].strip()],
               'EMAIL': [lst[4].strip()], 'PHONE_NUMBER': [lst[5].strip()], 'HIRE_DATE': [lst[6].strip()],
               'JOB_ID': [lst[7].strip()], 'SALARY': [lst[8].strip()], 'COMMISSION_PCT': [lst[9].strip()],
               'MANAGER_ID': [lst[10].strip()], 'DEPARTMENT_ID': [lst[11].strip()]}
    df = pd.DataFrame(dic)
    df.to_csv(file_name, mode='a', header=False)
f.close()


# task1
# Write a Pandas program to display all the records of REGIONS file

def regions_data():
    df = pd.read_csv("Other\converted_regions.csv")
    return df


# task 2
# Write a Pandas program to display all the location id from locations file

def display_locations_id():
    df = pd.read_csv("Other\converted_location.csv", index_col='LOCATION_ID')
    return df


# task3
# Write a Pandas program to extract first 7 records from employees file.
def seven_employees():
    df = pd.read_csv("Other\converted_employees.csv", nrows=7)
    return df


# task 4
# Write a Pandas program to select distinct department id from employees file
def distinct_department_id():
    df = pd.read_csv("Other\converted_employees.csv")
    return df["DEPARTMENT_ID"].unique()


# task5
# Write a Pandas program to display the first, last name, salary and department number for those employees whose first name starts with the letter 'S'.

def start_with_s():
    df = pd.read_csv("Other\converted_employees.csv")
    df_1 = df[df["FIRST_NAME"].str.startswith("S")]
    return df_1[["FIRST_NAME", "LAST_NAME", "SALARY", "DEPARTMENT_ID"]]


def main():
    print(regions_data())
    print(display_locations_id())
    print(seven_employees())
    print(distinct_department_id())
    print(start_with_s())


main()
