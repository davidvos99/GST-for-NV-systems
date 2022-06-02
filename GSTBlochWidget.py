import ipywidgets as widgets
from IPython.display import display
from qiskit.visualization import plot_bloch_multivector
import numpy as np
from io import BytesIO
from datetime import datetime


class GSTBlochWidget:
    def __init__(self, labels, gates, target_gates, dir_path):
        self.labels = labels
        self.gates = gates
        self.target_gates = list(map(lambda x: np.matrix(x), target_gates))
        self.dir_path = dir_path
        self.rho = zero_state
        self.target_state = np.matrix([[1], [0]])
        self.count = 0
        self.fidelity = 1
        self.bloch_coor = [0, 0, 1]
        self.history = []

    def render_widget(self):
        button_list = [widgets.Button(description=label, layout=widgets.Layout(width='5em', height='4em')) for label in
                       self.labels]
        button_list.append(widgets.Button(description='Reset', layout=widgets.Layout(width='6em', height='3em')))
        button_list.append(
            widgets.Button(description='Save circuit', layout=widgets.Layout(width='10em', height='3em')))
        count = widgets.Output(layout={'border': '1px solid black'})
        fidelity = widgets.Output(layout={'border': '1px solid black'})
        bloch_coord = widgets.Output(layout={'border': '1px solid black'})
        image = _img()

        def update_output():
            count.clear_output()
            fidelity.clear_output()
            bloch_coord.clear_output()
            count.append_stdout("Gates applied: " + str(self.count))
            fidelity.append_stdout("Fidelity: " + str(self.fidelity))
            bloch_coord.append_stdout("(x, y, z): " + str(self.bloch_coor))
            image.value = plot_bloch_multivector(self.rho)

        def apply_gates(b):
            if b.description == 'Reset':
                self.rho = zero_state
                self.target_state = np.matrix([[1], [0]])
                self.fidelity = 1
                self.count = 0
                self.bloch_coor = [0, 0, 1]
            elif b.description == 'Save circuit':
                self.save_circuit()
            else:
                self.rho = evolve(self.rho, self.gates[self.labels.index(b.description)])
                self.target_state = self.target_gates[self.labels.index(b.description)].dot(self.target_state)
                self.update_fidelity()
                self.update_bloch_coord()
                self.count += 1

        def on_button_click(b):
            apply_gates(b)
            update_output()
            self.history.append([b.description, self.fidelity, self.rho])

        for button in button_list:
            button.on_click(on_button_click)
        data_box = widgets.HBox([count, fidelity, bloch_coord])
        main_box = widgets.HBox(button_list)
        count.append_stdout("")
        fidelity.append_stdout("")
        bloch_coord.append_stdout("")
        update_output()
        display(data_box)
        display(main_box)
        display(image.widget)

    def update_bloch_coord(self):
        c0 = np.trace(pauli_i.dot(self.rho))
        c1 = np.trace(pauli_x.dot(self.rho))
        c2 = np.trace(pauli_y.dot(self.rho))
        c3 = np.trace(pauli_z.dot(self.rho))
        self.bloch_coor = np.around([np.real(c1 / c0), np.real(c2 / c0), np.real(c3 / c0)], 3)

    def update_fidelity(self):
        self.fidelity = np.around(
            np.real(self.target_state.conjugate().transpose().dot(self.rho.dot(self.target_state))), 3).item(0)

    def save_circuit(self):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d__%H-%M-%S") + ".txt"
        file_path = self.dir_path + dt_string
        f = open(file_path, "w")
        count = 0
        for hist in self.history:
            f.write(str(count) + "\n")
            f.write("Gate: " + str(hist[0]) + "\n")
            f.write("Fidelity: " + str(hist[1]) + "\n")
            f.write("Rho: " + "\n" + str(hist[2]) + "\n\n")
            count += 1
        f.close()


# Helper methods, evolve density matrix rho with superoperator super_op
def evolve(rho, super_op):
    c0 = np.trace(pauli_i.dot(rho))
    c1 = np.trace(pauli_x.dot(rho))
    c2 = np.trace(pauli_y.dot(rho))
    c3 = np.trace(pauli_z.dot(rho))
    super_rho = np.matrix([[c0], [c1], [c2], [c3]])
    # calculate new super rho
    ns_rho = super_op.dot(super_rho)
    n_rho = ns_rho.item(0) * pauli_i + ns_rho.item(1) * pauli_x + ns_rho.item(2) * pauli_y + ns_rho.item(3) * pauli_z
    return n_rho


class _img():

    def __init__(self, value=None):
        self.widget = widgets.Image(format='png')
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        if value is None:
            return

        data = BytesIO()
        value.savefig(data, format='png', facecolor=self.value.get_facecolor())
        data.seek(0)
        self.widget.value = data.read()


pauli_i = 1 / np.sqrt(2) * np.matrix([
    [1, 0],
    [0, 1]
])

pauli_x = 1 / np.sqrt(2) * np.matrix([
    [0, 1],
    [1, 0]
])

pauli_y = 1 / np.sqrt(2) * np.matrix([
    [0, -1j],
    [1j, 0]
])
pauli_z = 1 / np.sqrt(2) * np.matrix([
    [1, 0],
    [0, -1]
])

zero_state = np.matrix([
    [1, 0],
    [0, 0]
])

gi = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

gxpi2 = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, -1],
    [0, 0, 1, 0]
])

gypi2 = np.matrix([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, -1, 0, 0]
])

gxpi = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, -1]
])

gypi = np.matrix([
    [1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, -1]
])

