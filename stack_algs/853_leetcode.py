def carFleet(target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleet = 0
        slowest_car_time_to_dest = 0
        for pos, speed in cars:
            current_time = (target - pos) / speed
            if slowest_car_time_to_dest < current_time:
                fleet += 1
                slowest_car_time_to_dest = current_time
        return fleet




