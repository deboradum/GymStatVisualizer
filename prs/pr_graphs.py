import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import datetime as dt
from pprint import pprint
from prClass import ExercisePRs
from statsClass import Stats

SHEET_PATH = "/Users/pepijn/Desktop/Fitness.xlsx"
FIGSIZE = (15,12)

class ExcelFileReader:
    def __init__(self, filepath):
        self.pr_data = self.set_pr_data(filepath, 'PR')
        self.stats_data = self.set_stats_data(filepath, 'Stats')

    # Reads an excel file and returns a dictionary containing the parsed data
    # from the excel file.
    def set_pr_data(self, filepath, sheetname):
        # Reads excel file.
        pr_data_sheet = pandas.read_excel(filepath, sheet_name=sheetname, na_filter=False)
        pr_data = {}
        # Creates a dict with exercise names as keys and an ExercisePR class as
        # value.
        for ex in list(pr_data_sheet.columns):
            # Parses pr data into a list as follows:
            # "weight;reps;date" ==>  [weight, reps, date]
            prs = [entry.split(";") for entry in pr_data_sheet[ex].tolist() if entry]
            pr_data[ex] = ExercisePRs(ex, prs)

        return pr_data

    # Prints the pr data for every exercise.
    def print_pr_data(self):
        for ex in self.pr_data:
            print(self.pr_data[ex])

    # Reads an excel file and returns a dictionary containing the parsed data
    # from the excel file.
    def set_stats_data(self, filepath, sheetname):
        # Reads excel file.
        stats_data_sheet = pandas.read_excel(filepath, sheet_name=sheetname, na_filter=False)
        stats_data = {}
        for _, row in stats_data_sheet[:42].iterrows():  # TODO NaT error bij 28/09
            # Date "dd/mm/yyyy" is represented as a key like "ddmmyyy".
            stats_data[row.get("Dag").strftime('%d%m%Y')] = Stats(row)

        return stats_data

    # Prints the stats data for every day.
    def print_stats_data(self):
        for day in self.stats_data:
            print(self.stats_data[day])



    def plot_ex_pr_test(self, ex_name):
        weights = [float(entry["weight"]) for entry in self.pr_data[ex_name].data]
        reps = [int(entry["reps"]) for entry in self.pr_data[ex_name].data]
        dates = [dt.datetime.strptime(entry["date"],'%d/%m/%Y').date() for entry in self.pr_data[ex_name].data]
        volumes = [r*w for r,w in zip(reps,weights)]

        plt.figure(figsize=FIGSIZE)
        plt.title(ex_name)
        host = host_subplot(111, axes_class=AA.Axes)

        par1 = host.twinx()

        new_fixed_axis = par1.get_grid_helper().new_fixed_axis
        par1.axis["right"] = new_fixed_axis(loc="right", axes=par1)
        par1.axis["right"].toggle(all=True)

        host.set_xlim(dt.date(2022, 1, 1), dt.date(2022, 12, 31))
        host.set_ylim(int(min(weights)-0.1*min(weights)), int(max(weights)+0.1*max(weights)))

        host.set_xlabel('Date (dd/mm/yyyy)')
        host.set_ylabel('Weight (kg)')
        par1.set_ylabel("Volume (kg)")

        p1, = host.plot(dates, weights, label="Weight (kg)")
        p2, = par1.plot(dates, volumes, label="Volume (kg)")

        par1.set_ylim(int(min(volumes)-0.1*min(volumes)), int(max(volumes)+0.1*max(volumes)))
        print(host.get_ylim())
        host.legend()

        host.axis["left"].label.set_color(p1.get_color())
        par1.axis["right"].label.set_color(p2.get_color())

        plt.draw()
        # plt.savefig(f'{ex_name}.png')
        plt.show()

        plt.close()





    def plot_ex_pr(self, ex_name):
        weights = [float(entry["weight"]) for entry in self.pr_data[ex_name].data]
        reps = [int(entry["reps"]) for entry in self.pr_data[ex_name].data]
        dates = [dt.datetime.strptime(entry["date"],'%d/%m/%Y').date() for entry in self.pr_data[ex_name].data]

        # Changing figure size
        plt.figure(figsize=FIGSIZE)
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
        plt.xlabel('date (dd/mm/yyyy)')
        plt.ylabel('Weight (kg)')
        plt.savefig(f'{ex_name}.png')
        plt.close()



    # def get_weight_plot(self):
    #     weights = [self.stats_dict[date].get("Gewicht") for date in self.stats_dict if self.stats_dict[date].get("Gewicht")]
    #     dates = [date for date in self.stats_dict if self.stats_dict[date].get("Gewicht")]

    #     # Changing figure size
    #     plt.figure(figsize=FIGSIZE)
    #     plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
    #     plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    #     # Plot domains.
    #     # plt.xlim([dt.date(2022, 1, 1), dt.date(2022, 12, 31)])
    #     plt.ylim([int(min(weights)-0.05*min(weights)), int(max(weights)+0.05*max(weights))])
    #     plt.plot(dates, weights, 'ro')
    #     plt.gcf().autofmt_xdate()
    #     # Plot title.
    #     plt.title("Weight")
    #     # Plot labels.
    #     plt.xlabel('date (dd/mm/yyyy)')
    #     plt.ylabel('Weight (kg)')
    #     plt.savefig('weight.png')
    #     plt.close()


if __name__ == "__main__":
    sheet = ExcelFileReader(SHEET_PATH)
    sheet.plot_ex_pr_test("Bench Press (Barbell)")
    # sheet.get_weight_plot()
    # sheet.get_pr_plots()
    # sheet.stats_data
    # sheet.print_pr_data()
    # sheet.print_stats_data()
