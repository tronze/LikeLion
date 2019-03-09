import csv
import os
import sys

import django


def read_apply_csv():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSV_PATH = os.path.join(BASE_DIR, 'recruitment/total.csv')
    with open(CSV_PATH, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
    rcsv = csv.reader(lines[1:])
    for record in rcsv:
        name = record[1]
        year = record[2]
        major = record[3]
        phone = record[4].replace('-', '')
        if len(phone) > 13:
            phone = ""
        email = record[5]
        links = record[6]
        portfolio = record[7].split("\"")[1]
        q1 = record[8]
        q2 = record[9]
        q3 = record[10]
        q4 = record[11]
        q5 = record[12]
        group = Group.objects.get(pk=1)
        application = Evaluation.get_application()
        applicant = Applicant.objects.create(name=name, group=group, email=email, phone=phone, links=links,
                                             portfolio=portfolio)
        applicant_application = ApplicantApplication.objects.create(applicant=applicant, application=application)
        questions = Question.objects.filter(application=application).order_by('order')
        Answer.objects.create(applicant=applicant, question=questions[0], answer=q1)
        Answer.objects.create(applicant=applicant, question=questions[1], answer=q2)
        Answer.objects.create(applicant=applicant, question=questions[2], answer=q3)
        Answer.objects.create(applicant=applicant, question=questions[3], answer=q4)
        Answer.objects.create(applicant=applicant, question=questions[4], answer=q5)
        print(name)
        print(year)
        print(major)
        print(phone)
        print(email)
        print(links)
        print(portfolio)
        print(q1)
        print(q2)
        print(q3)
        print(q4)
        print(q5)
        print("==========")


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSV_PATH = os.path.join(BASE_DIR, 'recruitment/total.csv')
    print(CSV_PATH)
    sys.path.append(BASE_DIR)
    sys.path.append(CSV_PATH)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LikeLion.settings')
    django.setup()

    from django.contrib.auth.models import Group

    from recruitment.controller import EvaluationController
    from recruitment.models import Evaluation, Applicant, ApplicantApplication, Question, Answer

    read_apply_csv()
