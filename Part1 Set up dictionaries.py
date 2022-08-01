#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}

#Set a function that could return a string variable of "Worker + number"(finished)
def return_strvariable(x):
    strvariable = "Worker"
    strvariable += str(x)
    #return the string
    return(strvariable)

#def a function that could add new keys and values in workers.dict using the form of {"Worker+number": {}}(finished)
def adding_index_dict():
    #We already have 5 keys and values in worker.dict so we start from 6
    number = 6
    #make a loop
    while True:
        #If the string + number is already inside the workers.dict, then plus the number by 1 and
        #make workers + (number+1) until the number is not repeated in the workers.dict
        if return_strvariable(number) in workers.keys():
            number += 1
        #The number is now the biggest in the workers.dict
        else:
            #We now set an empty dict, x which is the dict to store worker's details
            x = {}
            #Update the workers.dict with {"Workers + number": {}}
            workers[return_strvariable(number)] = x
            #As one new key is added to the dict, then break the loop.
            break
