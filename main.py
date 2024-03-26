# Part 1
def read_csv(filename):
    """
    Process CSV file

    Arguments:
    filename: string - the name of the csv file

    Return:
    list - [header: list, data: list]
    """
    # Type your code below
    with open(filename, "r") as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i]=data[i].split(",")
        header = data[0]
        data.pop(0)
        # file.close() gets called automatically
    # Change data types of the data
    new_data = []
    for i in data:
        new_data.append([
            int(i[0]), # year
            i[1], # age
            i[2], # sex
            int(i[3]) # enrollment jc
        ])
    # remove "\n" from last header element
    header[-1] = header[-1][:-1]
    return [header, new_data]


# Part 2
def filter_gender(enrolment_by_age, sex):
    """a"""
    new_data = []
    for data in enrolment_by_age:
        if data[2] == sex:
            data.pop(2)
            new_data.append(data)
    return new_data

# Part 3
def sum_by_year(enrolment):
    """a"""
    data = {}
    for item in enrolment:
        year = item[0]
        if year in data:
            data[year] += item[-1]
        else:
            data[year] = item[-1]
    final = []
    for year in data:
        final.append([year, data[year]])
    return final


# Part 4
def write_csv(filename, header, data):
    """a"""
    with open(filename, "w") as file:
        header[-1] += "\n"
        header = ",".join(header)
        to_write = [header]
        for i in data:
            # make every element a string
            for index in range(len(i)):
                i[index] = str(i[index])

            to_write.append(",".join(i))
            to_write[-1] += "\n"

        file.writelines(to_write)
        # calls file.close() automatically

    return len(to_write)


# TESTING
# You can write code below to call the above functions
# and test the output
# h,d=read_csv("pre-u-enrolment-by-age.csv")
# write_csv("total-enrolment-by-year.csv",h,d)
# Tests removed/commented out for submission