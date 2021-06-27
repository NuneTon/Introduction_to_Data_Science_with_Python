import pandas as pd

f = open("Other\school_data.csv", 'r')
lines = f.readlines()
headers = lines[0].split()
n_list = []
school_list = []
class_list = []
name_list = []
date_list = []
age_list = []
height_list = []
weight_list = []
address_list = []
for i in lines[1:7]:
    i = i.split()
    i[3] = i[3] + " " + i[4]
    i.remove(i[4])
    n_list.append(i[0])
    school_list.append(i[1])
    class_list.append(i[2])
    name_list.append(i[3])
    date_list.append(i[4])
    age_list.append(int(i[5]))
    height_list.append(int(i[6]))
    weight_list.append(int(i[7]))
    address_list.append(i[8])
dict = {"N": n_list, headers[0]: school_list, headers[1]: class_list, headers[2]: name_list, headers[3]: date_list,
        headers[4]: age_list, headers[5]: height_list, headers[6]: weight_list, headers[7]: address_list}
df = pd.DataFrame(dict)
f.close()

#task1
#Write a Pandas program to split the following dataframe into groups based on school code
for a in df.groupby(["school"]):
    print(a)

#task2
#Write a Pandas program to split the following given dataframe by school code and get mean, min, and max value of age for each school
print("Means of ages by school are \n", df["age"].groupby(df["school"]).mean())
print("Min of ages by school are \n",df["age"].groupby(df["school"]).min())
print("Max of ages by school are \n",df["age"].groupby(df["school"]).max())

#task3
#Write a Pandas program to split the following given dataframe into groups based on school code and class
for b in df.groupby(["school", "class"]):
    print(b)

#task4
#Write a Pandas program to split the following given dataframe into groups based on school code and cast grouping as a list
group=[]
for c in df.groupby(["school"]):
    group.append(c)
print(group)

#task5

o = open("Other\school_data.csv", 'r')
rows = o.readlines()
columns = rows[9].split()
no_list = []
order_list = []
purchase_list = []
date_list = []
customer_list = []
salesman_list = []

for t in rows[10:23]:
    t = t.split()
    no_list.append(t[0])
    order_list.append(t[1])
    purchase_list.append(float(t[2]))
    date_list.append(t[3])
    customer_list.append(t[4])
    salesman_list.append(t[5])
dict = {"No": no_list, columns[0]: order_list, columns[1]: purchase_list, columns[2]: date_list, columns[3]: customer_list,
        columns[4]: salesman_list}
df = pd.DataFrame(dict)
o.close()

#task5
#Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id)

print("Means of purchase amount by customer_id are \n", df["purch_amt"].groupby(df["customer_id"]).mean())
print("Min of purchase amount by customer_id are \n",df["purch_amt"].groupby(df["customer_id"]).min())
print("Max of purchase amount by customer_id are \n",df["purch_amt"].groupby(df["customer_id"]).max())