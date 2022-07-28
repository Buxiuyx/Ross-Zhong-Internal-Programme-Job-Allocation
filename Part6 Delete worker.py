#Creating a dictionary store the jobs and the weekly salary for each job.
jobs = {'Programming': 22.00, "Cleaning": 18.90, "Doing Nothing": 1.00}
#Create an example worker1, which is me for testing and showing the user how the details are like.
worker1 = {'First name': 'Ross', 'Last name': 'Zhong', 'Job1': 'Programming', "Job1_hours": 8.00, "Job2": "Cleaning",
           "Job2_hours": 1.00, "Work day per week": 6}
#Create empty dictionaries so the user can add member's detail in it.
worker2, worker3, worker4, worker5 = {}, {}, {}, {}
#Set up a dictionary that make the connection between strings and the members' details.
workers = {'Worker1': worker1, "Worker2": worker2, "Worker3": worker3, "Worker4": worker4, "Worker5": worker5,}

#Def the function
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

deleting_workers()