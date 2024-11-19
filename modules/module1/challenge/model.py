'''
Clases

Gestión De Experimentos
    Creacion - Visualizacion
Análisis de Resultados
    Promedio - Maximo - Minimo - 
    Comparación (Desempeño Relativo)
Generación de Informe
    Resumen de los experimentos
    Estadisticas
    Conclusiones
    Opcion de Exportar en archivo txt
Cerrar el Programa
'''

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
