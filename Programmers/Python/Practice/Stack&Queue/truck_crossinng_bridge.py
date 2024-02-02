def solution(bridge_length, weight, truck_weights):
    bridge = []
    over = []

    answer = 0
    truck_index = 0
    while len(truck_weights) != len(over):
        answer += 1

        if bridge:
            for truck_info in bridge:
                truck_info[0] += 1

            if bridge[0][0] == bridge_length:
                _, truck = bridge.pop(0)
                over.append(truck)

        if sum([info[1] for info in bridge])+truck_weights[truck_index] <= weight and len(over) != len(truck_weights):
            if truck_index < len(truck_weights):
                bridge.append([0, truck_weights[truck_index]])

                if truck_index != len(truck_weights)-1:
                    truck_index += 1
    
    return answer