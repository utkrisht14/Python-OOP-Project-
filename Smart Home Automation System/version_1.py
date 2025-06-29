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


class SmartHomeController:
    def __init__(self, light, camera, thermostat):
        self.light = light
        self.camera = camera
        self.thermostat = thermostat

    def turn_off_all_devices(self):
        self.light.turn_off()
        self.camera.stop_recording()
        print("All devices turned off.")

    def activate_night_mode(self):
        print("\nActivating Night Mode...")
        self.light.turn_off()
        self.thermostat.lower_thermostat(2)
        self.camera.start_recording()


# --- Run Example ---

light = Light()
thermostat = Thermostat(22)
camera = SecurityCamera()

controller = SmartHomeController(light, camera, thermostat)
controller.activate_night_mode()
controller.turn_off_all_devices()
