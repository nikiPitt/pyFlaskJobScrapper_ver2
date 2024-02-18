import csv

def writeCSV(keyword, jobs_lists, domain):
    print("----- Writing a file -----")
    file = open(f"{keyword}_jobs.csv", "w")
    writer = csv.writer(file)
    if domain == "search by skill":
        writer.writerow(["Title", "Company", "Region", "url"])
    else:
        writer.writerow(["Title", "Company", "Position", "Region", "url"])
    for job in jobs_lists:
        writer.writerow(job.values())
    file.close()