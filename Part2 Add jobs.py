#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}


#define the function
def adding_jobs():
    while True:
        #Print the jobs
        for job, salary in jobs.items():
            print("{}, {}$ per hour".format(job, salary))
        #Ask the user the jobs they want to add
        job_adding = input("Enter the job type you want to add, or enter no to exit").title().strip()
        #to detect if the user wants to exit or keep.
        if job_adding != "No" and job_adding != "N":
            #Create a loop that it only ends when the user want to stop
            while True:
                #Create a try/except function that it only accept numbers or floats for the hourly salary of the job.
                try:
                    salary_adding = float(input('Please enter the hourly salary of "{}"'.format(job_adding)))
                    #Update the dictionary to put the new job in to it.
                    jobs.update({job_adding: salary_adding})
                    #Print the jobs in list so the user knows the job is added
                    for job, salary in jobs.items():
                        print("{}, {}$ per hour\n".format(job, salary))
                    break
                #If the user's input is a string or not a float, it (the function) asks the user to keep and try it again.
                except ValueError:
                    print("Please enter a number")
                    keep = input("Do you want to keep adding the job?").strip().lower()
                    if keep == "yes" or keep == "y":
                        change_job = input("Do you want to change the job you want to add?").strip().lower
                        if change_job == 'yes' or change_job == "y":
                            job_adding = input('Enter the job you want to add')
                        else:
                            pass
                        #Because the try/except function is in a loop, so you don't have to write code completely.
                        #'Pass' so that the code can go over and over again until code 'break'
                    else:
                        break
        else:
            break
        #If the user done a loop, It asks the user does he want to go over again.
        keep = str(input("Do you want to keep adding? Enter yes to continue")).strip().title()
        if keep == "Yes" or keep == "Y":
            pass
        else:
            break

adding_jobs()