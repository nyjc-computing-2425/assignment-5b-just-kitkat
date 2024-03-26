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
    """
    Filter the enrolment list by sex

    Arguments:
    enrolment_by_age: list - a list containing enrolment info (nested list)
    sex: string - "F" or "MF"

    Return:
    list: a list of similar structure to enrolment_by_age but only consisting of details where the "sex" column matches the "sex" argument
    """
    new_data = []
    for data in enrolment_by_age:
        if data[2] == sex:
            data.pop(2)
            new_data.append(data)
    return new_data

# Part 3
def sum_by_year(enrolment):
    """
    Calculate the total enrolment number in each year

    Arguments: 
    enrolment: list - a nested list containing enrolment details

    Return:
    list: a list of lists where each element contains [year, total_enrolment]
    """
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
    """
    Write the header and data to a csv

    Arguments:
    filename: str - name of the file to write the data to
    header: list - the header, where each element is a header
    data: list - enrolment data

    Return:
    int - number of lines written to the file
    """
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

        # remove the last newline to ensure "lines written" is accurate
        to_write[-1] = to_write[-1][:-1]
        file.writelines(to_write)
        # calls file.close() automatically

    return len(to_write)


# TESTING
# You can write code below to call the above functions
# and test the output
# h,d=read_csv("pre-u-enrolment-by-age.csv")
# print(write_csv("total-enrolment-by-year.csv",h,d))
# Tests removed/commented out for submission