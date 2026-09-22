package CENTRO_SALUD;

public abstract class Persona {
    private String idPersona;
    private String dni;
    private String nombres;
    private String apellidos;
 
    public Persona(String idPersona, String dni, String nombres, String apellidos) {
        this.idPersona = idPersona;
        this.dni = dni;
        this.nombres = nombres;
        this.apellidos = apellidos;
    }
 
    public String getIdPersona() { return idPersona; }
    public void setIdPersona(String idPersona) { this.idPersona = idPersona; }
 
    public String getDni() { return dni; }
    public void setDni(String dni) { this.dni = dni; }
 
    public String getNombres() { return nombres; }
    public void setNombres(String nombres) { this.nombres = nombres; }
 
    public String getApellidos() { return apellidos; }
    public void setApellidos(String apellidos) { this.apellidos = apellidos; }
 
    @Override
    public String toString() {
        return nombres + " " + apellidos + " (DNI: " + dni + ")";
    }
}
 