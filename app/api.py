import json
import re
import time
from datetime import datetime, date
import requests

class VacancyParser:

    hour_delta = 4

    @staticmethod
    def get_vacancies_by_date(date: datetime):
        vacancies = []
        for hour in range(0, 24, VacancyParser.hour_delta):
            begin_date = datetime(date.year, date.month, date.day, hour=hour)
            if hour + VacancyParser.hour_delta > 23:
                end_date = datetime.today()
            else:
                end_date = datetime(date.year, date.month, date.day, hour=hour + VacancyParser.hour_delta)
            first_page_info = VacancyParser.get_vacancies_info_by_page(0, begin_date, end_date)
            total_pages_count = first_page_info["pages"]
            vacancies.extend(map(VacancyParser.get_formatted_vacancy, first_page_info["items"]))
            for page in range(1, total_pages_count):
                vacancies.extend(map(VacancyParser.get_formatted_vacancy,
                                     VacancyParser.get_vacancies_info_by_page(page, begin_date, end_date)["items"]))
                time.sleep(0.2)
        return vacancies

    @staticmethod
    def get_vacancies_info_by_page(page: int, begin_date: datetime, end_date: datetime):
        begin_date_str = begin_date.strftime("%Y-%m-%dT%H:%M:%S")
        end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%S")
        params = {"page": page, "per_page": 100, "date_from": begin_date_str, "date_to": end_date_str,
                  "specialization": 1, "text": "NAME:C#", "only_with_salary": True, "currency": "RUR"}
        req = requests.get("https://api.hh.ru/vacancies", params)
        req.close()
        data = json.loads(req.content.decode())
        return data

    @staticmethod
    def get_formatted_vacancy(vacancy: dict):
        new_vacancy = {}
        vacancy_id = vacancy["id"]

        detailed_vacancy = requests.get(f"https://api.hh.ru/vacancies/{vacancy_id}")
        detailed_vacancy.close()
        data_key_skills = json.loads(detailed_vacancy.content.decode())

        new_vacancy["name"] = vacancy["name"]

        formated_description = re.sub(r"<[^>]+>", "", data_key_skills["description"], flags=re.S)
        if formated_description is not None:
            new_vacancy["description"] = formated_description
        else:
            new_vacancy["description"] = '-'

        skill_list = ""
        if len(data_key_skills["key_skills"]) != 0:
            for skill in data_key_skills["key_skills"]:
                skill_list += (skill["name"] + ', ')

            new_vacancy["key_skills"] = skill_list[:-2]
        else:
            new_vacancy["key_skills"] = '-'

        if vacancy["employer"]["name"] is not None:
            new_vacancy["employer"] = vacancy["employer"]["name"]
        else:
            new_vacancy["employer"] = '-'

        if vacancy["salary"]["from"] is not None:
            new_vacancy["salary_from"] = vacancy["salary"]["from"]
        else:
            new_vacancy["salary_from"] = '-'

        if vacancy["salary"]["to"] is not None:
            new_vacancy["salary_to"] = vacancy["salary"]["to"]
        else:
            new_vacancy["salary_to"] = '-'

        if vacancy["salary"]["currency"] is not None:
            new_vacancy["salary_currency"] = vacancy["salary"]["currency"]
        else:
            new_vacancy["salary_currency"] = '-'

        if vacancy["area"] is not None:
            new_vacancy["area_name"] = vacancy["area"]["name"]
        else:
            new_vacancy["area_name"] = '-'

        new_vacancy["published_at"] = datetime.strptime(vacancy["published_at"], "%Y-%m-%dT%H:%M:%S%z").date()

        return new_vacancy


date_to_parse = datetime(2023, 1, 16)
vacancies = VacancyParser.get_vacancies_by_date(date_to_parse)
print(vacancies)