#My Own Program
#Group Job Manager, can store people's detail.
#You can add members to it and stored their details.
#Set jobs, salary, work hours and work days for the members.
#Calculate the cost


#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}


#Define a function that add jobs and the salary for the job(finished)
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

#Define a function that delete jobs(finished)
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

#Define a function that view the workers details(finished)
def viewing_workers():
    #Loop
    while True:
        function = input("""1, Workers' detail
2, Workers' salary
Enter 1 or 2, or enter exit to return""").strip().lower()
        #Select the function
        if function == '1':
            workers_detail()
        elif function == '2':
            workers_salary()
        elif function == "exit":
            break
        else:
            print("That's not an option")

#define a function that shows the workers_details inside the function viewing_workers()(finished)
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

#def a function inside workers_detail for changing details(finished)
def worker_detail_change(detail):
    #Make a loop
    while True:
        #Ask the user to choose the one they want to change
        change = input("What do you want to change? Enter 'First name', 'Last name', 'Job', 'Job hours', "
                       "'Work day per week' and so on").strip().capitalize()
        #Change member's first name
        if change == "First name":
            #Ask for the new first name and update it
            detail_change = input("Please enter new first name").strip().capitalize()
            detail["First name"] = detail_change
        #Change member's last name
        elif change == "Last name":
            #Ask for the new last name and update it
            detail_change = input("Please enter new last name").strip().capitalize()
            detail["Last name"] = detail_change
        #Change member's jobs
        elif change == "Job":
            #Before changing, showing the user the jobs that the member is doing.
            for works in detail.keys():
                if "Job" in works:
                    print(detail[works])
            #Make a loop so if there are problems in entering new details, it can go over again.
            while True:
                #Ask the new jobs
                detail_change = input("Enter new jobs").capitalize()
                #If the job is not in the jobs.dict, which store jobs and salary,
                #ask the user to add then into the jobs.dict
                if detail_change not in jobs:
                    addtolist = input("{} is not in the list. "
                                      "Would you like to add it to jobs list? Enter yes".format(detail_change)).strip().title()
                    #Add the job to jobs.dict if the input is yes.
                    if addtolist == "Yes" or addtolist == "Y":
                        #Make a loop and show the user that the jobs is adding
                        while True:
                            print("You are adding job: ", detail_change, "to", detail["First name"], detail["Last name"])
                            #Using try and except function ask the user for the salary of that job.
                            try:
                                salary = int(input("Please enter the salary for it, or enter '0' to exit"))
                                #Money can't be a negative number. Go over again
                                if salary < 0:
                                    print("Please enter a positive number")
                                else:
                                    #Update the new job to job list
                                    jobs[detail_change] = salary
                                    break
                            except ValueError:
                                print("That's not a number")
                        #Print the new jobs.dict to show the user that the job is added successfully
                        for job, salary in jobs.items():
                            print("{}, {} per hour".format(job, salary))
                        #Ask the user to add this new job to member's detail
                        add = input("Would you like to add the job to the member's detail?").strip().title()
                        if add =="Yes" or add == "Y":
                            #The whole if/elif/else statement is to check that if the member has more than THREE jobs,
                            #because a person can't do that many jobs.
                            if "Job1" not in detail.keys():
                                #Input the job time and update them to member's detail
                                new_time = float(input("Enter the job time"))
                                new_job = {"Job1": detail_change, "Job1_hours": new_time}
                                detail.update(new_job)
                            elif "Job2" not in detail.keys():
                                # Input the job time and update them to member's detail
                                new_time = float(input("Enter the job time"))
                                new_job = {"Job2": detail_change, "Job2_hours": new_time}
                                detail.update(new_job)
                            elif "Job3" not in detail.keys():
                                # Input the job time and update them to member's detail
                                new_time = float(input("Enter the job time"))
                                new_job = {"Job3": detail_change, "Job3_hours": new_time}
                                detail.update(new_job)
                            else:
                                #If there are more than Three jobs, Ask the user to delete one job or not
                                job_delete = input(
                                    "Each worker can only have maximum of three jobs. Please enter a job1, "
                                    "job2 or job3 to delete the current jobs, or enter no "
                                    "to stop adding jobs").capitalize().strip()
                                #delete job1
                                if job_delete == "Job1":
                                    del detail["Job1"]
                                    print("You have deleted Job1, please enter new job")
                                #delte job2
                                elif job_delete == "Job2":
                                    del detail["Job2"]
                                    print("You have deleted Job2, please enter new job")
                                #delete job3
                                elif job_delete == "Job3":
                                    del detail["Job3"]
                                    print("You have deleted Job3, please enter new job")
                                #The loop will start again after delete jobs
                                else:
                                    break
                                #Break the loop if the user chose none of above
                        #Ask the users if they want to add mor jobs
                        keep = input("Would you like to keep changing? yes, y to continue").lower().strip()
                        if keep == "yes" or keep == "y":
                            pass
                        #Break the loop
                        else:
                            break
                #If the job is in the jobs.dict then do the same as the above code does.
                else:
                    #replace job1
                    if "Job1" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job1": detail_change, "Job1_hours": new_time}
                        detail.update(new_job)
                    #replace job2
                    elif "Job2" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job2": detail_change, "Job2_hours": new_time}
                        detail.update(new_job)
                    #replace job3
                    elif "Job3" not in detail.keys():
                        new_time = input("Enter the job time")
                        new_job = {"Job3": detail_change, "Job3_hours": new_time}
                        detail.update(new_job)
                    #delete one job above if there are three jobs
                    else:
                        job_delete = input("Each worker can only have maximum of three jobs. Please enter a job1,"
                                           "job2 or job3 to delete the current job").capitalize().strip()
                        #delete job1
                        if job_delete == "Job1":
                            del detail["Job1"]
                            print("You have deleted Job1, please enter new job")
                        #delete job2
                        if job_delete == "Job2":
                            del detail["Job2"]
                            print("You have deleted Job2, please enter new job")
                        #delete job3
                        if job_delete =="Job3":
                            del detail["Job3"]
                            print("You have deleted Job3, please enter new job")
                #Ask the user to keep or not
                keep = input("Would you like to keep changing? yes, y to continue").lower().strip()
                if keep == "yes" or keep == "y":
                    pass
                else:
                    break
        #Change job time
        elif change == "Jobhours":
            #Create a list to store 'jobs' that the worker is doing.
            #So the user can enter the jobs and see if the job is in the list to change the related job times.
            job = []
            #Add all the jobs that the worker is doing into the 'job' list
            for works in detail.keys():
                if "Job" in works:
                    print(detail[works])
                if "Job" in works and "hours" not in works:
                    job.append(detail[works])
            #Set a loop so the user can enter the jobs he wants to change and keep going this process until the user
            #break the loop
            while True:
                #Enter the job they want to change from the member
                choose = input("Please enter the job to change the work time").capitalize().strip()
                #To check if the job is in the job list we just created or it is Job1
                if choose == "Job1" or choose in job:
                    #If the job is in the list which means the worker is doing that job, set a Loop
                    while True:
                        #Entre the new job time of that job. If the job time is not a number or the worker DOES NOT
                        #have job 1
                        try:
                            new_time = float(input("Entre the new time"))
                            #Update the worker's detail
                            detail["Job1_hours"] = new_time
                            break
                        #Make sure the input in a number
                        except ValueError:
                            print("Please enter a number")
                        #Make sure the worker have job 1. If they don't have the app crashes
                        except KeyError:
                            print("Job1 is not available")
                #The same as the if statement above but for job2
                elif choose == "Job2" or choose in job:
                    while True:
                        try:
                            new_time = float(input("Entre the new time"))
                            detail["Job2_hours"] = new_time
                            break
                        except ValueError:
                            print("Please enter a number")
                        except KeyError:
                            print("Job2 is not available")
                #The smae function as above
                elif choose == "Job3" or choose in job:
                    while True:
                        try:
                            new_time = float(input("Entre the new time"))
                            detail["Job3_hours"] = new_time
                            break
                        except ValueError:
                            print("Please enter a number")
                        except KeyError:
                            print("Job3 is not available")
                #If the job the user entered is not in the list then show the user
                else:
                    print("The job is not in")
                #Usual things. Keep or exit.
                keep = input("Do you want to keep changing? yes or y").strip().lower()
                if keep == "yes" or keep == "y":
                    pass
                else:
                    break
        #Change the work day per week
        elif change == "Work day per week":
            #Loop
            while True:
                #Try statement for numbers correct
                try:
                    while True:
                        #The number of the work day per week must not greater than 7 or less than 0
                        detail_change = int(input("Enter the new work day per week"))
                        if detail_change > 7 or detail_change <= 0:
                            print("Please enter a number between 0 and 7")
                        elif detail_change < 7 or detail_change > 0:
                            #If the number is correct than update the worker's detail
                            detail["Work day per week"] = detail_change
                            break
                    break
                #If the input is not a number then print
                except ValueError:
                    print("Please enter a whole number")
        else:
            break

#def a function adding workers(finished)
def adding_worker():
    # Make a loop
    while True:
        # Enter the worker's first name
        new_worker = input("Please enter new worker's First name, or enter no to exit").title().strip()
        # If the user enter no then the function end
        if new_worker != "No" and new_worker != "N":
            # We have set a 2D dictionary, and we created some empty dictionaries. We use the loop to
            # find any dictionay that is empty, and set the details for that worker.
            for worker in workers.values():
                if len(worker) == 0:
                    # set the detials and Update the details to the dictionary
                    add = {"First name": new_worker, "Last name": "", "Job1": "", "Job1_hours": 0,
                           "Work day per week": 0}
                    worker.update(add)
                    # Enter the last name of the worker
                    lastname = input("Please enter new worker's last name?").title().strip()
                    # Update the last name
                    worker["Last name"] = lastname
                    # Ask the user if he wants to add more details to that worker
                    change = input(
                        "Would you like to change the new worker's detail? Enter yes to keep").strip().title()
                    if change == "Yes" or change == "Y":
                        # Use the function
                        worker_detail_change(worker)

                        # We need break here because we made a 'for' loop. As the function add the details
                        # to one empty dictionary, it stops so that the other dictionaries are still empty
                        break
                    else:
                        break
                # If the dictionary is not empty then looking for the next dictionary
                else:
                    pass
        # Break the While loop
        break

#def a function deleting workers(finished)
def deleting_workers():
    #loop
    while True:
        #Print out all the workers
        for num, worker in workers.items():
            if "First name" in worker.keys() and "Last name" in worker.keys():
                print(num, worker["First name"], worker["Last name"])
        #Enter the last name to delete the worker because people may have the same first name.
        deleted_worker = input("Please enter the worker's LAST name to delete, or enter No to exit").strip().title()
        #Looking for any worker who has the same last name as the user entered
        for worker in workers.values():
            #Because there may be some empty dictionaries which doesn't have the key "Last name" so we need try/except
            try:
                #If the worker's last name is the same as the user entered
                if deleted_worker == worker["Last name"]:
                    #The code below is to delete everything in the dictionary
                    #First create a list
                    list = []
                    #Copy the keys that are in the workers' detail dictionary to the list
                    #The list will have all the keys that are inside the dictionary
                    for keys, values in worker.items():
                        list.append(keys)
                    #We then delete every keys in the dictionary if the key is the same as the keys in the list
                    for keys in list:
                        if keys in worker.keys():
                            del worker[keys]
                #Pass if the worker's last name is not the one the user entered
                else:
                    pass
            #Pass if the KeyError because some of the dictionaries don't have anything in it. Skip the empty dictionaries
            except KeyError:
                pass
        #Ask the user to keep or not
        keep = input("Would you like to keep deleting? Enter Yes to keep").strip().title()
        if keep == "Yes" or keep == "Y":
            pass
        #End the function
        else:
            break

#define a function that shows the salary of workers inside the function viewing_workers()(finished)
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
            print(worker, worker_detail["First name"], worker_detail["Last name"], "Daily salary: {:.2f}$"
                  .format(daily_salary))
            pass
    #Calculate the total paid after calculate each worker's salary.
    daily_total_paid += daily_salary
    weekly_total_paid += weekly_salary
    #Print out the total paid
    print("Daily total paid is {:.2f}$\nWeekly total paid is {:.2f}$".format(daily_total_paid, weekly_total_paid))



#Set a menu so the user can use the functions(finished)
def menu():
    #loop
    while True:
        #Used number to chose the function so we need try/except
        try:
            #Enter the number
            choose = int(input("Enter 1 to add jobs \n"
                               "Enter 2 to deleting jobs \n"
                               "Enter 3 to view workers details \n"
                               "Enter 4 to add workers\n"
                               "Enter 5 to delete workers\n"
                               "Enter 0 to exit "))
            #Functions
            if choose == 0:
                break
            elif choose == 1:
                adding_jobs()
            elif choose == 2:
                deleting_jobs()
            elif choose == 3:
                viewing_workers()
            elif choose == 4:
                adding_worker()
            elif choose == 5:
                deleting_workers()
            #If the number is not in the range
            else:
                print("please enter a number 0 - 5")
        #If the input is not a number
        except ValueError:
            print("please enter a whole number")
#Run the code
menu()
