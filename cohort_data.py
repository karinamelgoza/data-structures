"""Functions to parse a file containing student data."""

filename = 'cohort_data.txt'


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    f = open(filename)
    raw_data = f.read().splitlines()

    houses = set()

    for i in raw_data:
        individual = i.split('|')
        if individual[2] != '':
            houses.add(individual[2])

    f.close()

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    f = open(filename)
    raw_data = f.read().splitlines()

    students = []
    all_students = []
    cohort_arg = cohort

    for i in raw_data:
        individual = i.split('|')
        if individual[4] != 'I' and individual[4] != 'G':
            all_students.append(individual)

    for student in all_students:
        ind_cohort = student[4]
        if ind_cohort == cohort_arg:
            students.append(student[0]+' ' + student[1])
        elif cohort_arg == 'All':
            students.append(student[0]+' ' + student[1])

    f.close()

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    f = open(filename)
    raw_data = f.read().splitlines()

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for i in raw_data:
        individual = i.split('|')
        if individual[2] == "Dumbledore's Army":
            dumbledores_army.append(individual[0]+' ' + individual[1])
        elif individual[2] == "Gryffindor":
            gryffindor.append(individual[0]+' ' + individual[1])
        elif individual[2] == "Hufflepuff":
            hufflepuff.append(individual[0]+' ' + individual[1])
        elif individual[2] == "Ravenclaw":
            ravenclaw.append(individual[0]+' ' + individual[1])
        elif individual[2] == "Slytherin":
            slytherin.append(individual[0]+' ' + individual[1])
        elif individual[4] == "G":
            ghosts.append(individual[0]+' ' + individual[1])
        elif individual[4] == "I":
            instructors.append(individual[0]+' ' + individual[1])

    roster = [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(
        ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]

    f.close()

    return roster


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    f = open(filename)
    raw_data = f.read().splitlines()

    all_data = []

    for i in raw_data:
        individual = i.split('|')
        all_data.append(
            (individual[0] + ' ' + individual[1], individual[2], individual[3], individual[4]))

    f.close()

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    f = open(filename)
    raw_data = f.read().splitlines()

    name_input = name
    for i in raw_data:
        individual = i.split('|')
        if name_input == individual[0] + ' ' + individual[1]:
            return individual[4]

    f.close()


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    f = open(filename)
    raw_data = f.read().splitlines()
    f.close()
    last = []
    uniq = []
    dup = set()
    for i in raw_data:
        individual = i.split('|')
        last.append(individual[1])

    for last_name in last:
        if last_name not in uniq:
            uniq.append(last_name)
        else:
            dup.add(last_name)
    return dup


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    f = open(filename)
    raw_data = f.read().splitlines()
    f.close()

    name_input = name
    students = {}
    for i in raw_data:
        individual = i.split('|')
        students[individual[0] + ' ' + individual[1]] = individual[2:]

    housemates = set()
    # print(students[name_input])

    for key in students:
        # print(key)
        if students[key][0] == students[name_input][0] and students[key][2] == students[name_input][2]:
            housemates.add(key)

    housemates.remove(name_input)

    return housemates

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
