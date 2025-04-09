import matplotlib.pyplot as plt
import numpy as np

class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint, dt):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.dt = dt
        self.integral = 0
        self.prev_error = 0
    
    def update(self, measurement):
        """
        Calculate PID control output for given measurement.
        """
        error = self.setpoint - measurement
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

def simulate_pid():
    # Simulation parameters
    dt = 0.1              # time step (seconds)
    total_time = 20       # total simulation time (seconds)
    n_steps = int(total_time / dt)
    time_array = np.linspace(0, total_time, n_steps)
    
    # PID controller parameters and setpoint
    setpoint = 10         # desired value
    pid = PIDController(Kp=0.8, Ki=0.2, Kd=0.1, setpoint=setpoint, dt=dt)
    
    # Process simulation: start with an initial process variable of 0.
    process_variable = 0
    pv_history = []

    # Simple simulation loop
    for t in time_array:
        # Compute control signal from PID controller
        control_signal = pid.update(process_variable)
        # Update the process variable:
        # For this example, assume a very simple process where the control signal
        # directly influences the rate of change of the process variable.
        process_variable += control_signal * dt
        pv_history.append(process_variable)
    
    # Plot the simulation results
    plt.figure(figsize=(10, 6))
    plt.plot(time_array, pv_history, label="Process Variable")
    plt.axhline(y=setpoint, color='r', linestyle='--', label="Setpoint")
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.title("PID Controller Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()


control_value = 0.0


def on_key(event):
    global control_value

    # For example, pressing the up arrow increases, and down arrow decreases the value
    if event.key == 'up':
        control_value += 0.5
        print(f"control_value increased to {control_value}")
    elif event.key == 'down':
        control_value -= 0.5
        print(f"control_value decreased to {control_value}")



def realtime():
    plt.ion()  # turn on interactive mode
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('key_press_event', on_key)

    # Create initial data
    dx = 0.1
    x = 0.0
    x_data = [x]
    # Base y data is, say, a sine wave; we will add the control_value to shift it.
    y = 0.0
    y_data = [y]

    # Plot the initial line
    line, = ax.plot(x_data, y_data, lw=1)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Realtime Plot (use Up/Down keys to change offset)")

    ax.set_xlim([0, 10])
    ax.set_ylim([-2, 2])

    while plt.fignum_exists(fig.number):
        # Here we recalc y_data with the current control_value as an offset
        x += dx
        y = np.sin(x) + control_value

        x_data.append(x)
        y_data.append(y)

        line.set_data(x_data, y_data)
        plt.draw()
        plt.pause(0.1)


if __name__ == '__main__':
    #simulate_pid()
    realtime()

