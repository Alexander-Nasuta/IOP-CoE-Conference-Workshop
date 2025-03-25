import time

from jsp_instance_utils.instances import ft06
from jsp_instance_utils.jsp_or_tools_solver import solve_jsp



if __name__ == '__main__':
    start_time = time.perf_counter()
    makespan, status, *_ = solve_jsp(jsp_instance=ft06, plot_results=True)
    end_time = time.perf_counter()

    assert status == "OPTIMAL"

    print(f"Time taken to solve the instance: {end_time - start_time} seconds")