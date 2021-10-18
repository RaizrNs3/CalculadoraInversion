# -*- coding: utf-8 -*-
import sys
import datetime


def calculate_returns():
    months_names = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
                    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
    print('-> Inicio del cálculo de rendimientos <-')
    # Todo: validar las entradas pasadas por parámetro
    """ Valores obligatorios, el programa no debería funciona si no están presentes """
    expected_total_amount = float(sys.argv[1])  # Cantidad que se espera obtener
    starting_amount = float(sys.argv[2])  # Monto con el que se inicia la inversión, valor por defecto 200,036.51
    monthly_user_increase = float(sys.argv[3])
    special_deduction = float(sys.argv[4])
    savings_bank = 0

    percentaje = 0.03
    end_of_year_bonus = 24000

    cont_months = float(datetime.datetime.today().strftime('%m')) - 1
    general_month_cont = 0
    yields = starting_amount * percentaje
    flag_special_deduction = True

    while yields < expected_total_amount:
        """ Deducciones especiales como rentas """
        savings_bank += 6400
        if yields >= special_deduction != 0:
            if flag_special_deduction:
                print("->*** El rendimiento supera la deducción especial ***<-")
                flag_special_deduction = False
            starting_amount = starting_amount - special_deduction

        starting_amount += yields + monthly_user_increase  # Se calcula el nuevo total obtenido
        yields = round(starting_amount * percentaje, 2)

        # Año cumplido
        if cont_months == 12:
            starting_amount = starting_amount + end_of_year_bonus + savings_bank
            savings_bank = 0
            cont_months = 0
            print("Fin de año")

        cont_months = cont_months + 1
        general_month_cont = general_month_cont + 1
        print(f"-> Mes: {months_names.get(cont_months)} inversión total: {round(starting_amount, 2)}, rendimiento generado: {round(yields, 2)}")
    print(f"-> Años para alcanzar la meta de ${expected_total_amount}: {general_month_cont / 12}<-")


if __name__ == '__main__':
    calculate_returns()
