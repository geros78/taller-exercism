def is_criticality_balanced(temperature, neutrons_emitted):
    
    """Verify criticality is balanced.
 
    :param temperature: temperature value in kelvin (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not
 
    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000

    

    
def reactor_efficiency(voltage, current, theoretical_max_power):
    
    """Assess reactor efficiency zone.
 
    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'
 
    Efficiency can be grouped into 4 bands:
 
    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.
 
    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
     
    power_eficence = ((voltage * current) / theoretical_max_power)*100
    
    if power_eficence >= 80:
        return "green"
    elif power_eficence < 80 and power_eficence >= 60:
        return "orange"
    elif power_eficence < 60 and power_eficence >= 30:
        return "red"
    else:
        return "black"
    
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    
    """Assess and return status code for the reactor.
 
    :param temperature: value of the temperature in kelvin (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'
 
    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    
    critical_balance = temperature * neutrons_produced_per_second
    
    if critical_balance < (threshold* 0.9):
        return 'LOW'
    elif (threshold* 0.11) > neutrons_produced_per_second > (threshold* 0.09):
        return 'NORMAL'
    else:
        return 'DANGER'

print("El reactor tiene un balance critico?")
print(is_criticality_balanced(600, 800))

print("En que estado se encuentra la eficiencia del reactor?")
print(reactor_efficiency(0.1,0.9, 0.22))

print("Estado se encuntra el codigo del reactor?")
print(fail_safe(4.3, 0.45, 2.1))