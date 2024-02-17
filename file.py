import csv

def writeCSV(keyword, jobs_lists):
    print("----- Writing a file -----")
    file = open(f"{keyword}_jobs.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "url"])
    for job in jobs_lists:
        writer.writerow(job.values())
    file.close()