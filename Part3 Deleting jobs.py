#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}


#Define a function to delete jobs in the dict.
def deleting_jobs():
    #A loop
    while True:
        #Show jobs
        for job, salary in jobs.items():
            print("{}, ${} per hour".format(job, salary))
        #Ask the user to enter the job they need to delete
        job_deleting = input("What job you wanna delete").title()
        #Check if the job is in the jobs.dict
        if job_deleting in jobs.keys():
            x = jobs.pop(job_deleting)
            print("The new job list:")
            #Print the new jobs.dict and show the user that the job is deleted
            for job, salary in jobs.items():
                print("{}, ${} per hour".format(job, salary))
            print("Job '{}' has been deleted from the job list".format(job_deleting))
        #If there isn't the job, then print the string.
        else:
            print("Sorry, '{}' not in the job list".format(job_deleting))
        #Ask the user to do the loop.
        keep = input("Do you want to keep deleting? Enter yes or no").title().strip()
        if keep == "Yes" or keep == "Y":
            pass
        else:
            break

deleting_jobs()