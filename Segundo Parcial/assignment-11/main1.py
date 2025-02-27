'''
#       Sesión 11: Assignment 11.1
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main1.py
#
#       Creado:                   26/02/2024
#       Última Modificación:      26/02/2024
'''
class Main():
    def __init__(self):
        pass

    def diccionario_calificaciones(self, grades):
        self.grades = {
            subjects[0]: grades[0],
            subjects[1]: grades[1],
            subjects[2]: grades[2],
            subjects[3]: grades[3],
            subjects[4]: grades[4],
            subjects[5]: grades[5]
        }

    def promediar(self):
        total = sum(self.grades.values())
        self.average = total / len(self.grades)

    def generar_reporte(self):
        report = "Reporte de calificaciones:\n"
        for subject, grade in self.grades.items():
            report += f"{subject}: {grade}\n"
        report += f"Promedio: {self.average:.2f}"
        return report


if __name__ == '__main__':
    main = Main()
    grades = []
    subjects = ['Matematicas', 'Español', 'Ingles', 'Fisica', 'Programacion', 'Artes']
    for subject in subjects:
        grade = float(input(f"Pon tu nota de {subject}: "))
        grades.append(grade)
    main.diccionario_calificaciones(grades)
    main.promediar()
    report = main.generar_reporte()
    print("====================================")
    print(report)
    print("====================================")
