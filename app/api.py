import json
import re
import time
from datetime import datetime, date, timedelta
import requests

class VacancyParser:

    @staticmethod
    def get_vacancies_by_date():
        vacancies = []
        begin_date = datetime.today() - timedelta(days=1)
        end_date = datetime.today()
        first_page_info = VacancyParser.get_vacancies_info_by_page(begin_date, end_date)
        vacancies.extend(map(VacancyParser.get_formatted_vacancy, first_page_info["items"]))
        vacancies.extend(map(VacancyParser.get_formatted_vacancy, VacancyParser.get_vacancies_info_by_page(begin_date,
                                                                                                end_date)["items"]))
        return vacancies

    @staticmethod
    def get_vacancies_info_by_page(begin_date: datetime, end_date: datetime):
        begin_date_str = begin_date.strftime("%Y-%m-%dT%H:%M:%S")
        end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%S")
        params = {"page": 0, "per_page": 10, "date_from": begin_date_str, "date_to": end_date_str,
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
