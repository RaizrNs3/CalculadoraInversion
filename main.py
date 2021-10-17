# -*- coding: utf-8 -*-
import sys
import datetime


def calculate_returns():
    print('-> Inicio del cálculo de rendimientos <-')
    # Todo: validar las entradas pasadas por parámetro
    """ Valores obligatorios, el programa no debería funciona si no están presentes """
    expected_total_amount = float(sys.argv[1])  # Cantidad que se espera obtener
    starting_amount = float(sys.argv[2])  # Monto con el que se inicia la inversión, valor por defecto 200,036.51
    monthly_user_increase = float(sys.argv[3])
    special_deduction = float(sys.argv[4])

    percentaje = 0.03
    end_of_year_bonus = 24000

    cont_months = 0
    general_cont = 0
    yields = starting_amount * percentaje

    while yields < expected_total_amount:
        """ Deducciones especiales como rentas """
        if yields >= special_deduction:
            print("-> El rendimiento supera la deducción especial <-")
            starting_amount = starting_amount - special_deduction

        starting_amount = starting_amount + yields + monthly_user_increase  # Se calcula el nuevo total obtenido
        yields = starting_amount * percentaje

        # Año cumplido
        if cont_months == 12:
            starting_amount = starting_amount + end_of_year_bonus
            cont_months = 0
            print("Fin de año")

        cont_months = cont_months + 1
        general_cont = general_cont + 1
        print("-> Mes: " + str(general_cont) + " inversión total: " + str(starting_amount))
    print(f"-> Años para alcanzar la meta de {expected_total_amount}: {general_cont / 12}<-")


def calculator():
    print("-> Inicio de cálculo <-")


if __name__ == '__main__':
    calculate_returns()
