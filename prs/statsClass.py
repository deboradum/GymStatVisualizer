

class Stats:
    def __init__(self, sheet_row):
        self.date = sheet_row.get("Dag").strftime('%d%m%Y')
        self.stats = self.parse_stats(sheet_row)

    def __str__(self):
        st = ""
        st += f"weight: {self.stats.get('Gewicht')}\n"
        st += f"bf_chest: {self.stats.get('Body fat C')}\n"
        st += f"bf_bb: {self.stats.get('Body fat N')}\n"
        st += f"bf_thigh: {self.stats.get('Body fat B')}\n"
        st += f"bf_prct: {self.stats.get('Body fat %')}\n"
        st += f"cals_in: {self.stats.get('Cal. Gegeten')}\n"
        st += f"prot_in: {self.stats.get('Proteine')}\n"
        st += f"prot_in_prct: {self.stats.get('% protein')}\n"
        st += f"gym_day: {self.stats.get('Gym day')}\n"
        st += f"gym_volume: {self.stats.get('Totaal volume')}\n"
        st += f"gym_calories: {self.stats.get('Gym calories')}\n"
        st += f"gym_avg_heart_rate: {self.stats.get('Avg gym heart rate')}\n"
        st += f"gym_max_heart_rate: {self.stats.get('Max gym heart rate')}\n"
        st += f"cardio_type: {self.stats.get('Cardio')}\n"
        st += f"cardio_calories: {self.stats.get('Cardio calories')}\n"
        st += f"cardio_avg_heart_rate: {self.stats.get('Avg cardio heart rate')}\n"
        st += f"cardio_max_heart_rate: {self.stats.get('Max cardio heart rate')}\n"
        st += f"calories_burned_total: {self.stats.get('Totaal calories verbrand')}\n"
        st += f"calories_surplus: {self.stats.get('Calories surplus')}\n"
        st += f"notes: {self.stats.get('Notes')}\n"

        return st


    def parse_stats(self, sheet_row):
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
             "gym_calories": sheet_row.get("Gym calories"),
             "gym_avg_heart_rate": sheet_row.get("Avg gym heart rate"),
             "gym_max_heart_rate": sheet_row.get("Max gym heart rate"),
             "cardio_type": sheet_row.get("Cardio"),
             "cardio_calories": sheet_row.get("Cardio calories"),
             "cardio_avg_heart_rate": sheet_row.get("Avg cardio heart rate"),
             "cardio_max_heart_rate": sheet_row.get("Max cardio heart rate"),
             "calories_burned_total": sheet_row.get("Totaal calories verbrand"),
             "calories_surplus": sheet_row.get("Calories surplus"),
             "notes": sheet_row.get("Notes")
            }

        return s



# class Stats:
#     def __init__(self, sheet_row):
#         self.date = sheet_row.get("Dag").strftime('%d%m%Y')
#         self.stats = self.parse_stats(sheet_row)

#     def __str__(self):
#         print(self.stats)
#         return

#     def parse_stats(self, sheet_row):
#         s = {"weight": float(sheet_row.get("Gewicht")),
#              "bf_chest": int(sheet_row.get("Body fat C")),
#              "bf_bb": int(sheet_row.get("Body fat N")),
#              "bf_thigh": int(sheet_row.get("Body fat B")),
#              "bf_prct": float(sheet_row.get("Body fat %")),
#              "cals_in": int(sheet_row.get("Cal. Gegeten")),
#              "prot_in": int(sheet_row.get("Proteine")),
#              "prot_in_prct": float(sheet_row.get("% protein")),
#              "gym_day": str(sheet_row.get("Gym day")),
#              "gym_volume": int(sheet_row.get("Totaal volume")),
#              "gym_calories": int(sheet_row.get("Gym calories")),
#              "gym_avg_heart_rate": int(sheet_row.get("Avg gym heart rate")),
#              "gym_max_heart_rate": int(sheet_row.get("Max gym heart rate")),
#              "cardio_type": str(sheet_row.get("Cardio")),
#              "cardio_calories": int(sheet_row.get("Cardio calories")),
#              "cardio_avg_heart_rate": int(sheet_row.get("Avg cardio heart rate")),
#              "cardio_max_heart_rate": int(sheet_row.get("Max cardio heart rate")),
#              "calories_burned_total": int(sheet_row.get("Totaal calories verbrand")),
#              "calories_surplus": int(sheet_row.get("Calories surplus")),
#              "notes": str(sheet_row.get("Notes"))
#             }

#         return s
