package CENTRO_SALUD;

public class FUA {
    private String idFUA;
    private String fecha;
    private String servicio;
    private String diagnostico;
    private String procedimiento;
    private Atencion atencion; // atencion que origina este formato
 
    public FUA(String idFUA, String fecha, String servicio, String diagnostico,
               String procedimiento, Atencion atencion) {
        this.idFUA = idFUA;
        this.fecha = fecha;
        this.servicio = servicio;
        this.diagnostico = diagnostico;
        this.procedimiento = procedimiento;
        this.atencion = atencion;
    }
 
    public String getIdFUA() { return idFUA; }
    public String getFecha() { return fecha; }
    public String getServicio() { return servicio; }
    public String getDiagnostico() { return diagnostico; }
    public String getProcedimiento() { return procedimiento; }
    public Atencion getAtencion() { return atencion; }
}
 