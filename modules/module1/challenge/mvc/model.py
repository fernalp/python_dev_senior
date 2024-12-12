
## Abstracion de experimento
class Experiment:
  def __init__(self, name, date, type_experiment, results):
    self.name = name
    self.date = date
    self.type_experiment = type_experiment
    self.results = results

## Abstracion de gestión de experimentos
class ExperimentManagement:
  
  def __init__(self):
    self.experiments = []
  
  def add_experiment(self, experiment):
    self.experiments.append(experiment)
  
  def get_experiments(self):
    return self.experiments
