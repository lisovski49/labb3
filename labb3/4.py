import json

with open('companies.rtf', 'r') as f:
    companies_list = []
    total_profit = 0
    for line in f:
        name, ownership, revenue, costs = line.split()
        revenue = int(revenue)
        costs = int(costs)
        profit = revenue - costs
        total_profit += profit
        company_dict = {'name': name, 'profit': profit}

        companies_list.append(company_dict)

    num_companies = len(companies_list)

    if num_companies > 0:
        average_profit = total_profit / num_companies
    else:
        average_profit = 0

    average_dict = {'average_profit': average_profit}

    result_list = [companies_list, average_dict]

    with open('result.json', 'w') as f:
        json.dump(result_list, f)