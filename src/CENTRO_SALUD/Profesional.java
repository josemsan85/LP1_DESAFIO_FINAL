package CENTRO_SALUD;

import java.util.ArrayList;
import java.util.List;

public class Profesional extends Persona {
    private String especialidad;
    private String cargo;
    private List<Cita> agenda = new ArrayList<>(); // 1 profesional -> N citas
 
    public Profesional(String idPersona, String dni, String nombres, String apellidos,
                        String especialidad, String cargo) {
        super(idPersona, dni, nombres, apellidos);
        this.especialidad = especialidad;
        this.cargo = cargo;
    }

    public void agregarCita(Cita cita) {
        agenda.add(cita);
    }

    public List<Cita> getAgenda() { return agenda; }
 
    public String getEspecialidad() { return especialidad; }
    public void setEspecialidad(String especialidad) { this.especialidad = especialidad; }
 
    public String getCargo() { return cargo; }
    public void setCargo(String cargo) { this.cargo = cargo; }
}