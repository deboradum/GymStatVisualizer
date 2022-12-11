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

CHEST_EXS = ["Bench Press (Barbell)", "Cable Crossover", "Chest Fly", "Incline Bench Press (Barbell)", "Incline Bench Press (Dumbells)"]
BACK_SHOULDER_EXS = ["Lat Pulldown (Cable)", "Reverse Fly (Machine)", "Seated Row (Cable)", "Overhead Press (Barbell)"]
LEG_EXS = ["Hip Ab-Adductor", "Leg Extension (Machine)", "Lying Leg Curl (Machine)", "Seated Leg Curl (Machine)", "Seated Leg Press", "Squat (Barbell)"]
BICEPS_EXS = ["Bicep Curl (Barbell)", "Hammer Curl (Dumbell)", "Preacher Curl (Barbell)"]
TRICEP_EXS = ["Skullcrusher (Barbell)", "Triceps Exentension (Cable)", "Triceps Pushdown (Cable)"]

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

    # Plots a specific exercise PRs and saves to PRs folder.
    def plot_exercise_pr(self, ex_name):
        weights = [float(entry["weight"]) for entry in self.pr_data[ex_name].data]
        reps = [int(entry["reps"]) for entry in self.pr_data[ex_name].data]
        dates = [dt.datetime.strptime(entry["date"],'%d/%m/%Y').date() for entry in self.pr_data[ex_name].data]

        plt.figure(figsize=FIGSIZE)
        plt.title(f'{ex_name} PRs')
        plt.xlim(dt.date(2022, 1, 1), dt.date(2022, 12, 31))
        plt.ylim(int(min(weights)-0.1*min(weights)), int(max(weights)+0.1*max(weights)))
        plt.xlabel('Date (dd/mm/yyyy)')
        plt.ylabel('Weight (kg)')
        plt.plot(dates, weights)
        plt.draw()
        plt.savefig(f'../pr_plots/{ex_name}.png')
        plt.close()

    # Plots the PR graph of every exercise.
    def plot_all_prs(self):
        for key in self.pr_data.keys():
            self.plot_exercise_pr(key)

    # Plots the PR graph of a group of exercises in one plot.
    def plot_group_of_exercises(self, group, filename):
        plt.figure(figsize=FIGSIZE)
        plt.title(f'PRs by category')
        plt.xlim(dt.date(2022, 1, 1), dt.date(2022, 12, 31))
        plt.xlabel('Date (dd/mm/yyyy)')
        plt.ylabel('Weight (kg)')
        for ex in group:
            if ex in self.pr_data.keys():
                weights = [float(entry["weight"]) for entry in self.pr_data[ex].data]
                dates = [dt.datetime.strptime(entry["date"],'%d/%m/%Y').date() for entry in self.pr_data[ex].data]

                plt.plot(dates, weights, label=ex)
        plt.legend()
        plt.draw()

        plt.savefig(f'../pr_plots/{filename}.png')

    # Reads an excel file and returns a dictionary containing the parsed data
    # from the excel file.
    def set_stats_data(self, filepath, sheetname):
        # Reads excel file.
        stats_data_sheet = pandas.read_excel(filepath, sheet_name=sheetname, na_filter=False)
        stats_data = {}
        for _, row in stats_data_sheet.iterrows():  # TODO NaT error bij 28/09
            # Date "dd/mm/yyyy" is represented as a key like "ddmmyyy".
            stats_data[row.get("Dag").strftime('%d%m%Y')] = Stats(row)

        return stats_data

    # Prints the stats data for every day.
    def print_stats_data(self):
        for day in self.stats_data:
            print(self.stats_data[day])

    def plot_weight(self):
        weights = [self.stats_data[day].get_weight() for day in self.stats_data if self.stats_data[day].get_weight()]
        dates = [dt.datetime.strptime(day, "%d%m%Y") for day in self.stats_data if self.stats_data[day].get_weight()]

        plt.figure(figsize=FIGSIZE)
        plt.title('Weight over time')
        # Whole year on x-axis
        # plt.xlim(dt.date(2022, 1, 1), dt.date(2022, 12, 31))
        # Time period where measurements were done on x-axis.
        plt.xlim(min(dates), max(dates))
        plt.ylim(int(min(weights)-0.04*min(weights)), int(max(weights)+0.04*max(weights)))
        plt.xlabel('Date (dd/mm/yyyy)')
        plt.ylabel('Weight (kg)')
        plt.plot(dates, weights)
        plt.draw()
        plt.savefig('../stat_plots/weight_progression.png')
        plt.close()

    def plot_weight_and_cals(self):
        weights = [self.stats_data[day].get_weight() for day in self.stats_data if self.stats_data[day].get_weight()]
        dates_w = [dt.datetime.strptime(day, "%d%m%Y") for day in self.stats_data if self.stats_data[day].get_weight()]
        calories_in = [self.stats_data[day].get_calories_in() for day in self.stats_data if self.stats_data[day].get_calories_in()]
        dates_c = [dt.datetime.strptime(day, "%d%m%Y") for day in self.stats_data if self.stats_data[day].get_calories_in()]

        fig,ax = plt.subplots(figsize=FIGSIZE)
        ax.plot(dates_w, weights, "b-", label="Weight")
        ax.set_xlim(min(dates_w + dates_c), max(dates_w + dates_c))
        ax.set_xlabel("Date (dd/mm/yyyy)")
        ax.set_ylabel("Weight (kg)")
        ax.yaxis.label.set_color('blue')

        ax2 = ax.twinx()
        ax2.plot(dates_c, calories_in, "r-", label="Calories")
        ax2.set_ylabel("Calories (kcal)")
        ax2.yaxis.label.set_color('red')

        ax.set_title('Weight and caloric intake over time')
        fig.legend()

        plt.draw()
        plt.savefig('../stat_plots/weight_calories.png')
        plt.close()

    def plot_weight_and_protein(self):
        pass

    def plot_weight_cal_surplus(self):
        weights = [self.stats_data[day].get_weight() for day in self.stats_data if self.stats_data[day].get_weight()]
        dates_w = [dt.datetime.strptime(day, "%d%m%Y") for day in self.stats_data if self.stats_data[day].get_weight()]
        calorie_surplus = [self.stats_data[day].get_calorie_surplus() for day in self.stats_data if self.stats_data[day].get_calorie_surplus()]
        dates_c = [dt.datetime.strptime(day, "%d%m%Y") for day in self.stats_data if self.stats_data[day].get_calorie_surplus()]

        fig,ax = plt.subplots(figsize=FIGSIZE)
        ax.plot(dates_w, weights, "b-", label="Weight")
        ax.set_xlim(min(dates_w + dates_c), max(dates_w + dates_c))
        ax.set_xlabel("Date (dd/mm/yyyy)")
        ax.set_ylabel("Weight (kg)")
        ax.yaxis.label.set_color('blue')

        ax2 = ax.twinx()
        ax2.plot(dates_c, calorie_surplus, "r-", label="Calorie surplus")
        ax2.set_ylabel("Calories (kcal)")
        ax2.yaxis.label.set_color('red')

        ax2.hlines(y=0, xmin=min(dates_w + dates_c), xmax=max(dates_w + dates_c), linewidth=2, color='gray', linestyles='dotted')

        ax.set_title('Weight and caloric surplus over time')

        fig.legend()
        plt.draw()
        plt.savefig('../stat_plots/weight_calorie_surplus.png')
        plt.close()


if __name__ == "__main__":
    sheet = ExcelFileReader(SHEET_PATH)
    # sheet.plot_group_of_exercises(TRICEP_EXS, "tricepExercises")
    # sheet.print_pr_data()
    # sheet.print_stats_data()
    sheet.plot_weight_and_cals()
    sheet.plot_weight_cal_surplus()
