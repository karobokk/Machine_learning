import requests
import matplotlib.pyplot as plt


def med_sal(name_vac):  # medium salary
    i = 0
    j = 0
    count_vac = 0
    cnst = 100  # 1-100 per page
    salary_done = []
    # цикл для const_per_page значений
    while i < 10:
        payload = {'per_page': cnst, 'page': i, 'only_with_salary': 'true', 'text': name_vac}
        r = requests.get('https://api.hh.ru/vacancies', params=payload)
        r_json = r.json()
        array_with_dict_with_salary = r_json['items']
        i += 1
        while j < const_per_page:
            if (array_with_dict_with_salary[j]['salary']['to'] == None):
                salary_done.append(array_with_dict_with_salary[j]['salary']['from'])
            elif (array_with_dict_with_salary[j]['salary']['from'] == None):
                salary_done.append(array_with_dict_with_salary[j]['salary']['to'])
            else:
                medium = (array_with_dict_with_salary[j]['salary']['to'] + array_with_dict_with_salary[j]['salary'][
                    'from']) / 2
                salary_done.append(medium)  # medium- это зарплата
            j += 1
            count_vac += 1
    salary_done.sort()
    return salary_done[count_vac // 2]


def graf_salary(name_vac):
    i = 0;
    j = 0;
    count_vac = 0
    const_per_page = 100  # 1-100
    salary_done = []
    # цикл для const_per_page значений
    while i < 10:
        payload = {'per_page': const_per_page, 'page': i, 'only_with_salary': 'true', 'text': name_vac}
        r = requests.get('https://api.hh.ru/vacancies', params=payload)
        r_json = r.json()
        array_with_dict_with_salary = r_json['items']
        i += 1
        while j < const_per_page:
            if (array_with_dict_with_salary[j]['salary']['to'] == None):
                salary_done.append(array_with_dict_with_salary[j]['salary']['from'])
            elif (array_with_dict_with_salary[j]['salary']['from'] == None):
                salary_done.append(array_with_dict_with_salary[j]['salary']['to'])
            else:
                medium = (array_with_dict_with_salary[j]['salary']['to'] + array_with_dict_with_salary[j]['salary'][
                    'from']) / 2
                salary_done.append(medium)  # medium- это зарплата
            j += 1
            count_vac += 1
    salary_done.sort()
    plt.xlabel('Зарплата, руб')
    plt.ylabel('Количество вакансий, шт')
    plt.title('Распределение ваканский по размеру ЗП')
    bins = plt.hist(salary_done, bins=[
        0,
        40000,
        80000,
        120000,
        150000,
        180000,
        220000,
        260000,
        320000,
        380000,
        500000
    ])
    plt.show()


# main
if __name__ == '__main__':
    def main()
        names_vac = ['mashine learning', 'c++', 'c#', 'golang', 'php']
        # for i in names_vac:
        # print(i)
        # print(  med_sal(i) )
        graf_salary('mashine learning')
