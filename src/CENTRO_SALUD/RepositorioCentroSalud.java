package CENTRO_SALUD;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Repositorio central (patron Singleton) que guarda en memoria
 * los pacientes, profesionales, atenciones y citas registrados
 * desde la interfaz grafica.
 */
public class RepositorioCentroSalud {
    private static RepositorioCentroSalud instancia;

    private List<Paciente> pacientes = new ArrayList<>();
    private List<Profesional> profesionales = new ArrayList<>();
    private List<Atencion> atenciones = new ArrayList<>();
    private List<Cita> citas = new ArrayList<>();
    private List<FUA> fuas = new ArrayList<>();

    private int contadorPaciente = 1;
    private int contadorProfesional = 1;
    private int contadorHistoria = 1;
    private int contadorCita = 1;
    private int contadorReceta = 1;
    private int contadorFua = 1;

    private RepositorioCentroSalud() {
        cargarDatosDePrueba();
    }

    public static RepositorioCentroSalud getInstancia() {
        if (instancia == null) instancia = new RepositorioCentroSalud();
        return instancia;
    }

    // Data pre-ingresada en los ArrayList para que el sistema no arranque vacio
    private void cargarDatosDePrueba() {
        Paciente luis = crearPaciente("87654321", "Luis", "Ramos Vega", "1990-05-10", "M");
        Paciente rosa = crearPaciente("71234567", "Rosa", "Chilon Diaz", "1985-02-20", "F");

        Profesional ana = crearProfesional("27654321", "Ana", "Torres Quispe", "Medicina General", "Medico");
        Profesional carlos = crearProfesional("29876543", "Carlos", "Mendoza Silva", "Enfermeria", "Enfermero");

        Atencion atencion1 = crearAtencion(luis, ana, LocalDate.now().minusDays(3).toString(),
                "Dolor de cabeza intenso", "Migraña", "Reposo y analgesico");
        crearReceta(atencion1, "Tomar con alimentos, reposo 24h",
                List.of("Paracetamol 500mg - cada 8h por 3 dias"));
        crearFua(atencion1, "Medicina General", "Consulta ambulatoria");

        Atencion atencion2 = crearAtencion(rosa, carlos, LocalDate.now().minusDays(1).toString(),
                "Control de presion arterial", "Hipertension leve", "Dieta baja en sodio");

        crearCita(luis, ana, LocalDate.now().plusDays(7).toString(), "10:00");
        crearCita(rosa, carlos, LocalDate.now().plusDays(10).toString(), "09:30");
    }

    public Paciente crearPaciente(String dni, String nombres, String apellidos,
                                   String fechaNacimiento, String sexo) {
        String id = String.format("PA%03d", contadorPaciente++);
        Paciente paciente = new Paciente(id, dni, nombres, apellidos, fechaNacimiento, sexo);

        HistoriaClinica historia = new HistoriaClinica(
                String.format("H%03d", contadorHistoria++),
                LocalDate.now().toString(), "Ninguno", "Ninguna", paciente);
        paciente.setHistoriaClinica(historia);

        pacientes.add(paciente);
        return paciente;
    }

    public Profesional crearProfesional(String dni, String nombres, String apellidos,
                                         String especialidad, String cargo) {
        String id = String.format("PR%03d", contadorProfesional++);
        Profesional profesional = new Profesional(id, dni, nombres, apellidos, especialidad, cargo);
        profesionales.add(profesional);
        return profesional;
    }

    public Atencion crearAtencion(Paciente paciente, Profesional profesional, String fecha,
                                   String motivo, String diagnostico, String tratamiento) {
        HistoriaClinica historia = paciente.getHistoriaClinica();
        Atencion atencion = new Atencion(fecha, motivo, diagnostico, tratamiento, profesional, historia);
        historia.agregarAtencion(atencion);
        atenciones.add(atencion);
        return atencion;
    }

    public RecetaMedica crearReceta(Atencion atencion, String indicaciones, List<String> medicamentos) {
        String id = String.format("REC%03d", contadorReceta++);
        RecetaMedica receta = new RecetaMedica(id, LocalDate.now().toString(), indicaciones, atencion);
        for (String medicamento : medicamentos) {
            receta.agregarMedicamento(medicamento);
        }
        atencion.agregarReceta(receta);
        return receta;
    }

    public Cita crearCita(Paciente paciente, Profesional profesional, String fecha, String hora) {
        String id = String.format("CITA%03d", contadorCita++);
        Cita cita = new Cita(id, fecha, hora, paciente, profesional);
        paciente.agregarCita(cita);
        profesional.agregarCita(cita);
        citas.add(cita);
        return cita;
    }

    public FUA crearFua(Atencion atencion, String servicio, String procedimiento) {
        String id = String.format("FUA%03d", contadorFua++);
        FUA fua = new FUA(id, atencion.getFecha(), servicio, atencion.getDiagnostico(), procedimiento, atencion);
        atencion.setFua(fua);
        fuas.add(fua);
        return fua;
    }

    public List<Paciente> getPacientes() { return pacientes; }
    public List<Profesional> getProfesionales() { return profesionales; }
    public List<Atencion> getAtenciones() { return atenciones; }
    public List<Cita> getCitas() { return citas; }
    public List<FUA> getFuas() { return fuas; }
}