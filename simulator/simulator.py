import json
import random
from datetime import datetime, timedelta, timezone


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

NUM_READINGS = 1000

STATION_ID = "GANGA-001"

LATITUDE = 25.3176
LONGITUDE = 83.0065

START_TIME = datetime.now(timezone.utc)

TIME_STEP_MINUTES = 10


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def add_noise(value, amount):
    return value + random.gauss(0, amount)


# ---------------------------------------------------------
# Environmental events
# ---------------------------------------------------------

def generate_environmental_effect():
    """
    Generate an occasional environmental event.

    Events influence multiple water-quality parameters
    instead of changing only one value randomly.
    """

    event = "normal"

    rainfall_effect = 0.0
    pollution_effect = 0.0
    temperature_effect = 0.0

    probability = random.random()

    if probability < 0.03:
        event = "heavy_rainfall"

        rainfall_effect = random.uniform(10, 25)
        temperature_effect = random.uniform(-2.0, -0.5)

    elif probability < 0.05:
        event = "pollution_event"

        pollution_effect = random.uniform(10, 25)

    return {
        "event": event,
        "rainfall_effect": rainfall_effect,
        "pollution_effect": pollution_effect,
        "temperature_effect": temperature_effect,
    }


# ---------------------------------------------------------
# Generate one water-quality reading
# ---------------------------------------------------------

def generate_reading(
    condition,
    current_temperature,
    timestamp,
):
    event = generate_environmental_effect()

    # Environmental events temporarily affect
    # the underlying water condition.

    effective_condition = condition

    effective_condition += event["rainfall_effect"]
    effective_condition += event["pollution_effect"]

    effective_condition = clamp(
        effective_condition,
        0,
        100,
    )

    # -----------------------------------------------------
    # Temperature
    # -----------------------------------------------------

    new_temperature = current_temperature

    new_temperature += event["temperature_effect"]

    # Natural variation
    new_temperature += random.uniform(-0.25, 0.25)

    new_temperature = clamp(
        new_temperature,
        20,
        35,
    )

    # -----------------------------------------------------
    # Turbidity
    # -----------------------------------------------------

    turbidity_base = (
        8 + (effective_condition * 0.45)
    )

    # Rainfall increases suspended material.
    turbidity_base += (
        event["rainfall_effect"] * 0.8
    )

    turbidity = add_noise(
        turbidity_base,
        3.0,
    )

    turbidity = clamp(
        turbidity,
        1,
        100,
    )

    # -----------------------------------------------------
    # Dissolved Oxygen
    # -----------------------------------------------------

    do_base = (
        8.2 - (effective_condition * 0.045)
    )

    # Higher temperature can reduce DO.
    do_base -= max(
        0,
        new_temperature - 25,
    ) * 0.04

    dissolved_oxygen = add_noise(
        do_base,
        0.18,
    )

    dissolved_oxygen = clamp(
        dissolved_oxygen,
        2,
        10,
    )

    # -----------------------------------------------------
    # pH
    # -----------------------------------------------------

    ph_base = (
        7.3 - (effective_condition * 0.004)
    )

    # Small independent environmental influence.
    ph_base += random.uniform(
        -0.08,
        0.08,
    )

    ph = add_noise(
        ph_base,
        0.06,
    )

    ph = clamp(
        ph,
        6.0,
        9.0,
    )

    # -----------------------------------------------------
    # Final reading
    # -----------------------------------------------------

    reading = {
        "timestamp": timestamp.isoformat(),
        "station_id": STATION_ID,
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "temperature": round(new_temperature, 2),
        "pH": round(ph, 2),
        "dissolved_oxygen": round(
            dissolved_oxygen,
            2,
        ),
        "turbidity": round(
            turbidity,
            2,
        ),
        "event": event["event"],
    }

    return reading, new_temperature


# ---------------------------------------------------------
# Generate complete dataset
# ---------------------------------------------------------

def generate_dataset():

    # Initial hidden water-condition state.
    # This is NOT stored in the final dataset.

    water_condition = 30.0

    # Initial temperature.
    # This fixes the previous UnboundLocalError.

    temperature = 27.0

    readings = []

    timestamp = START_TIME

    for _ in range(NUM_READINGS):

        # Gradual change in underlying water condition.
        natural_change = random.uniform(
            -2.0,
            2.0,
        )

        water_condition += natural_change

        water_condition = clamp(
            water_condition,
            5,
            85,
        )

        reading, temperature = generate_reading(
            water_condition,
            temperature,
            timestamp,
        )

        readings.append(reading)

        timestamp += timedelta(
            minutes=TIME_STEP_MINUTES
        )

    return readings


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print(
        "Starting Ganga Water Quality IoT Simulator..."
    )

    print(
        f"Station: {STATION_ID}"
    )

    print(
        f"Generating {NUM_READINGS} readings...\n"
    )

    readings = generate_dataset()

    output = {
        "station": {
            "station_id": STATION_ID,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
        },
        "readings": readings,
    }

    output_file = "iot_batch.json"

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            output,
            file,
            indent=2,
        )

    print("Simulation completed.")

    print(
        f"Generated readings: {len(readings)}"
    )

    print(
        f"Output: {output_file}"
    )


if __name__ == "__main__":
    main()