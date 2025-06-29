from functools import partial

# -------- Device Classes -------- #

class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print("Light has been turned on.")
        else:
            print("Light is already on.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print("Light has been turned off.")
        else:
            print("Light is already off.")


class Thermostat:
    def __init__(self, temp):
        self.temp = temp

    def set_temperature(self, new_temp):
        if isinstance(new_temp, (int, float)):
            self.temp = new_temp
            print(f"Temperature set to {self.temp}")
        else:
            print("Invalid temperature value.")

    def lower_thermostat(self, value):
        self.temp -= value
        print(f"Thermostat lowered. New temperature is: {self.temp}")

    def raise_thermostat(self, value):
        self.temp += value
        print(f"Thermostat increased. New temperature is: {self.temp}")


class SecurityCamera:
    def __init__(self):
        self.is_recording = False

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            print("Security camera started recording.")
        else:
            print("Camera is already recording.")

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            print("Security camera stopped recording.")
        else:
            print("Camera is already off.")


# -------- Room and Controller Classes -------- #

class Room:
    def __init__(self, name, light=None, thermostat=None, camera=None):
        self.name = name
        self.light = light
        self.thermostat = thermostat
        self.camera = camera

    def turn_off_all(self):
        print(f"\nTurning off devices in {self.name}...")
        if self.light:
            self.light.turn_off()
        if self.camera:
            self.camera.stop_recording()

    def night_mode(self):
        print(f"\n{self.name} - Night Mode:")
        if self.light:
            self.light.turn_off()
        if self.thermostat:
            self.thermostat.lower_thermostat(2)
        if self.camera:
            self.camera.start_recording()


class SmartHomeController:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def activate_night_mode_all(self):
        print("\nActivating Night Mode for all rooms...")
        for room in self.rooms:
            room.night_mode()

    def turn_off_all_rooms(self):
        print("\nTurning off all rooms...")
        for room in self.rooms:
            room.turn_off_all()


# -------- Scheduler and CommandHistory Classes -------- #

class Scheduler:
    def __init__(self):
        self.schedule = {}  # time: list of functions

    def add_task(self, time_str, task_func):
        if time_str not in self.schedule:
            self.schedule[time_str] = []
        self.schedule[time_str].append(task_func)

    def run(self, current_time):
        print(f"\n[Scheduler @ {current_time}]")
        if current_time in self.schedule:
            for task in self.schedule[current_time]:
                task()


class CommandHistory:
    def __init__(self):
        self.history = []

    def execute(self, do_func, undo_func=None):
        do_func()
        if undo_func:
            self.history.append(undo_func)

    def undo_last(self):
        if self.history:
            last = self.history.pop()
            last()


# -------- Usage -------- #

# Create devices
light1 = Light()
thermostat1 = Thermostat(22)
camera1 = SecurityCamera()

light2 = Light()
thermostat2 = Thermostat(20)
camera2 = SecurityCamera()

# Create rooms
living_room = Room("Living Room", light1, thermostat1, camera1)
bedroom = Room("Bedroom", light2, thermostat2, camera2)

# Create SmartHomeController and add rooms
controller = SmartHomeController()
controller.add_room(living_room)
controller.add_room(bedroom)

# Create Scheduler
scheduler = Scheduler()
scheduler.add_task("22:00", controller.activate_night_mode_all)
scheduler.add_task("07:00", controller.turn_off_all_rooms)

# Create CommandHistory and perform actions
history = CommandHistory()
history.execute(light1.turn_on, light1.turn_off)
history.execute(partial(thermostat1.raise_thermostat, 2), partial(thermostat1.lower_thermostat, 2))

# Run Scheduler
scheduler.run("22:00")
scheduler.run("07:00")

# Undo last action
print("\nUndoing last command:")
history.undo_last()
