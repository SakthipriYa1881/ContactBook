from asyncore import write
import sys
import csv

def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

add(['Anonymous','8825800294','sakthiii@mail.com','bangalore'])
add(['demo','883759989', 'adajkjf@mail.com', 'Bangalore'])
def view():
    data=[]
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
view()

def remove(i):
    def save(j):
        with open('data.csv') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    phone = i

    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

        for element in row:
            if element == phone:
                new_list.remove(row)

    save(new_list)


def update(i):

    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(i)
    new_list = []
    phone = i[0]
    #['Anonymous','8825800294','sakthiii@mail.com','bangalore']


    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == phone:
                    name= i[1]
                    phn= i[2]
                    mail =i[3]
                    addr =i[4]

                    data = [name,phn,mail,addr]
                    index= new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

#sample = ['123','girlcoder','sal@mail','banglore']
#update(sample)

def search(i):
    data = []
    phone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == phone:
                    data.append(row)

    return data
