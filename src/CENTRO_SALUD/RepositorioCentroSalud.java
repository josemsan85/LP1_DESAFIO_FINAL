package CENTRO_SALUD;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
public class RepositorioCentroSalud {
    private static RepositorioCentroSalud instancia;

    private List<Paciente> pacientes = new ArrayList<>();
    private List<Profesional> profesionales = new ArrayList<>();
    private List<Atencion> atenciones = new ArrayList<>();
    private List<Cita> citas = new ArrayList<>();

    private int contadorPaciente = 1;
    private int contadorProfesional = 1;
    private int contadorHistoria = 1;
    private int contadorCita = 1;
    private int contadorReceta = 1;

    private RepositorioCentroSalud() {}

    public static RepositorioCentroSalud getInstancia() {
        if (instancia == null) instancia = new RepositorioCentroSalud();
        return instancia;
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

    public List<Paciente> getPacientes() { return pacientes; }
    public List<Profesional> getProfesionales() { return profesionales; }
    public List<Atencion> getAtenciones() { return atenciones; }
    public List<Cita> getCitas() { return citas; }
}