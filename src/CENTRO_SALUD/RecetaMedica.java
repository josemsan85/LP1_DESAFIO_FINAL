package CENTRO_SALUD;

import java.util.ArrayList;
import java.util.List;

public class RecetaMedica {
    private String idReceta;
    private String fecha;
    private List<String> medicamentos = new ArrayList<>();
    private String indicaciones;
    private Atencion atencion; // atencion que origina la receta

    public RecetaMedica(String idReceta, String fecha, String indicaciones, Atencion atencion) {
        this.idReceta = idReceta;
        this.fecha = fecha;
        this.indicaciones = indicaciones;
        this.atencion = atencion;
    }

    public void agregarMedicamento(String medicamento) {
        medicamentos.add(medicamento);
    }

    public String getIdReceta() { return idReceta; }
    public String getFecha() { return fecha; }
    public List<String> getMedicamentos() { return medicamentos; }
    public String getIndicaciones() { return indicaciones; }
    public Atencion getAtencion() { return atencion; }

    @Override
    public String toString() {
        return "Receta " + idReceta + " (" + fecha + ") - " + medicamentos.size() + " medicamento(s)";
    }
}