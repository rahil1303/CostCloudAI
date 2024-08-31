import pandas as pd

class CostCloudAnalysis:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def compare_costs(self):
        return self.data.groupby('CloudProvider').mean()
    
    def get_best_option(self):
        efficiency_weighted_cost = self.data['CostPerHour'] / self.data['AIModelEfficiency']
        self.data['EfficiencyWeightedCost'] = efficiency_weighted_cost
        return self.data.loc[self.data['EfficiencyWeightedCost'].idxmin()]

if __name__ == "__main__":
    analysis = CostCloudAnalysis('../cloud_costs.csv')
    print("Average Cost per Cloud Provider:\n", analysis.compare_costs())
    print("\nBest Cloud Provider Option:\n", analysis.get_best_option())
