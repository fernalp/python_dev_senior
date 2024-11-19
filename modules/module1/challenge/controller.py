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

from datetime import datetime
import statistics

from model import Experiment, ExperimentManagement
from view import View

class Controller:
    
    def __init__(self):
        self.experiment_management = ExperimentManagement()
        self.view = View()
         
    def execute(self):
        while True:
            self.view.show_main_menu()
            option = self.view.show_and_select_an_option()
            self.verify_option_is_error(option)
            if option == 1:
                self.enter_experiment_management_menu()
            if option == 2:
                self.analysis_of_results()
            if option == 3:
                self.generate_report()
            if option == 4:
                print("Gracias por Utilizar Nuestro Programa!!")
                break
            if 0 < option > 4 :
                self.view.show_incorrect_option()
    
    def enter_experiment_management_menu(self):
        option_incorrect = True
        while option_incorrect:
            self.view.show_experiment_management_menu()
            option = self.view.show_and_select_an_option()
            self.verify_option_is_error(option)
            if option == 1:
                self.add_experiment()
                option_incorrect = False
            elif option == 2:
                self.get_experiments()
                option_incorrect = False
            if 0 < option > 2:
                self.view.show_incorrect_option()
            
    def add_experiment( self ):
        date_invalid = True
        results_invalid = True
        name = self.view.show_and_select_field_experiment(message="Ingrese el nombre del experimento")
        while date_invalid:
            date_str = self.view.show_and_select_field_experiment(message="Ingrese la fecha de realización del experimento (DD/MM/YYYY)")
            try:
                date = datetime.strptime(date_str, "%d/%m/%Y")  
                date_invalid = False       
            except ValueError:
                self.view.show_message("Fecha inválida")
        type_experiment = self.view.show_and_select_field_experiment(message="Ingrese el tipo de experimento(Estudio, Personal, Trabajo, etc)")
        while results_invalid:  
            results_str = self.view.show_and_select_field_experiment(message="Ingrese el resultado del experimento, separados por comas ejemplo 3,5,6")
            try: 
                results =  list(map(float, results_str.split(",")))
                results_invalid = False     
            except ValueError:
                self.view.show_message(message="Resultados inválidos")
        experiment = Experiment(name, date, type_experiment, results)
        self.experiment_management.add_experiment(experiment)
        self.view.show_message(message="Experimento agregado correctamente")
     
    def get_experiments(self):
        experiments = self.find_experiments()
        self.view.show_experiments(experiments)

    def analysis_of_results(self):
        analysis = self.calculate_analysis_results()
        self.view.show_analysis_results(analysis)
     
    def generate_report(self):
        ## Se genera un resumen de los experimentos
        ## Estadisticas
        ## Conclusiones
        self.view.show_generate_report()
    
    def export_report_to_txt(self, report):
        ## Se exporta el reporte generado
        pass
 
    def verify_option_is_error(self, option):
        if option == 0:
            self.view.show_error_option()
            
    def find_experiments(self):
        return self.experiment_management.get_experiments()
    
    def calculate_analysis_results(self):
        analysis = self.find_experiments()
        for experiment in analysis:
            experiment.prom = statistics.mean(experiment.results)
            experiment.min = min(experiment.results)
            experiment.max = max(experiment.results)
            experiment.comparate = statistics.median(experiment)
        return analysis
