def growing_plant(up, down, desired):
    days = 0
    plant_height = 0

    while (plant_height < desired):
        plant_height = plant_height + up
        days += 1

        if plant_height < desired:
            plant_height - down

    return days


# Test
print(growing_plant(100, 10, 910))  # 10
