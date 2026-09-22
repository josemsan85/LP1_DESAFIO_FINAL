package CENTRO_SALUD;

public class Cita {
    private String idCita;
    private String fecha;
    private String hora;
    private String estado; // PENDIENTE, ATENDIDA, CANCELADA
    private Paciente paciente;
    private Profesional profesional;

    public Cita(String idCita, String fecha, String hora, Paciente paciente, Profesional profesional) {
        this.idCita = idCita;
        this.fecha = fecha;
        this.hora = hora;
        this.paciente = paciente;
        this.profesional = profesional;
        this.estado = "PENDIENTE";
    }

    public void confirmarAtendida() { this.estado = "ATENDIDA"; }
    public void cancelar() { this.estado = "CANCELADA"; }

    public String getIdCita() { return idCita; }
    public String getFecha() { return fecha; }
    public String getHora() { return hora; }
    public String getEstado() { return estado; }
    public Paciente getPaciente() { return paciente; }
    public Profesional getProfesional() { return profesional; }

    @Override
    public String toString() {
        return "Cita " + idCita + " - " + paciente.getNombres() + " con " + profesional.getNombres()
                + " (" + fecha + " " + hora + ") [" + estado + "]";
    }
}