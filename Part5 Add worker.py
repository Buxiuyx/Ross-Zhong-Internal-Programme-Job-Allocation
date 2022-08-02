#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2,"Worker3": worker3, "Worker4": worker4, "Worker5": worker5}

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
            changing_detial(detial, change)
        #Change member's last name
        elif change == "Last name":
            #Ask for the new last name and update it
            changing_detial(detial, change)
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
                        show_jobs(jobs)
                        print("You have add", detail_change, "to the job list")
                        #Ask the user to add this new job to member's detail
                        add = input("Would you like to add the job to the member's detail?").strip().title()
                        if add =="Yes" or add == "Y":
                            #The whole if/elif/else statement is to check that if the member has more than THREE jobs,
                            #because a person can't do that many jobs.
                            adding_job_to_worker(detail, detail_change)

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
                    adding_job_to_worker(detail, detail_change)
                #Ask the user to keep or not
                keep = input("Would you like to keep changing? yes, y to continue").lower().strip()
                if keep == "yes" or keep == "y":
                    pass
                else:
                    break
        #Change job time
        elif change == "Job hours":
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

#Set a function that could return a string variable of "Worker + number"(finished)
def return_strvariable(x):
    #The function combine "Worker" and a number for our string key in workers.dict
    strvariable = "Worker"
    strvariable += str(x)
    #return the string
    return(strvariable)

#def a function that could add new keys and values in workers.dict using the form of {"Worker+number": {}}(finished)
def adding_index_dict(name):
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
            x = {"First name": name, "Last name": "",}
            #Update the workers.dict with {"Workers + number": {}}
            y = {return_strvariable(number) : x}
            workers.update(y)
            #As one new key is added to the dict, then break the loop.
            break
    return return_strvariable(number)

#def a function adding workers
def adding_worker():
    #Make a loop
    while True:
        #Show workers that are present
        showing_worker_list(workers)
        #Enter the worker's first name
        new_worker = input("Please enter new worker's First name, or enter no to exit").title().strip()
        #If the user enter no then the function end
        if new_worker != "No" and new_worker != "N":
            #we set the length of the dictionary as an variable so we can use it to know how many times we need to
            #use test if the workers.dict is full
            len_of_workers_dict = len(workers)
            #We start at 0 test
            number_we_tested = 0
            #There k
            for worker in workers.values():
                # We have set a 2D dictionary, and we created some empty dictionaries. We use the loop to
                # find any dictionay that is empty, and set the details for that worker.
                if len(worker) == 0:
                    #set the detials and Update the details to the dictionary
                    add = {"First name": new_worker, "Last name": "",}
                    worker.update(add)
                    #Enter the last name of the worker
                    lastname = input("Please enter new worker's last name").title().strip()
                    #Update the last name
                    worker["Last name"] = lastname
                    #Show the user all the workers and the worker they just added
                    for workernum, workerdetial in workers.items():
                        # Try and except for empty dict
                        try:
                            print(workernum, workerdetial["First name"], workerdetial["Last name"])
                        except KeyError:
                            pass
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
                    # We add the number_we_tested by one because we have experenced 1 test
                    number_we_tested += 1
                    #Once the number_we_tested is equal to the length of the worker.dict
                    if number_we_tested == len_of_workers_dict:
                        #The function add one more index in the dictionary so we can add more workers
                        workernum = adding_index_dict(new_worker)
                        #Enter the last name of the worker
                        lastname = input("Please enter new worker's last name").title().strip()
                        # Update the last name
                        lastnameupdate = {"Last name" : lastname}
                        workers[workernum].update(lastnameupdate)
                        #Show the user all the workers and the worker they just added.
                        for workernum, workerdetial in workers.items():
                            # Try and except for empty dict
                            try:
                                print(workernum, workerdetial["First name"], workerdetial["Last name"])
                            except KeyError:
                                pass
                        # Ask the user if he wants to add more details to that worker
                        change = input(
                            "Would you like to change the new worker's detail? Enter yes to keep").strip().title()
                        if change == "Yes" or change == "Y":
                            # Use the function to change detail.
                            worker_detail_change(workers[workernum])
                        break
        #Ask the user if they want to keep adding
        keep = input("Would you like to keep adding workers? Enter yes to continue").strip().title()
        if keep == "Yes" or keep == "Y":
            pass
        else:
            #Break the while True loop
            break

adding_worker()
