package CENTRO_SALUD;
 
public class Ejecucion {
    public static void main(String[] args) {
 
        // 1. Registrar al profesional que atiende
        Profesional profesional = new Profesional(
                "PR001", "27654321", "Ana", "Torres Quispe",
                "Medicina General", "Medico");
 
        // 2. Registrar al paciente
        Paciente paciente = new Paciente(
                "PA001", "87654321", "Luis", "Ramos Vega",
                "1990-05-10", "M");
 
        // 3. Abrir su historia clinica
        HistoriaClinica historia = new HistoriaClinica(
                "H001", "2026-09-12", "Ninguno", "Ninguna",
                paciente);
        paciente.setHistoriaClinica(historia);
 
        // 4. Registrar una atencion
        Atencion atencion = new Atencion(
                "2026-09-12", "Dolor de cabeza intenso", "Migraña",
                "Reposo y analgesico", profesional, historia);
        historia.agregarAtencion(atencion);
 
        // 5. Generar los documentos que origina la atencion
        FUA fua = new FUA(
                "FUA001", "2026-09-12", "Medicina General",
                "Migraña", "Consulta ambulatoria", atencion);
        atencion.setFua(fua);

        // 5.1 Generar receta medica asociada a la atencion
        RecetaMedica receta = new RecetaMedica(
                "REC001", "2026-09-12", "Tomar con alimentos, reposo 24h", atencion);
        receta.agregarMedicamento("Paracetamol 500mg - cada 8h por 3 dias");
        receta.agregarMedicamento("Ibuprofeno 400mg - solo si persiste el dolor");
        atencion.agregarReceta(receta);

        // 5.2 Registrar una cita futura de control
        Cita cita = new Cita("CITA001", "2026-09-19", "10:00", paciente, profesional);
        paciente.agregarCita(cita);
        profesional.agregarCita(cita);
 
        // 6. Mostrar el resultado
        System.out.println("=== Paciente ===");
        System.out.println(paciente);
        System.out.println("Fecha nacimiento: " + paciente.getFechaNacimiento());
 
        System.out.println("\n=== Profesional que atiende ===");
        System.out.println(profesional);
        System.out.println("Especialidad: " + profesional.getEspecialidad());
 
        System.out.println("\n=== Historia clinica ===");
        System.out.println("Id historia: " + historia.getIdHistoria());
        System.out.println("Cantidad de atenciones: " + historia.getAtenciones().size());
 
        System.out.println("\n=== Atencion registrada ===");
        System.out.println("Motivo: " + atencion.getMotivo());
        System.out.println("Diagnostico: " + atencion.getDiagnostico());
        System.out.println("Atendido por: " + atencion.getProfesional().getNombres());
 
        System.out.println("\n=== Documentos generados ===");
        System.out.println("FUA id: " + atencion.getFua().getIdFUA()
                + " | servicio: " + atencion.getFua().getServicio());

        System.out.println("\n=== Receta medica ===");
        System.out.println(receta);
        System.out.println("Medicamentos: " + receta.getMedicamentos());

        System.out.println("\n=== Cita registrada ===");
        System.out.println(cita);
    }
}