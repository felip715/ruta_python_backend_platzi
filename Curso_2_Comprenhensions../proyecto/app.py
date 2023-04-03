import csv
import matplotlib
matplotlib.use('TkAgg',force=True)
import matplotlib.pyplot as plt
print("Switched to:",matplotlib.get_backend())



def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data_dict = {key: value for key, value in iterable}
            data.append(data_dict)
    return data

def find_country(country, data):
    #selection = []
    #for i in data:
        # if i['country'] == country:
        #     selection.append[i]
    selection = [i for i in data if i['Country/Territory'] == country]
    return(selection) 

def chart_population(country_info):
    fig, ax = plt.subplots()
    labels = [k for k in country_info[0].keys() if (k.startswith('19') or k.startswith('20'))]
    labels.sort()
    values = []
    for i in labels:
        values.append([v for k,v in country_info[0].items() if k == i][0])
    labels = [i.split()[0] for i in labels]
    ax.bar(labels, values)
    plt.xlabel('Año')
    plt.ylabel('Ciudadanos')


def char_porcentage_population(data):
    labels = [i['Country/Territory'] for i in data]
    values = [i['World Population Percentage'] for i in data]
    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels = labels)
    ax2.set_title('Pie Chart')
    ax2.axis('equal')


if __name__ == '__main__':
    country = 'Argentina'
    path = './proyecto/world_population.csv'
    data = read_csv(path)
    country_info = find_country(country, data)
    chart_population(country_info)
    char_porcentage_population(data)
    plt.show()