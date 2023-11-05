import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/
#
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is
# created in the file `pets_db.py`.
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

SELECT a.name,a.species,a.age FROM animals as a WHERE animal_id NOT IN (SELECT pet_id FROM people_animals);

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners.
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(*) FROM people_animals as pa INNER JOIN people as p ON p.person_id = pa.owner_id INNER JOIN animals as a ON a.animal_id= pa.pet_id WHERE a.age>p.age;

"""

# Part 4.C: BONUS CHALLENGE!
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

SELECT p.name,a.name,a.species FROM people_animals as pa INNER JOIN people as p ON p.person_id = pa.owner_id INNER JOIN animals as a ON a.animal_id= pa.pet_id WHERE pa.owner_id =(SELECT p.person_id FROM people as p WHERE p.name='bessie');

"""
