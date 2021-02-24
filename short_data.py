import tools

workers_data = tools.get_arr_data('data')

tools.sort_data(workers_data)

tools.put_data('data_shorted', workers_data)
