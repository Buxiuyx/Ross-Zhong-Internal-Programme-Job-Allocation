#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}


#define a function that shows the workers_details inside the function viewing_workers()
def workers_detail():
    #A loop
    while True:
        #Print the member's number, first name and last name
        for worker, worker_detail in workers.items():
            if "First name" in worker_detail.keys() and "Last name" in worker_detail.keys():
                print(worker, worker_detail["First name"], worker_detail["Last name"])
            #If there is nothing in the dict, it passes so there won't be ValueError or KeyError bugs.
            else:
                pass
        #Ask the user to choose a member to see his detail.
        choose = input("Whose detail you wanna look at? Enter the worker and his number or enter No or N to return.").capitalize().strip()
        #To check if the member is in the dict
        if choose in workers.keys():
            print(workers[choose])
            #Ask the user if he wants to change the member's detail, and call the function to change detail
            change = input("Do you want to change his detail? Enter yes, y").strip().lower()
            if change == "y" or change == "yes":
                worker_detail_change(workers[choose])
        #If the user don't want to change the detail then break the loop
        elif choose == "No" or choose == "N":
            break
        #If the user enter the wrong person/number, then it prints to tell the user that the person is not in the members
        else:
            print("Sorry,", choose, "is not in the members")


#define a function that shows the salary of workers inside the function viewing_workers()
def workers_salary():
    #Set number variables
    daily_total_paid = 0.00
    weekly_total_paid = 0.00
    weekly_salary = 0.00
    daily_salary = 0.00
    job1_daily_salary = 0.00
    job2_daily_salary = 0.00
    job3_daily_salary = 0.00
    #Pick up every worker's detail
    for worker, worker_detail in workers.items():
        #If they have job1 then take the salary from job1, and set a variable for job1's salary
        if "Job1" in worker_detail:
            #take out job1
            job1 = worker_detail['Job1']
            #Take out job1's salary from the jobs.dict by job1
            job1_charges = jobs[job1]
            #Take out the work time
            job1_time = worker_detail["Job1_hours"]
            #Calculate the salary from job 1
            job1_daily_salary = job1_charges * job1_time
            #Add the money to daily salary.
            daily_salary += job1_daily_salary
        else:
            pass
        #Same as What Job1 did
        if "Job2" in worker_detail:
            job2 = worker_detail["Job2"]
            job2_charges = jobs[job2]
            job2_time = worker_detail["Job2_hours"]
            job2_daily_salary = job2_charges * job2_time
            daily_salary += job2_daily_salary
        else:
            pass
        #Same as what job1 did
        if "Job3" in worker_detail:
            job3 = worker_detail["Job3"]
            job3_charges = jobs[job3]
            job3_time = worker_detail["Job3_hours"]
            job3_daily_salary = job3_charges * job3_time
            daily_salary += job3_daily_salary
        else:
            pass
        #if there is work day per week in worker's detail than calculate the weekly salary
        if "Work day per week" in worker_detail:
            weekly_salary = daily_salary * worker_detail["Work day per week"]
            print(worker, worker_detail["First name"], worker_detail["Last name"], "Daily salary: {:.2f}$"
                  .format(daily_salary), "Weekly salary: {:.2f}$".format(weekly_salary))
        #If there isn't that detail than just print the daily salary
        else:
            try:
                print(worker, worker_detail["First name"], worker_detail["Last name"], "Daily salary: {:.2f}$"
                      .format(daily_salary))
            except KeyError:
                pass
    #Calculate the total paid after calculate each worker's salary.
    daily_total_paid += daily_salary
    weekly_total_paid += weekly_salary
    #Print out the total paid
    print("Daily total paid is {:.2f}$\nWeekly total paid is {:.2f}$".format(daily_total_paid, weekly_total_paid))

workers_detail()