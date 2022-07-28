#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}

#We need the function we made before in the add worker part
#So when the user finished adding workers, he can change the details if he want.
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


#def a function adding workers
def adding_worker():
    #Make a loop
    while True:
        #Enter the worker's first name
        new_worker = input("Please enter new worker's First name, or enter no to exit").title().strip()
        #If the user enter no then the function end
        if new_worker != "No" and new_worker != "N":
            #We have set a 2D dictionary, and we created some empty dictionaries. We use the loop to
            #find any dictionay that is empty, and set the details for that worker.
            for worker in workers.values():
                if len(worker) == 0:
                    #set the detials and Update the details to the dictionary
                    add = {"First name": new_worker, "Last name": "", "Job1": "", "Job1_hours": 0, "Work day per week": 0}
                    worker.update(add)
                    #Enter the last name of the worker
                    lastname = input("Please enter new worker's last name?").title().strip()
                    #Update the last name
                    worker["Last name"] = lastname
                    #Ask the user if he wants to add more details to that worker
                    change = input("Would you like to change the new worker's detail? Enter yes to keep").strip().title()
                    if change == "Yes" or change == "Y":
                        #Use the function
                        worker_detail_change(worker)

                        #We need break here because we made a 'for' loop. As the function add the details
                        #to one empty dictionary, it stops so that the other dictionaries are still empty
                        break
                    else:
                        break
                #If the dictionary is not empty then looking for the next dictionary
                else:
                    pass
        #Break the While loop
        break

adding_worker()