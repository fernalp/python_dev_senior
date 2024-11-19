
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


class View:
        
    def show_and_select_an_option(self):
        try:
          option = int(input("Seleccione una opción: "))
          return option
        except ValueError:
            return 0
    
    def show_and_select_field_experiment(self, message):
        message = message.capitalize() + ": "
        return input(message)
   
    def show_main_menu(self): 
        ## Muestra el Menu Principal
        ## Fernando        
        print("---Menú Principal---")
        print("1. Gestión de Experimentos")
        print("2. Análisis de Resultados")
        print("3. Generación de Informe")
        print("4. Salir Del Programa")
            
    def show_experiment_management_menu(self): 
        ## Muestra el Menu de agregar y mostrar experimento
        ## Fernando  
        print("---Menú Gestión de Experimentos---")
        print("1. Agregar Experimento")
        print("2. Ver Experimentos")
    
    def show_experiments(self, experiments):
        ## Mostrar todos los experimentos
        ## Fernando
        if not experiments:
            print("No hay experimentos registrados!!")
        else:
            for i, experiment in enumerate(experiments, start=1):
                print(f"\nExperimento {i}")
                print(f"Nombre: {experiment.name}")
                print(f"Fecha de Realización: {experiment.date.strftime('%d/%m/%Y')}")
                print(f"Tipo de Experimento: {experiment.type_experiment}")
                print(f"Resultados: {experiment.results}")
 
    def show_analysis_results(self, analysis):
        ## Mostrar el analisis de resultados
        if not analysis:
            print("No hay Experimentos!!, por lo que no se puede realizar un análisis!")
        else:
            for i, experiment in enumerate(analysis, start=1):
                print(f"\nAnalisis Experimento {i}")
                print(f"Nombre: {experiment.name}")
                print(f"Fecha: {experiment.date.strftime('%d/%m/%Y')}")
                print(f"Tipo de Experimento: {experiment.type_experiment}")
                print(f"Results: {experiment.results}")
                print("---Análisis de Resultados---")
                print(f"Promedio: {experiment.prom}")
                print(f"Mínimo: {experiment.min}")
                print(f"Máximo: {experiment.max}")
    
    def show_generate_report(self):
        ## Mostrar vista del reporte generado y preguntar si quiere exportarlo
        print("Vista de generar reporte")
 
    def show_error_option(self):
        self.show_message(message="Por favor selecciona solo el número de la opción")
    
    def show_message(self, message):
        message = message.capitalize() + "!"
        print(message)

    def show_incorrect_option(self):
        self.show_message(message="Opcion Incorrecta, Intenta de Nuevo!")
 