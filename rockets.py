################################################################################
# Description: Programs to display five rockets and call the cost per launch on each of
# 5 rockets
################################################################################

class Rocket:
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self, cost):
         return cost = self.booster_cost + self.upper_stage_cost + self.fuel_cost

class ReusableRocket(Rocket):
    def uses(self):
        return (self.booster_cost / super().uses()) + self.upper_stage_cost + self.fuel_cost

def main():
    atlas_v = ReusableRocket(name = 'Atlas V', booster_cost = 65.4, upper_stage_cost = 42.6, fuel_cost = 0.23, uses(1))
    ariane = ReusableRocket(name = 'Ariane 5', booster_cost = 83.5, upper_stage_cost = 55.6, fuel_cost = 0.69, uses(1))
    long_march = ReusableRocket(name = 'Long March 3B', booster_cost = 28.5, upper_stage_cost = 19.0, fuel_cost = 2.38, uses(1))
    soyuz = ReusableRocket(name = 'Soyuz 2', booster_cost = 20.9, upper_stage_cost = 13.9, fuel_cost = 0.24, uses(1))
    falcon = ReusableRocket(name = 'Falcon 9', booster_cost = 43.0, upper_stage_cost = 18.6, fuel_cost = 0.45, uses(10))
    for plane in (atlas_v, ariane, long_march, soyuz, falcon):

        print(f'This {plane.name} cost {plane.uses:.2f} million per launch.')

if __name__ == '__main__':
    main()
