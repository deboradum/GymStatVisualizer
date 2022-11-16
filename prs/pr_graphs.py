import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np

# TODO Reps integreren.

def graph_pr(pr_data, ex_name):
    weights = [float(entry[0]) for entry in pr_data.get(ex_name)]
    reps = [int(entry[1]) for entry in pr_data.get(ex_name)]
    dates = [dt.datetime.strptime(entry[2],'%d/%m/%Y').date() for entry in pr_data.get(ex_name)]

    # Changing figure size
    plt.figure(figsize=(15,12))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))

    # Plot domains.
    plt.xlim([dt.date(2022, 1, 1), dt.date(2022, 12, 31)])
    plt.ylim([int(min(weights)-0.1*min(weights)), int(max(weights)+0.1*max(weights))])

    plt.plot(dates, weights, 'ro')

    plt.gcf().autofmt_xdate()
    # Plot title.
    plt.title(ex_name)
    # Plot labels.
    plt.xlabel('date (mm/dd/yyyy)')
    plt.ylabel('Weight (kg)')

    plt.savefig(f'{ex_name}.png')
    plt.close()


def get_prs(filepath):
    excel_data = pandas.read_excel(filepath, sheet_name='PR', na_filter=False)

    exs = list(excel_data.columns)
    # PR dict is in the form:
    # {<Exercise name>: [[<Weigth>, <Reps>, <Date>], ..., [<Weigth>, <Reps>, <Date>]]}
    pr_data = {}
    for ex in exs:
        prs = [entry.split(";") for entry in excel_data[ex].tolist() if entry]
        pr_data[ex] = prs

    for name in pr_data:
        graph_pr(pr_data, name)


if __name__ == "__main__":
    get_prs("/Users/pepijn/Desktop/Fitness.xlsx")
