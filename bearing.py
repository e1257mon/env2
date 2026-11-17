
import numpy as np

# 1. Simulation settings
simulation_hours = 400000
number_of_bearings = 4

np.random.seed(42)

# 2. Bearing life distribution
bearing_life = [1200, 1400, 1600, 1800, 2000]
bearing_prob = [0.10, 0.25, 0.30, 0.25, 0.10]

# 3. Delay time distribution
delay_time = [2, 3, 4, 8]
delay_prob = [0.20, 0.30, 0.30, 0.20]

# 4. Replacement time in minutes
replacement_time = {
    1: 15,
    2: 25,
    3: 30,
    4: 35
}

# 5. Cost settings
bearing_cost = 30
technician_rate = 30
downtime_rate = 5


# =====================================
# PRESENT POLICY
# Replace only the failed bearing
# =====================================

present_bearings = np.random.choice(
    bearing_life,
    size=number_of_bearings,
    p=bearing_prob
)

present_time = 0
present_bearing_cost = 0
present_technician_cost = 0
present_downtime_cost = 0
present_replacements = 0

while present_time < simulation_hours:

    # Find the bearing with minimum remaining life
    min_life = np.min(present_bearings)

    present_time += min_life

    if present_time >= simulation_hours:
        break

    # Find which bearing failed
    failed_index = np.argmin(present_bearings)

    # Generate random delay
    delay = np.random.choice(delay_time, p=delay_prob)

    # Replacement time for one bearing
    repair_time = replacement_time[1]

    total_delay = delay + repair_time

    # Calculate costs
    present_bearing_cost += bearing_cost

    present_technician_cost += (repair_time / 60) * technician_rate

    present_downtime_cost += total_delay * downtime_rate

    present_replacements += 1

    # Add maintenance downtime
    present_time += total_delay / 60

    # Reduce remaining life of other bearings
    present_bearings -= min_life

    # Generate new life for replaced bearing
    present_bearings[failed_index] = np.random.choice(
        bearing_life, p=bearing_prob
    )


present_total_cost = (
    present_bearing_cost
    + present_technician_cost
    + present_downtime_cost
)


# =====================================
# PROPOSED POLICY
# Replace all four bearings together
# =====================================

proposed_bearings = np.random.choice(
    bearing_life,
    size=number_of_bearings,
    p=bearing_prob
)

proposed_time = 0
proposed_bearing_cost = 0
proposed_technician_cost = 0
proposed_downtime_cost = 0
proposed_replacements = 0

while proposed_time < simulation_hours:

    # Find the first failed bearing
    min_life = np.min(proposed_bearings)

    proposed_time += min_life

    if proposed_time >= simulation_hours:
        break

    # Generate random delay
    delay = np.random.choice(delay_time, p=delay_prob)

    # All four bearings are replaced
    repair_time = replacement_time[4]

    total_delay = delay + repair_time

    # Calculate costs
    proposed_bearing_cost += number_of_bearings * bearing_cost

    proposed_technician_cost += (repair_time / 60) * technician_rate

    proposed_downtime_cost += total_delay * downtime_rate

    proposed_replacements += 1

    # Add maintenance downtime
    proposed_time += total_delay / 60

    # Generate new life for all four bearings
    proposed_bearings = np.random.choice(
        bearing_life,
        size=number_of_bearings,
        p=bearing_prob
    )


proposed_total_cost = (
    proposed_bearing_cost
    + proposed_technician_cost
    + proposed_downtime_cost
)


# =====================================
# DISPLAY RESULTS
# =====================================

print("===== PRESENT POLICY =====")

print("Number of replacements:", present_replacements)
print("Bearing cost: $", round(present_bearing_cost, 2))
print("Technician cost: $", round(present_technician_cost, 2))
print("Downtime cost: $", round(present_downtime_cost, 2))
print("Total cost: $", round(present_total_cost, 2))


print("\n===== PROPOSED POLICY =====")

print("Number of replacements:", proposed_replacements)
print("Bearing cost: $", round(proposed_bearing_cost, 2))
print("Technician cost: $", round(proposed_technician_cost, 2))
print("Downtime cost: $", round(proposed_downtime_cost, 2))
print("Total cost: $", round(proposed_total_cost, 2))


# =====================================
# COMPARE BOTH POLICIES
# =====================================

print("\n===== POLICY COMPARISON =====")

if present_total_cost < proposed_total_cost:

    print("Present Policy is more economical.")

    print("Money saved: $",
          round(proposed_total_cost - present_total_cost, 2))

else:

    print("Proposed Policy is more economical.")

    print("Money saved: $",
          round(present_total_cost - proposed_total_cost, 2))
