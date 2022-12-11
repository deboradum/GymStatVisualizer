
import pandas


def ddmmyy_to_formatted(date):
    date_correct = ""
    i = 0
    for num in date:
        if i == 2 or i == 4:
            date_correct += '/'
        date_correct += num
        i += 1

    return date_correct

class Stats:
    def __init__(self, sheet_row):
        self.date = sheet_row.get("Dag").strftime('%d%m%Y')
        self.stats = self.parse_stats(sheet_row)

    def __str__(self):
        try:
            st  = f"{ddmmyy_to_formatted(self.date)}\n"
            if self.stats.get('weight'):
                st += f"weight:                     {self.stats.get('weight'):,}kg\n"
            if self.stats.get('bf_chest'):
                st += f"body fat chest:             {self.stats.get('bf_chest'):,}mm\n"
            if self.stats.get('bf_bb'):
                st += f"body fat belly button:      {self.stats.get('bf_bb'):,}mm\n"
            if self.stats.get('bf_thigh'):
                st += f"body fat thigh:             {self.stats.get('bf_thigh'):,}mm\n"
            if self.stats.get('bf_prct'):
                st += f"body fat percent:           {round(self.stats.get('bf_prct')*100, 2)}%\n"
            if self.stats.get('cals_in'):
                st += f"calories in:                {self.stats.get('cals_in'):,}kcal\n"
            if self.stats.get('prot_in'):
                st += f"protein in:                 {self.stats.get('prot_in'):,}g\n"
            if self.stats.get('prot_in_prct'):
                st += f"percent protein:            {round(self.stats.get('prot_in_prct')*100, 2)}%\n"
            if self.stats.get('gym_day'):
                st += f"gym day:                    {self.stats.get('gym_day')}\n"
            if self.stats.get('gym_volume'):
                st += f"total volume:               {self.stats.get('gym_volume'):,}kg\n"
            if self.stats.get('gym_cals'):
                st += f"calories burned gym:        {self.stats.get('gym_cals'):,}kcal\n"
            if self.stats.get('gym_avg_heart_rate'):
                st += f"avg heart rate gym:         {self.stats.get('gym_avg_heart_rate'):,}bpm\n"
            if self.stats.get('gym_max_heart_rate'):
                st += f"max heart rate gym:         {self.stats.get('gym_max_heart_rate'):,}bpm\n"
            if self.stats.get('cardio_type'):
                st += f"cardio day:                 {self.stats.get('cardio_type')}\n"
            if self.stats.get('cardio_cals'):
                st += f"calories burned cardio:     {self.stats.get('cardio_cals'):,}kcal\n"
            if self.stats.get('cardio_avg_heart_rate'):
                st += f"avg heart rate cardio:      {self.stats.get('cardio_avg_heart_rate'):,}bpm\n"
            if self.stats.get('cardio_max_heart_rate'):
                st += f"max heart rate cardio:      {self.stats.get('cardio_max_heart_rate'):,}bpm\n"
            if self.stats.get('calories_burned_total'):
                st += f"total calories burned:      {self.stats.get('calories_burned_total'):,}kcal\n"
            if self.stats.get('calories_surplus'):
                st += f"calories surplus:           {self.stats.get('calories_surplus'):,}kcal\n"
            if self.stats.get('Notes'):
                st += f"notes:                      {self.stats.get('Notes')}\n"

            return st
        except Exception:
            return ""

    def parse_stats(self, sheet_row):
        # print(sheet_row)
        s = {"weight": sheet_row.get("Gewicht"),
             "bf_chest": sheet_row.get("Body fat C"),
             "bf_bb": sheet_row.get("Body fat N"),
             "bf_thigh": sheet_row.get("Body fat B"),
             "bf_prct": sheet_row.get("Body fat %"),
             "cals_in": sheet_row.get("Cal. Gegeten"),
             "prot_in": sheet_row.get("Proteine"),
             "prot_in_prct": sheet_row.get("% protein"),
             "gym_day": sheet_row.get("Gym day"),
             "gym_volume": sheet_row.get("Totaal volume"),
             "gym_cals": sheet_row.get("Gym calories"),
             "gym_avg_heart_rate": sheet_row.get("Avg gym heart rate"),
             "gym_max_heart_rate": sheet_row.get("Max gym heart rate"),
             "cardio_type": sheet_row.get("Cardio"),
             "cardio_cals": sheet_row.get("Cardio calories"),
             "cardio_avg_heart_rate": sheet_row.get("Avg cardio heart rate"),
             "cardio_max_heart_rate": sheet_row.get("Max cardio heart rate"),
             "calories_burned_total": sheet_row.get("Totaal calories verbrand"),
             "calories_surplus": sheet_row.get("Calories surplus"),
             "notes": sheet_row.get("Notes")
            }

        return s

    def get_weight(self):
        if type(self.stats.get('weight')) is type(pandas.NaT):
            return None
        else:
            if self.stats.get('weight'):
                return float(self.stats.get('weight'))
            else:
                return None

    def get_calories_in(self):
        if type(self.stats.get('cals_in')) is not int:
            return None
        # if  type(self.stats.get('cals_in')) is type(pandas.NaT):
        #     return None
        if self.stats.get('cals_in'):
            return int(self.stats.get('cals_in'))
        else:
            return None
