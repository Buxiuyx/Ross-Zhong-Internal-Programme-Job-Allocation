#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}

#Define a function that shows jobs which can be used in adding_jobs and deleting_jobs functions
def show_jobs(dict):
    #Print
    for keys, values in dict.items():
        print("{}, ${} per hour".format(keys, values))


#define a function that shows workers which can be used in view_workers, adding_workers and deleting_workers functions
def showing_worker_list(dict):
    # Show workers that are present
    for keys, values in dict.items():
        # Try and except for empty dict
        try:
            print(keys, values["First name"], values["Last name"])
        except KeyError:
            pass

#def a function that can be used in worker_detail_change for mutiple times.
def changing_detial(dict, change):
    #Enter the changes
    detail_change = input("Please enter new", change).strip().capitalize()
    #append the changes to the dict
    dict[change] = detail_change

#def a function that can be used in worker_detail_change for mutiple times.
def append_jobs_to_dict(dict, change, a, b):
    new_time = float(input("Enter the job time"))
    new_job = {a: change, b: new_time}
    dict.update(new_job)

#def a function that can be used in worker_detail_change for mutiple times.
def remove_jobs_from_dict(dict, change):
    try:
        del dict[change]
        print("You have replaced", change)
    except KeyError:
        pass

#def a function that can be used in worker_detail_change for mutiple times.
#The function has two variables which are the worker's detail dictionary and the job which is adding to his detail dict.
def adding_job_to_worker(dict, job):
    while True:
        #If job1 is not there then the job become job1
        if "Job1" not in dict.keys():
            # Input the job time and update them to member's detail
            alpha, beta = "Job1", "Job1_hours"
            #call the function to append jobs to dict
            append_jobs_to_dict(dict, job, alpha, beta)
            break
        #if job1 is already there and then the job become job2
        elif "Job2" not in dict.keys():
            # Input the job time and update them to member's detail
            alpha, beta = "Job2", "Job2_hours"
            # call the function to append jobs to dict
            append_jobs_to_dict(dict, job, alpha, beta)
            break
        #if job1 and job2 is already there and then the job become job3
        elif "Job3" not in dict.keys():
            # Input the job time and update them to member's detail
            alpha, beta = "Job3", "Job3_hours"
            # call the function to append jobs to dict
            append_jobs_to_dict(dict, job, alpha, beta)
            break
        else:
            # If there are more than Three jobs, Ask the user to delete one job or not
            job_delete = input(
                "Each worker can only have maximum of three jobs. Please enter a job1, "
                "job2 or job3 to delete the current jobs, or enter no "
                "to stop adding jobs").capitalize().strip()
            # delete job1
            if job_delete == "Job1":
               remove_jobs_from_dict(dict, job_delete)
            # delte job2
            elif job_delete == "Job2":
                remove_jobs_from_dict(dict, job_delete)
            # delete job3
            elif job_delete == "Job3":
                remove_jobs_from_dict(dict, job_delete)
            #if the user doesn't want to delete any job
            elif job_delete == "No":
                #break the loop and tell the user that the adding is unsuccessful
                print("your job adding is not successful")
                break
            #if the user enter none of the option above
            else:
                print("that is not an option")

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
