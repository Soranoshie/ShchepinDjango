import json
import time
from datetime import datetime, date
import pandas as pd
import requests

class VacancyParser:

    hour_delta = 4

    @staticmethod
    def get_vacancies_by_date(date: datetime):
        vacancies = []
        for hour in range(0, 24, VacancyParser.hour_delta):
            begin_date = datetime(date.year, date.month, date.day, hour=hour)
            if hour + VacancyParser.hour_delta > 23:
                end_date = datetime(date.year, date.month, date.day, hour=hour, minute=59, second=59)
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
                  "specialization": 1, "text": "NAME:C#"}
        req = requests.get("https://api.hh.ru/vacancies", params)
        req.close()
        data = json.loads(req.content.decode())
        return data

    @staticmethod
    def get_formatted_vacancy(vacancy: dict):
        new_vacancy = {}
        new_vacancy["name"] = vacancy["name"]
        if vacancy["salary"] is not None:
            new_vacancy["salary_from"] = vacancy["salary"]["from"]
            new_vacancy["salary_to"] = vacancy["salary"]["to"]
            new_vacancy["salary_currency"] = vacancy["salary"]["currency"]
        else:
            new_vacancy["salary_from"] = None
            new_vacancy["salary_to"] = None
            new_vacancy["salary_currency"] = None
        if vacancy["area"] is not None:
            new_vacancy["area_name"] = vacancy["area"]["name"]
        else:
            new_vacancy["area_name"] = None
        new_vacancy["published_at"] = vacancy["published_at"]
        return new_vacancy


date_to_parse = date.today
vacancies = VacancyParser.get_vacancies_by_date(date_to_parse)
print(vacancies)