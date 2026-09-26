"""usa el Singleton RepositorioCentroSalud, que ya viene con datos de
prueba cargados (2 pacientes, 2 profesionales, atenciones y citas).
"""

from repositorio_centro_salud import RepositorioCentroSalud


def main():
    repo = RepositorioCentroSalud.get_instancia()

    print("=== Pacientes registrados ===")
    for paciente in repo.get_pacientes():
        print(paciente)
        print(f"  Fecha nacimiento: {paciente.get_fecha_nacimiento()}")

    print("\n=== Profesionales registrados ===")
    for profesional in repo.get_profesionales():
        print(f"{profesional} - {profesional.get_especialidad()}")

    print("\n=== Atenciones registradas ===")
    for atencion in repo.get_atenciones():
        print(f"{atencion.get_fecha()} | {atencion.get_motivo()} -> "
              f"{atencion.get_diagnostico()} "
              f"(atendido por {atencion.get_profesional().get_nombres()})")
        if atencion.get_fua() is not None:
            print(f"  FUA generado: {atencion.get_fua().get_id_fua()}")
        for receta in atencion.get_recetas():
            print(f"  {receta} -> {receta.get_medicamentos()}")

    print("\n=== Citas registradas ===")
    for cita in repo.get_citas():
        print(cita)


if __name__ == "__main__":
    main()
