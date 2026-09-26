package CENTRO_SALUD;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 * Ventana principal del sistema del Centro de Salud Rural "Santa Rosa".
 * Usa el patron Singleton (RepositorioCentroSalud) como fuente unica de datos
 * y demuestra programacion orientada a eventos (listeners sobre botones).
 */
public class VentanaPrincipal extends JFrame {

    private final RepositorioCentroSalud repo = RepositorioCentroSalud.getInstancia();

    // Tablas
    private DefaultTableModel modeloPacientes;
    private DefaultTableModel modeloProfesionales;
    private DefaultTableModel modeloAtenciones;
    private DefaultTableModel modeloCitas;
    private DefaultTableModel modeloFua;

    // Combos que dependen de los pacientes/profesionales registrados
    private JComboBox<Paciente> comboPacienteAtencion;
    private JComboBox<Profesional> comboProfesionalAtencion;
    private JComboBox<Paciente> comboPacienteCita;
    private JComboBox<Profesional> comboProfesionalCita;
    private JComboBox<Atencion> comboAtencionReceta;
    private JComboBox<Atencion> comboAtencionFua;

    private JTable tablaCitas;
    private DefaultListModel<String> modeloMedicamentos = new DefaultListModel<>();

    public VentanaPrincipal() {
        super("Centro de Salud Rural Santa Rosa - Chugur");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(850, 600);
        setLocationRelativeTo(null);

        JTabbedPane pestanas = new JTabbedPane();
        pestanas.addTab("Pacientes", crearPanelPacientes());
        pestanas.addTab("Profesionales", crearPanelProfesionales());
        pestanas.addTab("Atenciones y Recetas", crearPanelAtenciones());
        pestanas.addTab("FUA", crearPanelFua());
        pestanas.addTab("Citas", crearPanelCitas());

        add(pestanas);
    }

    // ---------------------------------------------------------
    // TAB 1: PACIENTES
    // ---------------------------------------------------------
    private JPanel crearPanelPacientes() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));

        JPanel formulario = new JPanel(new GridLayout(6, 2, 5, 5));
        JTextField txtDni = new JTextField();
        JTextField txtNombres = new JTextField();
        JTextField txtApellidos = new JTextField();
        JTextField txtFechaNac = new JTextField(LocalDate.now().minusYears(30).toString());
        JTextField txtSexo = new JTextField();

        formulario.add(new JLabel("DNI (8 digitos):"));
        formulario.add(txtDni);
        formulario.add(new JLabel("Nombres:"));
        formulario.add(txtNombres);
        formulario.add(new JLabel("Apellidos:"));
        formulario.add(txtApellidos);
        formulario.add(new JLabel("Fecha nacimiento (AAAA-MM-DD):"));
        formulario.add(txtFechaNac);
        formulario.add(new JLabel("Sexo (M/F):"));
        formulario.add(txtSexo);

        JButton btnRegistrar = new JButton("Registrar paciente");
        formulario.add(new JLabel());
        formulario.add(btnRegistrar);

        modeloPacientes = new DefaultTableModel(
                new Object[]{"ID", "DNI", "Nombres", "Apellidos", "F. Nacimiento", "Sexo"}, 0);
        JTable tabla = new JTable(modeloPacientes);

        for (Paciente p : repo.getPacientes()) {
            modeloPacientes.addRow(new Object[]{p.getIdPersona(), p.getDni(), p.getNombres(),
                    p.getApellidos(), p.getFechaNacimiento(), p.getSexo()});
        }

        // Evento: click en "Registrar paciente"
        btnRegistrar.addActionListener(e -> {
            String dni = txtDni.getText().trim();
            String nombres = txtNombres.getText().trim();
            String apellidos = txtApellidos.getText().trim();

            if (dni.length() != 8 || !dni.matches("\\d+")) {
                JOptionPane.showMessageDialog(this, "El DNI debe tener exactamente 8 digitos.",
                        "Dato invalido", JOptionPane.WARNING_MESSAGE);
                return;
            }
            if (nombres.isEmpty() || apellidos.isEmpty()) {
                JOptionPane.showMessageDialog(this, "Nombres y apellidos son obligatorios.",
                        "Dato invalido", JOptionPane.WARNING_MESSAGE);
                return;
            }

            Paciente paciente = repo.crearPaciente(dni, nombres, apellidos,
                    txtFechaNac.getText().trim(), txtSexo.getText().trim());

            modeloPacientes.addRow(new Object[]{paciente.getIdPersona(), paciente.getDni(),
                    paciente.getNombres(), paciente.getApellidos(),
                    paciente.getFechaNacimiento(), paciente.getSexo()});

            comboPacienteAtencion.addItem(paciente);
            comboPacienteCita.addItem(paciente);

            txtDni.setText("");
            txtNombres.setText("");
            txtApellidos.setText("");
            txtSexo.setText("");
        });

        panel.add(formulario, BorderLayout.NORTH);
        panel.add(new JScrollPane(tabla), BorderLayout.CENTER);
        return panel;
    }

    // ---------------------------------------------------------
    // TAB 2: PROFESIONALES
    // ---------------------------------------------------------
    private JPanel crearPanelProfesionales() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));

        JPanel formulario = new JPanel(new GridLayout(6, 2, 5, 5));
        JTextField txtDni = new JTextField();
        JTextField txtNombres = new JTextField();
        JTextField txtApellidos = new JTextField();
        JTextField txtEspecialidad = new JTextField();
        JTextField txtCargo = new JTextField();

        formulario.add(new JLabel("DNI (8 digitos):"));
        formulario.add(txtDni);
        formulario.add(new JLabel("Nombres:"));
        formulario.add(txtNombres);
        formulario.add(new JLabel("Apellidos:"));
        formulario.add(txtApellidos);
        formulario.add(new JLabel("Especialidad:"));
        formulario.add(txtEspecialidad);
        formulario.add(new JLabel("Cargo:"));
        formulario.add(txtCargo);

        JButton btnRegistrar = new JButton("Registrar profesional");
        formulario.add(new JLabel());
        formulario.add(btnRegistrar);

        modeloProfesionales = new DefaultTableModel(
                new Object[]{"ID", "DNI", "Nombres", "Apellidos", "Especialidad", "Cargo"}, 0);
        JTable tabla = new JTable(modeloProfesionales);

        for (Profesional p : repo.getProfesionales()) {
            modeloProfesionales.addRow(new Object[]{p.getIdPersona(), p.getDni(), p.getNombres(),
                    p.getApellidos(), p.getEspecialidad(), p.getCargo()});
        }

        btnRegistrar.addActionListener(e -> {
            String dni = txtDni.getText().trim();
            String nombres = txtNombres.getText().trim();
            String apellidos = txtApellidos.getText().trim();

            if (dni.length() != 8 || !dni.matches("\\d+")) {
                JOptionPane.showMessageDialog(this, "El DNI debe tener exactamente 8 digitos.",
                        "Dato invalido", JOptionPane.WARNING_MESSAGE);
                return;
            }

            Profesional profesional = repo.crearProfesional(dni, nombres, apellidos,
                    txtEspecialidad.getText().trim(), txtCargo.getText().trim());

            modeloProfesionales.addRow(new Object[]{profesional.getIdPersona(), profesional.getDni(),
                    profesional.getNombres(), profesional.getApellidos(),
                    profesional.getEspecialidad(), profesional.getCargo()});

            comboProfesionalAtencion.addItem(profesional);
            comboProfesionalCita.addItem(profesional);

            txtDni.setText("");
            txtNombres.setText("");
            txtApellidos.setText("");
            txtEspecialidad.setText("");
            txtCargo.setText("");
        });

        panel.add(formulario, BorderLayout.NORTH);
        panel.add(new JScrollPane(tabla), BorderLayout.CENTER);
        return panel;
    }

    // ---------------------------------------------------------
    // TAB 3: ATENCIONES + RECETAS
    // ---------------------------------------------------------
    private JPanel crearPanelAtenciones() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));

        // --- Formulario de atencion ---
        JPanel formAtencion = new JPanel(new GridLayout(6, 2, 5, 5));
        comboPacienteAtencion = new JComboBox<>();
        comboProfesionalAtencion = new JComboBox<>();
        JTextField txtFecha = new JTextField(LocalDate.now().toString());
        JTextField txtMotivo = new JTextField();
        JTextField txtDiagnostico = new JTextField();
        JTextField txtTratamiento = new JTextField();
        JButton btnRegistrarAtencion = new JButton("Registrar atencion");

        formAtencion.add(new JLabel("Paciente:"));
        formAtencion.add(comboPacienteAtencion);
        formAtencion.add(new JLabel("Profesional:"));
        formAtencion.add(comboProfesionalAtencion);
        formAtencion.add(new JLabel("Fecha:"));
        formAtencion.add(txtFecha);
        formAtencion.add(new JLabel("Motivo:"));
        formAtencion.add(txtMotivo);
        formAtencion.add(new JLabel("Diagnostico:"));
        formAtencion.add(txtDiagnostico);
        formAtencion.add(new JLabel("Tratamiento:"));
        formAtencion.add(txtTratamiento);

        for (Paciente p : repo.getPacientes()) comboPacienteAtencion.addItem(p);
        for (Profesional p : repo.getProfesionales()) comboProfesionalAtencion.addItem(p);

        modeloAtenciones = new DefaultTableModel(
                new Object[]{"Fecha", "Paciente", "Profesional", "Diagnostico"}, 0);
        JTable tablaAtenciones = new JTable(modeloAtenciones);

        for (Atencion a : repo.getAtenciones()) {
            Paciente pac = a.getHistoriaClinica().getPaciente();
            modeloAtenciones.addRow(new Object[]{a.getFecha(), pac.getNombres() + " " + pac.getApellidos(),
                    a.getProfesional().getNombres() + " " + a.getProfesional().getApellidos(), a.getDiagnostico()});
        }

        btnRegistrarAtencion.addActionListener(e -> {
            Paciente paciente = (Paciente) comboPacienteAtencion.getSelectedItem();
            Profesional profesional = (Profesional) comboProfesionalAtencion.getSelectedItem();

            if (paciente == null || profesional == null) {
                JOptionPane.showMessageDialog(this, "Registra al menos un paciente y un profesional primero.",
                        "Faltan datos", JOptionPane.WARNING_MESSAGE);
                return;
            }

            Atencion atencion = repo.crearAtencion(paciente, profesional, txtFecha.getText().trim(),
                    txtMotivo.getText().trim(), txtDiagnostico.getText().trim(), txtTratamiento.getText().trim());

            modeloAtenciones.addRow(new Object[]{atencion.getFecha(), paciente.getNombres() + " " + paciente.getApellidos(),
                    profesional.getNombres() + " " + profesional.getApellidos(), atencion.getDiagnostico()});
            comboAtencionReceta.addItem(atencion);
            comboAtencionFua.addItem(atencion);

            txtMotivo.setText("");
            txtDiagnostico.setText("");
            txtTratamiento.setText("");
        });

        JPanel norte = new JPanel(new BorderLayout());
        JButton btnVerRecetas = new JButton("Ver recetas del paciente");
        JPanel panelBotonesAtencion = new JPanel(new GridLayout(1, 2, 5, 5));
        panelBotonesAtencion.add(btnRegistrarAtencion);
        panelBotonesAtencion.add(btnVerRecetas);
        norte.add(formAtencion, BorderLayout.NORTH);
        norte.add(panelBotonesAtencion, BorderLayout.SOUTH);

        // Evento: abre una mini ventana con las recetas del paciente seleccionado
        btnVerRecetas.addActionListener(e -> {
            Paciente paciente = (Paciente) comboPacienteAtencion.getSelectedItem();
            mostrarRecetasPaciente(paciente);
        });

        // --- Formulario de receta (usa la atencion seleccionada) ---
        JPanel formReceta = new JPanel(new BorderLayout(5, 5));
        formReceta.setBorder(BorderFactory.createTitledBorder("Receta medica de la atencion seleccionada"));

        comboAtencionReceta = new JComboBox<>();
        comboAtencionReceta.setRenderer((lista, atencion, indice, seleccionado, foco) -> new JLabel(
                atencion == null ? "" : atencion.getFecha() + " - " + atencion.getDiagnostico()
                        + " (" + atencion.getProfesional().getNombres() + ")"));
        for (Atencion a : repo.getAtenciones()) comboAtencionReceta.addItem(a);

        JTextField txtMedicamento = new JTextField();
        JButton btnAgregarMedicamento = new JButton("+ Medicamento");
        JList<String> listaMedicamentos = new JList<>(modeloMedicamentos);
        JTextField txtIndicaciones = new JTextField();
        JButton btnGuardarReceta = new JButton("Guardar receta");

        JPanel filaMedicamento = new JPanel(new BorderLayout(5, 5));
        filaMedicamento.add(txtMedicamento, BorderLayout.CENTER);
        filaMedicamento.add(btnAgregarMedicamento, BorderLayout.EAST);

        JPanel abajoReceta = new JPanel(new GridLayout(3, 1, 5, 5));
        abajoReceta.add(comboAtencionReceta);
        abajoReceta.add(filaMedicamento);
        JPanel filaIndicaciones = new JPanel(new BorderLayout(5, 5));
        filaIndicaciones.add(new JLabel("Indicaciones: "), BorderLayout.WEST);
        filaIndicaciones.add(txtIndicaciones, BorderLayout.CENTER);
        filaIndicaciones.add(btnGuardarReceta, BorderLayout.EAST);
        abajoReceta.add(filaIndicaciones);

        formReceta.add(abajoReceta, BorderLayout.NORTH);
        formReceta.add(new JScrollPane(listaMedicamentos), BorderLayout.CENTER);

        btnAgregarMedicamento.addActionListener(e -> {
            String medicamento = txtMedicamento.getText().trim();
            if (!medicamento.isEmpty()) {
                modeloMedicamentos.addElement(medicamento);
                txtMedicamento.setText("");
            }
        });

        btnGuardarReceta.addActionListener(e -> {
            Atencion atencion = (Atencion) comboAtencionReceta.getSelectedItem();
            if (atencion == null || modeloMedicamentos.isEmpty()) {
                JOptionPane.showMessageDialog(this, "Selecciona una atencion y agrega al menos un medicamento.",
                        "Faltan datos", JOptionPane.WARNING_MESSAGE);
                return;
            }
            List<String> medicamentos = new ArrayList<>();
            for (int i = 0; i < modeloMedicamentos.size(); i++) medicamentos.add(modeloMedicamentos.get(i));

            RecetaMedica receta = repo.crearReceta(atencion, txtIndicaciones.getText().trim(), medicamentos);
            JOptionPane.showMessageDialog(this, "Receta " + receta.getIdReceta() + " guardada con "
                    + receta.getMedicamentos().size() + " medicamento(s).");

            modeloMedicamentos.clear();
            txtIndicaciones.setText("");
        });

        JSplitPane centro = new JSplitPane(JSplitPane.VERTICAL_SPLIT,
                new JScrollPane(tablaAtenciones), formReceta);
        centro.setResizeWeight(0.55);

        panel.add(norte, BorderLayout.NORTH);
        panel.add(centro, BorderLayout.CENTER);
        return panel;
    }

    // ---------------------------------------------------------
    // TAB: GENERAR FUA
    // ---------------------------------------------------------
    private JPanel crearPanelFua() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));

        JPanel formulario = new JPanel(new GridLayout(4, 2, 5, 5));
        comboAtencionFua = new JComboBox<>();
        comboAtencionFua.setRenderer((lista, atencion, indice, seleccionado, foco) -> new JLabel(
                atencion == null ? "" : atencion.getFecha() + " - " + atencion.getDiagnostico() + " ("
                        + atencion.getHistoriaClinica().getPaciente().getNombres() + ")"));
        for (Atencion a : repo.getAtenciones()) comboAtencionFua.addItem(a);

        JTextField txtServicio = new JTextField();
        JTextField txtProcedimiento = new JTextField();
        JButton btnGenerarFua = new JButton("Generar FUA");

        formulario.add(new JLabel("Atencion:"));
        formulario.add(comboAtencionFua);
        formulario.add(new JLabel("Servicio:"));
        formulario.add(txtServicio);
        formulario.add(new JLabel("Procedimiento:"));
        formulario.add(txtProcedimiento);
        formulario.add(new JLabel());
        formulario.add(btnGenerarFua);

        modeloFua = new DefaultTableModel(
                new Object[]{"ID FUA", "Fecha", "Servicio", "Diagnostico", "Procedimiento", "Paciente"}, 0);
        JTable tablaFua = new JTable(modeloFua);

        for (FUA fua : repo.getFuas()) {
            Paciente paciente = fua.getAtencion().getHistoriaClinica().getPaciente();
            modeloFua.addRow(new Object[]{fua.getIdFUA(), fua.getFecha(), fua.getServicio(),
                    fua.getDiagnostico(), fua.getProcedimiento(), paciente.getNombres() + " " + paciente.getApellidos()});
        }

        // Evento: generar el FUA a partir de la atencion seleccionada
        btnGenerarFua.addActionListener(e -> {
            Atencion atencion = (Atencion) comboAtencionFua.getSelectedItem();
            if (atencion == null) {
                JOptionPane.showMessageDialog(this, "Selecciona una atencion primero.",
                        "Faltan datos", JOptionPane.WARNING_MESSAGE);
                return;
            }
            if (atencion.getFua() != null) {
                JOptionPane.showMessageDialog(this, "Esta atencion ya tiene un FUA generado ("
                        + atencion.getFua().getIdFUA() + ").", "FUA existente", JOptionPane.WARNING_MESSAGE);
                return;
            }
            if (txtServicio.getText().trim().isEmpty() || txtProcedimiento.getText().trim().isEmpty()) {
                JOptionPane.showMessageDialog(this, "Completa servicio y procedimiento.",
                        "Faltan datos", JOptionPane.WARNING_MESSAGE);
                return;
            }

            FUA fua = repo.crearFua(atencion, txtServicio.getText().trim(), txtProcedimiento.getText().trim());
            Paciente paciente = atencion.getHistoriaClinica().getPaciente();
            modeloFua.addRow(new Object[]{fua.getIdFUA(), fua.getFecha(), fua.getServicio(),
                    fua.getDiagnostico(), fua.getProcedimiento(), paciente.getNombres() + " " + paciente.getApellidos()});

            txtServicio.setText("");
            txtProcedimiento.setText("");
        });

        panel.add(formulario, BorderLayout.NORTH);
        panel.add(new JScrollPane(tablaFua), BorderLayout.CENTER);
        return panel;
    }

    // ---------------------------------------------------------
    // TAB 4: CITAS
    // ---------------------------------------------------------
    private JPanel crearPanelCitas() {
        JPanel panel = new JPanel(new BorderLayout(10, 10));

        JPanel formulario = new JPanel(new GridLayout(5, 2, 5, 5));
        comboPacienteCita = new JComboBox<>();
        comboProfesionalCita = new JComboBox<>();
        JTextField txtFecha = new JTextField(LocalDate.now().plusDays(7).toString());
        JTextField txtHora = new JTextField("10:00");
        JButton btnRegistrarCita = new JButton("Registrar cita");

        formulario.add(new JLabel("Paciente:"));
        formulario.add(comboPacienteCita);
        formulario.add(new JLabel("Profesional:"));
        formulario.add(comboProfesionalCita);
        formulario.add(new JLabel("Fecha (AAAA-MM-DD):"));
        formulario.add(txtFecha);
        formulario.add(new JLabel("Hora (HH:MM):"));
        formulario.add(txtHora);
        formulario.add(new JLabel());
        formulario.add(btnRegistrarCita);

        for (Paciente p : repo.getPacientes()) comboPacienteCita.addItem(p);
        for (Profesional p : repo.getProfesionales()) comboProfesionalCita.addItem(p);

        modeloCitas = new DefaultTableModel(
                new Object[]{"ID", "Paciente", "Profesional", "Fecha", "Hora", "Estado"}, 0);
        tablaCitas = new JTable(modeloCitas);

        for (Cita c : repo.getCitas()) {
            modeloCitas.addRow(new Object[]{c.getIdCita(), c.getPaciente().getNombres() + " " + c.getPaciente().getApellidos(),
                    c.getProfesional().getNombres() + " " + c.getProfesional().getApellidos(),
                    c.getFecha(), c.getHora(), c.getEstado()});
        }

        JButton btnMarcarAtendida = new JButton("Marcar atendida");
        JButton btnCancelar = new JButton("Cancelar cita");
        JPanel panelBotones = new JPanel();
        panelBotones.add(btnMarcarAtendida);
        panelBotones.add(btnCancelar);

        btnRegistrarCita.addActionListener(e -> {
            Paciente paciente = (Paciente) comboPacienteCita.getSelectedItem();
            Profesional profesional = (Profesional) comboProfesionalCita.getSelectedItem();
            if (paciente == null || profesional == null) {
                JOptionPane.showMessageDialog(this, "Registra al menos un paciente y un profesional primero.",
                        "Faltan datos", JOptionPane.WARNING_MESSAGE);
                return;
            }
            Cita cita = repo.crearCita(paciente, profesional, txtFecha.getText().trim(), txtHora.getText().trim());
            modeloCitas.addRow(new Object[]{cita.getIdCita(), paciente.getNombres() + " " + paciente.getApellidos(),
                    profesional.getNombres() + " " + profesional.getApellidos(), cita.getFecha(), cita.getHora(), cita.getEstado()});
        });

        // Evento: cambiar estado de la cita seleccionada en la tabla
        btnMarcarAtendida.addActionListener(e -> actualizarEstadoCitaSeleccionada(true));
        btnCancelar.addActionListener(e -> actualizarEstadoCitaSeleccionada(false));

        panel.add(formulario, BorderLayout.NORTH);
        panel.add(new JScrollPane(tablaCitas), BorderLayout.CENTER);
        panel.add(panelBotones, BorderLayout.SOUTH);
        return panel;
    }

    // Mini ventana (JDialog) que muestra las recetas guardadas de un paciente
    private void mostrarRecetasPaciente(Paciente paciente) {
        if (paciente == null) {
            JOptionPane.showMessageDialog(this, "Selecciona un paciente primero.",
                    "Sin paciente", JOptionPane.WARNING_MESSAGE);
            return;
        }

        JDialog dialogo = new JDialog(this,
                "Recetas de " + paciente.getNombres() + " " + paciente.getApellidos(), true);
        dialogo.setSize(600, 350);
        dialogo.setLocationRelativeTo(this);

        DefaultTableModel modelo = new DefaultTableModel(
                new Object[]{"Receta", "Fecha", "Diagnostico atencion", "Medicamentos", "Indicaciones"}, 0);

        for (Atencion atencion : paciente.getHistoriaClinica().getAtenciones()) {
            for (RecetaMedica receta : atencion.getRecetas()) {
                modelo.addRow(new Object[]{receta.getIdReceta(), receta.getFecha(), atencion.getDiagnostico(),
                        String.join(", ", receta.getMedicamentos()), receta.getIndicaciones()});
            }
        }

        JTable tabla = new JTable(modelo);
        tabla.setRowHeight(24);
        dialogo.add(new JScrollPane(tabla));

        if (modelo.getRowCount() == 0) {
            dialogo.add(new JLabel("  Este paciente todavia no tiene recetas guardadas.", SwingConstants.CENTER),
                    BorderLayout.NORTH);
        }

        dialogo.setVisible(true);
    }

    private void actualizarEstadoCitaSeleccionada(boolean atendida) {
        int fila = tablaCitas.getSelectedRow();
        if (fila == -1) {
            JOptionPane.showMessageDialog(this, "Selecciona una cita de la tabla.",
                    "Sin seleccion", JOptionPane.WARNING_MESSAGE);
            return;
        }
        Cita cita = repo.getCitas().get(fila);
        if (atendida) cita.confirmarAtendida(); else cita.cancelar();
        modeloCitas.setValueAt(cita.getEstado(), fila, 5);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new VentanaPrincipal().setVisible(true));
    }
}