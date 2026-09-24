"""Demostración por consola del flujo completo: paciente -> atención -> documentos -> cita."""
from atencion import Atencion
from cita import Cita
from fua import FUA
from historia_clinica import HistoriaClinica
from paciente import Paciente
from profesional import Profesional
from receta_medica import RecetaMedica


def main() -> None:
    # 1. Registrar al profesional que atiende
    profesional = Profesional("PR001", "27654321", "Ana", "Torres Quispe",
                              "Medicina General", "Medico")

    # 2. Registrar al paciente
    paciente = Paciente("PA001", "87654321", "Luis", "Ramos Vega", "1990-05-10", "M")

    # 3. Abrir su historia clínica
    historia = HistoriaClinica("H001", "2026-09-12", "Ninguno", "Ninguna", paciente)
    paciente.historia_clinica = historia

    # 4. Registrar una atención
    atencion = Atencion("2026-09-12", "Dolor de cabeza intenso", "Migraña",
                        "Reposo y analgesico", profesional, historia)
    historia.agregar_atencion(atencion)

    # 5. Generar los documentos que origina la atención
    fua = FUA("FUA001", "2026-09-12", "Medicina General", "Migraña",
              "Consulta ambulatoria", atencion)
    atencion.fua = fua

    # 5.1 Generar receta médica asociada a la atención
    receta = RecetaMedica("REC001", "2026-09-12", "Tomar con alimentos, reposo 24h", atencion)
    receta.agregar_medicamento("Paracetamol 500mg - cada 8h por 3 dias")
    receta.agregar_medicamento("Ibuprofeno 400mg - solo si persiste el dolor")
    atencion.agregar_receta(receta)

    # 5.2 Registrar una cita futura de control
    cita = Cita("CITA001", "2026-09-19", "10:00", paciente, profesional)
    paciente.agregar_cita(cita)
    profesional.agregar_cita(cita)

    # 6. Mostrar el resultado
    print("=== Paciente ===")
    print(paciente)
    print("Fecha nacimiento:", paciente.fecha_nacimiento)

    print("\n=== Profesional que atiende ===")
    print(profesional)
    print("Especialidad:", profesional.especialidad)

    print("\n=== Historia clínica ===")
    print("Id historia:", historia.id_historia)
    print("Cantidad de atenciones:", len(historia.atenciones))

    print("\n=== Atención registrada ===")
    print("Motivo:", atencion.motivo)
    print("Diagnóstico:", atencion.diagnostico)
    print("Atendido por:", atencion.profesional.nombres)

    print("\n=== Documentos generados ===")
    print(f"FUA id: {atencion.fua.id_fua} | servicio: {atencion.fua.servicio}")

    print("\n=== Receta médica ===")
    print(receta)
    print("Medicamentos:", receta.medicamentos)

    print("\n=== Cita registrada ===")
    print(cita)


if __name__ == "__main__":
    main()
