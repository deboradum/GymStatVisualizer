import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

SHEET_PATH = "/Users/pepijn/Desktop/Fitness.xlsx"

# TODO Reps integreren.

class ExcelFile:
    def __init__(self, filepath):
        pr_data_sheet = pandas.read_excel(filepath, sheet_name='PR', na_filter=False)
        self.pr_data = {}
        for ex in list(pr_data_sheet.columns):
            prs = [entry.split(";") for entry in pr_data_sheet[ex].tolist() if entry]
            self.pr_data[ex] = prs
        self.stats_data = self.stats(filepath)

    def get_pr_plots(self):
        for name in self.pr_data:
            self.plot_ex(name)

    def plot_ex(self, ex_name):
        weights = [float(entry[0]) for entry in self.pr_data.get(ex_name)]
        reps = [int(entry[1]) for entry in self.pr_data.get(ex_name)]
        dates = [dt.datetime.strptime(entry[2],'%d/%m/%Y').date() for entry in self.pr_data.get(ex_name)]

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

    def stats(self, filepath):
        stats_data_dict = pandas.read_excel(filepath, sheet_name='Stats', na_filter=False).to_dict()
        self.stats_dict = {}
        for index in stats_data_dict["Dag"]:
            date = stats_data_dict.get("Dag").get(index).date()
            self.stats_dict[date] = {}
            for key in stats_data_dict.keys():
                if key != "Dag":
                    if stats_data_dict.get(key).get(index):
                        self.stats_dict[date][key] = stats_data_dict.get(key).get(index)
                    else:
                        self.stats_dict[date][key] = None

    def get_weight_plot(self):
        weights = [self.stats_dict[date].get("Gewicht") for date in self.stats_dict if self.stats_dict[date].get("Gewicht")]
        dates = [date for date in self.stats_dict if self.stats_dict[date].get("Gewicht")]

        # Changing figure size
        plt.figure(figsize=(15,12))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
        # Plot domains.
        # plt.xlim([dt.date(2022, 1, 1), dt.date(2022, 12, 31)])
        plt.ylim([int(min(weights)-0.05*min(weights)), int(max(weights)+0.05*max(weights))])
        plt.plot(dates, weights, 'ro')
        plt.gcf().autofmt_xdate()
        # Plot title.
        plt.title("Weight")
        # Plot labels.
        plt.xlabel('date (dd/mm/yyyy)')
        plt.ylabel('Weight (kg)')
        plt.savefig('weight.png')
        plt.close()


if __name__ == "__main__":
    sheet = ExcelFile(SHEET_PATH)
    sheet.get_weight_plot()
    # sheet.get_pr_plots()
    # sheet.stats()
