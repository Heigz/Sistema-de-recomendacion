from flask import Blueprint, request, render_template, flash
from functions.Funciones import *

preferencias_blueprint = Blueprint("preferencias", __name__, url_prefix="/preferencias")


@preferencias_blueprint.route("/recomendar", methods=["GET", "POST"])
def recomendar_auto():
    if request.method == "POST":
        # Marcas
        dodge = checkBoxAEntero(request.form.get("dodge"))
        seat = checkBoxAEntero(request.form.get("seat"))
        volkswagen = checkBoxAEntero(request.form.get("volkswagen"))
        porsche = checkBoxAEntero(request.form.get("porsche"))
        nissan = checkBoxAEntero(request.form.get("nissan"))
        mazda = checkBoxAEntero(request.form.get("mazda"))
        mitsubishi = checkBoxAEntero(request.form.get("mitsubishi"))
        audi = checkBoxAEntero(request.form.get("audi"))
        mercedesBenz = checkBoxAEntero(request.form.get("mercedesBenz"))
        hyundai = checkBoxAEntero(request.form.get("hyundai"))
        suzuki = checkBoxAEntero(request.form.get("suzuki"))
        toyota = checkBoxAEntero(request.form.get("toyota"))
        chevrolet = checkBoxAEntero(request.form.get("chevrolet"))

        # Potencias

        p70_80 = checkBoxAEntero(request.form.get("70_80"))
        p80_120 = checkBoxAEntero(request.form.get("80_120"))
        p120_200 = checkBoxAEntero(request.form.get("120_200"))
        p200_300 = checkBoxAEntero(request.form.get("200_300"))
        p300_400 = checkBoxAEntero(request.form.get("300_400"))
        p500 = checkBoxAEntero(request.form.get("500"))

        # Cantidad de cilindros
        cil_3 = checkBoxAEntero(request.form.get("3_cilindros"))
        cil_4 = checkBoxAEntero(request.form.get("4_cilindros"))
        cil_5 = checkBoxAEntero(request.form.get("5_cilindros"))
        cil_6 = checkBoxAEntero(request.form.get("6_cilindros"))
        cil_8 = checkBoxAEntero(request.form.get("8_cilindros"))
        cil_12 = checkBoxAEntero(request.form.get("12_cilindros"))

        # Tipo de Auto
        automovil = checkBoxAEntero(request.form.get("automovil"))
        hatchback = checkBoxAEntero(request.form.get("hatchback"))
        deportivo = checkBoxAEntero(request.form.get("deportivo"))
        lujo = checkBoxAEntero(request.form.get("lujo"))
        coupe = checkBoxAEntero(request.form.get("coupe"))
        off_road = checkBoxAEntero(request.form.get("off_road"))
        suv = checkBoxAEntero(request.form.get("suv"))
        pick_up = checkBoxAEntero(request.form.get("pick_up"))
        convertible = checkBoxAEntero(request.form.get("convertible"))
        camioneta = checkBoxAEntero(request.form.get("camioneta"))
        sedan = checkBoxAEntero(request.form.get("sedan"))

        # Tipo de combustible
        gasolina = checkBoxAEntero(request.form.get("gasolina"))
        diesel = checkBoxAEntero(request.form.get("diesel"))
        electrico = checkBoxAEntero(request.form.get("electrico"))

        # Cantidad de plazas
        dos_plazas = checkBoxAEntero(request.form.get("2_plazas"))
        cuatro_plazas = checkBoxAEntero(request.form.get("4_plazas"))
        cinco_plazas = checkBoxAEntero(request.form.get("5_plazas"))
        siete_plazas = checkBoxAEntero(request.form.get("7_plazas"))

        # Rango de precio
        mxn200_300 = checkBoxAEntero(request.form.get("200_300MXN"))
        mxn300_400 = checkBoxAEntero(request.form.get("300_400MXN"))
        mxn400_500 = checkBoxAEntero(request.form.get("400_500MXN"))
        mxn500_600 = checkBoxAEntero(request.form.get("500_600MXN"))
        mxn600_700 = checkBoxAEntero(request.form.get("600_700MXN"))
        mxn700 = checkBoxAEntero(request.form.get("700MXN"))

        # Tipo de traccion
        traccion_delantera = checkBoxAEntero(request.form.get("traccion_delantera"))
        traccion_trasera = checkBoxAEntero(request.form.get("traccion_trasera"))
        traccion_cuatroRuedas = checkBoxAEntero(
            request.form.get("traccion_cuatroRuedas")
        )
        traccion_cuatroRuedas4WD = checkBoxAEntero(
            request.form.get("traccion_cuatroRuedas4WD")
        )

        # Transmision
        transmision_manual = checkBoxAEntero(request.form.get("transmision_manual"))
        transmision_automatica = checkBoxAEntero(
            request.form.get("transmision_automatica")
        )
        transmision_cvt = checkBoxAEntero(request.form.get("transmision_cvt"))

        preferencias_usuario = [
            dodge,
            seat,
            volkswagen,
            porsche,
            nissan,
            mazda,
            mitsubishi,
            audi,
            mercedesBenz,
            hyundai,
            suzuki,
            toyota,
            chevrolet,
            p70_80,
            p80_120,
            p120_200,
            p200_300,
            p300_400,
            p500,
            cil_3,
            cil_4,
            cil_5,
            cil_6,
            cil_8,
            cil_12,
            automovil,
            hatchback,
            deportivo,
            lujo,
            coupe,
            off_road,
            suv,
            pick_up,
            convertible,
            camioneta,
            sedan,
            gasolina,
            diesel,
            electrico,
            dos_plazas,
            cuatro_plazas,
            cinco_plazas,
            siete_plazas,
            mxn200_300,
            mxn300_400,
            mxn400_500,
            mxn500_600,
            mxn600_700,
            mxn700,
            traccion_trasera,
            traccion_delantera,
            traccion_cuatroRuedas,
            traccion_cuatroRuedas4WD,
            transmision_manual,
            transmision_automatica,
            transmision_cvt,
        ]

        auto_recomendado = matchPreference(preferencias_usuario, obtenerDF(leerBase()))

        return render_template(
            "autoRecomendado.html", auto_recomendado=auto_recomendado
        )


def checkBoxAEntero(value):
    return 1 if value == "on" else 0
