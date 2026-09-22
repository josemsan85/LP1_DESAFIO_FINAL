package CENTRO_SALUD;

import java.util.ArrayList;
import java.util.List;
 
public class HistoriaClinica {
    private String idHistoria;
    private String fechaApertura;
    private String antecedentes;
    private String alergias;
    private Paciente paciente; // dueño de la historia
    private List<Atencion> atenciones = new ArrayList<>(); // 1 historia -> N atenciones
 
    public HistoriaClinica(String idHistoria, String fechaApertura, String antecedentes,
                            String alergias, Paciente paciente) {
        this.idHistoria = idHistoria;
        this.fechaApertura = fechaApertura;
        this.antecedentes = antecedentes;
        this.alergias = alergias;
        this.paciente = paciente;
    }
 
    public void agregarAtencion(Atencion atencion) {
        atenciones.add(atencion);
    }
 
    public String getIdHistoria() { return idHistoria; }
    public String getFechaApertura() { return fechaApertura; }
    public String getAntecedentes() { return antecedentes; }
    public String getAlergias() { return alergias; }
    public Paciente getPaciente() { return paciente; }
    public List<Atencion> getAtenciones() { return atenciones; }
}
 